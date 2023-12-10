import joblib

class MLModel:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, input_data):
        # Add any preprocessing if needed
        prediction = self.model.predict(input_data)
        return prediction
