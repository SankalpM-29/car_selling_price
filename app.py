
import pandas as pd
from flask import Flask, jsonify, request, render_template
import pickle
import preprocess

# load model
model = pickle.load(open('./models/model.pkl','rb'))

app = Flask(__name__)

# home page route to take input values
@app.route('/') #methods=['POST'])
def home():
    
    return render_template('index.html')


# to return the result  
@app.route('/predict', methods = ['POST'])
def predict():
    
    # getting all the inputted form values as a dict
    response = request.form.to_dict()
    values = list(response.values())
    final_input = preprocess.get_input(values)
    output = model.predict(final_input)
    return render_template('output.html', output = output[0].round(2))
    
if __name__ == '__main__':
    app.run()#, debug=True)