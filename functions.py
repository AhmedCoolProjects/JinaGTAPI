# graphecolo2=[[1,2,3,4,5],[(1,2),(1,3),(2,3),(3,4),(4,5)]]

def adjacent2(a,b,g):
    resultat=0
    for j in b :
        if ([a,j] in g[1] )or ([j,a] in g[1]):
            resultat+=1
    if resultat!=0:
        return True
    else:
        return False

def coloration2(g):
    nbrcouleur=0
    l=[0]*len(g[0])
    h=[False]*len(g[0])
    for i in range(len(g[0])):
        S=[g[0][i]]
        for j in range(len(g[0])):
            if adjacent2(g[0][j],S,g)==False and h[j]==False:
                l[j]=nbrcouleur
                h[j]=True
                S.append(g[0][j])
        nbrcouleur+=1
    return l
    