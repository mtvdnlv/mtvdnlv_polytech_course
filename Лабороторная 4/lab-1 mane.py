import json  #Вызываем модуль json для использования далее

INPUT_FILE = 'input.json'   #Обозначим названия файла

def task() -> float:
    with open(INPUT_FILE) as f:   #открываем файл для чтения и работы с данными
        data = json.load(f)  #загрузим данные в переменную data

    sum_ = sum([item["score"] * item["weight"] for item in data])
    return round(sum_, 3) #округляем до 3 знаков

print(task())