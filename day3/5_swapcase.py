def swap_case(list1):
    li = [ord(i) for i in list1]
    finallist=[]
    for i in range(len(li)):
        if( 65<= li[i] <=90 or 97<= li[i] <=122):
            if(65<= li[i] <=90):
                finallist.append(chr(li[i]+32))
            else:
                finallist.append(chr(li[i]-32))
        else:
            finallist.append(chr(li[i]))
    return list2string(finallist)

def list2string(thisfinal):
    outputstring = ''
    for i in range(len(thisfinal)):
        outputstring += thisfinal[i]
    return outputstring

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)