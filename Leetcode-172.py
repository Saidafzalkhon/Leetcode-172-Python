n = int(input())
son = 0
raqam = 1
while son != n:
    son+=1
    raqam*= son
if n > 0:
    son = 0
    for i in str(raqam)[::-1]:
        if i == '0':
            son+=1
        else:
            break
    print(son)
else:
    print(0)