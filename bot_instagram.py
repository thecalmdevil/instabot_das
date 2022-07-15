from time import sleep
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
my_bot.send_message("Hello Steve!", "stevedias796")

#like a post
my_bot.like_user("stevedias796", amount=2)

#comment
user_id = my_bot.get_user_id_from_username("stevedias796")
media_id = my_bot.get_last_user_medias#(user_id)
my_bot.comment(media_id, "This is very nice. I like it!")

sleep(20)
#get list of followers of anyone
followers_list = my_bot.get_user_followers("stevedias796")

following_list = my_bot.get_user_following("stevedias796")

for count, each_follower in enumerate(followers_list):
    print(my_bot.get_username_from_user_id(each_follower))

for each_follow in following_list:
    if count > 4:
        continue
    sleep(5)
    print(my_bot.get_username_from_user_id(each_follow))

my_bot.logout()
