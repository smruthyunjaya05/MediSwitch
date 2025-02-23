from flask import Flask, request, render_template, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load the dataset
file_path = r"\MediSwitch\Medicine_Details.csv"  # Replace with the correct file path
data = pd.read_csv(file_path)

# Combine relevant text fields into a single description for TF-IDF
text_features = ["Composition", "Uses", "Side_effects"]
data['combined_features'] = data[text_features].apply(lambda x: ' '.join(x.astype(str)), axis=1)

# Vectorize the combined text features using TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['combined_features'])

# Compute cosine similarity between medicines based on text features
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_medicine_type(medicine_name):
    keywords = ["Tablet", "Syrup", "Cream", "Inhaler", "Suspension", "Capsule", "Injection", "Ointment", "Gel", "Solution", "Drops", "Powder", "Spray", "Lotion"]
    for keyword in keywords:
        if keyword.lower() in medicine_name.lower():
            return keyword
    return None

def recommend_medicine(medicine_name):
    if medicine_name.lower() not in data['Medicine Name'].str.lower().values:
        return []
    idx = data[data['Medicine Name'].str.lower() == medicine_name.lower()].index[0]
    medicine_type = get_medicine_type(medicine_name)
    composition = data.iloc[idx]['Composition']
    dosage = data.iloc[idx]['Dosage'] if 'Dosage' in data.columns else None
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:]  # Exclude the first one as it is the same medicine

    recommendations = []
    for i, score in sim_scores:
        recommended_medicine = data.iloc[i]
        if get_medicine_type(recommended_medicine['Medicine Name']) == medicine_type and recommended_medicine['Composition'] == composition:
            if dosage is None or recommended_medicine['Dosage'] == dosage:
                recommendations.append({
                    'name': recommended_medicine['Medicine Name'],
                    'image_url': recommended_medicine['Image URL'],
                    'company': recommended_medicine['Company'] if 'Company' in recommended_medicine else 'Unknown',
                    'excellent_review': recommended_medicine['Excellent Review %'] if 'Excellent Review %' in recommended_medicine else 0,
                    'average_review': recommended_medicine['Average Review %'] if 'Average Review %' in recommended_medicine else 0,
                    'poor_review': recommended_medicine['Poor Review %'] if 'Poor Review %' in recommended_medicine else 0,
                    'description': recommended_medicine['Description'] if 'Description' in recommended_medicine else 'No description'
                })
        if len(recommendations) >= 5:  # Stop when we have enough recommendations
            break

    # Sort by Excellent Review % (descending)
    recommendations = sorted(recommendations, key=lambda x: x['excellent_review'], reverse=True)

    return recommendations


@app.route('/')
def home():
    num_medicines = len(data)
    total_companies = data['Company'].nunique() if 'Company' in data.columns else 0
    if 'Excellent Review %' in data.columns and 'Average Review %' in data.columns and 'Poor Review %' in data.columns:
        avg_rating = data[['Excellent Review %', 'Average Review %', 'Poor Review %']].mean(axis=1).mean()
    else:
        avg_rating = 0
    medicine_types = set()
    for name in data['Medicine Name']:
        medicine_type = get_medicine_type(name)
        if medicine_type:
            medicine_types.add(medicine_type)
    return render_template('home.html', num_medicines=num_medicines, total_companies=total_companies, avg_rating=avg_rating, medicine_types=medicine_types)

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        medicine_to_search = request.form['medicine_name']
        recommendations = recommend_medicine(medicine_to_search)
        return render_template('recommend.html', recommendations=recommendations)
    return render_template('recommend.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/suggestions', methods=['GET'])
def suggestions():
    query = request.args.get('query', '').lower()
    suggestions = data[data['Medicine Name'].str.lower().str.contains(query)]['Medicine Name'].tolist()
    return jsonify(suggestions)

@app.route('/medicine/<name>')
def medicine_detail(name):
    medicine = data[data['Medicine Name'].str.lower() == name.lower()].iloc[0]
    return render_template('medicine_detail.html', medicine=medicine)

if __name__ == '__main__':
    app.run(debug=True)
