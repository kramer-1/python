a=int(input("Let's make a triangle, what do you want length a to be?: "))
b=int(input("Ok, what should b be?: "))
c=int(input("Now what is c?:"))

if (a+b) < c:
    print("That's not a triangle")
elif ((a**2)+(b**2)) == (c**2):
    print("That is a right triangle")
elif ((a**2)+(b**2)) < (c**2):
    print("That is an obtuse triangle")
elif ((a**2)+(b**2)) > (c**2):
    print("That is an acute triangle")