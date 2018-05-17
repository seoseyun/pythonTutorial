from sklearn import  svm,metrics
import random, re
import pandas as pd
from sklearn.model_selection import train_test_split

csv = []

csv = pd.read_csv('./iris.csv')
csv_data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
csv_label = csv["Name"]
training_data, test_data, training_label, test_label = train_test_split( csv_data,csv_label )

#학습시키기
clf = svm.SVC()
clf.fit(training_data,training_label)
pre = clf.predict(test_data)


#정답률!
ac_score = metrics.accuracy_score(test_label,pre)
print(ac_score)