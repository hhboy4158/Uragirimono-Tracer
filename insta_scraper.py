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

    def scrape_followers(self):
       
        for follower in self.profile.get_followers():
            self.followers_list.append(follower.username)
        print("myfollowers:",  self.followers_list)
        
        # get today ex:Sep-16-2019
        today = date.today()
        d1 = today.strftime("%b-%d-%Y")
        print("d1 =", d1)

        # filename = today + unfollowers_ + id + .txt
        filename = d1 + "_followers_" + self.username + ".txt"

        # create & write
        file = open(filename, "w")
        for person in self.followers_list:
            file.write(person + "\n")
        file.close()

    def scrape_following(self):

        for followee in self.profile.get_followees():
            self.following_list.append(followee.username)
        print("following_list:",  self.following_list)

    def generate_unfollowers_list(self):

        # get the different way from two arrays
        unfollow_list = np.setdiff1d(self.following_list, self.followers_list) # unfollow people who are only in following list and not in followers list
        # print("unfollow_list: ", unfollow_list)

        # get today ex:Sep-16-2019
        today = date.today()
        d1 = today.strftime("%b-%d-%Y")
        print("d1 =", d1)

        # filename = today + unfollowers_ + id + .txt
        filename = d1 + "_unfollowers_" + self.username + ".txt"

        # create & write
        file = open(filename, "w")
        for person in unfollow_list:
            file.write(person + "\n")
        file.close()
