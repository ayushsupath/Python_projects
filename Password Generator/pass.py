import streamlit as st
import random
import string

st.set_page_config(
    page_title="Password Generator",
    page_icon="🔐",
    layout="centered",
)

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(160deg, #0d0d0d, #1a1a2e, #0f3460);
}
[data-testid="stHeader"] { background: transparent; }

html, body, p, div, span, label, h1, h2, h3, h4 {
    color: #ffffff !important;
}

/* Password display card */
.pw-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255, 200, 0, 0.25);
    border-radius: 16px;
    padding: 1.5rem;
    margin: 1rem 0;
    text-align: center;
}
.pw-text {
    font-family: 'Courier New', monospace;
    font-size: 1.4rem;
    font-weight: 700;
    color: #ffd166 !important;
    word-break: break-all;
    letter-spacing: 1px;
}

/* Strength bar */
.strength-bar {
    height: 8px;
    border-radius: 6px;
    margin-top: 0.8rem;
    transition: all 0.3s;
}

/* Slider */
[data-testid="stSlider"] label {
    color: rgba(255,255,255,0.7) !important;
    font-weight: 500;
}

/* Checkbox */
[data-testid="stCheckbox"] label {
    color: rgba(255,255,255,0.8) !important;
    font-size: 0.92rem;
}

/* Buttons */
[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #ffd166, #ff9f1c) !important;
    color: #000 !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    width: 100%;
    padding: 12px !important;
    transition: all 0.2s;
}
[data-testid="stButton"] > button:hover {
    box-shadow: 0 6px 20px rgba(255,209,102,0.4) !important;
    transform: translateY(-1px);
}

/* Copy button */
[data-testid="stDownloadButton"] > button,
.copy-btn {
    background: rgba(255,209,102,0.15) !important;
    color: #ffd166 !important;
    border: 1px solid rgba(255,209,102,0.3) !important;
    border-radius: 8px !important;
}

/* Alerts */
[data-testid="stAlert"] { border-radius: 10px !important; }

#MainMenu, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style='text-align:center; padding: 1.5rem 0 0.5rem 0;'>
    <div style='font-size:3rem;'>🔐</div>
    <h1 style='font-size:2rem; font-weight:700; margin:0; color:#fff;'>Password Generator</h1>
    <p style='color:rgba(255,255,255,0.35); font-size:0.88rem; margin:4px 0 0 0;'>Generate strong, random passwords instantly</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Session State ─────────────────────────────────────────────────────────────
if "password" not in st.session_state:
    st.session_state.password = ""

# ── Controls ──────────────────────────────────────────────────────────────────
length = st.slider("Password Length", min_value=4, max_value=32, value=12)

st.markdown("<div style='color:rgba(255,255,255,0.5); font-size:0.85rem; margin: 0.5rem 0;'>Include:</div>", unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    use_upper = st.checkbox("Uppercase (A-Z)", value=True)
    use_digits = st.checkbox("Numbers (0-9)", value=True)
with c2:
    use_lower = st.checkbox("Lowercase (a-z)", value=True)
    use_symbols = st.checkbox("Symbols (!@#$%)", value=True)

st.markdown("<br>", unsafe_allow_html=True)


def password_generator(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    if length < 4:
        return "weak"

    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password


def get_strength(length, types_selected):
    score = types_selected
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    if score <= 2:
        return "Weak", "#ff6b6b", "33%"
    elif score <= 4:
        return "Medium", "#ffd166", "66%"
    else:
        return "Strong", "#00c896", "100%"


# ── Generate Button ───────────────────────────────────────────────────────────
if st.button("🎲 Generate Password"):
    types_selected = sum([use_upper, use_lower, use_digits, use_symbols])
    if types_selected == 0:
        st.warning("⚠️ Select at least one character type.")
    else:
        result = password_generator(length, use_upper, use_lower, use_digits, use_symbols)
        if result == "weak":
            st.warning("⚠️ Minimum 4 characters required for a password.")
        else:
            st.session_state.password = result

# ── Display Password ─────────────────────────────────────────────────────────
if st.session_state.password:
    pw = st.session_state.password
    types_selected = sum([use_upper, use_lower, use_digits, use_symbols])
    label, color, width = get_strength(len(pw), types_selected)

    st.markdown(f"""
    <div class='pw-card'>
        <div class='pw-text'>{pw}</div>
        <div style='background:rgba(255,255,255,0.08); border-radius:6px; margin-top:1rem;'>
            <div class='strength-bar' style='width:{width}; background:{color};'></div>
        </div>
        <div style='margin-top:6px; font-size:0.8rem; color:{color} !important; font-weight:600;'>
            Strength: {label}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Copy-friendly text input
    st.text_input("Copy your password:", value=pw, key="copy_field")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align:center; color:rgba(255,255,255,0.15); font-size:0.75rem;'>Password Generator • Python Practice Project</div>",
    unsafe_allow_html=True,
)