import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ------------------------------------------------------------

#  Streamlit Page Setup
# ------------------------------------------------------------
st.set_page_config(
    page_title="🏠 House Price Prediction",
    layout="wide",
    page_icon="🏠"
)

# ------------------------------------------------------------
#  Load trained model pipeline

@st.cache_resource
def load_model():
    try:
        with open("modell.pkl", "rb") as file: 
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")
        st.stop()

model = load_model()

# ------------------------------------------------------------


st.title("🏡 King County House Price Prediction App")
st.markdown("### Provide the information below to get a house price estimate.")

st.sidebar.header("📘 About the App")
st.sidebar.write("""
The **King county house price prediction app** is a **Machine Learning web application** designed to estimate house prices in **King County, Washington.** It leverage historical data and key property features to make accurate predictions. Some of these features include `yr_built`, `total_rooms` and other property characteristics.
""") 

# ------------------------------------------------------------
#  Input Section
# ------------------------------------------------------------
st.subheader("🏗️ Enter Property Details:")

col1, col2 = st.columns(2)

with col1:
     view = st.slider("View Rating", 0, 4, 0)
     condition = st.slider("Condition", 1, 5, 3)
     bedrooms = st.number_input("Bedrooms", min_value= 0, max_value = 10, value=3)
     bathrooms = st.number_input("Bathrooms", min_value= 0.0, max_value=10.0, step=0.25, value=2.0)
     floors = st.number_input("Floors", min_value= 1.0, max_value= 3.5, step=0.5, value=1.0)
     total_room = st.number_input("Total Room", min_value= 0.0, max_value= 15.0, step=0.3)
     sqft_living = st.number_input("Living Area (sqft)", min_value = 370, max_value = 13540)
     

with col2:
     sqft_lot = st.number_input("Lot Area (sqft)", min_value= 600, max_value = 1074218)
     waterfront = st.selectbox("Waterfront View", [0, 1])
     sqft_above = st.number_input("Sqft Above", min_value = 370, max_value = 9410)
     sqft_basement = st.number_input("Sqft Basement", min_value = 0, max_value = 4820)
     yr_built = st.number_input("Year Built", min_value = 1900, max_value = 2025)
     city = st.selectbox(
        "City",
        [
            'Seattle', 'Bellevue', 'Redmond', 'Kirkland', 'Kent', 'Auburn',
            'Renton', 'Issaquah', 'Shoreline', 'Bothell', 'Sammamish',
            'Federal Way', 'Maple Valley', 'Woodinville', 'Des Moines',
            'Newcastle', 'Covington', 'Burien', 'Medina', 'Enumclaw'
        ]
    )
     house_age = st.number_input("House Age", min_value = 11, max_value = 125)


# ------------------------------------------------------------
#  Feature Engineering (same as in training)
# ------------------------------------------------------------
house_age = 2025 - yr_built
total_rooms = bedrooms + bathrooms

input_data = pd.DataFrame([{
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'sqft_living': sqft_living,
    'sqft_lot': sqft_lot,
    'floors': floors,
    'waterfront': waterfront,
    'view': view,
    'condition': condition,
    'sqft_above': sqft_above,
    'sqft_basement': sqft_basement,
    'yr_built': yr_built,
    'city': city,
    'house_age': house_age,
    'total_rooms': total_rooms
}])

# ------------------------------------------------------------
#  Prediction
# ------------------------------------------------------------
st.markdown("---")
if st.button("🔮 Predict House Price"):
    try:
        # Predict log(price) and then convert back
        log_price_pred = model.predict(input_data)[0]
        price_pred = np.expm1(log_price_pred)

        st.success(f"💰 **Estimated House Price:** ${price_pred:,.2f}")
        #st.caption("🧠 Model prediction uses logarithmic transformation (expm1 reverse applied).")

    except Exception as e:
        st.error(f"Prediction failed: {e}")

# ------------------------------------------------------------
#  Footer
# ------------------------------------------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>Powered by  ❤️ Python, Streamlit & Machine Learning | Built by Agboola Isaac Oluwatomiwa </p>", unsafe_allow_html=True
)
