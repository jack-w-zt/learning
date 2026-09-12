ok_account=111
ok_password=111
account=input("请输入你的账号：")
password=input("请输入你的密码：")
if ok_account==account and ok_password==password:
    print("登录成功")
if ok_account!=account or ok_password !=password:
    print("登录失败")