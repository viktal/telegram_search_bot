import telebot

import parser_html
import requests
import typing

from states.State import State
from states.constants import URL_RUTOR
from states import RutorSearchResultsState


class RutorSearchState(State):

    def __init__(self, machine) -> None:
        self.machine = machine

    def on_start(self, bot: telebot.TeleBot) -> None:
        bot.send_message(self.machine.chat_id, "What do you want to download?")

    def on_user_input(self, bot: telebot.TeleBot, message: telebot.types.Message) -> None:
        bot.send_message(message.chat.id, "Please wait!")

        try:
            search_url, text = parser_html.get_html(URL_RUTOR + message.text)
        except requests.ConnectionError as err:
            bot.send_message(message.chat.id, f"Something went wrong:( Try again\n\nERROR: {err}")
            self.machine.update_state(RutorSearchState(self.machine))
            return
        FILES: typing.Optional[typing.List[parser_html.File]]
        try:
            FILES = sorted(parser_html.parser_text(text), key=lambda file: int(file.distributions), reverse=True)
        except ValueError as err:
            bot.send_message(self.machine.chat_id, err)
            return

        if len(FILES) == 0:
            bot.send_message(self.machine.chat_id, "Sorry, nothing found:( Try again")
        else:
            self.machine.update_state(RutorSearchResultsState.RutorSearchResultsState(self.machine, FILES, search_url))
