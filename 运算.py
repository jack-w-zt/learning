#加
def add(x,y):
    return x+y
#减
def substract(x,y):
    return x-y
#乘
def a(x,y):
    return x*y
#除
def divid(x,y):
    return round(x/y,3)
def cal(x,y,oper):
    return oper(x,y)
print(cal(111,567,a))