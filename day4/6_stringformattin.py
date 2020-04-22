from __future__ import print_function

def print_formatted(number):
    w = len(bin(number)[2:])
    for number in range(1,number+1):
        print(str(number).rjust(w,' '),str(oct(number)[2:]).rjust(w,' '),str(hex(number).swapcase()[2:]).rjust(w,' '),str(bin(number)[2:]).rjust(w,' '),sep=' ')
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)