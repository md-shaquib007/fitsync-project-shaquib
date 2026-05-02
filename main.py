import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Additional formatting for concise and professional display
st.set_page_config(page_title="FitSync", layout="centered")  # Layout centered for compact display

# Function to load Lottie animations from URL
@st.cache_data
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None

# Fetch Lottie animation JSON data
lottie_animation_url = "https://assets6.lottiefiles.com/packages/lf20_tll0j4bb.json"  # Replace with any free-to-use URL
lottie_animation = load_lottieurl(lottie_animation_url)

# Hero Image with reduced height
st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", width=400)  # Reduce width

# Adjusted headers for concise professionalism
st.title("Welcome to FitSync")
st.subheader("Your Personal Health Analytics Dashboard")  # Subheader instead of header for less prominence
st.markdown("<style>.main {max-width: 800px;}</style>", unsafe_allow_html=True)  # Limit width for all content

# More compact welcome text
st.write("Welcome! This platform offers insights into your personal health metrics. Navigate via the sidebar.")
# Separation and about section
st.write("---")  # Horizontal rule

# Concise about section
st.subheader("About FitSync")
st.caption("Empowering personal health through comprehensive analytics.")  # Brief caption

st.write("""
- **Tracks** physical activities and dietary habits.
- Provides **predictive analytics** for assessments.
- Integrates data for a **holistic view**.
Tailored insights for optimized living.
""")

# Smaller Lottie animation for concise appearance
if lottie_animation:
    st_lottie(lottie_animation, height=150, key="bottom")  # Reduce animation height further

