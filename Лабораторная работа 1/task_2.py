SIZE_OF_DISK = 1.44 #Размер дискеты в Мб
PAGES = 100         #Кол-во страниц в книге
LINES = 50          #Кол-во строк на странице
SYMBOLS = 25        #Кол-во символов в строке
STORAGE_FOR_SYMBOL = 4 #Количество байт для одного символа

SYMBOLS_IN_BOOK = PAGES * LINES * SYMBOLS #размер книги в символах
neccesary_storage = SYMBOLS_IN_BOOK * STORAGE_FOR_SYMBOL
SIZE_OF_DISK_IN_BYTES = SIZE_OF_DISK * 1024 * 1024          #Переводим МБ сначала в Килобайты потом в Байты

Quantity_of_boooks = SIZE_OF_DISK_IN_BYTES // neccesary_storage #Целочисленно делим объем памяти на размер книги и в ответе переводим в формат int ради числа без точки
print("Количество книг, помещающихся на дискету:",int(Quantity_of_boooks))