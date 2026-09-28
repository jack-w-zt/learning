str=input("请输入字符串：")
def vowel_count():
    """
    计算字符串中元音字母的个数
    ：param str:输入的字符串
    ：return:元音字母的个数"""
    count=0
    for i in str:
         if i in "aeiouAEIOU":
             count+=1
    return count
print("元音字母的个数为：",vowel_count())