# RedditBot
Takes user input to perform predefined functions on a Reddit account using the PRAW API

The account on which the functions can be performed can be changed by modifying the log-in credentials under praw.ini.

The bot is currently configured to save new posts that contain user-specific keywords from a subreddit of the users choice. It runs on a 30 minute loop where it constantly checks the top 5 posts on the subreddit of choice for newer posts while constantly keeping track of posts that have already been saved in a different file.
