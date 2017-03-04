# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 00:11:37 2017

@author: gpd
"""
#(1)字符串拼接
str1 = input("请输入姓名：")
str2 = input("请输入国家：")
print("世界这么大，{}想去{}看看！".format(str1,str2))

#(2)整数序列求和
n = input("请输入整数N：")
sum = 0
for i in range(int(n)):
    sum += i + 1
print("1到N求和结果是：",sum)

#(3)九九乘法表输出
#完整格式输出九九乘法表
for i in range(1,10):
    for j in range(1,10):
        print("{}*{}={:2}".format(i,j,i*j),end = ' ')
    print('')

#完整格式输出九九乘法表(倒)
for i in range(9,0,-1):
    for j in range(9,0,-1):
        print("{}*{}={:2}".format(i,j,i*j),end = ' ')
    print('') 
    
#左下三角格式输出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={:2}".format(j,i,i*j),end = ' ')
    print('')

#左上三角格式输出九九乘法表
for i in range(1,10):
    for j in range(i,10):
        print("{}*{}={:2}".format(i,j,i*j),end = ' ')
    print('')        

#右下三角格式输出九九乘法表
for i in range(1,10):
    for k in range(1,10-i):
        print(end="       ")
    for j in range(1,i+1):
        product=i*j
        print("%d*%d=%2d" % (i,j,product),end=" ")
    print (" ")
#右上三角格式输出九九乘法表
for i in range(1,10):
    for k in range(1,i):
        print (end="       ")
    for j in range(i,10):
            print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print("")   
    
#(4)阶乘计算
sum,tmp = 0,1
for i in range(1,11):
    tmp *= i
    sum += tmp
print("运算结果是：{}".format(sum))

#(5)猴子吃桃问题
n = 1
for i in range(5,0,-1):
    n = (n+1)<<1
print(n)

#(6)健康食谱输出
diet = [' 西红柿', ' 花椰菜', ' 黄瓜', ' 牛排', ' 虾仁']
count = 0
leng = len(diet)
for x in range(0,5):
    for y in range(0,5):
        if not(x==y):
            count += 1
            print("{}{}".format(diet[x],diet[y]))
print("{}种食材，每次两两相配共有{}种搭配方案".format(leng,count))

#(7)五角星绘制
import turtle
turtle.fillcolor("red")
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.right(144)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
turtle.done()

#(8)太阳花的绘制
import turtle
turtle.color("red","yellow")
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill
turtle.done()

#(9)螺旋线绘制
import turtle
import time
turtle.speed("fastest")
turtle.pensize(2)
for i in range(100):
    turtle.forward(2*i)
    turtle.left(90)
time.sleep(3)

#(10)彩色螺旋线的绘制
import turtle
turtle.pensize(2)
turtle.bgcolor("black")
colors = ["red", "yellow",'purple','blue']
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x % 4])
    turtle.left(91)
turtle.tracer(True)
