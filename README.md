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
python post_replies.py subreddit_name output_filename -l 10
```

### Example usage
Test posting and replying to top post on subreddit testingground4bots.
```bash
python tester.py
```
Replying to top 1 post on subreddit AskReddit.
```bash
> python post_replies.py "AskReddit" "data/results.csv" -l 1
"One thing I've noticed is a lot of people say they want a world where everyone is completely honest all the time. While it sounds great in theory, the reality would likely be a disaster! Imagine the social chaos and hurt feelings that could arise from an unfiltered truth. Small comments could spiral into massive confrontations, and while some honesty is definitely necessary, there’s a reason we have social niceties and white lies. Plus, what about professional settings? Imagine telling your boss exactly what you think of their ideas… yikes! Sometimes, a little tact goes a long way!" Data saved to data/results.csv
```