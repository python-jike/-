# 作业1_猜年龄14
# answer='Y'
# while answer=='Y'or answer=='y':
# #while answer=='Y'or'y':犯过的错误，==和or是一类运算符会导致这个表达式变成while (answer == 'Y') and True
#         for i in range(3):
#             age = input('请输入年龄')
#             if age == '18':
#                 print('恭喜你，猜对了')
#                 break
#             else:
#                 print('很遗憾，猜错了')
#         if age == '18':
#             break
#         else:
#             answer = input('是否继续猜（是Y否N）')#             _
# 作业2 计算BMI打印结果
height_w=1.75
weight_w=80.5
BMI=weight_w/(height_w**2)
if BMI>32:
    print('BMI为%d,严重肥胖'%BMI)
    pass
elif BMI>28 and BMI<=32:
    print('BMI为%d,肥胖' % BMI)
elif BMI>25 and BMI<=28:
    print('BMI为%d,过重' % BMI)
elif BMI>18.5 and BMI<=25:
    print('BMI为%d,肥胖' % BMI)
else:
    print('BMI为%d,肥胖' % BMI)
