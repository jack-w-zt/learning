outline=lambda : print("----------")
outline()
add=lambda x,y:x+y
sum=add(10,20)
print(sum)
#匿名函数典型应用场景：把列表中的每一个元素按照字符数量从小到大进行排序
data_list=["c","c++","go","python"]
print(data_list)
data_list.sort(key=lambda item:len(item))
print(data_list)
#从大到小排序
data_list.sort(key=lambda item:len(item),reverse=True)
print(data_list)