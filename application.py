from flask import Flask,request,render_template,jsonify
from src.pipelines.prediction_pipeline import CustomData,PredictPipeline


application=Flask(__name__)

app=application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
        
    else:
        data=CustomData(
            journey_month=int(request.form.get('journey_month')),
            journey_day =int(request.form.get('journey_day')),
            Price='Price',
            Airline =request.form.get('Airline'),
            Source = request.form.get('Source'),
            Destination =request.form.get('Destination'),
            Total_Stops =request.form.get('Total_Stops')
            
        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)

        return render_template('form.html',final_result=results)
    

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)