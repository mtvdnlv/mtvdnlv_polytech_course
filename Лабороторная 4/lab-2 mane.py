import csv #импортируем нужные модули
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f: #открываем файл для прочтения
        rows = [row for row in csv.DictReader(f)] #считываем строки в переменную для записи далее

        with open(OUTPUT_FILENAME, "w") as f: #открываем новый файл для записи
            json.dump(rows, f, indent=4)      #Сериализуем с отступами равными 4

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

'''p.s: у меня в paycharm-e программа не выдает толком ответа, на выходе получаю "[]", а прога 
ожидает список с отступами. Я думаю проблема в исходном файле, "input.csv", т.к он пустой, а должен содержать
данные. Задание кажется несложным, но не знаю как проверить. спасибо за внимание'''