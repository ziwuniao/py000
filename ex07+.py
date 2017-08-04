# 1.注释

# 输出字符串。
print("Mary had a little lab.")
# 输出带格式化变量的字符串。
print("Its fleece was white as {}".format('snow'))
# 输出字符串。
print("And everywhere that Mary went.")
# 输出字符串并且运算。额，真是个偷懒的好办法啊。
print("." * 10) # what'd that do?

# 输出一系列单个字母型自串符。（做的时候不明所以。后来发现有彩蛋。作者的幽默。）
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e\000"
# 参考http://www.runoob.com/python3/python3-string.html
# 不得已而为之，否则输出的字母总是全部连在一起...不知其他同学如何解决这个问题。
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# end=''的作用是，不用换行，继续显示输出。。。
# (PS：和前面的作业可以联系起来。不用换行的办法。)

# watch end = '' at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6,end='')
print(end7 + end8 + end9 + end10 + end11 + end12)

# 2.已读。

#3.额，还是标点符号有时会遗漏一两个，以及更大的bug...。

# print("Its fleece was white as {}".format('snow'))

# 应该是 print("Its fleece was white as {}.".format('snow'))

# print(end7 + end8 + end9 + end11 + end12) 应该是

print(end7 + end8 + end9 + end10 + end11 + end12)

#4.记住了。

#5.ok.这是安慰么？。。。
