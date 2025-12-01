print ("a. v=u + a t ")
print ("b. s= u t + 1/2 a t^2")
print ("c. v^2 = u^2 + 2 a s")
print ("d. s = (u+v)/2 * t")

#the formulas above are the equations of motion in physics 

print("which of this equation do you want to use?")
choice = input("enter a, b, c, or d: ")
if choice == "a":
    u = float(input("enter inital velocity (u):"))
    a = float(input(" enter acceleration (a):"))
    t = float(input("enter time (T):"))
    v = u + a * t 
    print ("final velocity (V) is == ", v)
elif choice == "b":
    u = float (input("enter inital velocity (u):"))
    a = float (input(" enter acceleration (a): "))
    t = float(input("enter time (t):"))
    s = u *  t + 0.5 * a * t**2
    print ("displacemet (s) is == ", s)
elif choice == "c":
    u = float (input("enter inital velocity (u):"))
    a = float (input(" enter acceleration (a): "))
    s = float ( input("enter displacement (s):"))
    v = (u**2 + 2 * a * s)**0.5
    print ("final velocity (v) is == ", V)
elif choice == "d":
    u = float (input("enter inital velocity (u):"))
    v = float (input(" enter final velocity (v): "))
    t = float (input("enter time (t): "))
    s = (u + v) / 2 * t 
    ptint ("displacent (s) is == ", s)
#the code above is a simple physics calculator .
else:
    print ("invalid choice, please run the programeem again ////")

    #end of code 

