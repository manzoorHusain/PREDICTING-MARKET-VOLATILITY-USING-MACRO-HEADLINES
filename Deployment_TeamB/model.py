import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from sklearn.naive_bayes import GaussianNB
class Models():
    def __init__(self):
        pass
    def convert(self,x):
        if x < -0.5:
            return -1
        elif x > 0.5:
            return 1
        else:
            return 0

    def SentimentModel(self,text):
        text=str(text)
        text=text.replace('\d+', '')
        text=text.replace(r'[^\w\s]+', '')
        text=text.replace(r'\^[a-zA-Z]\s+', '')
        text=text.lower()
        sid = SentimentIntensityAnalyzer()
        sentiment=sid.polarity_scores(text)
        score=self.convert(sentiment['compound'])
        return score

    def Stock_model(self,day,month):
        df=pd.read_csv('modeling_data.csv',index_col = 0)
        df["day"] = df['Date'].map(lambda x: pd.to_datetime(x).day)
        df["month"] = df['Date'].map(lambda x: pd.to_datetime(x).month)
        X=df[['day','month']]
        Y=df["SameDay_Binary"]
        smodel = GaussianNB()
        smodel.fit(X,Y)
        return smodel.predict([[int(day),int(month)]])[0]
        

        


