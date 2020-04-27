from itertools import permutations

hack,size = input().strip().split(" ")
hack = sorted(hack)
print(*[''.join(i) for i in permutations(hack,int(size))],sep='\n')