num1=float(input("请输入数字:"))
num2=float(input("请输入数字:"))
a=input("请输入运算符:")
match a:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/" if num2!=0:
        print(num1/num2)
    case "/" if num2==0:
        print("除数不能为0")
    case _:
        print("运算符错误")