import streamlit as st

st.set_page_config(
    page_title="ATM Simulator",
    page_icon="🏧",
    layout="centered",
)

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(160deg, #0a0a0a, #1a1a2e, #16213e);
}
[data-testid="stHeader"] { background: transparent; }

html, body, p, div, span, label, h1, h2, h3, h4 {
    color: #ffffff !important;
}

/* ATM Card */
.atm-card {
    background: linear-gradient(135deg, #1e3a5f, #0f2027);
    border: 1px solid rgba(0,200,150,0.3);
    border-radius: 20px;
    padding: 1.8rem 2rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 32px rgba(0,200,150,0.1);
}
.atm-card-label {
    font-size: 0.75rem;
    color: rgba(0,200,150,0.7) !important;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.atm-balance {
    font-size: 2.8rem;
    font-weight: 700;
    color: #00c896 !important;
    letter-spacing: -1px;
    margin: 4px 0;
}
.atm-title {
    font-size: 0.82rem;
    color: rgba(255,255,255,0.35) !important;
}

/* Tabs */
[data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.04);
    border-radius: 12px;
    padding: 4px;
    gap: 4px;
}
[data-baseweb="tab"] {
    background: transparent !important;
    color: rgba(255,255,255,0.45) !important;
    border-radius: 8px !important;
    font-weight: 500;
    font-size: 0.88rem;
}
[aria-selected="true"] {
    background: linear-gradient(135deg, #00c896, #00a878) !important;
    color: #000 !important;
    font-weight: 700 !important;
}

/* Input */
[data-testid="stNumberInput"] input,
[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 10px !important;
    color: #fff !important;
    font-size: 1.1rem !important;
    padding: 10px 14px !important;
}
[data-testid="stNumberInput"] input:focus {
    border-color: #00c896 !important;
    box-shadow: 0 0 0 2px rgba(0,200,150,0.2) !important;
}
[data-testid="stNumberInput"] label,
[data-testid="stTextInput"] label {
    color: rgba(255,255,255,0.6) !important;
    font-size: 0.85rem !important;
    font-weight: 500;
}

/* Buttons */
[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #00c896, #00a878) !important;
    color: #000 !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    width: 100%;
    padding: 12px !important;
    transition: all 0.2s;
}
[data-testid="stButton"] > button:hover {
    box-shadow: 0 6px 20px rgba(0,200,150,0.4) !important;
    transform: translateY(-1px);
}

/* Transaction history */
.txn-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.75rem 1rem;
    border-radius: 10px;
    margin-bottom: 8px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
}
.txn-credit { color: #00c896 !important; font-weight: 700; }
.txn-debit  { color: #ff6b6b !important; font-weight: 700; }
.txn-label  { color: rgba(255,255,255,0.7) !important; font-size: 0.9rem; }
.txn-time   { color: rgba(255,255,255,0.3) !important; font-size: 0.75rem; }

/* Alert tweaks */
[data-testid="stAlert"] { border-radius: 10px !important; }

/* Metric */
[data-testid="stMetric"] {
    background: rgba(0,200,150,0.07);
    border-radius: 12px;
    padding: 0.8rem 1rem;
    border: 1px solid rgba(0,200,150,0.15);
}
[data-testid="stMetricValue"] { color: #00c896 !important; }
[data-testid="stMetricLabel"] { color: rgba(255,255,255,0.5) !important; }

#MainMenu, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Session State ─────────────────────────────────────────────────────────────
if "balance" not in st.session_state:
    st.session_state.balance = 0.0
if "transactions" not in st.session_state:
    st.session_state.transactions = []
if "owner" not in st.session_state:
    st.session_state.owner = "Ayush"

def add_txn(txn_type, amount):
    from datetime import datetime
    st.session_state.transactions.append({
        "type": txn_type,
        "amount": amount,
        "time": datetime.now().strftime("%I:%M %p"),
    })

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style='text-align:center; padding: 1.5rem 0 0.5rem 0;'>
    <div style='font-size:3rem;'>🏧</div>
    <h1 style='font-size:2rem; font-weight:700; margin:0; color:#fff;'>ATM Simulator</h1>
    <p style='color:rgba(255,255,255,0.35); font-size:0.88rem; margin:4px 0 0 0;'>Python Practice Project</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Balance Card ──────────────────────────────────────────────────────────────
total_deposited = sum(t["amount"] for t in st.session_state.transactions if t["type"] == "Deposit")
total_withdrawn = sum(t["amount"] for t in st.session_state.transactions if t["type"] == "Withdraw")

st.markdown(f"""
<div class='atm-card'>
    <div class='atm-card-label'>Current Balance</div>
    <div class='atm-balance'>₹ {st.session_state.balance:,.2f}</div>
    <div class='atm-title'>Account Holder: {st.session_state.owner}</div>
    <div style='margin-top:1rem; display:flex; gap:1rem;'>
        <div>
            <div style='font-size:0.72rem; color:rgba(0,200,150,0.6); letter-spacing:1px;'>TOTAL DEPOSITED</div>
            <div style='color:#00c896; font-weight:600;'>₹ {total_deposited:,.2f}</div>
        </div>
        <div style='border-left:1px solid rgba(255,255,255,0.1); padding-left:1rem;'>
            <div style='font-size:0.72rem; color:rgba(255,100,100,0.6); letter-spacing:1px;'>TOTAL WITHDRAWN</div>
            <div style='color:#ff6b6b; font-weight:600;'>₹ {total_withdrawn:,.2f}</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["💰  Deposit", "💸  Withdraw", "📋  History"])

# ── DEPOSIT ───────────────────────────────────────────────────────────────────
with tab1:
    st.markdown("### Deposit Money")
    st.divider()
    amount = st.number_input("Enter Amount to Deposit (₹)", min_value=0.0, step=100.0, key="dep_amt")

    # Quick amount buttons
    st.markdown("<div style='color:rgba(255,255,255,0.45); font-size:0.8rem; margin-bottom:6px;'>Quick Select:</div>", unsafe_allow_html=True)
    q1, q2, q3, q4 = st.columns(4)
    with q1:
        if st.button("₹500", key="q500"):
            st.session_state.balance += 500
            add_txn("Deposit", 500)
            st.success("✅ ₹500 Deposited!")
            st.rerun()
    with q2:
        if st.button("₹1000", key="q1000"):
            st.session_state.balance += 1000
            add_txn("Deposit", 1000)
            st.success("✅ ₹1000 Deposited!")
            st.rerun()
    with q3:
        if st.button("₹2000", key="q2000"):
            st.session_state.balance += 2000
            add_txn("Deposit", 2000)
            st.success("✅ ₹2000 Deposited!")
            st.rerun()
    with q4:
        if st.button("₹5000", key="q5000"):
            st.session_state.balance += 5000
            add_txn("Deposit", 5000)
            st.success("✅ ₹5000 Deposited!")
            st.rerun()

    st.markdown("")
    if st.button("💰 Deposit", key="btn_dep"):
        if amount <= 0:
            st.warning("⚠️ Enter a valid amount.")
        else:
            st.session_state.balance += amount
            add_txn("Deposit", amount)
            st.success(f"✅ ₹{amount:,.2f} Deposited! New Balance: ₹{st.session_state.balance:,.2f}")
            st.rerun()

# ── WITHDRAW ──────────────────────────────────────────────────────────────────
with tab2:
    st.markdown("### Withdraw Money")
    st.divider()
    amount = st.number_input("Enter Amount to Withdraw (₹)", min_value=0.0, step=100.0, key="wd_amt")

    st.markdown("")
    if st.button("💸 Withdraw", key="btn_wd"):
        if amount <= 0:
            st.warning("⚠️ Enter a valid amount.")
        elif amount > st.session_state.balance:
            st.error(f"❌ Insufficient Balance! Available: ₹{st.session_state.balance:,.2f}")
        else:
            st.session_state.balance -= amount
            add_txn("Withdraw", amount)
            st.success(f"✅ ₹{amount:,.2f} Withdrawn! Remaining: ₹{st.session_state.balance:,.2f}")
            st.rerun()

# ── HISTORY ───────────────────────────────────────────────────────────────────
with tab3:
    st.markdown("### Transaction History")
    st.divider()

    if not st.session_state.transactions:
        st.info("📭 No transactions yet.")
    else:
        txns = list(reversed(st.session_state.transactions))
        for t in txns:
            sign = "+" if t["type"] == "Deposit" else "-"
            cls = "txn-credit" if t["type"] == "Deposit" else "txn-debit"
            icon = "⬆️" if t["type"] == "Deposit" else "⬇️"
            st.markdown(f"""
            <div class='txn-item'>
                <div>
                    <div class='txn-label'>{icon} {t['type']}</div>
                    <div class='txn-time'>{t['time']}</div>
                </div>
                <div class='{cls}'>{sign}₹{t['amount']:,.2f}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("")
        if st.button("🗑️ Clear History", key="clr"):
            st.session_state.transactions = []
            st.rerun()

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align:center; color:rgba(255,255,255,0.15); font-size:0.75rem;'>ATM Simulator • Python Practice Project</div>",
    unsafe_allow_html=True,
)