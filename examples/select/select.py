from cursesinquirer import CursesInquirer, Select


def program(ci):
    tasks = ["Return a random number", "Say hello", "Exit"]
    task = ci.ask(Select("What do you want to do?", tasks))

    if task == tasks[0]:
        import random
        return random.randint(1, 10)
    elif task == tasks[1]:
        print("Hello!")
    elif task == tasks[2]:
        exit(0)

print(CursesInquirer(program).result)
