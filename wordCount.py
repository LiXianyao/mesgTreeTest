#-*-coding:utf-8-*-#
import jieba
jieba.load_userdict("mydict.txt")
diction = {}

fr = open("./model/2.txt","r")
line = fr.readline()
c = 0
while line:
    c +=1

    res = jieba.lcut(line)#分词为list
    for word in res:
        if word in diction:
            diction[word] += 1
        else:
            diction[word] = 1

    line = fr.readline()

    if c==100:
        break