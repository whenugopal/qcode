# Got to know that its linked with FLAT subject

def minion_game(string):
    ks = ss= 0
    sl = len(string)
    itrtr = 0
    for i in range(sl):
        itrtr = sl - i
        if string[i] in 'AEIOU': ks += itrtr
        else: ss += itrtr
    if ks > ss: print("Kevin", ks)
    elif ks<ss : print("Stuart", ss)
    else: print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)