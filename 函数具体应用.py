#N的阶乘
num=int(input())
def cal(args):
    a=1
    for i in range(1,args+1):
        a=a*i
    return a
result=cal(num)
print("N的阶乘：",result)
#N的阶乘简易写法(递归：先层层递进，再层层回归)
def jc(n):
    if n==1:
        return 1
    return n*jc(n-1)
result=jc(num)
print("N的阶乘：",result)