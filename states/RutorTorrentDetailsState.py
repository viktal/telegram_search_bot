import telebot
import requests
import states.State
from states import RutorSearchState

State = states.State.State
# RutorSearchState = RutorSearchState.RutorSearchState
# hack to avoid circular dependencies
# https://stackoverflow.com/questions/744373/circular-or-cyclic-imports-in-python


class RutorTorrentDetailsState(State):
    def __init__(self, machine: 'TorrentSearchBot', file, prev_state: 'RutorSearchResultsState') -> None:
        self.machine: 'TorrentSearchBot' = machine
        self.file = file
        self.prev_state: 'RutorSearchResultsState' = prev_state

    def on_start(self, bot: telebot.TeleBot) -> None:
        link_download: str = self.file.download
        link_file: str = "http://www.rutor.info" + self.file.link
        bot.send_message(self.machine.chat_id, f"You download link {link_download} and file link {link_file}")
        torrent = requests.get(link_download)
        bot.send_document(self.machine.chat_id, torrent.content, caption=self.file.name)

        bot.send_message(self.machine.chat_id, "Enter 'back'/'назад' to choose other file or "
                                               "enter 'exit'/'выход' to new search")

    def on_user_input(self, bot: telebot.TeleBot, message: telebot.types.Message) -> None:
        if message.text in ["back", 'назад']:
            self.machine.update_state(self.prev_state)
        elif message.text in ["exit", 'выход']:
            self.machine.update_state(RutorSearchState.RutorSearchState(self.machine))
        else:
            bot.send_message(message.chat.id, "I don't understate you:( Try again")