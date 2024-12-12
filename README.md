# reddit-bot
Reddit bot that replies to top posts in a subreddit using Chatgpt. Records replies in csv file.

## Installation
Install praw and chatai.
```bash
pip install praw openai
```

## How to run
Modify `constants.py` to use your [Reddit API credentials](https://www.reddit.com/prefs/apps) and Chatgpt API key.

Use `tester.py` to test posts and replies to subreddit [testingground4bots](https://www.reddit.com/r/testingground4bots/).

Run `post_replies.py` to reply to top `-l` posts on subreddit `subreddit_name`.
```bash
python post_replies.py subreddit_name output_filename -l num_posts_to_reply_to
```

### Example usage
Test posting and replying to top post on subreddit testingground4bots.
```bash
python tester.py
```
Replying to top 1 post on subreddit AskReddit.
```bash
python post_replies.py "AskReddit" "data/results.csv" -l 1
```
![Alt text](https://github.com/user-attachments/assets/077bc2dc-44bb-422d-be6f-25bf1f39e7be)
![Alt text](https://github.com/user-attachments/assets/1376244c-5f29-4bb4-99e9-e8389b4c0761)