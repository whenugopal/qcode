def count_substring(string, sub):
    subc = 0
    for i in range(len(string)):
        if(len(string[i:])<len(sub)):
            break
        
        if( sub[0] == string[i]):

            yes = 1
            x=i
            for j in range(len(sub)):
                if(sub[j]!=string[x]):
                    yes = 0
                x=x+1
            if(yes == 1):
                subc += 1
    return subc

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
