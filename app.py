# app.py
from flask import Flask, request, send_from_directory
from flask_restful import Resource, Api
import joblib
import pandas as pd  # Make sure to import Pandas if needed
import numpy as np  # Import NumPy for array operations

app = Flask(__name__)
api = Api(app)

# Load your machine learning model
model_path = 'polishbankmodel.pkl'  # Update with the actual path
model = joblib.load(model_path)

class PredictResource(Resource):
    def get(self):
        return {'message': 'Use POST request to submit data for prediction.'}

    def post(self):
        data = request.get_json(force=True)
        input_data = data.get('input_data', None)

        if input_data is None:
            return {'error': 'Input data is missing'}, 400

        try:
            # Parse the string representation of the array
            input_array_str = input_data.strip("[]")  # Remove square brackets
            input_array = [float(value) for value in input_array_str.split(',')]  # Convert to list of floats

            # Ensure that the input_array is a 1D array
            input_array = np.array(input_array).reshape(1, -1)

            # Perform prediction
            prediction = model.predict(input_array)

            return {'prediction': prediction.tolist()}
        except Exception as e:
            return {'error': f'Prediction failed: {str(e)}'}, 500


# Add the route to serve the index.html file
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

api.add_resource(PredictResource, '/predict')

if __name__ == '__main__':
    app.run(debug=True)
 