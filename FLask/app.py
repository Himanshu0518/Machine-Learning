from flask import Flask , redirect , render_template , request 
import numpy as np
import pickle 

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

def predict(input_list):
    input_list = np.asarray(input_list)
    input_list = input_list.reshape(1,-1)
    model = pickle.load(open('trained_model.sav','rb')) 
    prediction = model.predict(input_list) 
    return prediction[0]

@app.route('/result',methods=['POST'])

def result():
    if(request.method == 'POST') :
      try:
        to_pred = request.form.to_dict()
        to_pred = list(to_pred.values())
        to_pred = list(map(float,to_pred))
        result = predict(to_pred)
        if int(result) == 1:
            pred = 'Person has diabetes'
        else:
            pred = 'Person is non diabetic'
        return render_template('index.html',prediction=pred)
      except Exception as e :
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)