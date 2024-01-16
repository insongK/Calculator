import multiply
import division
import add_sub

def start():
    
    input_str = input("정수, 기호, 정수를 입력하세요 (예: 5 + 3): ") 

    # 입력된 문자열을 공백을 기준으로 분리
    num1, symbol, num2 = input_str.split()

    # 분리된 문자열을 각각 정수와 문자열로 변환
    num1 = int(num1)
    num2 = int(num2)

    if symbol == '*':
        print(multiply.mul(num1,num2),"입니다")
    elif symbol == '/':
        print(division.div(num1,num2),"입니다")
    elif symbol == '+':
        print(add_sub.add(num1,num2),"입니다")
    else:
        print(add_sub.sub(num1,num2),"입니다")




    


