def handler (status):
    match status:
        case 400:
            print("Bad Request")
        case 201:
            print("Created")
        case 200:
            print("Успешно")
        case _:
            print("Другое")

#Изменение в Master
#Добавилось в Master 1
#Добавилось в Master 2
#Добавилось в Master 3
#Изменение в Develop2
#Добавим строку в Develop2
#Что-то интересное и просто и (согласен, не очень креативно)