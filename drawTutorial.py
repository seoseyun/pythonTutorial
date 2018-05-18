import matplotlib.pyplot as plt
import pandas as pd
import json

#해당숫자별 각 그레이스케일 빈도 읽어들이기
with open("./mnist/numCnt.json","r",encoding="utf-8") as fp:
    freq=json.load(fp)

num_dic = {}
#각 숫자마다 계산하기
for i in range(10):
    num_dic[i] = [0 for n in range(256)]
    for j in range(256) :
        num_dic[i][j] = freq[i][j]

asclist = [[n for n in range(256)]]
df = pd.DataFrame(num_dic,index=asclist)

plt.style.use('ggplot')
df.plot(kind = "line")
plt.savefig("test.png")
