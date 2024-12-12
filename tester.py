import constants
import praw
import constants

reddit = praw.Reddit(client_id=constants.client_id,
                         client_secret=constants.client_secret,
                         user_agent=constants.user_agent,
                         username=constants.username,
                         password=constants.password)

def test_post(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    title = "Testing bot"
    subreddit.submit(title=title, selftext="Text body")

def test_comment(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)

    for submission in subreddit.hot(limit=5):
        comment = "Test comment"
        submission.reply(comment)

def main():
    test_post("testingground4bots")
    test_comment("testingground4bots")

if __name__ == "__main__":
    main()