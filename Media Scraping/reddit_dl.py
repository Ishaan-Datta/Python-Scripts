import praw

# Reddit API credentials
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
USERNAME = "your_username"
PASSWORD = "your_password"
USER_AGENT = "your_user_agent"


def get_saved_posts():
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        username=USERNAME,
        password=PASSWORD,
        user_agent=USER_AGENT,
    )

    # Get the user's saved items
    saved_items = reddit.user.me().saved(limit=None)

    # Create a dictionary to store saved posts by subreddit
    saved_by_subreddit = {}

    for item in saved_items:
        if isinstance(item, praw.models.Submission):
            subreddit = item.subreddit.display_name
            title = item.title

            # Add the title to the list of saved posts for the subreddit
            if subreddit not in saved_by_subreddit:
                saved_by_subreddit[subreddit] = []
            saved_by_subreddit[subreddit].append(title)

    return saved_by_subreddit


def print_saved_posts(saved_by_subreddit):
    # Print the saved posts sorted by subreddit
    for subreddit, titles in saved_by_subreddit.items():
        print(f"Subreddit: {subreddit}")
        for title in titles:
            print(f"  - {title}")
        print("\n")


if __name__ == "__main__":
    saved_by_subreddit = get_saved_posts()
    print_saved_posts(saved_by_subreddit)


# scrape reddit saved posts by communities
# save images after found communities
# Reddit scrape saved posts and new priv account
