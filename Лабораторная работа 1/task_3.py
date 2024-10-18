list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

Middle = len(list_players)//2  #найдем середину списка

first_team = list_players[:Middle] #первая половина участников
second_team = list_players[Middle:] #вторая половина

print(first_team)
print(second_team)
