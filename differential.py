while True:
        
    title = 'Simple Differentiation -- Polynomials'
    print(title.center(100)) 

    n = int(input('Enter the number of terms in the equation:\n'))

    list1 = []
    list2 = []
    forbidden_nos = ['0','1','2','3','4','5','6','7','8','9']

    wrt = str(input('With what variable should the differentiation be done?\n'))

    if wrt in forbidden_nos:
            print('Numbers cannot be variables!! Replacing number with \'x\'')  
            wrt = 'x'

    if len(wrt) != 1:
            print('Variable is only one letter, defaulting variable to \'x\'')
            wrt = 'x'

    for x in range (n):

        a = str(input('Enter the variable: \n')) 

        if a in forbidden_nos:
            print(f'Numbers cannot be variables!! Replacing number with \'{wrt}\'')  
            a = wrt

        if len(a) != 1:
            print(f'Variable is only one letter, defaulting variable to \'{wrt}\'')
            a = wrt    
                    
        coeff = int(input('Enter the coefficient of the variable: \n'))
        b = int(input('Enter it\'s power: \n'))
        
        c = str(coeff)+a+'^'+str(b)

        e = b-1
        dif = str(b*coeff)+a+'^'+str(e)

        if b == 0:
            dif = str(0)

        if e == 0:
            dif = str(coeff)

        if a != wrt:
            dif = str(0)            

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

    loop_ = input('Want a solution for a different problem? Press y or hit enter to end program: \n')

    if loop_ != 'y':
        break
    else: 
        list1.clear()
        list2.clear()
