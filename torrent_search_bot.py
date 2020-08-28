import telebot
import typing
import states.RutorSearchState

RutorSearchState = states.RutorSearchState.RutorSearchState
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
