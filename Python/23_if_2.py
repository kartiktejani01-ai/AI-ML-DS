# write a program to findout whether given shape is portrait or landscape or square from user given length and width.
#task findout display ratio of width vs length

length = float(input("Enter length:"))
width = float(input("Enter width:"))
'''
if length>width:
    print("Shape is Portrait")
if length<width:
    print("Shape is landscape")
if length==width:
    print("Shape is Square")

print("Good Bey") '''

ratio = width / length

print("Shape Ratio:", ratio)