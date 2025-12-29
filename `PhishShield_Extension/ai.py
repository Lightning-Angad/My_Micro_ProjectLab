import re
import math
import joblib
import tldextract
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import shap

app = FastAPI(title="PhishShield AI™ Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLPayload(BaseModel):
    url: str
MODEL_PATH = "model.joblib"

try:
    model = joblib.load(MODEL_PATH)
    explainer = shap.TreeExplainer(model)
    print(f"Loaded model from {MODEL_PATH}")
except Exception as e:
    print(f"ERROR loading model ({MODEL_PATH}): {e}")
    raise SystemExit(1)

def compute_entropy(s: str) -> float:
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    entropy = 0.0
    length = len(s)
    for count in counts.values():
        p = count / length
        entropy -= p * math.log2(p)
    return entropy

def extract_features(url: str) -> tuple[list, list]:
    ext = tldextract.extract(url)
    path = url.split(ext.suffix)[-1] if ext.suffix else ""
    url_lower = url.lower()
    feats = {
        "url_length": len(url),
        "subdomain_length": len(ext.subdomain),
        "domain_length": len(ext.domain),
        "suffix_length": len(ext.suffix),
        "path_length": len(path),
        "entropy": compute_entropy(url),
        "count_login": url_lower.count("login"),
        "count_verify": url_lower.count("verify"),
        "count_secure": url_lower.count("secure"),
        "has_ip": 1 if re.match(r"^https?://\d+\.\d+\.\d+\.\d+", url) else 0,
    }
    return list(feats.keys()), list(feats.values())

@app.post("/ai/scan")
async def scan_url(payload: URLPayload):
    url = payload.url.strip()
    if not url.startswith(("http://", "https://")):
        raise HTTPException(
            status_code=400, detail="URL must start with http:// or https://"
        )
    feature_names, feature_values = extract_features(url)
    X = np.array([feature_values])

    try:
        proba = model.predict_proba(X)[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {e}")

    safe_prob, malicious_prob = float(proba[0]), float(proba[1])
    if malicious_prob >= 0.5:
        label = "malicious"
        confidence = malicious_prob
        cls_index = 1
    else:
        label = "safe"
        confidence = safe_prob
        cls_index = 0

    try:
        shap_values = explainer.shap_values(X)
        sv = shap_values[cls_index][0]
        top_idx = np.argsort(np.abs(sv))[::-1][:3]
        flags = [f"{feature_names[i]} ({sv[i]:+.3f})" for i in top_idx]
    except Exception:
        flags = []

    return {"label": label, "confidence": round(confidence, 4), "flags": flags}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("ai:app", host="0.0.0.0", port=8000, reload=True)