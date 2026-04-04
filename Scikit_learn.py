from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier

#Linear Regression
# Step 1: Data
X = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]

# Step 2: Create model
model = LinearRegression()

# Step 3: Train
model.fit(X, y)

# Step 4: Predict
result = model.predict([[5]])

print(result)


#Decision Tree Classifier
# Data: [height, weight]
X = [[150, 50], [160, 60], [170, 70], [180, 80]]
y = ["short", "short", "tall", "tall"]

model = DecisionTreeClassifier()
model.fit(X, y)

print(model.predict([[165, 65]]))