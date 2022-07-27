# © @Kenil261615

# Importing Modules
import requests, re
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.types.bots_and_keyboards import inline_keyboard_button
import pickledb
# from sqlalchemy import alias
from config import Config
import time
from selenium import webdriver
from selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os

# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")
# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

# Vars
url = "https://linkshortify.com/api?api="
db = pickledb.load("api.db", True)
db3 = pickledb.load("email.db", True)
db4 = pickledb.load("password.db", True)
bot = Client('linkshortiify',
             api_id=5363773,
             api_hash="0433df559c3256e881f48a19171a80b8",
             bot_token='5029137284:AAE2eNEMQnPi3EhAu8VfuxFx9nxUT-GKGFg',
             workers=50,
             sleep_threshold=10)


# HOME Msg

image = "https://telegra.ph/file/624b37149a995536c0065.png"
@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    text = Config.HOME_TEXT.format(message.chat.first_name, message.chat.id)
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton('Help', callback_data="help"),
         InlineKeyboardButton('About Bot', callback_data="about")]
    ]

    )
    # await message.reply_text(

    #     text=text,
    #     reply_markup=reply_markup,
    #     disable_web_page_preview=True
    # )
    await bot.send_photo(message.chat.id,image,caption=text,reply_markup=reply_markup)

# HELP
@bot.on_message(filters.command('help') & filters.private)
async def start(bot, message):
    helpp = Config.HELP_TEXT
    await message.reply_text(helpp)
# API CMD


@bot.on_message(filters.command('api') & filters.private)
async def api(bot, message):
    if len(message.command) > 1:
        db.set(str(message.from_user.id), message.command[1])
        await message.reply_text('Api Added Successfully ✅')
    else:
        await message.reply("Please Provide API Along With Command.\n\n Click On **Help** Button To Know", bot,
                            reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton('Help', callback_data="help"),
                                 InlineKeyboardButton('About Bot', callback_data="about")]
                            ]

                            )
                            )

# Short CMD


@bot.on_message(filters.command('short') & filters.private)
async def short(bot, message):
    if len(message.command) > 1:
        LINK = message.command[1]
        API = db.get(str(message.from_user.id))
        endpoint = f"{url}{API}&url={LINK}" 
        print(endpoint)
        r = requests.get(endpoint)
        data = r.json()
        print(data)
        data2 = data['shortenedUrl']
        # db2.dump()
        if "linkshortify" in data2:
            msg = f"**Here Is Your Link:\n\n{data2}"
            await message.reply_text((msg), quote=True)
        else:
            await message.reply_text("Please Add Your API", quote=True)
# EMAIL
@bot.on_message(filters.command('email') & filters.private)
async def email(bot, message):
    if len(message.command) > 1:
        db3.set(str(message.from_user.id), message.command[1])
        await message.reply_text('Email Added Successfully ✅')
    else:
         await message.reply("Please Provide Email Along With Command.\n\n Click On **Help** Button To Know", bot,
                            reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton('Help', callback_data="help"),
                                 InlineKeyboardButton('About Bot', callback_data="about")]
                            ]

                            )
                            )

# Password
@bot.on_message(filters.command('password') & filters.private)
async def password(bot, message):
    if len(message.command) > 1:
        db4.set(str(message.from_user.id), message.command[1])
        await message.reply_text('Password Added Successfully ✅')
    else:
         await message.reply("Please Provide Password Along With Command.\n\n Click On **Help** Button To Know", bot,
                            reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton('Help', callback_data="help"),
                                 InlineKeyboardButton('About Bot', callback_data="about")]
                            ]

                            )
                            )

# Balance 
@bot.on_message(filters.command('stats') & filters.private)
def balance(bot, message):
  try:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    fetch = message.reply_text("**🔍 Fetching Details....**\n**🚫 Don't Spam**", quote=True)
    login2 = "https://linkshortify.com/auth/signin"
    # driver = webdriver.Chrome()WebDriverWait(driver, 20).until(EC.element_to_be_clickable
    driver.get(login2)
    mail = db3.get(str(message.from_user.id))
    username = driver.find_element("xpath",'//*[@id="username"]').send_keys(mail)
    time.sleep(3)
    passwd = db4.get(str(message.from_user.id))
    passeword = driver.find_element("xpath",'//*[@id="password"]').send_keys(passwd)
    time.sleep(3)
    WebElement sign = driver.find_element("xpath","""//button[@id='invisibleCaptchaSignin']""")
    Actions actions = new Actions(driver);
    actions.moveToElement(si)gn.click().perform();
#     sign.click()
    time.sleep(5)
    # balance = driver.find_element("xpath",'/html/body/div[1]/div[1]/section/div[3]/div[2]/div/div/div/div[1]/span').text()
    view = driver.find_element('xpath',"/html[1]/body[1]/div[1]/div[1]/section[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").text
    view2 = view.replace(" ","")
    balance = driver.find_element("xpath",'/html[1]/body[1]/div[1]/div[1]/section[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]').text
    name = driver.find_element('xpath',"//p[@class='name']").text 
    date = driver.find_element('xpath',"//div[4]//div[1]//div[1]//div[1]//p[1]//span[2]").text
    avg_cpm = driver.find_element('xpath',"//div[4]//div[4]//div[1]//div[1]//div[1]//div[1]//span[1]").text
    ref_earn = driver.find_element('xpath',"/html[1]/body[1]/div[1]/div[1]/section[1]/div[4]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]").text
    tbalance = driver.find_element("xpath","""//span[n"xpath",ormalize-space()='Payments']""")
    tbalance.click()
    time.sleep(3)
    total_balance = driver.find_element('xpath',"/html[1]/body[1]/div[1]/div[1]/section[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/h6[1]").text
    msg = f"**😎Username:** {name}\n**🗓Date:** {date}\n\n**📊Your Today's Statistic\n\n**👀 Views:** {view2}\n**💰Earnings:** {balance}\n**👬REF Earn:** {ref_earn}\n**💲Avg CPM:** {avg_cpm}\n\n**🤑 Total Available Balance :** {total_balance}"
    driver.close()
    fetch.delete()
    message.reply_text(msg, quote=True)
    driver.quit()
  except NoSuchElementException:
    fetch.delete()
#     message.reply_text(f"**Please Add Mail & Password Before Using This Command!!**\n\n**(or)**\n\n**Invalid Email or Password**", quote=True)
    message.reply(f"**Please Add Mail & Password Before Using This Command!!**\n\n**(or)**\n\n**Invalid Email or Password**\n\n Click On **Help** Button To Know", bot,
                            reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton('Help', callback_data="help"),
                                 InlineKeyboardButton('About Bot', callback_data="about")]
                            ]

                            )
                            )
# Refferal 
@bot.on_message(filters.command('ref') & filters.private)
def balance(bot, message):
  try:
#   emaill = message.from_user.id
#   email_file = open("email.db")
#   file_contents = email_file.read()
#   if str(email) in file_contents:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    fetch = message.reply_text("**🔍 Fetching Details....**\n**🚫 Don't Spam**", quote=True)
    url = "https://linkshortify.com/auth/signin"
    # driver = webdriver.Chrome()
    mail = db3.get(str(message.from_user.id))
    passwd = db4.get(str(message.from_user.id))
    driver.get(url)
    username = driver.find_element('xpath',"""//*[@id="username"]""").send_keys(mail)
    time.sleep(3)
    passeword = driver.find_element('xpath',"""//*[@id="password"]""").send_keys(passwd)
    time.sleep(3)
    sign = driver.find_element("xpath","""//button[@id='invisibleCaptchaSignin']""")
    sign.click()
    name = driver.find_element('xpath',"""//p[@class='name']""").text
    referral = driver.find_element('xpath',"//span[normalize-space()='Referrals']")
    referral.click()
    referrallink = driver.find_element('xpath',"/html[1]/body[1]/div[1]/div[1]/section[1]/div[3]/div[1]/pre[1]").text
    print(referrallink)
    msg = f"**😎 Username :** {name}\n\n**🎊 Your Referral Link Is 👇**\n```➡️ {referrallink}``` (Tap To Copy)"
    driver.close()
    fetch.delete()
    message.reply_text(msg, quote=True)
    driver.quit()
  except NoSuchElementException:
    fetch.delete()
#     message.reply_text(f"**Please Add Mail & Password Before Using This Command!!**\n\n**(or)**\n\n**Invalid Email or Password**", quote=True) 
    message.reply(f"**Please Add Mail & Password Before Using This Command!!**\n\n**(or)**\n\n**Invalid Email or Password**\n\n Click On **Help** Button To Know", bot,
                            reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton('Help', callback_data="help"),
                                 InlineKeyboardButton('About Bot', callback_data="about")]
                            ]

                            )
                            )
#   else:
#     await message.reply_text("Please Add Mail And Password!!")
# Mass
@bot.on_message(filters.command('mass') & filters.private)
def mass(bot, message):
    API = db.get(str(message.from_user.id))
    message2 = message.command
    regex = r'\bhttps?://.\S+'
    raw_links = re.findall(regex,str(message2))
    print(raw_links)
    shortlinks = []
    for link in raw_links:
        blanklist = []
        blanklist.append(link)
        k = str(blanklist)
        ks = k[2:-4]
        print(ks)
        short_link = requests.get(f'https://linkshortify.com/api?api={API}&url={ks}&format=text').text
        shortlinks.append(short_link)
    output = '\n'.join(shortlinks)
    if "linkshortify" in output:
        msg = f"**Here Are Your Links:**\n\n{output}"
        message.reply_text((msg), quote=True)
    else:
        message.reply_text("Please Add Your API First", quote=True)
#CallBack @ueries
@bot.on_callback_query()
async def button(bot, cmd: CallbackQuery):
    cb_data = cmd.data
    if "help" in cb_data:
        await cmd.message.edit(
            Config.HELP_TEXT,
            parse_mode="Markdown",
            disable_web_page_preview=True,
             reply_markup = InlineKeyboardMarkup([
    [InlineKeyboardButton('Go Home', callback_data="gotohome"),
    InlineKeyboardButton('About Bot', callback_data="about")]
    ]
    
    )
        )
    elif "about" in cb_data:
        await cmd.message.edit(
            Config.ABOUT_BOT_TEXT,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([
    [InlineKeyboardButton('Go Home', callback_data="gotohome"),
     InlineKeyboardButton('Help', callback_data="help")]
    ]
    
    )
        )
    elif "gotohome" in cb_data:
        await cmd.message.edit(
            Config.HOME_TEXT,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([
    [InlineKeyboardButton('Help', callback_data="help"),
     InlineKeyboardButton('About Bot', callback_data="about")]
    ]
    
    )
        )
bot.run()
