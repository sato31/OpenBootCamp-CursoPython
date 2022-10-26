# >= Mayor o igual
# == Exactamente igual
# <= Menor o igual
# <  Menor

a = 5
b = 6
c = 7
print(a < b)    # True

resultado = (a > 5 and c > 7)
# resultado = (False and c > 7)
# resultado = (False and False)
# resultado = (False)
print(resultado)    #False

#           AND                         OR 
# True  and True  => True       True or True   => True
# True  and False => False      True or False  => True
# False and True  => False      False or True  => True
# False and False => False      False or False => False 

resultado = ((a >= 5 or c > 7) and (b == 5))
# resultado = (True or False) and False
# resultado = True and False
# resultado = False