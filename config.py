import os
from pyrogram import Client, filters
import json
from distutils.util import strtobool as stb
SUDO_CHATS_ID = [1344584512]

class Config(object):
# HOME MESSAGE
    HOME_TEXT = """
    **Hello Dear** 👋

This Is Cyberurl.me Next Generation Bot

⚠️ Note : In order to use this bot you need to add first email, password and api.

❤ Click Help to know that how to use this bot

© Bot By @Cyber_url"""

# About Bot Message
    ABOUT_BOT_TEXT = f"""
**This Is https://cyberurl.me/ Next Generation Bot**

🤖 **My Name:** [Cyber URL Bot](https://t.me/Cyber_url)\n
📝 **URL Shortner Site:** [Cyber URL](https://cyberurl.me/)\n
📚 **Sponsor By:** [Cyberstockofficial](https://telegram.me/cyberstock_server)\n
📡 **Hosted on:** [Heroku](https://t.me/cyberstock_support/124)\n
🧑🏻‍💻 **Developer:** @Cyberstock_server
"""

#Help Message
    HELP_TEXT = f"""
🥳 Welcome To Help Section Of LinkShortify Bot
😊 Here You Can Find Use Of All Commands And Also Understand Them Easily 

**💠 Command : /Email**
➡️ Use : Just Type /Email cyberstock.help@gmail.com

**💠 Command : /password**
➡️ Use : Just Type /password yourpassword

**💠 Command : /api**
➡️ Just Type /api 26cdb51c97301*bdd81d09432

❤ Your Mail, Password And Api Are Completely Secure By Us ❤️
**⚠️ Note : Above Details Are For Demo Use Your Own Details 🙏**

**💠 Command : /stats & /ref**
➡️ Use : Just Type /stats and wait for few minutes to get your account stats
➡️ Use : Just Type /ref and wait for few minutes to get your referral link

**💠 Commands : /mass & /short**
➡️ Use : Just Type /short link1 to get your link
➡️ Use : Just Type /mass link1 link2 link3 link4 to get mass links one by one

**⚠️ Note : Type Your link instead of link1, link2 , link3 etc.**

🔰 For Support Msg Us At @Cyberurl_support
    """
