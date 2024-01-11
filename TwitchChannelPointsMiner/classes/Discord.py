from textwrap import dedent

import requests

from TwitchChannelPointsMiner.classes.Settings import Events


class Discord(object):
    __slots__ = ["webhook_api", "events"]

    def __init__(self, webhook_api: str, events: list):
        self.webhook_api = webhook_api
        self.events = [str(e) for e in events]

    def send(self, message: str, event: Events) -> None:
        if str(event) in self.events:
            requests.post(
                url=self.webhook_api,
                data={
                    "content": dedent(message),
                    "username": "Twitch Channel Points Nof",
                    "avatar_url": "https://i.pinimg.com/564x/9a/8b/33/9a8b33f2ee21808b2a7e58905af47d8e.jpg",
                },
            )
