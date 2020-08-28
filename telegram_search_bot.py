import typing

import telebot
import parser
import requests

SEARCH: str = "http://www.rutor.info/search/"
LIST_BOTS: typing.Dict[typing.Any, 'TorrentSearchBot'] = {}

class TorrentSearchBot:
    bot: telebot.TeleBot = telebot.TeleBot('1322977421:AAHeAFwl5unLwT6KmZmGjkjrTw5Yanl4Pug')

    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.update_state(RutorSearchState(self))

    @staticmethod
    @bot.message_handler(commands=['start'])
    def start_message(message: telebot.types.Message) -> None:
        torrent_search_bot: TorrentSearchBot = TorrentSearchBot(message.chat.id)
        global LIST_BOTS
        LIST_BOTS[torrent_search_bot.chat_id] = torrent_search_bot

    @staticmethod
    @bot.message_handler(content_types=['text'])
    def on_user_input(message: telebot.types.Message) -> None:
        torrent_search_bot: TorrentSearchBot = LIST_BOTS[message.chat.id]
        if torrent_search_bot is not None:
            torrent_search_bot.state.on_user_input(torrent_search_bot.bot, message)
        else:
            print('ERROR')

    def update_state(self, state) -> None:
        self.state = state
        self.state.on_start(self.bot)


class RutorSearchState:

    def __init__(self, machine: TorrentSearchBot) -> None:
        self.machine: TorrentSearchBot = machine

    def on_start(self, bot: telebot.TeleBot) -> None:
        bot.send_message(self.machine.chat_id, "What do you want to download?")

    def on_user_input(self, bot: telebot.TeleBot, message: telebot.types.Message) -> None:
        bot.send_message(message.chat.id, "Please wait!")
        global SEARCH
        SEARCH += message.text

        with open("text.html", "w") as fh:
            try:
                SEARCH, text = parser.get_html(SEARCH)
            except requests.ConnectionError as err:
                bot.send_message(message.chat.id, f"Something went wrong:( Try again\n\nERROR: {err}")
                self.machine.update_state(RutorSearchState(self.machine))
                return
            fh.write(text)
        FILES: typing.List = sorted(parser.parser_text(text), key=lambda file: int(file.distributions), reverse=True)

        if len(FILES) == 0:
            bot.send_message(self.machine.chat_id, "Sorry, nothing found:( Try again")
        else:
            self.machine.update_state(RutorSearchResultsState(self.machine, FILES))


class RutorSearchResultsState:
    def __init__(self, machine, FILES) -> None:
        self.machine: TorrentSearchBot = machine
        self.FILES: typing.List = FILES
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
            bot.send_message(message.chat.id, f"You search link: {SEARCH}")

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
            self.machine.update_state(RutorTorrentDetailsState(self.machine, file, self))

        elif message.text in ['exit', 'выход']:
            self.machine.update_state(RutorSearchState(self.machine))
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


class RutorTorrentDetailsState:
    def __init__(self, machine: TorrentSearchBot, file, prev_state: RutorSearchResultsState) -> None:
        self.machine: TorrentSearchBot = machine
        self.file = file
        self.prev_state: RutorSearchResultsState = prev_state

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
            self.machine.update_state(RutorSearchState(self.machine))
        else:
            bot.send_message(message.chat.id, "I don't understate you:( Try again")


TorrentSearchBot.bot.polling()
