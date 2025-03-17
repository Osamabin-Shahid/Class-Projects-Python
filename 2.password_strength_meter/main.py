import streamlit as st
import re

# Add custom CSS
st.markdown("""
    <style>
               
        /* Suggestions Styling */
        .css-suggest {
            
            font-size: 1.1em;
            color: #333;
            background-color: #00d2b3;
            padding: 8px;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🔐 Password Strength Meter")
st.write("This app checks the strength of your password")

# Function to check password strength
def password_strength_check(password):
    score = 0

    # Password length Check
    if len(password) >= 8:
        score += 1
    else:
        st.markdown('<p class="css-suggest">Password must be at least 8 characters long</p>', unsafe_allow_html=True)

    # Upper and lower case check in password    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.markdown('<p class="css-suggest">Password must include both upper and lower case letters</p>', unsafe_allow_html=True)

    # Digits check in password
    if re.search(r"\d", password):
        score += 1
    else:
        st.markdown('<p class="css-suggest">Password must include at least one number</p>', unsafe_allow_html=True)

    # Special character check in password
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        st.markdown('<p class="css-suggest">Password must include at least one special character !@#$%^&*</p>', unsafe_allow_html=True)

    # Strength ratings
    if score == 4:
        st.success("✅ Strong password")
    elif score == 3:
        st.warning("⚠ Medium strength - Consider making it stronger")
    else:
        st.warning("❌ Weak Password - Improve it by using suggestions above")

# Get user input
password = st.text_input("Enter your password", type="password")
password_strength_check(password)

