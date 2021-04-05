def cost(array, x, y):
    cnt=0
    PC = PJ = False
    for string in array:
        if PC and string =='C':
            cnt+= (not PJ) * y
            PJ = True
        elif PC and string == 'J':
            cnt+= PJ * x
            PJ = False
        elif not PC and string != '?':
            PC = True
            if string == 'C':
                PJ = True
    return cnt


t = int(input())
case = 1
for _ in range(t):
    alist = list(input().split(" "))
    x, y, array = int(alist[0]), int(alist[1]), alist[2]
    print((f"Case #{case}: {cost(array, x, y)}"))
    case += 1
