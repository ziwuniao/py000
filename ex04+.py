# 1.没有必要。如果用4.0结果不变。额，还有这里是司机数量，弄一个小数点好奇怪。难道还有不够整数的个司机么？
# 2.如果用浮点运算，需要4.0
# 3.给每行添加注释。。。翻译。。。

#  车数
cars = 100
# 每辆车载人数
space_in_a_car = 4.0
# 司机数
drivers = 30
# 乘客数
passengers = 90
# 无法载客的车数= 车数-司机数
cars_not_driven = cars - drivers
# 能载客的车数=司机数量
cars_driven = drivers
# 车能载人的总数 = 能开的车 * 每辆车载人数
carpool_capacity = cars_driven * space_in_a_car
# 每辆车平均载人的数量
average_passengers_per_car = passengers / cars_driven


print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today")
print("We need to put about",average_passengers_per_car,"in each car.")

#4. = 赋值,命名。

#5. _ 这个字符在变量里通常被用作假想的空格，用来隔开单词。

#6.i=12
x=13
j=x+y
print(j)

终端里运行得到25 ok
