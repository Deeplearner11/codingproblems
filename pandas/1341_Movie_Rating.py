# Table: Movies

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | movie_id      | int     |
# | title         | varchar |
# +---------------+---------+
# movie_id is the primary key (column with unique values) for this table.
# title is the name of the movie.
# Each movie has a unique title.
# Table: Users

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | name          | varchar |
# +---------------+---------+
# user_id is the primary key (column with unique values) for this table.
# The column 'name' has unique values.
# Table: MovieRating

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | movie_id      | int     |
# | user_id       | int     |
# | rating        | int     |
# | created_at    | date    |
# +---------------+---------+
# (movie_id, user_id) is the primary key (column with unique values) for this table.
# This table contains the rating of a movie by a user in their review.
# created_at is the user's review date. 
 

# Write a solution to:

# Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
# Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.



# Solution : 

import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    
    # ====================== Part 1: User with MOST RATINGS (Overall) ======================
    # Count total ratings per user (all time)
    user_count = (movie_rating.groupby('user_id').size()
                  .reset_index(name='rating_count'))
    
    user_count = user_count.merge(users, on='user_id')
    
    # Sort: highest count first, then smallest name
    user_count = user_count.sort_values(by=['rating_count', 'name'], 
                                        ascending=[False, True])
    top_user = user_count.iloc[0]['name']
    
    # Part 2: Highest Average Rating in February 2020 
    # Filter February 2020
    feb_ratings = movie_rating[
        (movie_rating['created_at'].dt.month == 2) & 
        (movie_rating['created_at'].dt.year == 2020)
    ]
    
    # Average rating per movie in Feb 2020
    movie_avg = (feb_ratings.groupby('movie_id')['rating']
                 .mean()
                 .reset_index(name='avg_rating'))
    
    movie_avg = movie_avg.merge(movies, on='movie_id')
    
    # Sort: highest avg first, then smallest title
    movie_avg = movie_avg.sort_values(by=['avg_rating', 'title'], 
                                      ascending=[False, True])
    top_movie = movie_avg.iloc[0]['title']
    
    return pd.DataFrame({'results': [top_user, top_movie]})
