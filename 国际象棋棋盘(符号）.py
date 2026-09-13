a="🫠"
b="😎"
for i in range(1,9):
    for j in range(1,9):
        if i%2 !=0:
            if j%2 !=0:
                print(a,end="  ")
            else:
                print(b,end=" ")
        else:
            if j%2==0:
                print(a,end="  ")
            else:
                print(b,end=" ")
    print()
