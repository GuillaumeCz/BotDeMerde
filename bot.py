import os
import time
import re
from slackclient import SlackClient

from generateur import getSentence



slack_cli = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
starterbot_id = None

RTM_READ_DELAY = 1
EXAMPLE_COMMAND = "do"
SENTENCE_COMMAND = "eclaire-nous"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(slack_events):
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    matches = re.search(MENTION_REGEX, message_text)
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    default_response = "Putain mais qu'est-ce que tu dis ? Essaie *{}*. ".format(EXAMPLE_COMMAND)
    response = None
    if command.startswith(EXAMPLE_COMMAND):
        response = "Ok camarade, va falloir un peu coder pour que je fasse des choses"
    if command.startswith(SENTENCE_COMMAND):
        response = getSentence(1)

    slack_cli.api_call(
            "chat.postMessage",
            channel=channel,
            text= response or default_response
            )

if __name__ == "__main__":
    if slack_cli.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running")
        starterbot_id = slack_cli.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_cli.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed")
