import streamlit as st
import pandas as pd
import joblib
import random


# Load trained model
model = joblib.load("house_price_model.pkl")

st.title(" 🏠 House Price Prediction App")


# ----------- Custom CSS with Header & Footer ------------
st.markdown("""
<style>
/* Background Image */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1576941089067-2de3c901e126?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzF8fGhvdXNlfGVufDB8fDB8fHww");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Top-right Header */
#top-header {
    position: fixed;
    top: 80px;
    right: 20px;
    background-color: rgba(0,0,0,0.5);
    padding: 8px 16px;
    border-radius: 8px;
    color: white;
    font-size: 18px;
    font-weight: bold;
    z-index: 100;
}

/* Bottom-left Footer */
#bottom-footer {
    position: fixed;
    bottom: 10px;
    left: 20px;
    background-color: rgba(0,0,0,0.5);
    padding: 6px 14px;
    border-radius: 6px;
    color: white;
    font-size: 14px;
    z-index: 100;
}
</style>

<div id="top-header">Respected Sir Shahzaib & Sir Ali Hamza</div>
<div id="bottom-footer">Developed by Faraz Hussain</div>
""", unsafe_allow_html=True)

# User inputs
square_feet = st.number_input("📏Square Feet", min_value=500, max_value=5000, value=2000)
bedrooms = st.number_input("🛏Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("🛁 Bathrooms", min_value=1, max_value=5, value=2)
neighborhood = st.selectbox("🏙 Neighborhood", ["Rural", "Suburb", "Urban"])
year_built = st.number_input(" 📅 Year Built", min_value=1900, max_value=2025, value=2000)

# Predict
if st.button("🚀 Predict Price"):
    input_data = [[square_feet, bedrooms, bathrooms, neighborhood, year_built]]
    prediction = model.predict(pd.DataFrame(input_data, columns=["SquareFeet", "Bedrooms", "Bathrooms", "Neighborhood", "YearBuilt"]))
    st.success(f" 💰 Estimated Price: ${prediction[0]:,.2f}")

# Advice logic
    advice = []
    if year_built < 2000:
        advice.append("🏚 Consider renovating or upgrading interiors to increase value.")
    if bedrooms > 4 and square_feet < 2000:
        advice.append("⚠ Large family space but limited area — consider space optimization.")
    if neighborhood == "Urban":
        advice.append("🏙 Prime location! High demand area — expect good resale value.")
    if neighborhood == "Rural":
        advice.append("🌳 Peaceful environment, but resale might take longer.")
    if bathrooms < 2:
        advice.append("🚿 Adding another bathroom can boost your property value.")
    
    # Display advice
    if advice:
        st.markdown("<div class='advice'><b>📌 Helpful Advice:</b><br>" + "<br>".join(advice) + "</div>", unsafe_allow_html=True)
    
    # AI-style explanation
    ai_reasons = [
        f"The spacious layout of {square_feet} sq.ft combined with {bedrooms} bedrooms makes it attractive for families.",
        f"Since this property is in a {neighborhood.lower()} area, location plays a big role in pricing.",
        f"The year built ({year_built}) influences the maintenance cost and resale value.",
        f"Having {bathrooms} bathrooms affects buyer interest and comfort level.",
        f"Market trends show properties with more than {bedrooms} bedrooms in {neighborhood.lower()} areas have higher demand."
    ]
    random.shuffle(ai_reasons)
    ai_tip_text = " ".join(ai_reasons[:2])
    
    st.markdown(f"<div class='ai-tips'>💡 AI Insight: {ai_tip_text}</div>", unsafe_allow_html=True)

    # Investment tips
    investment_tips = [
        "📈 Investing in properties near upcoming commercial areas can increase future resale value.",
        "🏦 If the mortgage rate is low, consider buying now to lock in better financing.",
        "🚗 Properties near public transport hubs tend to appreciate faster.",
        "🏫 Proximity to schools and hospitals increases buyer interest.",
        "🌳 Green surroundings and parks nearby attract family buyers."
    ]
    st.markdown(f"<div class='investment-tips'>💼 Investment Tip: {random.choice(investment_tips)}</div>", unsafe_allow_html=True)

    # Market trend simulation
    market_trends = [
        "📊 Current trend: Urban property prices are rising by 5% annually.",
        "📉 Suburb areas are seeing stable prices with slight growth.",
        "📈 Rural lands are attracting eco-friendly housing projects.",
        "📊 Renovated houses are selling 12% faster in your area."
    ]
    st.markdown(f"<div class='market-trend'>📢 Market Trend: {random.choice(market_trends)}</div>", unsafe_allow_html=True)

   