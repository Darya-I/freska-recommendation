from flask import Flask, request, jsonify
from recommender import get_recommendations, user_sim_df, interaction_matrix

app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID not provided'}), 400
    
    recommendations = get_recommendations(user_id, user_sim_df, interaction_matrix)
    
    # ѕровер€ем, €вл€етс€ ли результат списком, если да, то просто возвращаем его
    if isinstance(recommendations, list):
        return jsonify(recommendations)

    # ¬ случае, если это не список (например, если это может быть pandas Series или иной тип данных)
    return jsonify(recommendations.tolist())

if __name__ == '__main__':
    app.run(debug=True)
