# Curses Inquirer
A python library to create curses based CLIs.

## Usage
```python
from cursesinquirer import CursesInquirer, Select


# Define your program
def program(ci):
    tasks = ["Say hello", "Exit"]
    task = ci.ask(Select("What do you want to do?", tasks))
    
    if task == tasks[0]:
        print("Hello!")
    elif task == tasks[1]:
        exit(0)

# Run your program in a Curses Inquirer context.
CursesInquirer(program)
```

More examples available in [examples](examples) folder. 

## Customizability
The [builtin](cursesinquirer/builtins.py) question components does not have a lot of customizability options.
That said you can create your own to suite your needs.
Create a class that inherits from the abstract base class [Question](cursesinquirer/question.py) and implement the necessary methods.

## Limitations
See [issues](issues).

## Similar libraries
Here is a list of similar libraries that have been an inspiration to this library and might fit your needs better.
* [Inquirer](https://github.com/magmax/python-inquirer)
* [Pick](https://github.com/wong2/pick)
* [Picker](https://github.com/pp19dd/picker)

## License
MIT, see [LICENSE](LICENSE) file.
