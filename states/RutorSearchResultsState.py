import typing

import telebot

from states import RutorTorrentDetailsState, RutorSearchState
from states.State import State

# hack to avoid circular dependencies
# https://stackoverflow.com/questions/744373/circular-or-cyclic-imports-in-python


class RutorSearchResultsState(State):
    def __init__(self, machine, FILES, search_url) -> None:
        self.machine = machine
        self.FILES: typing.List = FILES
        self.search_url: str = search_url
        self.shown_files: int = 0

    def on_start(self, bot: telebot.TeleBot) -> None:
        if self.shown_files == 0:
            bot.send_message(self.machine.chat_id,
                             f"{len(self.FILES)} result{'s' if len(self.FILES) > 1 else ''} found")
            self.paginator(bot, self.shown_files, self.shown_files + 10)

        else:
            help_message: str = "Enter '[number]' for download, or 'paginate' to see more, " \
                                "or 'open search' or 'exit' to new search (you can use russian language)"
            bot.send_message(self.machine.chat_id, help_message)

    def on_user_input(self, bot: telebot.TeleBot, message: telebot.types.Message) -> None:
        if message.text in ["open search", "открыть поиск"]:
            bot.send_message(message.chat.id, f"You search link: {self.search_url}")

        elif message.text in ['paginate', 'пагинировать']:
            if self.shown_files > len(self.FILES):
                bot.send_message(self.machine.chat_id, "I showed all the results that were found")
            else:
                self.paginator(bot, self.shown_files, self.shown_files + 10)

        elif message.text.isdigit():
            if int(message.text) - 1 > len(self.FILES):
                bot.send_message(self.machine.chat_id, f"I found only {len(self.FILES)} "
                                                       f"result{'s' if len(self.FILES) > 1 else ''}!")
                return
            file = self.FILES[int(message.text) - 1]
            self.machine.update_state(RutorTorrentDetailsState.RutorTorrentDetailsState(self.machine, file, self))

        elif message.text in ['exit', 'выход']:
            self.machine.update_state(RutorSearchState.RutorSearchState(self.machine))
        else:
            bot.send_message(message.chat.id, "I don't understate you:( Try again")

    def paginator(self, bot: telebot.TeleBot, start=0, end=None) -> None:
        if end is None or end > len(self.FILES):
            end = len(self.FILES)
        for i, item in enumerate(self.FILES[start:end], start=start + 1):
            answer: str = f"{i}: {item.date}  {item.size}  ↑{item.distributions}  ↓{item.loadings}   {item.name} \n"
            bot.send_message(self.machine.chat_id, answer)

        bot.send_message(self.machine.chat_id, f"Showing results {start + 1} to {end} of {len(self.FILES)}")
        self.shown_files += 10

        help_message: str = "Enter '[number]' for download, or 'paginate' to see more, " \
                            "or 'open search' or 'exit' to new search (you can use russian language)"
        bot.send_message(self.machine.chat_id, help_message)