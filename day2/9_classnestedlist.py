# Takes student name with score and prints the second least scores

if __name__ == '__main__':
    nl = [] # For student entire data
    scorelist = [] # seperate list for scores
    scorelist2 = [] # you will know why
    smallgradekid = [] # yes, read the name.
    for _ in range(int(input())): #getting values 
        name = input()
        score = float(input())
        scorelist.append(score)
        nl.append([name,score])
    for i in range(len(nl)): # sorting scorelist
        for j in range(len(nl)-i-1):
            if(scorelist[j]>scorelist[j+1]):
                scorelist[j],scorelist[j+1] = scorelist[j+1],scorelist[j]
    for i in range(len(scorelist)): # retriving 
        if (scorelist[0] != scorelist[i]):
            scorelist2.append(scorelist[i])
    smallmax = min(scorelist2)
    for k in range(0,len(nl)): # getting smallgradekid
        if(nl[k][1]==smallmax):
            smallgradekid.append(nl[k][0]) 
    smallgradekid.sort()
    for i in smallgradekid:
        print(i)
        