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
import pandas as pd

CURRENT_POSTS = len(pd.read_csv("labels.csv"))

def main():
    print("TakeMeter Data Collection")
    print(f"Community: r/{SUBREDDIT}")
    print(f"Target posts: {TARGET_POSTS}")
    print(f"Output file: {OUTPUT_FILE}")
    print("Status: Waiting for Reddit API approval")
    print(f"Posts collected: {CURRENT_POSTS}")
    print(f"Posts remaining: {TARGET_POSTS - CURRENT_POSTS}")
    print("\nLabel distribution:")
    df = pd.read_csv("labels.csv")
    print(df["label"].value_counts().to_string())

    print("\nLabel balance check:")

    for label, count in df["label"].value_counts().items():
        percentage = count / len(df) * 100

        if percentage > 40:
            print(f"[WARNING] {label}: {percentage:.1f}% exceeds 40%")
        else:
            print(f"[OK] {label}: {percentage:.1f}%")
    print("\nMinimum examples check:")

    for label in ["question", "experience", "opinion", "promotion"]:
        count = df["label"].value_counts().get(label, 0)

        if count < 20:
            print(f"[NEEDS DATA] {label}: {count}/20 examples")
        else:
            print(f"[OK] {label}: {count} examples")
    print("\nDuplicate check:")

    duplicates = df["text"].duplicated().sum()

    if duplicates == 0:
        print("[OK] No duplicate posts found")
    else:
        print(f"[WARNING] {duplicates} duplicate posts found")
if __name__ == "__main__":
    main()