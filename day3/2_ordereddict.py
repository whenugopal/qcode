if __name__ == "__main__":
    from collections import OrderedDict
    ord = OrderedDict()
    iterator = int(input())
    for i in range(iterator):
        line = input().split()
        name,prices = ' '.join(line[:-1]), int(line[-1])
        # prices = list(map(int, price))
        # prices = prices[0]
        if(name in ord):
            ord[name] = ord[name]+prices
        else:
            ord[name] = prices
    for key,value in ord.items():
        print(key,value)