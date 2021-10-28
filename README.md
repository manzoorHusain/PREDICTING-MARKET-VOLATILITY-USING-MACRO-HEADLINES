# PREDICTING-MARKET-VOLATILITY-USING-MACRO-HEADLINES-MLD
We predict equity market vol using tweets from major news sources, hedge funds and investment banks, and notable economists.

---
## Scrapping tweets from twitter and Stock data from NASDAQ
we have downloaded 6 months fainancial data for 5 companies and scrapped the tweets using `snscrape` midule.


---
## Stock data Preprocessing and Labeling
### Preprosseccing:
fristly:Inserting missing Weekend days,then removing dollar sign and coverting columns to numerical and
filling null values.Afterthat, splitting date colume into (day,month,year) numerical values.
### Labelng:
A) For Binary classification:
1.Same Day approch:


```python
df['SameDay_Binary']=0
for i in range(183):
    df['SameDay_Binary'][i]=int(np.sign(df['Close/Last'][i]-df['Open'][i]))
```
2.Previous day approach :

```python
df['PreviousDay_Binary']=0
for i in range(183):
    try:
        df['PreviousDay_Binary'][i]=int(np.sign(df['Close/Last'][i]-df['Close/Last'][i-1]))
    except KeyError:
        df['PreviousDay_Binary'][i]=int(np.sign(df['Close/Last'][i]-np.mean(df['Close/Last'])))
```
and then Mapping labels to (0 and 1).

B) Percentage Change technique:

1.Same day approach :
```python
df['SameDay_Percentage']=0.0
for i in range(183):
    df['SameDay_Percentage'][i]=((df['Close/Last'][i]-df['Open'][i])/df['Open'][i])*100
```
2.Previous day percentage :

```python
df['PreviousDay_Percentage']=0.0
for i in range(183):
    try:
        df['PreviousDay_Percentage'][i]=(((df['Close/Last'][i]-df['Open'][i-1])/df['Open'][i-1])*100)
    except KeyError:
        df['PreviousDay_Percentage'][i]=(((df['Close/Last'][i]-np.mean(df['Open']))/np.mean(df['Open']))*100)
```
and finally mapping to (0,1,-1)

---
## NLP on twitter data

we used nltk library to do sentiment analysis.it removes the undefined symbols and stopping words then uses the predefined dictionary to classify tweets into (positive,negative,and neutral)

---
## Modeling
our model is to predict increase of=r decrease in market volatility 
A.Stock data model:
*1) Naive Bayes : *
with usage of `GaussianNB()` module.
we used (day,month) as inputs and then predict (0 for decrease , 1 for increase) for both sameday and previousday approch.
We achived average accuracy 65% for sameday approch and 58% for previousday approach.

*2) PCA with Logistic Regression :*

Firstly we applied `StandardScaler` then `PCA` to perform scaling and dimentionality reduction.Afterthat we applied LogisticRegression model.
we used (volume,high,low,day,month) as input features and predict (0 for neutral , 1 for increae , -1 for decrease)
Achieved Accuracy is 55% for sameday approach and 35% for previousday approach

B.Sentimental Model : 

to have any twitter sentiment as input and predict the volatilty based on its meening.

---
## *Deployment Process*
we have used Flask and python as a Backened for our webapp and HTML,CSS for Frontend then we Deployed it using Heroku app 

### *Deployment link*
[Link](https://marketvolatiltypredection.herokuapp.com/)
