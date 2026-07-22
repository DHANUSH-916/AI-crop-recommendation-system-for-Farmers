
# Re-train model
from sklearn.ensemble import RandomForestClassifier
import pandas as pd, pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data=pd.read_csv("crop_data.csv")
X=data.drop("label",axis=1)
y=data["label"]
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.2,random_state=42)
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(Xtr,ytr)
acc=accuracy_score(yte,model.predict(Xte))
with open("model.pkl","wb") as f:
    pickle.dump((model,X.columns,acc),f)
print("Model trained | Accuracy:",acc*100,"%")
