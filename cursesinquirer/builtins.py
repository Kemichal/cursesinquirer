# -*- coding: utf-8 -*-

import curses
import copy
from .question import Question


class MultiSelect(Question):
    """MultiSelect

    :param title: a title or None
    :param opt: a list of options
    """

    def __init__(self, title, opt):
        self.screen = None
        self.title = title
        self.opt = copy.deepcopy(opt)  # Don't mutate the argument

        self.curr_pos = 0

        # Set offset. Offset is how many lines down the options should be printed
        # TODO Handle multi line title
        if self.title:
            self.offset = 1
        else:
            self.offset = 0

    def set_screen(self, screen):
        self.screen = screen

    def input(self, c):
        if c == " ":
            self.opt[self.curr_pos][1] = not self.opt[self.curr_pos][1]
        elif c == curses.KEY_UP:
            if self.curr_pos != 0:
                self.curr_pos -= 1
        elif c == curses.KEY_DOWN:
            if self.curr_pos != len(self.opt) - 1:
                self.curr_pos += 1

    def renderer(self):
        self.screen.clear()

        # Add title
        if self.title:
            self.screen.addstr(0, 0, " " + self.title)

        # Add all options
        for i, value in enumerate(self.opt):
            self.screen.addstr(i + self.offset, 0, " [")
            if value[1]:
                self.screen.addstr("✓", curses.color_pair(1))
            else:
                self.screen.addstr(" ", curses.color_pair(1))
            self.screen.addstr("] " + value[0])
        # Reverse currently selected box
        if self.opt[self.curr_pos][1]:
            self.screen.chgat(self.curr_pos + self.offset, 2, 1, curses.color_pair(1) | curses.A_REVERSE)
        else:
            self.screen.chgat(self.curr_pos + self.offset, 2, 1, curses.A_REVERSE)

    def answer(self):
        return self.opt


class Select(Question):
    """Select

    :param title: a title or None
    :param opt: a list of options
    :param selected: pre-selected option
    """

    def __init__(self, title, opt, selected=0):
        self.screen = None
        self.title = title
        self.opt = opt

        self.curr_pos = min(selected, len(opt)-1)

        # Set offset. Offset is how many lines down the options should be printed
        if self.title:
            self.offset = 1
        else:
            self.offset = 0

    def set_screen(self, screen):
        self.screen = screen

    def input(self, c):
        if c == curses.KEY_UP:
            if self.curr_pos != 0:
                self.curr_pos -= 1
        elif c == curses.KEY_DOWN:
            if self.curr_pos != len(self.opt) - 1:
                self.curr_pos += 1

    def renderer(self):
        self.screen.clear()

        # Add title
        if self.title:
            self.screen.addstr(0, 0, " " + self.title)

        # Add all options
        for i, value in enumerate(self.opt):
            self.screen.addstr(i + self.offset, 0, " ")
            if i == self.curr_pos:
                self.screen.addstr(value, curses.A_REVERSE)
            else:
                self.screen.addstr(value)

    def answer(self):
        return self.opt[self.curr_pos]


class Text(Question):

    def __init__(self, text, prompt, is_password):
        self.screen = None
        self.text = text
        self.prompt = prompt
        self.data = ""
        self.is_password = is_password

        if self.text is None:
            self.offset = 0
        else:
            self.offset = 1

    def set_screen(self, screen):
        self.screen = screen

    def input(self, c):
        if c == curses.KEY_BACKSPACE:
            self.data = self.data[:-1]
        elif type(c) is str:
            self.data = self.data + c

    def renderer(self):
        self.screen.clear()
        curses.curs_set(True)

        if self.text is not None:
            self.screen.addstr(0, 0, " " + self.text)

        self.screen.addstr(self.offset, 0, " ")
        if self.is_password:
            self.screen.addstr(self.prompt + ": ")
        else:
            self.screen.addstr(self.prompt + ": " + self.data)

    def answer(self):
        curses.curs_set(False)
        return self.data


class YesNo(Question):
    """YesNo

    :param prompt: a question
    :param default: pre-selected value; True or False for yes or no respectively
    """

    def __init__(self, prompt, default=False):
        self.screen = None
        self.prompt = prompt
        self.res = default

    def set_screen(self, screen):
        self.screen = screen

    def input(self, c):
        if c == curses.KEY_LEFT:
            self.res = True
        elif c == curses.KEY_RIGHT:
            self.res = False

    def renderer(self):
        self.screen.clear()

        self.screen.addstr(0, 0, " " + self.prompt + ": ")

        if self.res:
            self.screen.addstr("Yes", curses.color_pair(1) | curses.A_REVERSE)
            self.screen.addstr(" ")
            self.screen.addstr("No", curses.color_pair(2))
        else:
            self.screen.addstr("Yes", curses.color_pair(1))
            self.screen.addstr(" ")
            self.screen.addstr("No", curses.color_pair(2) | curses.A_REVERSE)

    def answer(self):
        return self.res


class Print(Question):
    """Print
    
    :param text: text to print
    """

    def __init__(self, text):
        self.screen = None
        self.text = text

    def set_screen(self, screen):
        self.screen = screen

    def input(self, c):
        pass

    def renderer(self):
        self.screen.clear()

        self.screen.addstr(0, 0, " " + self.text)

    def answer(self):
        return None
