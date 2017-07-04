#-*-coding:utf-8-*-#
from sort import heapNode

class TrieNode:
    def __init__(self,keyword):
        self.keyword = keyword  #该节点对应的关键词
        self.list = []          #能与该节点匹配成功的句子编号列表
        self.listlen = 0
        self.children = {}     #该节点的子节点列表,"子节点的词"：子节点对象

    def addChild(self,childNode):
        #children中插入一个新点，dict的key为节点的关键词
        self.children[childNode.keyword] = childNode

    def getListLen(self):
        return len(self.list)

    def addList(self,no):
        if no in self.list:
            return
        self.list.append(no)
        self.listlen += 1

    def matchWord(self,Mesg,lenMesg,loc,no,deepth,lenLowb): #递归回溯法插入节点
        #print "%s %s %d %d %d"%(self.keyword,Mesg,lenMesg,loc,no)
        if loc >= lenMesg or (deepth + (lenMesg - loc) < lenLowb): #递归到了句子结尾，结束
            return

        while loc<lenMesg: #对每一层，它都试图和字符串当前位置之后的每个词为开头的子句做一次匹配
            if Mesg[loc] in self.children: #当前节点的后代中有可用匹配上的词
                next = self.children.get(Mesg[loc]) #取出对应的字典树节点
                next.addList(no)                    #添加匹配句子编号队列
                next.matchWord(Mesg,lenMesg,loc+1,no,deepth + 1,lenLowb)  #对这个对象递归处理
            else:#当前节点的后代中没有以 Mesg[loc]开头的子句
                newNode = TrieNode(Mesg[loc])
                self.addChild(newNode)  #新点是当前点的一个新后代
                newNode.addList(no)     #新句子当然包含了本身
                newNode.matchWord(Mesg,lenMesg,loc+1,no, deepth + 1,lenLowb) #对新点递归处理
            #当前点匹配下一个位置
            loc += 1

    def Trans(self,roadRecord):
        for childkey in self.children:
            child = self.children[childkey]
            child.Trans(roadRecord+child.keyword+",")
        print ("%s %d %s")%(roadRecord,self.getListLen(),self.list)

    def heapSort(self,str,deepLBD,heap,nowDeep):
        for childkey in self.children:
            child = self.children[childkey]
            newNode = heapNode(str+child.keyword+",",child.getListLen(),child.list)
            if(nowDeep>=deepLBD) and (child.listlen>1) and (child.listlen >= self.listlen*0.3):
                heap.addHeap(newNode)
            child.heapSort(str+child.keyword+",",deepLBD,heap,nowDeep+1)