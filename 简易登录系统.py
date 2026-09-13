while True:
    amount=input("请输入账号: ")
    answer=input("请输入密码: ")
    if amount=="admin" and answer=="666888" or amount=="zhangsan" and answer=="123456" or amount=="taoge" and answer=="888666":
        print("登录成功,进入B站首页~")
        break
    else:
        print("账号或密码错误,请重新输入~")