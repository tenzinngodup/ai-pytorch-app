from flask import Flask, render_template, request
import torch

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Load the PyTorch model (replace with your actual model)
    model = torch.nn.Linear(1, 1)

    # Get the input data from the request
    input_data = float(request.form['input_data'])

    # Make a prediction using the model
    output = model(torch.tensor([input_data]))

    # Return the prediction as a string
    return str(output.item())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
