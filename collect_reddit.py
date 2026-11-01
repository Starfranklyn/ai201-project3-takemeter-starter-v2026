"""
TakeMeter Reddit Data Collection

Community: r/datascience
Target: 200 labeled posts

Reddit API access: Pending approval.
Do not make API requests until access is authorized.
"""

SUBREDDIT = "datascience"
TARGET_POSTS = 200
OUTPUT_FILE = "reddit_posts_unlabeled.csv"

def main():
    print("TakeMeter Data Collection")
    print(f"Community: r/{SUBREDDIT}")
    print(f"Target posts: {TARGET_POSTS}")
    print(f"Output file: {OUTPUT_FILE}")
    print("Status: Waiting for Reddit API approval")


if __name__ == "__main__":
    main()