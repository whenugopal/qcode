if __name__ == '__main__':
    def sortof(listo):
        for iterator in range(len(listo)):
            for loc in range((len(listo)-iterator-1)):
                if (listo[loc] > listo[loc+1]):
                    listo[loc],listo[loc+1] = listo[loc+1],listo[loc]
        return listo
   
    # def remover(list1,item):
    #     list2 = []
    #     for i in range(len(list1)):
    #         if(item != list1[i]):
    #             list2.append(list1[i])
    #     return list2


    n = int(input())
    list1 = []
    for i in range(n):
        command,*value =  input().split()
        values = list(map(int , value))
        if (command == 'insert'):
            list1.insert(values[0],values[1])
        if (command == 'print'):
            print(list1)
        if (command == 'remove'):
            list1 = list1.remove(values[1])
        if (command == 'append'):
            list1.append(values[0])
        if (command == 'sort'):
            list1 = sortof(list1)
        if (command == 'pop'):
            list1 = list1[:-1]
        if (command == 'reverse'):
            list1  = list1[::-1]
