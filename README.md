# VDO DevOps Bot 

This exists primarily to provide emphasis to James flipping people off in Slack.  Probably add something else to it at some point.

## Installation

This software is build using [Slackbot](https://github.com/lins05/slackbot). To get the software to run you first need to install Slackbot. The easiest way to install it is by using pip.

```
sudo pip install slackbot
```

## Usage

### Generate the Slack API token

First you need to get the slack api token for your bot. You have two options:

1. If you use a [bot user integration](https://api.slack.com/bot-users) of slack, you can get the api token on the integration page.
2. If you use a real slack user, you can generate an api token on [slack web api page](https://api.slack.com/web).

### Configure the API token

You need to configure the `API_TOKEN` in a python module `slackbot_settings.py`, which must be located in a python import path. There is a example file `slackbot_settings.py.sample`, rename the file and add your API token and you're ready to go.

slackbot_settings.py:

```python
API_TOKEN = "<your-api-token>"
PLUGINS = []
```

### Starting the bot

After you've configured everything simply start the bot by running the python-script.

```
python vdobot.py
```
