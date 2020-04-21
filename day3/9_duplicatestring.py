string = ['a','b','c','d','c','d','c','d','c','d','c','d']
sub = ['a','b','c']
sublen = 0
for i in range(len(string)-len(sub)+1):
    sublen += len(sub)
    print(string[i:sublen])
