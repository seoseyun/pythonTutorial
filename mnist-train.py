from sklearn import model_selection,svm,metrics
import json

cnt = [[] for n in range(10)]

for i in range(10):
    cnt[i] = [0 for n in range(0,256)]

print(cnt)
#csv파일 읽고 가공

def load_csv(fname):
    global cnt
    labels = []
    images = []



    with open(fname,"r") as f:
        for line in f:
            cols = line.split(",")
            if cols[0].isdigit():
                label = int(cols[0])
            print(label)
            if len(cols) < 2: continue #라벨만 있는 경우
            labels.append(int(cols.pop(0)))
            vals = list(map(lambda n :int(n)/256,cols))
            if cols[0].isdigit():
                for num in cols:
                    num = int(num)
                    cnt[label][num] += 1
            images.append(vals)
    return {"labels":labels,"images":images}

data = load_csv("./mnist/train.csv")
test = load_csv("./mnist/t10k.csv")

with open("./mnist/numCnt.json","w",encoding="utf-8") as fp:
    json.dump(cnt,fp)

#학습하기
clf = svm.SVC()
clf.fit(test["images"],test["labels"])

#예측하기
predict = clf.predict(data["images"])

#결과확인
ac_score = metrics.accuracy_score(data["labels"],predict)
cl_report = metrics.classification_report(data["labels"],predict)
print("정답률 =",ac_score)
print("리포트 = ")
print(cl_report)