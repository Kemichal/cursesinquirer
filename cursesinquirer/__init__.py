# -*- coding: utf-8 -*-

import curses
import os
import sys
import traceback

from .builtins import MultiSelect, Print, Text, YesNo, Select

__version__ = '0.1.0'


class CursesInquirer:
    """CursesInquirer
    
    :param program_func: a function to run
    """

    def __init__(self, program_func):
        self.program = program_func
        self.result = None
        self.screen = None
        self.custom_stdout = StdOutWrapper()
        self.start()

    def ask(self, question):
        question.set_screen(self.screen)
        return self.run_loop(question)

    def run_loop(self, question):
        while True:
            question.renderer()

            c = self.screen.get_wch()
            if type(c) is str and ord(c) == 27:  # Esc
                exit(0)
            elif c in (curses.KEY_ENTER, "\n", "\r"):
                # Enter detected, exit question
                break
            else:
                question.input(c)

        return question.answer()

    def _start(self, screen):
        self.screen = screen

        # Hide cursor
        curses.curs_set(False)

        # Define colors
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

        # Fix stdout
        sys.stdout = self.custom_stdout
        sys.stderr = self.custom_stdout

        self.result = self.program(self)

    def start(self):
        # Set the escape key delay in ms, must be done before wrapper.
        os.environ.setdefault("ESCDELAY", "25")

        # Redirect stdout to buffer
        sys.stdout = self.custom_stdout
        sys.stderr = self.custom_stdout

        try:
            curses.wrapper(self._start)
        except SystemExit as e:
            self.restore_stdout()
            raise e
        except:
            traceback.print_exc(file=sys.stdout)

        self.restore_stdout()

    def restore_stdout(self):
        # Restore/print stdout
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        sys.stdout.write(self.custom_stdout.text)


# Helper class to buffer stdout while curses is active.
class StdOutWrapper:

    def __init__(self):
        self.text = ""

    def write(self, txt):
        self.text += txt
