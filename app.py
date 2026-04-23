import streamlit as st
import pandas as pd
import pickle
import numpy as np

# ─── Load Model ───
import joblib
model = joblib.load("churn_model.pkl")

# ─── Page Config ───
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="🛒",
    layout="wide"
)

# ─── Custom CSS ───
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        padding: 12px 40px;
        border-radius: 10px;
        border: none;
        width: 100%;
    }
    .stButton>button:hover { background-color: #cc0000; }
    .result-box {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ─── Header ───
st.title("🛒 Customer Churn Prediction App")
st.markdown("Fill in the customer details below to predict whether they will **churn or stay**.")
st.divider()

# ─── Input Form ───
st.subheader("📋 Customer Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Account Details**")
    tenure = st.number_input("Tenure (months)", 0, 60, 12)
    city_tier = st.selectbox("City Tier", [1, 2, 3])
    warehouse_to_home = st.number_input("Warehouse to Home (km)", 1, 127, 15)
    num_address = st.number_input("Number of Addresses", 1, 22, 3)
    complain = st.selectbox("Raised a Complaint?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

with col2:
    st.markdown("**Preferences**")
    login_device = st.selectbox("Preferred Login Device",
                                ["Mobile Phone", "Computer", "Phone"])
    payment_mode = st.selectbox("Preferred Payment Mode",
                                ["Debit Card", "Credit Card", "Cash on Delivery",
                                 "E wallet", "UPI", "COD"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    order_cat = st.selectbox("Preferred Order Category",
                             ["Laptop & Accessory", "Mobile", "Mobile Phone",
                              "Fashion", "Grocery", "Others"])
    marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])

with col3:
    st.markdown("**Activity & Engagement**")
    hour_spend = st.number_input("Hours Spent on App", 0, 10, 3)
    devices_registered = st.number_input("Devices Registered", 1, 6, 3)
    satisfaction = st.slider("Satisfaction Score", 1, 5, 3)
    order_hike = st.number_input("Order Amount Hike % (vs last year)", 0, 100, 15)
    coupon_used = st.number_input("Coupons Used (last month)", 0, 16, 2)
    order_count = st.number_input("Order Count (last month)", 1, 16, 3)
    day_since_last_order = st.number_input("Days Since Last Order", 0, 46, 5)
    cashback = st.number_input("Avg Cashback Amount (₹)", 0, 325, 150)

st.divider()

# ─── Encode Inputs ───
login_map     = {"Mobile Phone": 2, "Computer": 0, "Phone": 1}
payment_map   = {"Debit Card": 3, "Credit Card": 2, "Cash on Delivery": 0,
                 "E wallet": 4, "UPI": 5, "COD": 1}
gender_map    = {"Male": 1, "Female": 0}
order_cat_map = {"Laptop & Accessory": 1, "Mobile": 3, "Mobile Phone": 4,
                 "Fashion": 0, "Grocery": 2, "Others": 5}
marital_map   = {"Single": 2, "Married": 1, "Divorced": 0}

input_data = pd.DataFrame([[
    tenure,
    login_map[login_device],
    city_tier,
    warehouse_to_home,
    payment_map[payment_mode],
    gender_map[gender],
    hour_spend,
    devices_registered,
    order_cat_map[order_cat],
    satisfaction,
    marital_map[marital_status],
    num_address,
    complain,
    order_hike,
    coupon_used,
    order_count,
    day_since_last_order,
    cashback
]], columns=[
    'Tenure', 'PreferredLoginDevice', 'CityTier', 'WarehouseToHome',
    'PreferredPaymentMode', 'Gender', 'HourSpendOnApp',
    'NumberOfDeviceRegistered', 'PreferedOrderCat', 'SatisfactionScore',
    'MaritalStatus', 'NumberOfAddress', 'Complain',
    'OrderAmountHikeFromlastYear', 'CouponUsed', 'OrderCount',
    'DaySinceLastOrder', 'CashbackAmount'
])

# ─── Predict Button ───
col_btn = st.columns([1, 2, 1])
with col_btn[1]:
    predict = st.button("🔍 Predict Churn")

if predict:
    prediction  = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.divider()
    st.subheader("📊 Prediction Result")

    res_col1, res_col2, res_col3 = st.columns(3)

    with res_col1:
        st.metric("Prediction",
                  "⚠️ Will Churn" if prediction == 1 else "✅ Will Stay")

    with res_col2:
        st.metric("Churn Probability", f"{probability * 100:.1f}%")

    with res_col3:
        st.metric("Retention Confidence", f"{(1 - probability) * 100:.1f}%")

    st.divider()

    # ─── Action Recommendation ───
    st.subheader("💡 Recommended Action")

    if prediction == 1:
        if probability > 0.80:
            st.error("🚨 **HIGH RISK** — Immediate action required!")
            st.markdown("""
            - 📧 Send a **personalized retention email** with a special discount
            - 🎁 Offer a **loyalty reward** or cashback bonus
            - 📞 Assign a **customer success rep** to reach out directly
            """)
        else:
            st.warning("⚠️ **MEDIUM RISK** — Proactive engagement suggested")
            st.markdown("""
            - 🏷️ Send a **coupon or promo code** for next purchase
            - 📱 Push a **re-engagement notification** on the app
            - ⭐ Ask for **feedback** to understand dissatisfaction
            """)
    else:
        st.success("✅ **LOW RISK** — Customer is likely to stay!")
        st.markdown("""
        - 🌟 Enroll in **loyalty/rewards program**
        - 📣 Ask for a **referral or review**
        - 🎯 Upsell with **personalized product recommendations**
        """)
        