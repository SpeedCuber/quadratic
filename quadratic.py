import math

def quadratic (a, b, c):
    if a == 0:
        print("Non quadratic equation")
        sol_1 = -c/b
        sol_2 = None
    elif ((b**2)-4*a*c) > 0:
        sol_1 = (-b + math.sqrt((b**2)-4*a*c))/(2*a)
        sol_2 = (-b - math.sqrt((b**2)-4*a*c))/(2*a)
    
    else:
        print("Complex solutions")
        sol_1 = complex((-b)/(2*a), math.sqrt(4*a*c-(b**2)))/(2*a)
        sol_2 = complex((-b)/(2*a), -math.sqrt(4*a*c-(b**2)))/(2*a)

    return sol_1,sol_2

equation = [-78, -10, 1]
solution = quadratic(equation[0], equation[1], equation[2])
print(solution)