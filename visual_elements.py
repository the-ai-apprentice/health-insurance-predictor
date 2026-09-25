import streamlit as st

def render_banner(amount):
    banner_html = f"""
    <div style="
        background-color: #ffffff; 
        border-radius: 10px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); 
        padding: 15px 20px; /* Highly compressed vertical padding */
        text-align: center; 
        margin-bottom: 20px; 
        border: 1px solid #eaeaea;
    ">
        <h1 style="
            color: #1a7a27; /* Force target green color */
            font-size: 2.3rem; 
            margin: 0; /* Annihilate default Streamlit h1 margins */
            padding: 0; 
            font-weight: 700; 
            line-height: 1.2;
        ">
            Estimated Annual Premium: ₹{amount}
        </h1>
        <p style="
            color: #6c6c75; 
            font-size: 0.95rem; 
            margin: 5px 0 0 0; /* Only 5px of space between title and subtitle */
            padding: 0;
        ">
            (*Estimation based on provided data)
        </p>
    </div>
    """
    return banner_html

def apply_custom_css():
    css = """
    <style>
        /* Main background color - Off-white/Cream */
        [data-testid="stAppViewContainer"] {
            background-color: #fcf9f2; 
        }

        /* Sidebar background color - Dark theme */
        [data-testid="stSidebar"] {
            background-color: #17171e;
        }

        /* Hide default top header line */
        [data-testid="stHeader"] {
            background-color: transparent;
        }

        /* Adjust global font to match the clean sans-serif UI */
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }

        /* Force typography in the sidebar to white for legibility */
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] > p {
            color: #ffffff !important;
        }

        /* --- FIX 1: Force solid white border by overriding transparency --- */
        [data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] {
            border: 1.5px solid rgba(255, 255, 255, 1) !important; /* Forces 100% opacity */
            background-color: #21212b !important;
            border-radius: 10px !important;
        }

        /* --- FIX 2: Make the sidebar collapse arrow white --- */
        [data-testid="stSidebarCollapseButton"] svg,
        [data-testid="stSidebar"] button svg {
            color: #ffffff !important;
            fill: #ffffff !important;
            stroke: #ffffff !important;
        }

        /* Make the expand arrow dark so it's visible on the cream background when closed */
        [data-testid="collapsedControl"] svg {
            color: #17171e !important;
            fill: #17171e !important;
            stroke: #17171e !important;
        }

        /* Slider Red Accent Override */
        div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"] { background-color: #ff4b4b; }
        div.stSlider > div[data-baseweb="slider"] > div > div > div:nth-child(2) { background-color: #ff4b4b; }

        /* Style the select box inputs in sidebar to match dark theme */
        [data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background-color: #2b2b36 !important; /* Added !important to enforce dark theme */
            color: white !important;
            border-color: #444 !important;
        }

        [data-testid="stSidebar"] div[data-baseweb="select"] span {
            color: white !important;
        }

        [data-testid="stSidebar"] svg {
            fill: white !important; 
        }
        /* --- Hide the sidebar collapse button --- */
        [data-testid="stSidebarCollapseButton"] {
            display: none !important;
        }
        /* Target native containers in the main area to match the white, shadowed card design */
        [data-testid="stMain"] [data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #ffffff;
            border: 1px solid #f0f0f0 !important;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04); /* Subtle shadow */
            padding: 10px;
        }

        /* Style the multiselect tags (chips) to be dark/grey and compact */
        [data-testid="stMain"] span[data-baseweb="tag"] {
        background-color: #8c8c9b !important;
        color: white !important;
        font-size: 12px !important;      /* Reduce font size */
        padding: 0px 6px !important;     /* Shrink internal padding */
        margin: 2px !important;          /* Shrink external spacing */
        height: 24px !important;         /* Force a shorter tag height */
        }
    
        /* Ensure the text inside the tag inherits the smaller font */
        [data-testid="stMain"] span[data-baseweb="tag"] span {
        font-size: 12px !important;
        }
        /* Main area typography needs to be dark, unlike the sidebar */
        [data-testid="stMain"] label {
            color: #111111 !important;
            font-weight: 500;
        }
        /* Force Segmented Control to expand to full container width */
        [data-testid="stSegmentedControl"] {
            width: 100%;
        }
        [data-testid="stSegmentedControl"] > div {
            width: 100%;
            display: flex;
        }
        [data-testid="stSegmentedControl"] label[data-baseweb="radio"] {
            flex: 1; /* Forces each toggle button to share the space evenly */
            text-align: center;
            justify-content: center;
        }
        .st-key-my_health_container {
        background-color: rgba(255, 255, 255, 1);
        }
        .st-key-my_double_container {
        background-color: rgba(255, 255, 255, 1);
        }
        .st-key-my_personal_container {
        background-color: rgba(30, 30, 34, 1);
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)