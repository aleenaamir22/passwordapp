import streamlit as st
import re
import random
import string

st.set_page_config(page_title="SecurePass App", page_icon="🔒", layout="wide")

st.sidebar.title("🔑 SecurePass Navigation")
page = st.sidebar.radio("Go to", ["Home", "Strength Checker", "Password Generator", "About"])

#HomePage
if page == "Home":
    st.title("🔒 SecurePass: Your Ultimate Password Companion")
    st.markdown("""
    ## 🛡️ Stay Secure with Strong Passwords
    In today's digital age, security starts with a strong password. 
    SecurePass helps you **create**, **evaluate**, and **improve** your passwords for better security. 
    
    ➤ Check your password strength with **Strength Checker** 🔍
    
    ➤ Generate secure passwords with **Password Generator** 🔐
    
    Stay safe, stay protected! 💪
    """)

#StrengthCheckerPage
elif page == "Strength Checker":
    st.title("🔍 Password Strength Checker")
    password = st.text_input("Enter Your Password", type="password")
    feedback = []
    score = 0

    if password:
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("🔹 Use at least **8 characters**.")

        if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("🔹 Include **both uppercase and lowercase letters**.")

        if re.search(r'\d', password):
            score += 1
        else:
            feedback.append("🔹 Add **at least one number**.")

        if re.search(r'[!@&$%]', password):
            score += 1
        else:
            feedback.append("🔹 Use **special characters** like !, @, &, $, %.")

        if score == 4:
            feedback.append("✅ **Strong Password!** You're good to go! 👍")
        elif score == 3:
            feedback.append("⚠️ **Medium Strength** – Consider making it stronger! 💪")
        else:
            feedback.append("❌ **Weak Password** – Improve security with the tips above! 🔐")

        st.markdown("### 🔎 Password Strength Feedback")
        for tip in feedback:
            st.write(tip)
    else:
        st.info("Enter a password to check its strength!")

#PasswordGeneratorPage
elif page == "Password Generator":
    st.title("🔐 Password Generator")

    name = st.text_input("Enter Your Name")
    birthday = st.text_input("Enter Your Birthday (DDMMYYYY)")

    base_word = (name[:3] + birthday[-4:]).strip()
    if len(base_word) > 6:
        base_word = base_word[:6]

    length = st.slider("Select Your Password Length", min_value=8, max_value=50, value=12)
    use_digits = st.checkbox("Include Numbers")
    use_special = st.checkbox("Include Special Characters")

    def generate_password(base_word, length, use_digits, use_special):
        characters = string.ascii_letters
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation
        random_part = ''.join(random.choice(characters) for _ in range(length - len(base_word)))
        return base_word + random_part

    if st.button("Generate Secure Password"):
        if not base_word:
            st.warning("Please enter at least your Name or Birthday for personalization.")
        else:
            password = generate_password(base_word, length, use_digits, use_special)
            st.success(f"Generated Password: `{password}`")

#AboutPage
elif page == "About":
    st.title("📜 Abou SecurePass")
    st.markdown("""
    **SecurePass** is an all-in-one password management tool that helps users **evaluate password strength** 
    and **generate secure passwords** for online security.This app is developed by  **Aleena Amir**.
    
    ### Features:
    - ✅ Password Strength Checker
    - ✅ Secure Password Generator
    - ✅ Personalized password suggestions
    - ✅ Easy-to-use interface
    
    Developed with ❤️ to keep your accounts **safe and secure**!
    """)
