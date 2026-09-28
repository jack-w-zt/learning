#根据传入的一批商品信息（商品名，价格，数量），优惠（优惠券，积分抵扣），运费信息计算订单的总金额
#注：优惠券要商品总金额满5000才能使用，优惠券金额不能超过商品总价
#注：积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣
def cal_price(*args,coupon=0,points=0,express=0):
    """
    根据传入的一批商品信息（商品名，价格，数量），优惠（优惠券，积分抵扣），运费信息计算订单的总金额
    :param args:商品信息
    :param coupon:优惠券
    :param points:积分
    :param express:运费
    """
    #1.计算商品总金额
    price=[goods[1]*goods[2] for goods in args]
    total_price=sum(price)
    #2.优惠券抵扣
    if total_price>=5000 and coupon<=total_price:
        total_price-=coupon
    #3.积分抵扣
    if total_price>=5000 and points // 100 <= total_price:
        total_price-=points//100
    #4.添加运费
    total_price += express
    return total_price
import ast
goods=input("请输入商品信息：")
price_info=ast.literal_eval(goods)
coupon=eval(input("请输入你的优惠券金额："))
points=eval(input("请输入你的积分："))
express=eval(input("请输入你的运费："))
result=cal_price(*price_info,coupon=coupon,points=points,express=express)
print("商品最终支付金额：",result)