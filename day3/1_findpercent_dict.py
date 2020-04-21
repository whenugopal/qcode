def sumof(glist):
    sum = 0
    for x in glist:
        sum = sum+x
    return sum
def lenof(glist):
    count = 0
    for x in glist:
        count = count + 1
    return count

if __name__ == '__main__':
    student_scores = {}
    n = int(input())
    for _ in range(n):
        name, *scoresline = input().split()
        scores  = list(map(float ,scoresline))
        student_scores[name] = scores
    query = input()
    avg = student_scores[query]
    print('{:.2f}'.format(sumof(avg)/lenof(avg)))