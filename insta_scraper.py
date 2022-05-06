import instaloader
import numpy as np
from datetime import date

class InstagramScraper:

    def __init__(self, username, password):
        
        self.username = username
        self.password = password
        self.profile = None
        self.followers_list = []
        self.following_list = []

    def create_session(self):

        L = instaloader.Instaloader()
        L.login(self.username, self.password) # Login or load session
        self.profile = instaloader.Profile.from_username(L.context, self.username) # Obtain profile metadata
        # self.profile = instaloader.Profile.from_username(L.context, 'gnauh_cire')

    def scrape_followers(self):
       
        for follower in self.profile.get_followers():
            self.followers_list.append(follower.username)
        print("粉絲:",  self.followers_list)
        
        # 取得今天日期 ex:Sep-16-2019
        today = date.today()
        d1 = today.strftime("%b-%d-%Y")
        print("d1 =", d1)

        # 檔案名稱 = 今天日期 + unfollowers_ + id + .txt
        filename = d1 + "_followers_" + self.username + ".txt"

        # 建立 + 寫入檔案
        file = open(filename, "w")
        for person in self.followers_list:
            file.write(person + "\n")
        file.close()

    def scrape_following(self):

        for followee in self.profile.get_followees():
            self.following_list.append(followee.username)
        print("追蹤中:",  self.following_list)

    def generate_unfollowers_list(self):

        # 取兩個陣列的不同處
        unfollow_list = np.setdiff1d(self.following_list, self.followers_list) # unfollow people who are only in following list and not in followers list
        # print("你已經追蹤了，但這些廢物沒追蹤你: ", unfollow_list)

        # 取得今天日期 ex:Sep-16-2019
        today = date.today()
        d1 = today.strftime("%b-%d-%Y")
        print("d1 =", d1)

        # 檔案名稱 = 今天日期 + unfollowers_ + id + .txt
        filename = d1 + "_unfollowers_" + self.username + ".txt"

        # 建立 + 寫入檔案
        file = open(filename, "w")
        for person in unfollow_list:
            file.write(person + "\n")
        file.close()