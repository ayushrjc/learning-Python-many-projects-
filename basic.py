# # to know all the methods available for string
# print(dir("string"))
# # output-->
#     # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#     # '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
#     # '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
#     # '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
#     # 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
#     # 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex',
#     # 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# #  eg:->
#
# x="AYush"
# print(x.capitalize())
# print(x.title())
# # both does same work
#
# a = 'silly question'
# a.title()
# # 'Silly Question'
# a.capitalize()
# # 'Silly question'
# # This is difference
#
# print(x.casefold())
# #  i.e. ignores cases when comparing.
# # For example, German lowercase letter ß is equivalent to ss.
# # However, since ß is already lowercase, lower() method does nothing to it. But, casefold() converts it to ss.
#
# print(x.count("AYu",0,2))
# # count of AYu substring in string AYush from index 0 to 2
# print(x.center(10,'#'))
# # 10 here is total length i.e. weidth and # is filling string
#
# print(x.encode(encoding='utf-8',errors='ignore'))
# # to get unicode of any char
# print(chr(128013))
# # to get char of any unicode
# print(ord("🐍"))
#
# print(print("hello",print("hello"),end=" "))
#

######### Date and Time #########

# import datetime
# print(datetime.datetime.now())
# # string format of time and date
# x = datetime.datetime.now()
# print(x.strftime("%A"))
# print(x.strftime("%a"))

# date formatting methoods in python


########### File Handling ##########
# file = open("abc.txt","r")
# x= file.read()
# print(x)

# #if file is not there
# file1 = open("xyz.txt","w")
# file1.write("hello python Cluster")
# file1.close()
# # file1.write("hello python Cluster")
# # If again you open file with 'w' it will errase everything and open file on termi
# # file1.close()
# file1 = open("xyz.txt","a")
# file1 = open("xyz.txt","r+")
# file1 = open("xyz.txt","x")

#
# ######## libreries #######
# import json
# x = '{"name":"ayush","age":20}'
# y= json.loads(x)
# print(y["name"])