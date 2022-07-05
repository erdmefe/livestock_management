import itertools
def numDistinct(s, t):
    counter=0
    liste = []
    if len(s) < len(t):
        return 0
    else:
        for i in t:
            temp = []
            for e,q in enumerate(s):
                if i == q:
                    temp.append(int(e))          
            liste.append(temp)
        lastList = list(itertools.product(*liste))               
        for index,i in enumerate(lastList):
            tempList = list(i).copy()
            tempList.sort()
            if tempList != list(i) or len(set(i)) != len(i):
                counter += 1
        return(len(lastList)-counter)
numDistinct("dbaaadcddccdddcadacbadbadbabbbcad","dadcccbaab")