title = 'Simple Differentiation -- Polynomials'
print(title.center(100)) 

n = int(input('Enter the number of terms in the equation:\n'))
list1= []
list2 = []

for x in range (n):

    a = str(input('Enter the variable: \n')) 

    forbidden_nos = ['0','1','2','3','4','5','6','7','8','9']
    if a in forbidden_nos:
     print('Numbers cannot be variables!! Replacing number with \'a\'')  
     a = 'a'
                
    coeff = int(input('Enter the coefficient of the variable: \n'))
    b = int(input('Enter it\'s power: \n'))
     
    c = str(coeff)+a+'^'+str(b)

    z = b-1
    dif = str(b*coeff)+a+'^'+str(z)

    list1.append(c)
    list2.append(dif)
    
poly = ''

for kk in list1:
    if kk == list1[-1]:
        poly = poly+kk
    else:
        poly = poly+kk+'+'

d = input(f'Your equation is {poly}.')
print(d)

doly = ''

for cc in list2:
    if cc == list2[-1]:
        doly = doly+cc
    else:
        doly = doly+cc+'+'

print(f'Differentiating the given equation, the result is {doly}.')
