from flask import Flask ,render_template ,request
from model import Models 
app = Flask(__name__)

@app.route("/" , methods=['GET','POST'])
def ModelPredict():
    if request.method == "POST" :
        try:
            choise=request.form["ChooseModel"]
            if(choise == 'StockData'):
                day= request.form["day"]
                month=request.form["month"]
                S=Models()
                score=S.Stock_model(day=day,month=month)
            else:
                semtemental_text= request.form["sentiment"]
                S=Models()
                score=S.SentimentModel(semtemental_text)
            return render_template("index.html" , Sscore=score)
        except:
            return render_template("index.html" )
    else:
        return render_template("index.html" )


if __name__ == "__main__":
    app.run()
