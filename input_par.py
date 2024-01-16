def input_2par_1symbol():
    input_str = input("정수, 기호, 정수를 입력하세요 (예: 5 + 3): ")

    # 입력된 문자열을 공백을 기준으로 분리
    num1, symbol, num2 = input_str.split()

    # 분리된 문자열을 각각 정수와 문자열로 변환
    num1 = int(num1)
    num2 = int(num2)

    return num1, symbol, num2

