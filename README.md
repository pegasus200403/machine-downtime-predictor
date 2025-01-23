Overview
This API predicts machine downtime based on various manufacturing parameters such as pressure, temperature, vibration, etc.
It uses a trained machine learning model to classify whether downtime will occur or not.

Features
Predict Downtime: Provide real-time predictions on machine downtime based on input features.
Confidence Score: Returns a confidence score along with the prediction.
Input Validation: Ensures all required features are provided for accurate predictions.

Setup Instructions
Prerequisites
Ensure you have the following installed on your system:

Python 3.7 or higher
pip (Python package manager)

How to run Api:-
Clone API folder to your local computer.Open pycharm and set enviornment of python 3 or higher.Run app.py on pycharm you will get "http://127.0.0.1:5000".

Now,open postman to test the machine learning model

select and open new request,name the request and enter "localhost:5000/predict" and Method: POST whereas select body go to 'raw' and set form to 'JSON' and OUTPUT form as JSON

Enter the input in body:-
input format example:
{
    "Hydraulic_Pressure(bar)": 150,
    "Coolant_Pressure(bar)": 3.2,
    "Air_System_Pressure(bar)": 2.8,
    "Coolant_Temperature": 75,
    "Hydraulic_Oil_Temperature(?C)": 65,
    "Spindle_Bearing_Temperature(?C)": 50,
    "Spindle_Vibration(?m)": 0.003,
    "Tool_Vibration(?m)": 0.004,
    "Spindle_Speed(RPM)": 2000,
    "Voltage(volts)": 220,
    "Torque(Nm)": 35,
    "Cutting(kN)": 10
}


click on send:
we will get ouput as:-
example
    "Confidence": 1.0,
    "Downtime": "Yes",
    "Input_Features": {
        "Air_System_Pressure(bar)": 2.8,
        "Coolant_Pressure(bar)": 3.2,
        "Coolant_Temperature": 75,
        "Cutting(kN)": 10,
        "Hydraulic_Oil_Temperature(?C)": 65,
        "Hydraulic_Pressure(bar)": 150,
        "Spindle_Bearing_Temperature(?C)": 50,
        "Spindle_Speed(RPM)": 2000,
        "Spindle_Vibration(?m)": 0.003,
        "Tool_Vibration(?m)": 0.004,
        "Torque(Nm)": 35,
        "Voltage(volts)": 220
    }
}
Thank You.
