from sklearn import svm,metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

#키와 몸무게 GET!
tbl = pd.read_csv("./bmi.csv")

#칼럼자르기
label = tbl["label"]
w = tbl["weight"] / 100
h = tbl["height"] / 200
wh = pd.concat([w,h],axis=1)

#학습전용데이터, 테이스전용데이터 나누기
data_train,data_test,label_train,label_test = train_test_split(wh,label)

#데이터 학습하기
clf=svm.SVC()
clf.fit(data_train,label_train)

#데이터 예측
predict = clf.predict(data_test)

#결과확인
ac_score = metrics.accuracy_score(label_test,predict)
cl_repost = metrics.classification_report(label_test,predict)

print("정답률 = ",ac_score)
print("리포트 = \n",cl_repost)