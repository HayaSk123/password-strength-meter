import streamlit as st
import random
import string

st.title("🔐 Password Strength Meter")

# Password generator function
def generate_password(length):
    if length < 8:
        st.error("Password length must be at least 8 characters.")
        return None

    digit = random.choice(string.digits)
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    special = random.choice("!@#$%^&*")

    remaining_length = length - 4
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    remaining_chars = random.choices(all_chars, k=remaining_length)

    pass_chars = list(digit + upper + lower + special + ''.join(remaining_chars))
    random.shuffle(pass_chars)
    return ''.join(pass_chars)

# Password strength checker
def strength_checker(password):
    score = 0
    if len(password) >= 8:
        score += 1
    else:
        st.warning("Password must be at least 8 characters long")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        st.warning("Password must contain at least one digit")

    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        score += 2
    else:
        st.warning("Password must contain both uppercase and lowercase letters")

    if any(char in "!@#$%^&*" for char in password):
        score += 1
    else:
        st.warning("Password must contain at least one special character (!@#$%^&*)")

    return score

# Strength declaration
def declare_strength(score):
    if score in [0,1, 2]:
        return "Weak"
    elif score in [3, 4]:
        return "Moderate"
    elif score == 5:
        return "Strong"

# User input
password = st.text_input("Enter your password", type="password")

if password:
    score = strength_checker(password)
    strength = declare_strength(score)

    if strength == "Weak":
        st.warning("🔴 Password is weak")
        st.write("Here is a stronger password suggestion for you:")
        pass_suggestion = generate_password(12)
        if pass_suggestion:
            st.success(f"💡 Suggested Password: {pass_suggestion}")

    elif strength == "Moderate":
        st.info("🟡 Password is moderate")

    elif strength == "Strong":
        st.success("🟢 Password is strong")