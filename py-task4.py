from random import randint
child1 = randint(1,10)
child2 = (child1+child1)*2
total = child1*2+child2
print(f"{total} -> {child1} {child2} {child1}")


# В 4 задаче можно также идти от обратного и проверить введенное число всех журавликов
# while True:
#     try:
#         S = int(input('Введите количество журавликов: '))
#         if S % 6 == 0:
#             x = S // 6
#             print(f'Петя и Сережа сделали по {x}, а Катя - {x * 4} журавликов')
#             break
#         else:
#             print('Это количество нельзя распределить в соответствии с условиями задачи! Попробуйте еще раз!')
#     except:
#         print('Некорректный ввод. Попробуйте еще раз!')
