import math

def quadratic (a, b, c):
    if a == 0:
        print("Non quadratic equation")
        if b == 0 and c != 0:
            print("Both a and b can not be 0 at the same time unless the constants value is 0")
            return
        elif b == c and c == 0:
            print("Every value solves the equation")
            return
        sol_1 = -c/b
        sol_2 = None
    elif ((b**2)-4*a*c) > 0:
        sol_1 = (-b + math.sqrt((b**2)-4*a*c))/(2*a)
        sol_2 = (-b - math.sqrt((b**2)-4*a*c))/(2*a)
    
    else:
        print("Complex solutions")
        sol_1 = complex((-b)/(2*a), math.sqrt(4*a*c-(b**2)))/(2*a)
        sol_2 = complex((-b)/(2*a), -math.sqrt(4*a*c-(b**2)))/(2*a)

    return sol_1, sol_2
equation = [0, 0, 0]
equation[0]=int(input("Imput the the 2nd grade coefficient a\n"))
equation[1]=int(input("Imput the the 1st grade coefficient b\n"))
equation[2]=int(input("Imput the constants value c\n"))
solution = quadratic(equation[0], equation[1], equation[2])
if not(equation[0] == 0 and equation[1] == 0):
    print("The solution for the equation " + str(equation[0]) + "xx + " + str(equation[1]) + "x + " + str(equation[2]) + " = 0 are \n")
    print(solution[0], solution[1])