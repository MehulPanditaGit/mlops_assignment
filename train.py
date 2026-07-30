from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# Train model
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predict & Evaluate
predictions = clf.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Training Complete! Accuracy: {accuracy * 100:.2f}%")