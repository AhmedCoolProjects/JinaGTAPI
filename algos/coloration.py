# [[1,2,3,4,5,6,7,8,9,10],[[1,2],[1,6],[3,2],[4,5],[6,5],[6,3],[4,7],[5,8],[7,8],[8,10],[8,9],[9,10]]]
# BY ANAS
class Coloration():
    def __init__(self, graph):
        self.graph = graph
    def deg(self,i):
        count = 0
        for j in self.graph[1]:
            if j[0] == i or j[1] == i:
                count+=1
        return count
    def list_deg(self):
        list = []
        for i in self.graph[0]:
            list.append([i,self.deg(i)])
        list.sort(key=lambda x:x[1])
        list.reverse()
        return list
    def adj(self,i,j):
        if [i,j] in self.graph[1] or [j,i] in self.graph[1]:
            return True
        else:
            return False
    def main(self):
        color = 0
        sommetTraite = 0
        D = self.list_deg()
        n = len(D)
        while sommetTraite < n:
            for i in range(n):
                if len(D[i]) == 2:
                    coloPoss = True
                    for j in range (i):
                        if len(D[j])==3 and D[j][2] == color and self.adj(D[i][0],D[j][0])==True:
                            coloPoss = False
                            break
                    if coloPoss:
                            D[i].append(color)
                            sommetTraite += 1
            color+=1
        COLORS_LIST = ["red","blue","green","yellow","orange","purple","brown","pink","grey","black"]
        D2 = []
        for sommetList in D:
            Dtest = {"sommet":"","deg":"","color":""}
            Dtest["sommet"] = sommetList[0]
            Dtest["deg"] = sommetList[1]
            Dtest["color"] = COLORS_LIST[sommetList[2]]
            D2.append(Dtest)

        result = {"colorsCount":color,"finalList":D2}
        return result

