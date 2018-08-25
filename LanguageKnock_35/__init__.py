# coding: UTF-8
from LanguageKnock_30 import makeMecabPattern


class extractVersMethods:
    def checkNovel(self, novelListS):
        nounList=[]
        for sentenseListS in novelListS:
            nounList.append(self.getNounList(sentenseListS))
        return nounList
            
            
    def getNounList(self, sentenseListS):
        nounList=[]
        nounList.append(self.searchNoun(sentenseListS))
        return nounList
        
    def searchNoun(self, sentenseList):
        nounList=[]
        for i in range(len(sentenseList)):
            if sentenseList[i]["pos"]=="名詞" and sentenseList[i+1]["pos"]=="名詞":
                nounList.append(sentenseList[i]["surface"])
                nounList.append(sentenseList[i+1]["surface"])
                nounList.append(self.listupNoun(i,sentenseList))
        return nounList

    def listupNoun(self, i,sentenseList):
        nounList=[]
        for j in range (i+2,len(sentenseList)):
            if sentenseList[j]["pos"]=="名詞":
                nounList.append(sentenseList[j]["surface"])
            else:
                return None
        return nounList


if __name__ == '__main__':
    cal = extractVersMethods()
    novelListS = makeMecabPattern()
    ans = cal.checkNovel(novelListS)
    print (ans)
