from openai import OpenAI
import constants
import praw
import argparse
import csv
import constants

def generate_comment(query):
    client = OpenAI(api_key=constants.APIKEY)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a user commenting on a Reddit post."},
            {
                "role": "user",
                "content": f"Write a comment about the topic: {query}"
            }
        ]
    )

    return completion.choices[0].message.content


def get_top_subreddit_posts(subreddit_name, limit):
    reddit = praw.Reddit(client_id=constants.client_id,
                         client_secret=constants.client_secret,
                         user_agent=constants.user_agent,
                         username=constants.username,
                         password=constants.password)
    
    subreddit = reddit.subreddit(subreddit_name)

    new_replies = []
    
    for submission in subreddit.hot(limit=limit):
        comment = generate_comment(submission.title)
        submission.reply(comment)

        print(comment)

        new_replies.append({
            'title': submission.title,
            'id': submission.id,
            'url': submission.url,
            'comment': comment
        })

    return new_replies
    

def save_to_csv(data, output_file_name):
    with open(output_file_name, 'w', newline='', encoding='utf-8') as data_file:
        csv_writer = csv.writer(data_file)

        header = data[0].keys()
        csv_writer.writerow(header)

        for entry in data:
            csv_writer.writerow(entry.values())


def main():
    parser = argparse.ArgumentParser(description="Replies to hottest n posts of a subreddit.")
    parser.add_argument('subreddit', help='Name of subreddit')
    parser.add_argument('output_filename', help='Name of the output csv file')
    parser.add_argument('-l', '--limit', help="Limit on the number of posts to reply to", nargs='?', const=10, type=int)
    args = parser.parse_args()

    new_replies_data = get_top_subreddit_posts(args.subreddit, limit=args.limit)

    save_to_csv(new_replies_data, args.output_filename)

    print(f"Data saved to {args.output_filename}")

if __name__ == "__main__":
    main()
