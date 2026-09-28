list_1 = list(map(float,input("班级学员高考成绩：").split()))
def max_min_avg():
    """
    计算高考成绩最高分，最低分，平均分
    ：param list_1:输入的成绩表
    ：return:最高分，最低分，平均分
    """
    max_score = max(list_1)
    min_score = min(list_1)
    avg_score = sum(list_1)/len(list_1)
    return max_score,min_score,avg_score
a,b,c=max_min_avg()
print(f"最高分为：{a},最低分：{b},平均分：{c:.3f}")