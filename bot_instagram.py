from instabot import Bot

my_bot = Bot()
#login
my_bot.login(username="coding101withsteve", password="vgegikgerier")

#follow a user
my_bot.follow("python_app_projects")

#follow multiple users
my_bot.follow_users(["coding_for_beginners_,""python.app","py_beginners"])

#unfollow the non followers
#my.bot.unfollow_non_followers()

#upload and image
my_bot.upload_photo("pytube.jpg, caption=Pytube | Create your own youtube video downloader using python")

#send message to user
