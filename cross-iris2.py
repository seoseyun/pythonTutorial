import pandas as pd
from sklearn import svm, metrics, model_selection
import random, re

#붓꽃 csv데이터
csv = pd.read_csv('iris.csv')

#리스트를훈련용데이터,테스트전용 데이터 분할
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv[["Name"]]

#크로스벨리데이션
clf = svm.SVC()
scores = model_selection.cross_val_score(clf,data,label,cv=5)
print(scores)