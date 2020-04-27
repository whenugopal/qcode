def merge_the_tools(string, k):
    lk = 0
    for i in range(0,len(string),k):
        list1 = ''
        test = string[i:k+lk]
        test = ''.join([j for i,j in enumerate(test) if j not in test[:i]])
        print(test)
        lk = lk + k
                
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)