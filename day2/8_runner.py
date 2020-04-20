if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()[:n]))
    big = 0
    sbig = 0
    for i in range(n):
        if(arr[i]>big and arr[i]!= big):
            sbig = big
            big = arr[i]
        else:
            if(arr[i] != big):
                if(sbig<arr[i]):
                    sbig = arr[i]
                else:
                    if(sbig > arr[i]):
                        sbig = arr[i]
                        if (sbig > big):
                            temp = big
                            big = sbig
                            sbig = temp    
    print(sbig)
