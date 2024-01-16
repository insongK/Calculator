import input_par
import multiply
import division
import add_sub

def start():
    
    num1, symbol, num2 = input_par.input_2par_1symbol()

    if symbol == '*':
        print(multiply.mul(num1,num2),"입니다")
    elif symbol == '/':
        print(division.div(num1,num2),"입니다")
    elif symbol == '+':
        print(add_sub.add(num1,num2),"입니다")
    else:
        print(add_sub.sub(num1,num2),"입니다")




    


