# recommender.py

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from data_loader import load_user_cart_items, load_user_preferences, load_user_sessions

# Загрузка данных из базы данных
user_cart_items_df = load_user_cart_items()

# Построение модели
def build_model(user_cart_items_df):
    interaction_matrix = user_cart_items_df.pivot_table(index='UserId', columns='ProductId', values='Quantity', fill_value=0)
    user_similarities = cosine_similarity(interaction_matrix)
    user_sim_df = pd.DataFrame(user_similarities, index=interaction_matrix.index, columns=interaction_matrix.index)
    return user_sim_df, interaction_matrix

# Генерация рекомендаций
def get_recommendations(user_id, user_sim_df, interaction_matrix, n_recommendations=5):
    if user_id not in user_sim_df.index:
        return []

    similar_users = user_sim_df[user_id].sort_values(ascending=False).index[1:n_recommendations+1]
    similar_users_data = interaction_matrix.loc[similar_users]
    recommended_items = similar_users_data.sum().sort_values(ascending=False).index[:n_recommendations]
    
    # Преобразование индексов в список перед возвращением
    return list(recommended_items)

# Построение модели
user_sim_df, interaction_matrix = build_model(user_cart_items_df)
