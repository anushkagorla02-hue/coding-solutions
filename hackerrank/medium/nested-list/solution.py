if __name__ == '__main__':
    stu=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stu.append([name,float(score)])
    scores=sorted(list(set(s[1] for s in stu)))
    lowest=scores[1]
    names=[s[0] for s in stu if s[1]==lowest]
    for name in sorted(names):
        print(name)
