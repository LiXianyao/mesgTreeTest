#-*-coding:utf-8-*-#
from Trie import TrieNode
from sort import heap
resultDict = {} #存储结果的字典结构

def insertMsg(rootNode,Msg,no):
    #root是字典树的根节点，Msg是某条短信（只有关键词部分的内容）,no是句子的序号（保存在树中用来标识结果模板都有哪些句子）
    loc = 0
    lenMsg = len(Msg)
    now = rootNode
    deepth = 1
    lenLowb = lenMsg/2
    rootNode.listlen +=1
    rootNode.matchWord(Msg,lenMsg,loc,no,deepth, lenLowb) #从根节点开始，以回溯法把句子Msg插入字典树,

if __name__ == '__main__':
    #这里将输入数据读入（已分词？未分词？）
    keywords = []  # 假设这里存关键词
    #sentenses = [[u'我',u'是',u'中国人'],[u'中国人',u'是',u'我'],[u'我',u'爱',u'二次元'],[u'我',u'是',u'北邮人'],[u'我',u'爱',u'北邮'],[u'我',u'爱',u'熬夜',u'写',u'代码']]  # 这里存短信句子
    sentenses = [['逾期', '提醒', '今日', '逾期', '本期', '金额', '今日', '存入', '58车分期']]
    #省略对句子内容的过滤部分，即先认为此时的sentenses已经是只含有关键词的句子集合

    rootNode = TrieNode("")  #根节点
    lenSen = len(sentenses)
    for i in range(0,lenSen):
        insertMsg(rootNode,sentenses[i],i) #将句子依次插入字典树

    #遍历树看看情况
    #rootNode.Trans("")
    mindeep = 2
    nowdeep = 1
    k = lenSen / 2 + 1
    sortHeap = heap(k)
    #rootNode.Trans("")
    rootNode.heapSort("",mindeep,sortHeap,nowdeep)

    vis = [False]*lenSen
    sortHeap.Trans(vis,sentenses)
    print("====未归类=====")
    for i in range(0,lenSen):
        if vis[i] == False:
            out = str(sentenses[i]).replace('u\'', '\'')
            print out.decode("unicode-escape")

