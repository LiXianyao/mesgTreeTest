# -*- coding: utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def notNum(str):
    matchNum = re.search("^[0-9]+$",str)
    if matchNum == None:
        return True
    return False

fr = open("./model/2.txt","r")
fw = open("mydict.txt","w")
fwdir = {}
diction = []
lineRecord = {}
line = fr.readline()
c = 0
while line:
    # print c
    headRe = re.search(r'^【(.*?)】', line, re.M | re.I)
    if headRe != None:
        headRe = headRe.groups()[0].decode('utf-8')
        lineRecord[c] = headRe
        if (headRe in diction) == False and notNum(headRe):
            diction.append(headRe)
            fw.write(headRe+'\n')
            fwdir[headRe] = open("./model/group-key/" + headRe + ".txt", "a")
            # print(headRe)

    else:  # 句首没有标签
        tailRe = re.search(r'【([^】]*?)】$',line,re.M | re.I|re.U)
        if tailRe == None:
            tailRe = re.search(r'【([^【]*?)】$',line,re.M | re.I|re.U)
        if tailRe != None:
            tailRe = tailRe.groups()[0].decode('utf-8')
            lineRecord[c] = tailRe
            if (tailRe in diction) == False and notNum(tailRe):
                diction.append(tailRe)
                #print(tailRe)
                fwdir[tailRe] = open("./model/group-key/" + tailRe + ".txt", "a")
                fw.write(tailRe+'\n')
        else:  # 句首句尾都没有标签
            lineRecord[c] = "KeyWordUndefined"

    line = fr.readline()
    c += 1
fwdir["KeyWordUndefined"] = open("./model/group-key/" + "KeyWordUndefined" + ".txt", "a")
fr.close()
fw.close()

# 从头读
fr = open("./model/2.txt", "r")
line = fr.readline()
c = 0
while line:
    filename = lineRecord[c]
    fw = fwdir[filename]
    fw.write(line + '\n')
    line = fr.readline()
    c += 1

for fd in fwdir:
    fwdir[fd].close()
fr.close()