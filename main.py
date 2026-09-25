import streamlit as st
from premium_estimator import predict_amount
from visual_elements import render_banner, apply_custom_css

st.set_page_config(
        page_title="Health Insurance Cost Predictor",
        page_icon="🛡️", # Placeholder favicon matching the shield logo
        layout="wide",
        initial_sidebar_state="expanded"
    )

apply_custom_css()

header_col1, header_col2 = st.sidebar.columns([1, 3], gap = "small")

with header_col1:
    st.markdown(
        "<div style='font-size: 3.2rem; line-height: 1; margin-top: 3px;'>🛡️</div>",
        unsafe_allow_html=True
    )
with header_col2:
    st.markdown(
        "<h3 style='margin: 0; padding: 0; line-height: 1.3; font-size: 1.6rem; padding-top: 0px;'>Health Insurance<br>Cost Predictor</h3>",
        unsafe_allow_html=True
    )

st.sidebar.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)

# --- Personal Details Section ---
with st.sidebar.container(border=True, key = "my_personal_container"):
    st.markdown(
        '<div style="font-size: 1.1rem; font-weight: 600; color: #ffffff; margin-bottom: 15px; display: flex; align-items: center; gap: 8px;">👦 Personal Details</div>',
        unsafe_allow_html=True
    )

    age = st.slider("**👤 Age**",
                    min_value=18,
                    max_value=100,
                    key="age_input")
    gender = st.selectbox("**⚧ Gender**",
                          options=["Male", "Female"],
                          index=0,
                          key="gender_input")
    region = st.selectbox("**🗺️ Region**",
                          options=["Northwest", "Northeast", "Southwest", "Southeast"],
                          index=0,
                          key="region_input")
    marital_status = st.selectbox("**💍 Marital Status**",
                                  options=["Unmarried", "Married"],
                                  index = 0,
                                  key = "marital_status_input")


# Retrieve the dynamically calculated premium
premium_amount = 0.00
banner_placeholder = st.empty()

# 3. Render
banner_placeholder.markdown(render_banner(0.00), unsafe_allow_html=True)

col1, col2 = st.columns([0.6, 1], gap = "small")

with col1:
    with st.container(border = True, key = "my_health_container"):
        st.markdown(
            '<div style="font-size: 1.15rem; font-weight: 600; color: #111; margin-bottom: 15px; display: flex; align-items: center; gap: 8px;">🏃 Health & Lifestyle</div>',
            unsafe_allow_html=True
        )
        smoking_status = st.selectbox("**🚬 Smoking Status**",
                                      options = ["No Smoking","Regular", "Occasional"],
                                      index = 0,
                                      key = "smoking_input")
        bmi_category = st.selectbox("**⚖️ BMI Category**",
                                    options = ["Underweight", "Normal", "Overweight", "Obesity"],
                                    index = 1,
                                    key = "bmi_input")
        medical_history = st.multiselect("**🏥 Medical History**",
                                         options = ["No Disease", "Heart disease", "High blood pressure","Diabetes", "Thyroid"],
                                         default = ["No Disease"],
                                         key = "medical_input")
        genetical_risk = st.slider("**🧬 Genetical Risk**",
                                 min_value = 0,
                                 max_value = 5,
                                 value = 0,
                                 key = "genetic_input")
with col2:
    with st.container(border = True, key = "my_double_container"):
        st.markdown(
            '<div style="font-size: 1.15rem; font-weight: 600; color: #111; margin-bottom: 15px; display: flex; align-items: center; gap: 8px;">💰 Financial Details</div>',
            unsafe_allow_html=True
        )
        f_col1, f_col2, f_col3 = st.columns(3, gap = "xsmall")
        with f_col1:
            dependants = st.number_input("**👥 Number of Dependants**",
                                         min_value = 0,
                                         max_value = 5,
                                         step = 1,
                                         value = 1,
                                         key = "dependant_input")
        with f_col2:
            income = st.slider("**₹ Income (in Lakhs)**",
                               min_value = 1,
                               max_value = 100,
                               value = 1,
                               key = "income_input")
        with f_col3:
            employment = st.selectbox("**💼 Employment Status**",
                                      options = ['Self-Employed', 'Freelancer', 'Salaried'],
                                      index = 2,
                                      key = "employment_input")

        st.markdown('<div style="height: 33px;"></div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="font-size: 1.15rem; font-weight: 600; color: #111; margin-bottom: 15px; display: flex; align-items: center; gap: 8px;">🏷️ Plan Tier</div>',
            unsafe_allow_html=True
        )
        plan_selection = st.segmented_control("🏷️ Plan Tier",
                                              width = "stretch",
                                              options = ["**🟤 Bronze**", "**⚪ Silver**", "**🟡 Gold**"],
                                              default = "**🟤 Bronze**",
                                              key = "plan_input",
                                              label_visibility = "collapsed")
        st.markdown('<div style="height: 52px;"></div>', unsafe_allow_html=True)
        st.markdown('<hr style="margin: 0 0 15px 0; border: none; border-top: 1px solid #eaeaea;">', unsafe_allow_html=True)

        b_col1, b_col2 = st.columns([1.5,1])
        with b_col2:
            predict_btn = st.button("**🔮 Predict Insurance Cost**", use_container_width = True)

input_dict = {
    # Demographics
    "age": age,
    "gender": gender,
    "region": region,
    "marital_status": marital_status,

    # Health & Lifestyle
    "smoking_status": smoking_status,
    "bmi_category": bmi_category,
    "medical_history": medical_history,  # Returns a list (e.g., ["Diabetes", "Thyroid"])
    "genetical_risk": genetical_risk,

    # Financial Details
    "number_of_dependants": dependants,
    "income_lakhs": income,
    "income_level" : "<10L",
    "employment_status": employment,

    # Target Plan
    "insurance_plan": plan_selection[4:-2]
}

if predict_btn:
    premium_amount = predict_amount(input_dict)
    premium_amount = str(premium_amount)[:-6]+","+str(premium_amount)[-6:]
    banner_placeholder.markdown(render_banner(premium_amount), unsafe_allow_html = True)