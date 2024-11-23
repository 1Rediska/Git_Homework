def handler (status):
    match status:
        case 400:
            print("Bad Request")
        case 201:
            print("Created")
        case 200:
            print("ОК")
        case _:
            print("Other")

#Изменение в Master
#Добавилось в Master 1
#Добавилось в Master 2
#Добавилось в Master 3
#Что-то интересное и просто и (согласен, не очень креативно)