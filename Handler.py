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

#Что-то интересное
#Что-то интересное и просто и (согласен, не очень креативно)