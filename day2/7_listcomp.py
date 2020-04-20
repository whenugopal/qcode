if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i,j,k] for i in range(n) for j in range(n) for k in range(n) if(i+j+k != n)])