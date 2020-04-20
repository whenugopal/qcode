
if __name__ == '__main__':
    n = int(input())
    # * args concept boii, *[3,5]
    print(*[i*i for i in range(0,n)],sep="\n")