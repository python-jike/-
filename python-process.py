# 嵌套流程
chengji=int(input('请输入您的成绩'))
if chengji>=80:
    if chengji>=90:
        print('太棒了')
    else:
        print('还不错')
    pass
elif chengji>=70:
    print('良好')
    pass
elif chengji>=60:
    print('及格')
    pass
else:
    print('不及格')