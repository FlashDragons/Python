A = input("A = ")
B = input("B = ")
A = float(A)
B = float(B)
mode = input("""你希望进行什么运算？
A.加法运算
B.减法运算
C.乘法运算
D.除法运算
E.比较大小
F.乘方运算：A^B=
G.开方运算：B√A= （在输入负数时有BUG，慎用）
""").upper()
if mode == "A":
    print(f"计算结果为{A + B}。")
elif mode == "B":
    print(f"计算结果为{A - B}。")
elif mode == "C":
    print(f"计算结果为{A * B}。")
elif mode == "D":
    if B != 0:
        print(f"计算结果为{A / B}。")
    else:
        print("无解")
elif mode == "E":
    if A > B:
        print("A比B大。")
    elif A < B:
        print("B比A大。")
    elif A == B:
        print("A和B一样大。")
elif mode == "F":
    print(f"计算结果为{A ** B}。")
elif mode == "G":
    if B > 0 and B % 2 != 0:
        B = 1 / B
        print(f"计算结果为{A ** B}")
        #开指数>0的奇次方
    elif B != 0 and B % 2 == 0 and A > 0:
        B = 1 / B
        print(f"计算结果为{A ** B}")
        #开偶次方，底数为正数
    elif B > 0 and B % 2 == 0 and A == 0:
        B = 1 / B
        print(f"计算结果为{A ** B}")
        #开偶次方，底数为0
    elif B < 0 < A:
        B = 1 / B
        print(f"计算结果为{A ** B}")
        #指数为负数，底数为正数
    elif B < 0 and A < 0 and B % 2 != 0:
        B = 1 / B
        print(f"计算结果为{A ** B}")
        #指数和底数均为负数，开奇次方
    else:
        print("无解")
        #开偶次方，底数为负数；或开0次方；或指数为负数，底数为0
