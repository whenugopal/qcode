if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()[:n]))
    big = 0
    sbig = 0
    # for i in range(n):
    #     if(arr[i]>big and arr[i]!= big):
    #         sbig = big
    #         big = arr[i]
    #     else:
    #         if(arr[i] != big):
    #             if(sbig<arr[i]):
    #                 sbig = arr[i]
    #             else:
    #                 if(sbig > arr[i]):
    #                     sbig = arr[i]
    #                     if (sbig > big):
    #                         temp = big
    #                         big = sbig
    #                         sbig = temp    
    # print(sbig)
    big = sbig = arr[0];
    for item in range(1,n):
        if(big<arr[item] ):
            sbig = big
            big = arr[item]
            continue
        elif(big == arr[item]):
            continue
        else:
            if(sbig == big or sbig <= arr[item]):
                sbig = arr[item]
                continue
    print(sbig)