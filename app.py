
from flask import Flask,render_template,request
import pickle
import pandas as pd

fertilizer={
"Rice":"Urea, DAP",
"Maize":"Urea, MOP",
"Wheat":"Urea, SSP",
"Cotton":"NPK 20-20-0",
"Sugarcane":"Urea, Potash",
"Tomato":"NPK 19-19-19",
"Onion":"DAP, Potash",
"Potato":"Urea, Potash",
"Brinjal":"NPK 10-26-26",
"Chilli":"DAP, NPK"
}

app=Flask(__name__)
model,columns,acc=pickle.load(open("model.pkl","rb"))

@app.route("/",methods=["GET","POST"])
def index():
    result=None; fert=None; probs=None
    if request.method=="POST":
        vals=[float(request.form[x]) for x in columns]
        df=pd.DataFrame([vals],columns=columns)
        result=model.predict(df)[0]
        fert=fertilizer.get(result)
        p=model.predict_proba(df)[0]
        probs=sorted(zip(model.classes_,p),key=lambda x:x[1],reverse=True)
    return render_template("index.html",result=result,fert=fert,probs=probs,acc=round(acc*100,2))

if __name__=="__main__":
    app.run(debug=True)
