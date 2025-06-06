from flask import Flask,render_template,request,jsonify

from src.utils import load_object
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)
app=application


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results = predict_pipeline.predict(pred_df)
        formatted_result = f"{results[0]:.2f}"
        
        return jsonify({"prediction": formatted_result})
        #return render_template('home.html', results=formatted_result)

    

if __name__=="__main__":
    app.run(host="0.0.0.0")        