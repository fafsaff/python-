list=[
    ["罗恩",23,35,44],
    ["哈利",60, 77 ,68 ,88, 90],
    ["赫敏", 97 ,99 ,89 ,91, 95, 90],
    ["马尔福",100, 85 ,90]
]

for i in range(len(list)):
    score = 0
    for j in range(len(list[i])):
        j+=1
        if j==len(list[i]):
            continue
        else:
            score += int(list[i][j])

    print(list[i][0],"的总成绩为：",score)


    # if i==0:
    #     print("罗恩的总成绩为:",score)
    # elif i==1:
    #     print("哈利的总成绩为:", score)
    # elif i==2:
    #     print("赫敏的总成绩为:", score)
    # elif i==3:
    #     print("马尔福的总成绩为:", score)