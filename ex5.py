my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
height = my_height * 2.54 # centimeter
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d centimeter tall." % height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky try to get it exactly right
print("If add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))
print("%r, %r, %r" % (my_height, my_weight, my_name)) # "%r" 不管什么都打印出来 