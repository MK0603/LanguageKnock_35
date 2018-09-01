# coding: UTF-8
from LanguageKnock_30 import makeMecabPattern


class extractVersMethods:
    def checkNovel(self, novelListS):
        wordDic={}
        nounList=[]
        for sentenseList in novelListS:
            i=0
            while i<len(sentenseList):
                wordDic=self.getNounList(sentenseList,i)
                if len(wordDic["nounList"])>0:
                    nounList.append(wordDic["nounList"])
                i=max(i+1,wordDic["counter"])
        return nounList

    def getNounList(self, sentenseList,i):
        wordDic={}
        nounList=[]
        j=0
        if sentenseList[i]["pos"]=="名詞" and sentenseList[i+1]["pos"]=="名詞":
            nounList.append(sentenseList[i]["surface"])
            nounList.append(sentenseList[i+1]["surface"])
            for j in range (i+2,len(sentenseList)):
                if sentenseList[j-1]["pos"]=="名詞" and sentenseList[j]["pos"]=="名詞":
                    nounList.append(sentenseList[j]["surface"])
                else:
                    break
        wordDic.setdefault("nounList",nounList)
        wordDic.setdefault("counter",j)
        return wordDic
                


if __name__ == '__main__':
    cal = extractVersMethods()
    novelListS = makeMecabPattern()
    ans = cal.checkNovel(novelListS)
    print (ans)
