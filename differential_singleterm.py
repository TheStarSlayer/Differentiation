while True:
    def f1():
            title = 'Simple Differentiation'
            print(title.center(100))        
            
            f1.a = str(input('Enter the variable: \n')) 

            forbidden_nos = ['0','1','2','3','4','5','6','7','8','9']
            if f1.a in forbidden_nos:
              print('Numbers cannot be variables!! Replacing number with \'a\'')  
              f1.a = 'a'
            
            f1.coeff = int(input('Enter the coefficient of the variable: \n'))
            f1.b = int(input('Enter it\'s power: \n'))

            c = str(f1.coeff)+f1.a+'^'+str(f1.b)

            d = input(f'Your equation is {c}. Do you want to change it? If yes, then press y. If alright, hit enter: \n')
            print(d)
            
            if d == 'y':
                f1()
            else:
                pass

    f1()

    if len(f1.a) != 1:
            print('Variable is only 1 letter')
            f1()

    z = f1.b-1

    dif = str(f1.b*f1.coeff)+f1.a+'^'+str(z)
        
    if f1.b == 0:
            dif = str(0)

    if z == 0:
            dif = str(f1.coeff)

    print(f'Differentiating the equation given, the answer is: \n{dif}.')   

    loop_ = input('Want a solution for a different problem? Press y or hit enter to end program: \n')

    if loop_ != 'y':
        break
