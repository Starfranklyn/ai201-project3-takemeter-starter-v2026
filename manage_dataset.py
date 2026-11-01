import pandas as pd

EXISTING_FILE = "labels.csv"
NEW_FILE = "new_posts_pending.csv"

VALID_LABELS = [
    "question",
    "experience",
    "opinion",
    "promotion"
]
PREVIEW_FILE = "labels_merged_preview.csv"

def main():
    existing = pd.read_csv(EXISTING_FILE)
    new = pd.read_csv(NEW_FILE)

    print("TakeMeter Dataset Manager")
    print(f"Existing posts: {len(existing)}")
    print(f"New posts pending: {len(new)}")
    print(f"Total posts: {len(existing) + len(new)}")
    print("\nDuplicate check:")

    duplicates = new["text"].isin(existing["text"]).sum()

    if duplicates == 0:
        print("[OK] No duplicates found")
    else:
        print(f"[WARNING] {duplicates} posts already exist")
    print("\nInternal duplicate check:")

    internal_duplicates = new["text"].str.strip().str.lower().duplicated().sum()

    if internal_duplicates == 0:
        print("[OK] No duplicates within new posts")
    else:
        print(f"[WARNING] {internal_duplicates} repeated posts within new data")
    print("\nLabel validation:")

    invalid_labels = new[~new["label"].isin(VALID_LABELS)]

    if invalid_labels.empty:
        print("[OK] All labels are valid")
    else:
        print("[WARNING] Invalid labels found:")
        print(invalid_labels["label"].unique())

    print("\nEmpty text check:")

    empty_text = new["text"].isna() | (
        new["text"].astype(str).str.strip() == ""
    )

    if empty_text.any():
        print(f"[WARNING] {empty_text.sum()} posts have empty text")
    else:
        print("[OK] No empty posts found")

    print("\nMissing label check:")

    missing_labels = new["label"].isna() | (
        new["label"].astype(str).str.strip() == ""
    )

    if missing_labels.any():
        print(f"[WARNING] {missing_labels.sum()} posts have missing labels")
    else:
        print("[OK] No missing labels found")

        print("\nMerge preview:")

    if (
        duplicates == 0
        and internal_duplicates == 0
        and invalid_labels.empty
        and not empty_text.any()
        and not missing_labels.any()
    ):
        merged = pd.concat([existing, new], ignore_index=True)

        merged.to_csv(PREVIEW_FILE, index=False)

        print(f"[OK] Preview created: {PREVIEW_FILE}")
        print(f"Preview rows: {len(merged)}")
    else:
        print("[BLOCKED] Fix dataset errors before merging.")
if __name__ == "__main__":
    main()