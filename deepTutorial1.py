from sklearn import svm,metrics
import pandas as pd

xor_input = [
    #P,Q,result
    [1,"A"],
    [2,"B"],
    [3,"C"],
    [4,"D"]
]

xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.ix[:,0:0]
xor_label = xor_df.ix[:,1]

clf = svm.SVC()
clf.fit(xor_data,xor_label)
pre = clf.predict(xor_data)

as_score = metrics.accuracy_score(xor_label,pre)
print(as_score)





