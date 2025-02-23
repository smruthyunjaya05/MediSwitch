# MediSwitch

MediSwitch is an alternative medicine recommendation system that helps users find suitable alternative medicines based on their prescribed treatments. The system leverages advanced analysis to recommend personalized, safe, and effective alternatives. It also includes a chatbot powered by Botpress that provides recommendations for Ayurvedic medicines and assists with user queries.

## Description

### Web Pages

- **Home Page**: Provides an overview of the dataset, including the total number of medicines, total number of companies, and average rating. It also highlights the features of the system.
- **Recommendation Page**: Allows users to enter the name of a medicine and get recommendations for alternative medicines. Displays the recommendations with details such as company, rating, and image.
- **Medicine Detail Page**: Shows detailed information about a specific medicine, including its composition, uses, side effects, and reviews. Also displays recommended alternative medicines.
- **About Page**: Provides information about the system, its use cases, and how to use it.

### Features

- **Smart Medicine Recommendations**: Find alternatives based on composition similarity and get the top 5 recommended alternatives.
- **Detailed Analysis of Medicines**: View comprehensive information about medicines, including composition, uses, and side effects.
- **Review Trends and Patterns**: Analyze review trends and patterns for different medicines.
- **Comparison of Side Effects and Uses**: Compare side effects and uses of different medicines.
- **Personal Assistant Chatbot**: A chatbot powered by Botpress that recommends Ayurvedic medicines and assists with user queries.

### Chatbot Integration

The system includes a chatbot integrated using Botpress. The chatbot is Ayurvedic-centric and provides recommendations for Ayurvedic medicines. It assists users with their queries and helps them find suitable alternatives based on their prescribed treatments.

To use the chatbot, simply interact with it on any page of the website. The chatbot is embedded using the following scripts in the `templates/base.html` file:

```html
<script src="https://cdn.botpress.cloud/webchat/v2.2/inject.js"></script>
<script src="https://files.bpcontent.cloud/2025/01/23/03/20250123034030-O2SIT1UT.js"></script>
```

## Preview

Here are some screenshots and videos showcasing the system in action:

### Screenshots
![Home Page](static/assets/demo/home.png)
![Recommendation Page](static/assets/demo/recommend.png)
![Chatbot](static/assets/demo/chatbot.png)

### Demo Video
[Watch Demo Video](static/assets/demo/demo.mp4)


## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/MediSwitch.git
   cd MediSwitch
   ```

2. Install the required packages:

   ```sh
   pip install Flask pandas scikit-learn
   ```

3. Update the file path for `Medicine_Details.csv` in `app.py`:

   ```python
   file_path = r"\MediSwitch\Medicine_Details.csv"  # Replace with the correct file path
   ```

4. Run the Flask application:

   ```sh
   python app.py
   ```

5. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

- Navigate to the Home page to get an overview of the dataset and features.
- Use the Recommendation page to find alternative medicines based on your prescribed treatments.
- View detailed information about specific medicines on the Medicine Detail page.
- Learn more about the system and its use cases on the About page.
- Interact with the chatbot for Ayurvedic medicine recommendations and assistance.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
