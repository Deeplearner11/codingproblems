# You are given the list of Facebook friends and the list of Facebook pages that users follow. Your task is to create a new recommendation system for Facebook. For each Facebook user, find pages that this user doesn't follow but at least one of their friends does. Output the user ID and the ID of the page that should be recommended to this user.

# DataFrames
# users_friends
# users_pages
# Expected Output Type
# pandas.DataFrame

# users_friends
# user_id:int64
# friend_id:int64

# users_pages
# user_id:int64
# page_id:int64

import pandas as pd

# 1. Find all pages followed by the users' friends
# Merge friends with pages on friend_id == user_id
friends_pages = pd.merge(
    users_friends,
    users_pages,
    left_on="friend_id",
    right_on="user_id",
    suffixes=("_user", "_friend"),
    )

# Keep only the target user and the pages their friends follow
friends_pages = friends_pages[["user_id_user", "page_id"]].rename(columns={"user_id_user": "user_id"})

# 2. Find pages the user DOES NOT follow yet
# We do a LEFT JOIN between 'friends_pages' and 'users_pages'
# If a user already follows a page, the right side 'page_id' will match.
# If they don't follow it, the right side will be NaN (Null).
merged = pd.merge(
        friends_pages,
        users_pages,
        on=["user_id", "page_id"],
        how="left",
        indicator=True,
    )

# Filter for rows that only existed in the left dataframe (not followed yet)
recommendations = merged[merged["_merge"] == "left_only"].drop(
        columns=["_merge"]
    )

# 3. Clean up duplicates (multiple friends might follow the same page)
recommendations = recommendations.drop_duplicates().reset_index(drop=True)

recommendations[["user_id", "page_id"]]
