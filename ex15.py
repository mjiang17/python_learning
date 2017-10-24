#coding=utf-8
from sys import argv 
script, filename = argv # 定义参数变量
txt = open(filename) 	# 打开filename文件并传给txt
	
print("Here's you file %r:" % filename) # 打印文件名称
print (txt.read())		# 调用read（）函数，读取txt文件内容

print("Type the filename again:")
file_again = input("> ") # 输入文件名

txt_again = open(file_again) # 再次打开文件

print(txt_again.read()) 	 # 打印读取到的内容
txt_again.close()
txt.close()