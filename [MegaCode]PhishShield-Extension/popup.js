document.addEventListener("DOMContentLoaded", () => {
  const urlDisplay = document.getElementById("urlDisplay");
  const manualResult = document.getElementById("manualResult");
  const aiResult = document.getElementById("aiResult");
  const aiScanBtn = document.getElementById("aiScanBtn");
  const userUrlInput = document.getElementById("userUrl");
  const submitUrlBtn = document.getElementById("submitUrlBtn");

  let currentUrl = "";

  // 🔹 Auto-load current tab URL and scan
  chrome.storage.local.get("currentUrl", async (data) => {
    currentUrl = data.currentUrl || "";
    urlDisplay.textContent = `URL: ${currentUrl || "No URL found"}`;

    if (currentUrl.startsWith("http")) {
      await runManualScan(currentUrl);
      await runAIScan(currentUrl);
    }
  });

  // 🔹 Manual URL input
  submitUrlBtn.addEventListener("click", async () => {
    const inputUrl = userUrlInput.value.trim();
    if (!inputUrl.startsWith("http")) {
      urlDisplay.textContent = "⚠ Invalid URL format";
      manualResult.textContent = "";
      aiResult.textContent = "";
      return;
    }

    currentUrl = inputUrl;
    urlDisplay.textContent = `URL: ${currentUrl}`;
    manualResult.textContent = "Manual Scan: ⏳ Checking...";
    aiResult.textContent = "";

    await runManualScan(currentUrl);
    await runAIScan(currentUrl);
  });

  // 🔹 AI Scan button
  aiScanBtn.addEventListener("click", async () => {
    if (!currentUrl.startsWith("http")) {
      aiResult.textContent = "AI Scan: ⚠ Invalid URL";
      return;
    }

    await runAIScan(currentUrl);
  });

  // 🔹 Manual Scan with timeout
  async function runManualScan(url) {
    const apiKey = "YOUR_GOOGLE_SAFE_BROWSING_API_KEY"; // Replace with your actual key
    const endpoint = `https://safebrowsing.googleapis.com/v4/threatMatches:find?key=${apiKey}`;

    const requestBody = {
      client: {
        clientId: "phishshield",
        clientVersion: "1.0"
      },
      threatInfo: {
        threatTypes: ["MALWARE", "SOCIAL_ENGINEERING"],
        platformTypes: ["ANY_PLATFORM"],
        threatEntryTypes: ["URL"],
        threatEntries: [{ url }]
      }
    };

    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 5000); // 5 seconds

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        body: JSON.stringify(requestBody),
        headers: { "Content-Type": "application/json" },
        signal: controller.signal
      });

      clearTimeout(timeout);
      const result = await response.json();

      if (result && result.matches && result.matches.length > 0) {
        manualResult.textContent = "Manual Scan: ❌ Malicious";
      } else {
        manualResult.textContent = "Manual Scan: ✅ Safe";
      }
    } catch (err) {
      clearTimeout(timeout);
      if (err.name === "AbortError") {
        manualResult.textContent = "Manual Scan: ⏳ Timed out";
      } else {
        manualResult.textContent = "Manual Scan: ⚠ Error";
        console.error("Manual scan error:", err);
      }
    }
  }

  // 🔹 AI Scan via Python backend
  async function runAIScan(url) {
    aiResult.textContent = "AI Scan: ⏳ Running...";

    try {
      const aiResponse = await fetch("http://localhost:8000/ai/scan", {
        method: "POST",
        body: JSON.stringify({ url }),
        headers: { "Content-Type": "application/json" }
      });

      const aiData = await aiResponse.json();
      aiResult.textContent = `AI Scan: ${aiData.label.toUpperCase()} (${Math.round(aiData.confidence * 100)}%)`;

      if (aiData.flags && aiData.flags.length > 0) {
        const flagsList = aiData.flags.map(f => `• ${f}`).join("\n");
        aiResult.textContent += `\n${flagsList}`;
      }
    } catch (err) {
      aiResult.textContent = "AI Scan: ⚠ Error";
      console.error("AI scan error:", err);
    }
  }
});