from sys import argv

script, input_file = argv

def print_all(f):  # 打印读取到的文件内容
	print(f.read())

def rewind(f):
	f.seek(0) # 设置文件当前位置

def print_a_line(line_count, f):
	print(line_count, f.readline())

# readline()里边的代码会扫描文件的每一个字节，
# 直到找到一个\n 为止，然后它停止读取文件，
# 并且返回此前的文件内容。
# 文件f会记录每次调用readline()后的读取位置，
# 这样它就可以在下次被调用时读取接下来的一行了。

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
