from cursesinquirer import CursesInquirer, Text


def program(ci):
    username = ci.ask(Text("Enter your username", "Username", is_password=False))
    password = ci.ask(Text(None, "Password", is_password=True))
    return username, password

print(CursesInquirer(program).result)
