def alphanum(string):
    flag = 'False'
    for i in range(len(string)):
        if('a'<= string[i] <= 'z' or 'A' <= string[i] <= 'Z' or 48 <= ord(string[i]) <= 57):
            flag = 'True'
    print(flag)
    return(alpha(string))

def alpha(string):
    flag = 'False'
    for i in range(len(string)):
        if('a'<= string[i] <= 'z' or 'A' <= string[i] <= 'Z'):
            flag = 'True'
    print(flag)
    return(num(string))

def num(string):
    flag = 'False'
    for i in range(len(string)):
        if(48 <= ord(string[i]) <= 57):
            flag = 'True'
    print(flag)
    return(lower(string))

def lower(string):
    flag = 'False'
    for i in range(len(string)):
        if('a'<= string[i] <= 'z'):
            flag = 'True'
    print(flag)
    return(upper(string))

def upper(string):
    flag = 'False'
    for i in range(len(string)):
        if('A' <= string[i] <= 'Z'):
            flag = 'True'
    print(flag)

if __name__ == '__main__':
    mstring = input().strip()
    alphanum(mstring)