def find_index(list, aim): #создадим функцию с аргументами список и цель
    for index, piece in enumerate(list): # когда перебираемое piece совпадет с искомывм aim,то вытащим индекс piece
        if piece == aim:
            return index


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:  #подставляя значенния для трех искомых объектов
    index_item = find_index(items_list, find_item) #получая индексы каждого искомого объекта (а если его нет,то none)
    if index_item is not None: #если есть в списке то выводим индекс, а если функция индекса не дала, то none ведет к надписи, что нет  в списке
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
