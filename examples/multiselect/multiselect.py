from cursesinquirer import CursesInquirer, MultiSelect


def program(ci):
    options = [["Linux", False], ["Windows", False], ["BSD", False], ["OS X", False], ["Emacs", False]]
    answers = ci.ask(MultiSelect("Which operative systems do you use?", options))
    return list(map(lambda x: x[0], filter(lambda x: x[1], answers)))

print(CursesInquirer(program).result)
