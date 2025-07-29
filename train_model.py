import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load the dataset
data = pd.read_csv('data/food_requirements_by_menu.csv')

# Print the columns to check what we have
print("Dataset columns:", data.columns)

# Selecting features from the dataset (adjust based on your data)
X = data[['People_Count', 'Rice_kg', 'Roti_kg', 'Dal_kg', 'Vegetables_kg', 
          'Chicken_kg', 'Salad_kg', 'Curd_kg']]  # Features

# Assuming 'Total_Food_kg' is the target variable
y = data['Total_Food_kg']  # The target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Check if training starts
print("Training the model...")

# Fit the model to the training data
model.fit(X_train, y_train)

# Check if training is successful
print("Model training completed.")

# Save the trained model as 'model10.pkl'
model_filename = 'model10.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(model, file)

# Confirm that the model is saved
print(f"Model saved as {model_filename}")
