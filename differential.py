title = 'Simple Differentiation -- Polynomials'
print(title.center(100)) 

n = int(input('Enter the number of terms in the equation:\n'))
list1 = []
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

    e = b-1
    dif = str(b*coeff)+a+'^'+str(e)

    list1.append(c)
    list2.append(dif)
    
poly = ''
for f in list1:
    if f == list1[-1]:
        poly = poly+f
    else:
        poly = poly+f+'+'

d = input(f'Your equation is {poly}.')
print(d)

doly = ''
for g in list2:
    if g == list2[-1]:
        doly = doly+g
    else:
        doly = doly+g+'+'

print(f'Differentiating the given equation, the result is {doly}.')
