# this one is like your scripts with argv
def print_two(*args): # *号做形参，在不清楚参数个数时使用，传递的是一个元组
					  # **做形参，传递的是字典
	arg1, arg2 = args
	print("arg1: %r, arg2: %r" % (arg1, arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print("arg1: %r, arg2: %r" % (arg1, arg2))

# this just takes one argument
def print_one(arg1):
	print("arg1: %r" % arg1)

# this just takes no argument
def print_none():
	print("I got nothing.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()