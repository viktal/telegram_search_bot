from abc import ABCMeta, abstractmethod


class State:
    __metaclass__ = ABCMeta

    @abstractmethod
    def on_start(self, bot):
        pass

    @abstractmethod
    def on_user_input(self, bot, message):
        pass
