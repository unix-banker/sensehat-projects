import pandas as pd 

import numpy as np 

import joblib 

from sense_hat import SenseHat 

import time 

 

# Load the trained model 

loaded_model = joblib.load('trained_model.pkl') 

 

# Initialize Sense HAT 

sense = SenseHat() 

 

# Function to collect sensor data and make predictions 

def predict_gesture(): 

    while True: 

        # Collect new sensor data 

        a = sense.get_accelerometer_raw() 

        m = sense.get_compass_raw()
        
        g = sense.get_gyroscope_raw()

         

        # Prepare the data for prediction 

        new_data = np.array([[g['y'], g['x'], g['z'], a['x'], a['y'], a['z'], m['x'], m['y'], m['z']]]) 

         

        # Make prediction 

        predicted_gesture = loaded_model.predict(new_data) 

         

        # Print the predicted gesture 

        print("Predicted gesture:", predicted_gesture) 

         

        # Add a delay (adjust as needed) 

        time.sleep(3) 

 

# Start the gesture prediction loop 

predict_gesture() 