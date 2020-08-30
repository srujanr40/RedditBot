import praw
import re
import os
import pdb
import time


reddit = praw.Reddit('bot')

sub = input("Enter the name of the subreddit (without the 'r/'): ")
subreddit = reddit.subreddit(sub)

searchText = input("Enter the keywords to search for: ")

while (True):

    if not os.path.isfile("saved_posts.txt"):
        saved_posts = []

    else:
        with open("saved_posts.txt", "r") as file:
            saved_posts = file.read()
            saved_posts = saved_posts.split("\n")
            # For getting rid of all empty post_ids in the list
            saved_posts = list(filter(None, saved_posts))
            # From https://stackoverflow.com/questions/40598248/removing-all-empty-elements-from-a-list

    for submission in subreddit.new(limit=20):

        if submission.id not in saved_posts:

            if re.search(searchText, submission.title, re.IGNORECASE):
                print(submission.title)
                print(submission.selftext)
                print(submission.url)
                print("---------------------------------------------------------------------------------------------------------------------")
                # From https://github.com/praw-dev/praw/blob/master/docs/getting_started/quick_start.rst

                submission.save()
                saved_posts.append(submission.id)

    with open("saved_posts", "w") as file:
        for post_id in saved_posts:
            file.write(post_id + "\n")

    time.sleep(1800)
