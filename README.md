# 📰 Fake News Detection System

## 📌 Project Overview

In today's digital age, the rapid dissemination of information has made it challenging to distinguish between genuine and fake news. This project aims to develop a **Fake News Detection System** using Natural Language Processing (NLP) and Machine Learning techniques to classify news articles as real or fake.

---

## 📂 Repository Contents

- `fakenews_detection.ipynb`: Jupyter Notebook containing the data analysis, preprocessing, model training, and evaluation.
- `Scraper.py`: Python script designed to scrape news articles for real-time analysis.
- `model_BernoulliNB.pkl`: Pre-trained Bernoulli Naive Bayes model.
- `model_GaussianNB.pkl`: Pre-trained Gaussian Naive Bayes model.
- `model_RandomForestClassifier.pkl`: Pre-trained Random Forest Classifier model.
- `Design_document_Map.pdf`: Design document outlining the project's architecture and workflow.
- `Report_Project_News.pdf`: Comprehensive report detailing the project's methodology, results, and conclusions.

---

## 🛠️ Installation and Setup

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Vishhh25/Fake_News_Detection_System.git
   cd Fake_News_Detection_System
Create a Virtual Environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install Required Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Note: Ensure you have Python 3.x installed on your system.

📜 Usage
Data Preprocessing and Model Training:

Open and run the fakenews_detection.ipynb notebook to preprocess data, train models, and evaluate their performance.
Real-Time News Scraping:

Use the Scraper.py script to fetch and preprocess news articles for real-time analysis.
Model Inference:

Load the pre-trained models (model_BernoulliNB.pkl, model_GaussianNB.pkl, or model_RandomForestClassifier.pkl) to classify new news articles as real or fake.
🧠 Machine Learning Models
The project explores multiple machine learning algorithms to determine the most effective model for fake news detection:

Bernoulli Naive Bayes: Suitable for binary/boolean features.
Gaussian Naive Bayes: Assumes features follow a normal distribution.
Random Forest Classifier: An ensemble method that operates by constructing multiple decision trees.
The pre-trained models are saved in the repository for immediate use.

📄 Design and Documentation
Design Document: Refer to Design_document_Map.pdf for a detailed overview of the system architecture and workflow.
Project Report: Report_Project_News.pdf provides an in-depth analysis of the project's objectives, methodologies, results, and conclusions.
🤝 Contributing
We welcome contributions to enhance this project. To contribute:

Fork the repository.
Create a new branch: git checkout -b feature-branch-name.
Make your changes and commit them: git commit -m 'Add new feature'.
Push to the branch: git push origin feature-branch-name.
Submit a pull request detailing your changes.
🛡️ License
This project is licensed under the MIT License.

📞 Contact
ravalvishwa2501@gmail.com.

Note: This project is for educational purposes and should not be used as a sole resource for critical decision-making processes.

markdown
Copy
Edit

---

**Instructions**:

1. **Add a `requirements.txt` File**: Ensure that all necessary dependencies are listed in a `requirements.txt` file for easy installation.

3. **Contact Information**: If you're open to collaboration or feedback, consider providing an email address or other contact details.

This `README.md` provides a clear and structured overview of your project, guiding users through understanding, setting up, and utilizing the Fake News Detection System.
::contentReference[oaicite:0]{index=0}
 






