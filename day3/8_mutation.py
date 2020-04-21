def mutate_string(string, position, character):
    string = list(string)
    newstring = ""
    string[position] = character
    for i in range(len(string)):
        newstring += string[i]
    return newstring

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)