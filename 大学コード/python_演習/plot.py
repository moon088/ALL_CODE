#matplotlib出力
import numpy as np
import matplotlib.pyplot as plt
import random


left = np.array([0,1,2,3,4,5,6,7,8,9])

trial = 10000
height = np.array([0]*len(left))

for i in range(trial):
    trial_num = int(random.random()*10)
    height[trial_num] += 1
    
plt.title("ランダム関数による数値カウント")
plt.xlabel("各数値")
plt.ylabel("出現回数")

plt.bar(left,height,align="center",)
plt.show()

