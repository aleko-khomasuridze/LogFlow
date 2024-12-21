from formaters import *
from handler import Handler
from logFlow.formaters.logformater import logFormater

class ConsoleHandler(Handler):
    def handle(self, log) -> None:
        print(logFormater.format(log))