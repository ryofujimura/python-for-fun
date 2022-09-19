'''
bot to post images to instagram

'''
from instabot import Bot
bot = Bot()

bot.login(username = "ryofuji.dev", password = "176999Ryo")

bot.upload_photo("one.jpg", caption="post by bot")
