#1.记诵熟悉。。。

# \\	Backslash (\)
# \'	Single-quote (')
# \"	Double-quote (")
# \a	ASCII bell (BEL)
# \b	ASCII backspace (BS)
# \f	ASCII formfeed (FF)
# \n	ASCII linefeed (LF)
# \N{name}	Character named name in the Unicode database (Unicode only)
# \r	Carriage Return (CR)
# \t	Horizontal Tab (TAB)
# \uxxxx	Character with 16-bit hex value xxxx
# \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx
# \v	ASCII vertical tab (VT)
# \ooo	Character with octal value ooo
# \xhh	Character with hex value hh

# 2.当字符串中有双引号时，该用三引号。或者用转义符标注。

#3.

a = ("\n\t'i'")
b = ('\n\t"have" \'a\'')
c = ('\n\tdream')

print(a + b +c)
