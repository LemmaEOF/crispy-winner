import requests
from .webhooks import HOOKS

# a Discord webhook payload packet that pings everyone in the server and sends them pig poop balls
data = {"username": "lmao", "content": "@everyone nice discord webhook", "embeds": [{"image": {"url": "https://i.kym-cdn.com/photos/images/newsfeed/001/421/934/795.jpg"}}]}


def run():
    while True:
        for hook in HOOKS:
            response = requests.post(hook, data)
            print("Sent payload to webhook !" + str(HOOKS.index(hook)) + "! Response code " + str(response.status_code))

if __name__ == "__main__":
    run()
