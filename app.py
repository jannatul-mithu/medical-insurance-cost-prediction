import numpy as np
from flask import Flask, render_template, request
# from flask import jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open('rfr_model_with_standardization.pkl', 'rb')) 
   

@app.route("/")
# @app.route("/home")

# def home_page():
def home_page():
    return  render_template("index.html")

@app.route("/result", methods =['POST']) 
# def result_page():
def result():
    if request.method == 'POST':
        
        
        Age = float(request.form['age'])
        BMI = float(request.form['bmi'])
        Children = float(request.form['children'])
        
        
        
        
        # Gender
        Gender = request.form['gender']
        Gender = Gender.lower()
        if Gender == 'male':
            Gender=0
        elif Gender == 'female':
            Gender=1
        else:
            print("Enter right value in Gender")
         
            
         
        # Smoking Habit
        Smoker = request.form['smoker']
        Smoker = Smoker.lower()
        if Smoker == 'no':
            Smoker=0
        elif Smoker == 'yes':
            Smoker=1
        else:
            print("Enter right value in Somking Habit")



        # Region
        Region = request.form['region']
        Region = Region.lower()
        if Region == 'northeast':
            Region=1
        elif Region == 'northwest':
            Region=2
        elif Region == 'southeast':
            Region=3
        elif Region == 'southwest':
            Region=4
        else:
            print("Enter right value in Region")
        
        

    input_query = np.array([[Age,Gender,BMI,Smoker,Region,Children]])
    prediction = model.predict(input_query)[0]
#    output = round(prediction[0], 2)
#    return jsonify({'diabetes':str(result)})
    return render_template("index.html", prediction_text="Your medical insurance cost is: $ {}".format(prediction))




if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
    