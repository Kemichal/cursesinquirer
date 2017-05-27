from abc import ABCMeta, abstractmethod


class Question(metaclass=ABCMeta):

    @abstractmethod
    def set_screen(self, screen): raise NotImplementedError

    @abstractmethod
    def input(self, c): raise NotImplementedError

    @abstractmethod
    def renderer(self): raise NotImplementedError

    @abstractmethod
    def answer(self): raise NotImplementedError
