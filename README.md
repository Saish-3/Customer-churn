Customer Churn Prediction App
A complete end-to-end Machine Learning project that predicts whether an e-commerce customer will churn or stay, built with XGBoost and deployed as a Streamlit web app.

📌 Table of Contents

Overview
Dataset
ML Pipeline
Model Performance
Web App Features
Tech Stack
Project Structure
How to Run Locally
Deployment


🔍 Overview
E-commerce companies lose customers every day without knowing it's coming. This project builds a machine learning model that predicts the likelihood of a customer churning — before it happens — so businesses can launch targeted retention campaigns at the right time.
Live App 👉 https://customerchurn-predictorapp.streamlit.app/

📊 Dataset
PropertyDetailsSourceKaggle — E-Commerce DatasetRows5,630 customersColumns20 featuresTargetChurn (1 = Churned, 0 = Stayed)Class Distribution83% Stayed · 17% Churned
Key Features
FeatureDescriptionTenureHow long the customer has been with the companySatisfactionScoreCustomer satisfaction rating (1–5)DaySinceLastOrderDays since the customer's last orderCashbackAmountAverage cashback received last monthOrderCountTotal orders placed last monthComplainWhether the customer raised a complaintCouponUsedNumber of coupons used last month

⚙️ ML Pipeline
Raw Data (.xlsx)
      ↓
Load Correct Sheet ('E Comm')
      ↓
Handle Missing Values (Median Imputation)
      ↓
Encode Categorical Features (Label Encoding)
      ↓
Train/Test Split (80% / 20%, Stratified)
      ↓
Balance Classes (SMOTE)
      ↓
Train XGBoost Classifier
      ↓
Evaluate → Save Model (.pkl)
      ↓
Streamlit Web App
Why SMOTE?
The dataset had a class imbalance — only 17% of customers churned. Without correction, the model would just predict "stays" every time and still appear 83% accurate. SMOTE creates synthetic churner examples to balance the training data.
Why XGBoost?
XGBoost is a gradient boosting algorithm that consistently outperforms other models on tabular data. It handles missing values well, is robust to outliers, and delivers high accuracy with relatively little tuning.

📈 Model Performance
MetricScoreAccuracy99%ROC-AUC Score0.9988Precision (Churn)96%Recall (Churn)96%F1-Score (Churn)96%

Out of every 100 customers about to leave, the model correctly identifies 96 of them.


🖥️ Web App Features

Real-time prediction — fill in customer details and get an instant churn prediction
Churn probability score — see exactly how likely a customer is to churn
Risk classification — High / Medium / Low risk levels
Actionable recommendations — specific retention strategies based on risk level

🚨 High Risk → Immediate personal outreach + discount offer
⚠️ Medium Risk → Coupon or re-engagement notification
✅ Low Risk → Loyalty rewards + upsell opportunity




🛠️ Tech Stack
ToolPurposePythonCore languageGoogle ColabModel training environmentPandas & NumPyData manipulationScikit-learnPreprocessing & evaluationXGBoostML modelimbalanced-learnSMOTE for class balancingJoblibModel serializationStreamlitWeb app frameworkStreamlit CloudDeployment

📁 Project Structure
customer-churn-prediction/
│
├── app.py                        # Streamlit web application
├── churn_model.pkl               # Trained XGBoost model
├── requirements.txt              # Python dependencies
├── Customer Churn.ipynb          # Google Colab training notebook
└── README.md                     # Project documentation

🚀 How to Run Locally
Prerequisites

Python 3.9+
Git

Steps
bash# 1. Clone the repository
git clone https://github.com/yourusername/customer-churn-prediction.git
cd customer-churn-prediction

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
The app will open at http://localhost:8501

☁️ Deployment
This app is deployed on Streamlit Cloud (free tier).
To deploy your own version:

Fork this repository
Go to share.streamlit.io
Sign in with GitHub
Select this repo, set main file to app.py
Click Deploy!


📚 What I Learned

Handling real-world class imbalance with SMOTE
Why ROC-AUC is a better metric than accuracy for imbalanced datasets
End-to-end ML workflow: data → model → deployment
Building interactive ML apps with Streamlit
Deploying ML models to the cloud for free
