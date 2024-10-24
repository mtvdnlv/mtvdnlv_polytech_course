from operator import length_hint
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

gap = 4 #Обозначаем пропуск как переменную 

sum_of_numbers_without_none = sum(numbers[:gap]) + sum(numbers[gap+1:]) #Сумма всех оставшихся элементов
length_with_none = len(numbers)                 #Количество всех элементов
average_numbers_without_none = sum_of_numbers_without_none/length_with_none #Нахождение среднего арифметического

numbers[gap] = average_numbers_without_none


print("Измененный список:", numbers)
