#IMPORT LIBRARIES

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score

# LOAD THE DATASET

df = pd.read_csv('results.csv')

# SEPARATE OUR FEATURES AND TARGET

#IMPORT LIBRARIES

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score

# LOAD THE DATASET

df = pd.read_csv('results.csv')

# SEPARATE OUR FEATURES AND TARGET

X = df[["ax", "ay", "az", "gx", "gy", "gz", "mx", "my", "mz"]]

y = df['gesture']

# SPLIT DATA INTO TRAINING AND TESTING DATA

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# USE A DECISIONTREE ALGORITHM

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

# MAKE A PREDICTION ON THE TEST DATA

y_pred = model.predict(X_test)

# EVALUATE THE MODEL

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

import joblib

# Save the trained model

joblib.dump(model, 'trained_model.pkl')

# SPLIT DATA INTO TRAINING AND TESTING DATA

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# USE A DECISIONTREE ALGORITHM

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

# MAKE A PREDICTION ON THE TEST DATA

y_pred = model.predict(X_test)

# EVALUATE THE MODEL

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

import joblib

# Save the trained model

joblib.dump(model, 'trained_model.pkl')