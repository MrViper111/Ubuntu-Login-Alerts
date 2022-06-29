import os
import sys
import requests

server_ip = requests.get("https://api.ipify.org").text
panel_page = "" # If the server is hosted externally, add a link to the panel here. Otherwise, leave it blank
webhook_url = "" # Put the Discord webhook URL here


if panel_page == "":
    embed_description = f"Someone has logged into `{server_ip}`!"
else:
    embed_description = f"Someone has logged into `{server_ip}`! If this was not you, please power off the machine and change the password [here]({panel_page})"

embed = {
    "description": embed_description,
    "title": ":inbox_tray: Logged In",
    "color": 2752256
}

data = {
    "content": "",
    "username": server_ip,
    "embeds": [
        embed
    ]
}


result = requests.post(
    webhook_url,
    json=data
)

try:
    result.raise_for_status()
except requests.exeptions.HTTPError as error:
    print(f"[ERROR] {error}")
else:
    pass
