#-*-coding:utf-8-*-#
class heapNode:
    wordSeq = []
    triePtr = []
    value = 0
    def __init__(self,seq,value,ptr):
        self.wordSeq = seq
        self.value = value
        self.triePtr = ptr

class heap:#小根堆
    def __init__(self,size):
        self.nodeList = [None]*(size+1)
        self.size = 0
        self.MaxSize = size

    def pop(self):
        if(self.size == 0):
            print("heap is already empty")
            return

        self.nodeList[1] = self.nodeList[self.size]
        self.nodeList[self.size] = heapNode("",float('inf'),None) #清理被置换的尾节点为无穷大
        self.size -= 1
        self.pushDown(1)

    def addHeap(self, newNode):
        if self.size == self.MaxSize:#堆已经达到预定的最大容量，不再追加新点，而考虑更新根点
            if self.nodeList[1].value < newNode.value:
                self.pop()
                self.addHeap(newNode)
            elif self.nodeList[1].value == newNode.value and len(self.nodeList[1].wordSeq)<len(newNode.wordSeq):
                self.pop()
                self.addHeap(newNode)
        else:#加新点
            self.size += 1
            self.nodeList[self.size] = newNode
            self.pushUp(self.size) #新的叶节点上浮

    def pushUp(self,pos):
        while(pos>1):
            parent = pos / 2
            # 比较父节点与本节点
            if self.nodeList[pos].value < self.nodeList[parent].value:  # 根节点大于左儿子
                self.nodeList[pos], self.nodeList[parent] = self.nodeList[parent], self.nodeList[pos]
                pos = parent
            elif self.nodeList[pos].value == self.nodeList[parent].value and len(self.nodeList[pos].wordSeq) < len(self.nodeList[parent].wordSeq):
                self.nodeList[pos], self.nodeList[parent] = self.nodeList[parent], self.nodeList[pos]
                pos = parent
            else:  # 浮动不上去，结束
                break

    def pushDown(self,pos):
        while(pos*2<=self.size):
            lch = pos*2
            rch = pos*2 + 1
            #在左右孩子中选择一个较小的（就不用考虑交换一次后再换一次）
            if self.nodeList[rch].value > self.nodeList[lch].value: #根节点大于左儿子
                minch = lch
            elif self.nodeList[rch].value == self.nodeList[lch].value and len(self.nodeList[rch].wordSeq) >= len(self.nodeList[lch].wordSeq):
                minch = lch
            else:
                minch = rch

            #比较父节点与
            if self.nodeList[pos].value > self.nodeList[minch].value: #根节点大于左儿子
                self.nodeList[pos], self.nodeList[minch] = self.nodeList[minch], self.nodeList[pos]
                pos = minch
            elif self.nodeList[rch].value == self.nodeList[lch].value and len(self.nodeList[pos].wordSeq) > len(self.nodeList[minch].wordSeq):
                self.nodeList[pos], self.nodeList[minch] = self.nodeList[minch], self.nodeList[pos]
                pos = minch
            else:#沉不下去，结束
                break

    def Trans(self):
        for i in range(1,self.MaxSize+1):
            if self.nodeList[i] == None:
                continue
            node = self.nodeList[i]
            print ("seq:'%s' has %d sentences are %s" %(node.wordSeq,node.value,node.triePtr))



