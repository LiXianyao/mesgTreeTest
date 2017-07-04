# -*- coding:utf-8 -*-

import sys
import jieba
import re
import math
from sort import heap
from Trie import TrieNode
reload(sys)
sys.setdefaultencoding('utf-8')


def insertMsg(rootNode,Msg,no):
    #root是字典树的根节点，Msg是某条短信（只有关键词部分的内容）,no是句子的序号（保存在树中用来标识结果模板都有哪些句子）
    loc = 0
    lenMsg = len(Msg)
    now = rootNode
    deepth = 1
    lenLowb = lenMsg/2
    rootNode.matchWord(Msg,lenMsg,loc,no,deepth, lenLowb) #从根节点开始，以回溯法把句子Msg插入字典树,

fr = open("./diction.txt","r")
fc = open("./checkword.txt","r")
check_word = []
ww = fc.readline()
while ww:
    ww = ww.decode("gbk")
    ww = ww.strip()
    check_word.append(ww)
    ww = fc.readline()
line = fr.readline()
while line:
    #line = line.decode("utf-8")
    line = line.strip()
    k_word = {}
    result = []
    temp_r = []
    #对每个分类词打开其分类文件
    path = "./classify/" + line + ".txt"
    print(path)
    dir_file = open(path, "r")

    #将分类词添加到自定义词典中避免被切割
    jieba.add_word(line) 
    mess = dir_file.readline()
    cnt = 0
    while mess:
        cnt += 1
        #mess = mess.decode("utf-8")
        #精确模式分词
        seg_list = jieba.cut(mess, cut_all=False)
        #print("/".join(seg_list))
        #对每一条短信的分词结果进行词频统计
        for seg_word in seg_list:
            #print"***%s***"%seg_word
            if seg_word in k_word:
                k_word[seg_word] += 1
            else:
                k_word[seg_word] = 1
        mess = dir_file.readline()

    #从字典中获取数据对  
    pairs = list(k_word.items())
   
    #列表中的数据对交换位置,按频率由大到小排序 
    exchan_p = [[x,y]for (y,x)in pairs]   
    exchan_p.sort()  
    exchan_p.reverse()
    print "%d"%len(exchan_p)

    limit_n = int(math.log(len(exchan_p))) * 6  #取前n个作为关键词
    print "%d"%limit_n
    #输出词频统计结果
    for i in range(limit_n):
        #print"%s\t%s"%(exchan_p[i][1],str(exchan_p[i][0]))
        Check_F = re.search(ur'(.*[\u4E00-\u9FA5].*)', exchan_p[i][1], re.M | re.I)
        if Check_F != None and exchan_p[i][0] != 1:
            Check_F = Check_F.groups()[0]
            temp_r.append(Check_F)
    result = [word for word in temp_r if word not in check_word]
    for i in result:
        print i
    print "rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr"

    #对每条短信进行关键词筛选处理,并放入字典树
    #rootNode = TrieNode("")  # 根节点
    dir_file.seek(0)   #回到文件头部重新遍历短信
    mess = dir_file.readline()
    cnt = 0
    while mess:
        mes_deal=[]
        seg_list = jieba.cut(mess, cut_all=False)
        for seg_word in seg_list:      #筛出关键词
            if result.count(seg_word) == 1:
                mes_deal.append(seg_word)
        s = str(mes_deal).replace('u\'','\'')
        print s.decode("unicode-escape")
        print "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        #insertMsg(rootNode, mes_deal, cnt)  # 插入字典树
        del mes_deal[:]
        cnt += 1
        mess = dir_file.readline()
        #if cnt == 50:
            #break

    print"===================================="
    '''
    mindeep = 2
    nowdeep = 1
    k = cnt / 2 + 1
    sortHeap = heap(k)
    rootNode.Trans("")
    rootNode.heapSort("", mindeep, sortHeap, nowdeep)
    sortHeap.Trans()
    '''
    k_word.clear()
    del result[:]
    jieba.del_word(line)
    line = fr.readline()
    
