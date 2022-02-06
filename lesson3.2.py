operation = input('Выберите операцию для выполнения программы: ')
while operation != '-' and operation != '+' and operation != '*' and operation != '/':
   print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
   operation = input('Выберите операцию: ')
operands = int(input('Сколько операндов? '))
answer = int(input('Введите операнд 1: '))
answer_string = str(answer)

for n in range(2, operands + 1):
   member_n = int(input(f'Введите операнд {n}: '))
   if operation == '-':
      answer -= member_n
      answer_string += ' - ' + str(member_n) 
   elif operation == '+':
      answer += member_n
      answer_string += ' + ' + str(member_n)
   elif operation == '*':
      answer *= member_n
      answer_string += ' * ' + str(member_n)
   elif operation == '/':
      answer /= member_n
      answer_string += ' / ' + str(member_n)
print(answer_string, '=', answer)
print('Конец программы')

