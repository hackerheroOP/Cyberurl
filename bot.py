# © @Kenil261615

# Importing Modules
import requests, re
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.types.bots_and_keyboards import inline_keyboard_button
import pickledb
import mysql.connector
from mysql.connector import IntegrityError
# from sqlalchemy import alias
from config import Config
import time
from selenium import webdriver
from selenium import *
from selenium.common.exceptions import NoSuchElementException
import os
import pymysql
# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")
# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

# Vars
url = "https://cyberurl.me/api?api="
# mydb = mysql.connector.connect(host="46.4.79.187",user="cybersto_test1	",passwd="8Rf&as=RA0L_",database="cybersto_test1", Connection Lifetime=0,
#  Connection Timeout=0)
mydb  = pymysql.connect(host='46.4.79.187', user='cybersto_test1', password='8Rf&as=RA0L_', database='cybersto_test1	')
cur = mydb.cursor()
# db = pickledb.load("api.db", True)
# db3 = pickledb.load("email.db", True)
# db4 = pickledb.load("password.db", True)
bot = Client('cyberurl',
             api_id=18321001,
             api_hash="84ec30a4ef1c44650127f1c6c35d4429",
             bot_token='6093920300:AAGWTdF3X0uDVF-HedkFaRR_0w0ByYnyLL8',
             workers=50,
             sleep_threshold=10)

def db_init():
    sql = """CREATE TABLE IF NOT EXISTS users_info (
                 user_id INT(10) DEFAULT 0, api VARCHAR(50) DEFAULT NULL, email_id VARCHAR(50) DEFAULT NULL, passwd VARCHAR(40) DEFAULT NULL, PRIMARY KEY(user_id)
              )
              """
    cur.execute(sql)
    print("TABLE INITIATED!")

def user_id(id):
    try:
        sql = "INSERT INTO users_info(user_id) VALUES(%s)"
        cur.execute(sql,(id,))
        mydb.commit()
    except pymysql.err.IntegrityError:
        e = ("User Already Exists")
        # print(e)
        return e

def add_api(api,user):
    sql = "UPDATE users_info SET api = (%s) WHERE user_id = (%s)"
    cur.execute(sql,(api,user))
    mydb.commit()
    # print("API ADDED")

def add_email(email,user):
    sql = "UPDATE users_info SET email_id = (%s) WHERE user_id = (%s)"
    cur.execute(sql,(email,user))
    mydb.commit()

def add_password(passwd,user):
    sql = "UPDATE users_info SET passwd = (%s) WHERE user_id = (%s)"
    cur.execute(sql,(passwd,user))
    mydb.commit()

def get_api(id):
    api_query = ("SELECT api FROM users_info WHERE user_id= (%s)")
    cur.execute(api_query,(id,))
    result = cur.fetchone()
    email = (result[0])
    if email != None:
        return email
    else:
        a = ("No API Added")
        return a
def get_email(id):
    api_query = ("SELECT email_id FROM users_info WHERE user_id= (%s)")
    cur.execute(api_query,(id,))
    result = cur.fetchone()
    email = (result[0])
    if email != None:
        return email
    else:
        a = ("No Email Added")
        return a

def get_password(id):
    api_query = ("SELECT passwd FROM users_info WHERE user_id= (%s)")
    cur.execute(api_query,(id,))
    result = cur.fetchone()
    email = (result[0])
    if email != None:
        return email
    else:
        a = ("No Password Added")
        return a
# HOME Msg

image = "https://telegra.ph/file/60c2aa953eae14761e700.jpg"
@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    userid = message.from_user.id
    user_id(userid)
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
        userid = message.from_user.id
        apii = message.command[1]
        add_api(apii,userid)
#         db.set(str(message.from_user.id), message.command[1])
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
        userid = message.from_user.id
        LINK = message.command[1]
        API = get_api(userid)
        if "No API" in API:
            await message.reply_text("**Please Add API First**", quote=True)
        else:
#         API = db.get(str(message.from_user.id))
            endpoint = f"{url}{API}&url={LINK}" 
#             print(endpoint)
            r = requests.get(endpoint)
            data = r.json()
            print(data)
            data2 = data['shortenedUrl']
        # db2.dump()
            if "linkshortify" in data2:
                msg = f"**Here Is Your Link:\n\n{data2}"
                await message.reply_text((msg), quote=True)
                
@bot.on_message(filters.command('custom') & filters.private)
async def custom(bot, message):
    userid = message.from_user.id
    alias = message.command[1]
    link = message.command[2]
    API = get_api(userid)
    f_url = f"https://cyberurl.me/api?api={API}&url={link}&alias={alias}&format=text"
    r = requests.get(f_url)
    url = r.text
    msg = f"Your Link:\n{url}"
    await message.reply_text(msg, quote=True)
    
# EMAIL
@bot.on_message(filters.command('email') & filters.private)
async def email(bot, message):
    if len(message.command) > 1:
        userid = message.from_user.id
        email_id = message.command[1]
        add_email(email_id, userid)
#         db3.set(str(message.from_user.id), message.command[1])
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
        userid = message.from_user.id
        passwordd = message.command[1]
        add_password(passwordd, userid)
#         db4.set(str(message.from_user.id), message.command[1])
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
    userid = message.from_user.id
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    fetch = message.reply_text("**🔍 Fetching Details....**\n**🚫 Don't Spam**", quote=True)
    login2 = "https://cyberurl.me/auth/signin"
    # driver = webdriver.Chrome()
    driver.get(login2)
    mail = get_email(userid)
    if "No Email" in mail:
           message.reply_text("**Please Add Email First**", quote=True)
#     mail = db3.get(str(message.from_user.id))
    username = driver.find_element("xpath",'//*[@id="username"]').send_keys(mail)
    time.sleep(3)
    passwd = get_password(userid)
    if "No Password" in passwd:
          message.reply_text("**Please Add Password First**", quote=True)
#     passwd = db4.get(str(message.from_user.id))
    passeword = driver.find_element("xpath",'//*[@id="password"]').send_keys(passwd)
    time.sleep(3)
    sign = driver.find_element("xpath",'//*[@id="invisibleCaptchaSignin"]').click()
    time.sleep(5)
    # balance = driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div[3]/div[2]/div/div/div/div[1]/span').text()
    view = driver.find_element('xpath',"/html/body/div[1]/div[1]/section/div[3]/div[1]/div/div/div/div[1]/span").text
    view2 = view.replace(" ","")
    balance = driver.find_element("xpath",'/html/body/div[1]/div[1]/section/div[3]/div[2]/div/div/div/div[1]/span').text
    name = driver.find_element('xpath',"/html/body/div[1]/aside/section/li/a/div[2]/p").text 
    date = driver.find_element('xpath',"/html/body/div[1]/div[1]/section/div[3]/div[1]/div/div/p/span[2]").text
    avg_cpm = driver.find_element('xpath',"/html/body/div[1]/div[1]/section/div[3]/div[4]/div/div/div/div[1]/span").text
    ref_earn = driver.find_element('xpath',"/html/body/div[1]/div[1]/section/div[3]/div[3]/div/div/div/div[1]/span").text
    tbalance = driver.find_element('xpath',"/html/body/div[1]/aside/section/ul/li[3]/a/span").click()
    time.sleep(3)
    total_balance = driver.find_element('xpath',"/html/body/div[1]/div[1]/section/div[2]/div[1]/div/div/div/div/h6").text
    msg = f"**😎Username:** {name}\n**🗓Date:** {date}\n\n**📊Your Today's Statistic\n\n**👀 Views:** {view2}\n**💰Earnings:** {balance}\n**👬REF Earn:** {ref_earn}\n**💲Avg CPM:** {avg_cpm}\n\n**🤑 Total Available Balance :** {total_balance}"
    driver.close()
    fetch.delete()
    message.reply_text(msg, quote=True)
    driver.quit()
  except NoSuchElementException as e:
    print(e)
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
    userid = message.from_user.id
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
    url = "https://cyberurl.me/auth/signin"
    mail = get_email(userid)
    if "No Email" in mail:
           message.reply_text("**Please Add Email First**", quote=True)
    # driver = webdriver.Chrome()
#     mail = db3.get(str(message.from_user.id))
    passwd = get_password(userid)
    if "No Password" in passwd:
          message.reply_text("**Please Add Password First**", quote=True)
#     passwd = db4.get(str(message.from_user.id))
    driver.get(url)
    username = driver.find_element("xpath",'//*[@id="username"]').send_keys(mail)
    time.sleep(3)
    passeword = driver.find_element("xpath",'//*[@id="password"]').send_keys(passwd)
    time.sleep(3)
    sign = driver.find_element('xpath',"//button[@id='invisibleCaptchaSignin']").click()
    name = driver.find_element('xpath',"//p[@class='name']").text
    referral = driver.find_element('xpath',"//span[normalize-space()='Referrals']").click()
    referrallink = driver.find_element('xpath',"/html/body/div[1]/div[1]/section/div[2]/div/pre").text
    print(referrallink)
    msg = f"**😎 Username :** {name}\n\n**🎊 Your Referral Link Is 👇**\n```➡️ {referrallink}``` (Tap To Copy)"
    driver.close()
    fetch.delete()
    message.reply_text(msg, quote=True)
    driver.quit()
  except NoSuchElementException as e:
    print(e)
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
    userid = message.from_user.id
    API = get_api(userid)
    if "No API" in API:
        message.reply_text("**Please Add API First**", quote=True)
#     API = db.get(str(message.from_user.id))
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
        short_link = requests.get(f'https://cyberurl.me/api?api={API}&url={ks}&format=text').text
        shortlinks.append(short_link)
    output = '\n'.join(shortlinks)
    if "cyberurl" in output:
        msg = f"**Here Are Your Links:**\n\n{output}"
        message.reply_text((msg), quote=True)
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
db_init()
print("Bot Started!")
bot.run()
