import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = np.random.rand(200, 10) * [100, 30, 20, 10, 100, 5, 3, 3, 3, 1]
y = np.random.choice([0, 1], size=200, p=[0.7, 0.3])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "model.joblib")
print("✅ Dummy model saved as model.joblib")