from sklearn import svm,metrics
import random,re

#read Data
lines = open('iris.csv','r',encoding='utf-8').read().split("\n")
f_tonum = lambda n : float(n) if re.match(r'^[0-9]\.+$' ,n) else n
f_cols = lambda li : list(map(f_tonum,li.strip().split(',')))
csv = list(map(f_cols,lines))
del csv[0]
random.shuffle(csv)

#데이터 k만큼 나누기
k = 5
csvk = [ [] for i in range(k) ]
for i in range(len(csv)):
    csvk[i % k].append(csv[i])

#리스트를 훈련 전용 데이터와 테스트전용 데이터로 분할하는 함수
def split_data_label(rows):
    data=[];label=[];
    for row in rows:
        data.append(row[0:4])
        label.append(row[4])
    return (data,label)

#정답률 구하기
def calc_score(test,train):
    test_f, test_l = split_data_label(test)
    train_f,train_l = split_data_label(train)

    #학습
    clf = svm.SVC()
    clf.fit(train_f,train_l)
    pre = clf.predict(test_f)
    return metrics.accuracy_score(test_l,pre)

#K개로 분할해서 정답률 구하기
score_list=[]
for testc in csvk:
    #testc 이외의 데이터를 훈련 전용 데이터로 사용하기
    trainc = []
    for i in csvk:
        if i != testc: trainc +=i
    sc = calc_score(testc,trainc)
    score_list.append(sc)

print(score_list)
print(sum(score_list)/len(score_list))
