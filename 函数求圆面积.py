a=float(input("请输入圆的半径："))
def circle_area(r):
    """
    计算圆的面积
    :param r: 圆的半径
    :return: 圆的面积
    """
    return round(3.1415926525*r**2,3)
help(circle_area)
print("圆的面积是：",circle_area(a))