def cal_data(*args,**kwargs):
    data_min=min(args)
    data_max=max(args)
    data_avg=sum(args)/len(args)
    if kwargs.get("round") is not None:
        data_avg=round(data_avg,kwargs.get("round"))
    if kwargs.get("print"):
        print(f"最大值：{data_max}最小值：{data_min}平均值：{data_avg}")
data=cal_data(1,2,3,4,5,6,11999,round=3,print=True)
print(data)