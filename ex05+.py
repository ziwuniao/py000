# 1.修改变量。

name = 'goodman'
age = 24 #
height = 170 # cm
weight = 120 # kg
eyes = 'black'
teeth = 'White'
hair = 'black'

print(f"let's talk about {name}.")
print(f"he's {height} cm tall.")
print(f"He's {weight} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky,try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height},and {weight} I get {total}.")

# 2 单位换算。

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie...so youhth...
my_height = 74*2.54  # 一英寸=2.54厘米
my_weight = 180*0.45 # 一磅 = 0.45千克
my_eyes = 'bule'
my_teeth = 'White'
my_hair = 'Brown'

print(f"let's talk about {my_name}.")
print(f"he's {my_height} cm tall.")
print(f"He's {my_weight} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky,try to get it exactly right
total = round(my_age + my_height + my_weight)
print(f"If I add {my_age}, {my_height},and {my_weight} I get {total}.")
