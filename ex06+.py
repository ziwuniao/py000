# 1.注释。

# 定义变量

types_of_people= 10

# 赋值X，包含格式化变量以及字符串。
x = f"There are {types_of_people} types of people."

#定义变量
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# 输出变量x和y
print(x)
print(y)

# 输出包含格式化变量以及字串符的字串符。
print(f"I said: {x}")
print(f"I also said: '{y}'")

#定义变量
hilarious = False

# 定义变量，并且留了一个坑。{}待填写。
joke_evaluation = "Isn't that joke of funny?!{}"

# 输出并填坑。格式化变量的另外写法。
print(joke_evaluation.format(hilarious))

# 定义变量，w,e.都是字符串。
w = "This is the left side of..."
e = " a string with a right side."

# 输出w+e。就是两个字符串在一起。（联想习题1，又是一个只输出一行的办法。）
print(w + e)

# 2.包含字符串的字符串。

# 分别是y = f"Those who know {binary} and those who {do_not}."

# 以及print(f"I said: {x}") 和print(f"I also said: '{y}'")

# 如果把第一处算两个，则一共4个。

# 3.只有4个，是的。

#4.+的作用是把两个字符串连在一起。实验发现用，也可以做到。不过多了一个空格。
