from instabot import Bot
bot = Bot()
bot.login(username="_y.o.u.n.g_t_", password="iamtired@insta")

######  upload a picture #######
bot.upload_photo("test.jpg", caption="publication automatique Test II")

######  follow someone #######
# bot.follow("youngt.backup")

######  send a message #######
# bot.send_message("Hello from Eric", ['user1','user2'])

######  get follower info #######
# my_followers = bot.get_user_followers("dhavalsays")
# for follower in my_followers:
#     print(follower)

# bot.unfollow_everyone()