def func(a, b, c):
    discriminant=b**2 - 4*a*c
    if discriminant>0:
        x1=(-b + discriminant**(0.5))/(2*a)
        x2=(-b - discriminant**(0.5))/(2*a)
        return x1, x2
    elif discriminant==0:
        return -b/(2*a)
    else:
        return "Дискриминант < 0 и не имеет корней"

print(func(3, 7, -10))    