FROM python:3.7

WORKDIR /app
COPY requirements.txt main.py parser_html.py torrent_search_bot.py ./
COPY states ./states
RUN python3.7 -m pip install -r requirements.txt

ENTRYPOINT ["/usr/local/bin/python3.7"]
CMD ["main.py"]

