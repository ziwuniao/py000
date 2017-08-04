#1.注释。

定义格式化变量。

formatter = "{} {} {} {}"

# 输出各种格式化变量。可以自定义。各种折腾。可以是数字，字符串，真假值，还有格式化变量本身。。。
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
     "Try your",
     "Own text here",
     "Maybe a poem",
     "Or a song about fear"
))

# 2.检错。

# 之前忘漏了一个{} ，已补上。
