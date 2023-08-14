import pandas as pd

data = {
    'post_id': [1, 2, 3, 4, 5],
    'likes': [50, 100, 150, 75, 200]
}

interaction_data = pd.DataFrame(data)

likes_freq = interaction_data['likes'].value_counts()

likes_freq = likes_freq.sort_index()

print(likes_freq)
