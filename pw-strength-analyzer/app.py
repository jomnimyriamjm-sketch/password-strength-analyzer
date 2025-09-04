import streamlit as st
import pandas as pd
import re

st.set_page_config(page_title="Password Strength Analyzer", page_icon="🔐", layout="centered")

st.title("🔐 Password Strength Analyzer")

# --- Password Strength Function ---
def check_strength(pw):
    score = 0
    if len(pw) >= 8: score += 1
    if re.search(r"[A-Z]", pw): score += 1
    if re.search(r"[a-z]", pw): score += 1
    if re.search(r"[0-9]", pw): score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw): score += 1
    
    if score <= 1:
        label, color = "🔴 Very Weak", "red"
    elif score == 2:
        label, color = "🟠 Weak", "orange"
    elif score == 3:
        label, color = "🟡 Medium", "gold"
    elif score == 4:
        label, color = "🟢 Strong", "green"
    else:
        label, color = "💎 Very Strong", "darkgreen"
    
    return score, label, color

# --- User Input ---
password = st.text_input("Enter a password to analyze:", type="password")

if password:
    score, label, color = check_strength(password)

    # Nice colored box instead of raw JSON
    st.markdown(
        f"""
        <div style="padding:15px; border-radius:10px; background-color:{color}; color:white; font-size:20px; text-align:center;">
            {label}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add progress bar
    st.progress(score / 5)
