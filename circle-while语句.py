# 循环嵌套 九九乘法表
# row=1
# while row<=9:
#     col=row
#     while col<=9:
#         print('%i*%i=%i'%(row,col,row*col),end=" ")
#         col+=1
#         pass
#     print()
#     row+=1
#     pass
# 直角三角形
# row=1
# while row<=7:
#     j=1
#     while j<=row:
#         print('*',end=' ')
#         j+=1
#         pass
#     # print()
#     row+=1
#     print()
#     pass
# 等腰三角形
row=1
while row<=7:
    j=1
    while j<=7-row:
        print(' ',end=' ')
        j+=1
        pass
    k=1
    while k<=2*row-1:
        print('*',end=' ')
        k+=1
        pass
    row+=1
    print()

