import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample user-item rating matrix (rows: users, columns: items)
# Replace this matrix with actual user-item ratings
ratings_matrix = np.array([
    [5, 3, 0, 1],  # User 1
    [4, 0, 0, 1],  # User 2
    [1, 1, 0, 5],  # User 3
    [0, 0, 5, 4],  # User 4
    [2, 0, 4, 0],  # User 5
])

# Calculate similarity between items
item_similarity = cosine_similarity(ratings_matrix.T)

def recommend_items(user_id, num_recommendations=2):
    # Get user ratings
    user_ratings = ratings_matrix[user_id]

    # Compute scores for each item
    scores = item_similarity.dot(user_ratings)
    scores[user_ratings > 0] = 0  # Ignore items already rated by the user

    # Recommend items with the highest scores
    recommended_items = np.argsort(scores)[::-1][:num_recommendations]
    return recommended_items

# Example: Recommend items for user 0
user_id = 0
recommendations = recommend_items(user_id)
print(f"Recommended items for user {user_id}: {recommendations}")