import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Machine Downtime Prediction API!"})


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract JSON input
        data = request.get_json(force=True)

        # Ensure required features are in the input
        required_features = [
            'Hydraulic_Pressure(bar)', 'Coolant_Pressure(bar)',
            'Air_System_Pressure(bar)', 'Coolant_Temperature',
            'Hydraulic_Oil_Temperature(?C)', 'Spindle_Bearing_Temperature(?C)',
            'Spindle_Vibration(?m)', 'Tool_Vibration(?m)', 'Spindle_Speed(RPM)',
            'Voltage(volts)', 'Torque(Nm)', 'Cutting(kN)'
        ]
        if not all(feature in data for feature in required_features):
            return jsonify({"error": f"Missing required features: {required_features}"}), 400

        # Convert input values to a numpy array
        input_features = np.array([[data[feature] for feature in required_features]])

        # Make prediction
        prediction = model.predict(input_features)
        output = prediction[0]

        # Map output to a downtime status
        downtime_status = "Yes" if output == 1 else "No"

        # Get prediction probability (confidence)
        confidence = model.predict_proba(input_features).max()

        return jsonify({
            "Downtime": downtime_status,
            "Confidence": round(confidence, 2),
            "Input_Features": data
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
