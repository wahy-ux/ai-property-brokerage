
Run locally: streamlit run app.py

Purpose: Demonstrate AI-assisted brokerage logic (profit, ROI, verdict)

import streamlit as st

st.set_page_config(page_title="AI Property Brokerage Bot", layout="centered")

st.title("🏢 AI Investment Property Brokerage Bot") st.caption("AI-assisted market & profit identification for residential deals (1–4 units)")

st.markdown("---")

SELLER INPUT

st.subheader("Property Intake (Seller)") address = st.text_input("Property Address", "123 Main St, Phoenix AZ") condition = st.selectbox("Property Condition", ["Move-in Ready", "Light Repairs", "Heavy Repairs"]) asking_price = st.number_input("Asking Price ($)", min_value=0, step=1000, value=250000)

run = st.button("Run Market & Profit Analysis")

if run: # --- DEMO LOGIC (replace with real AI later) --- base_roi = 0.18 if condition == "Heavy Repairs": base_roi -= 0.04 elif condition == "Move-in Ready": base_roi += 0.02

expected_profit = asking_price * base_roi
roi_percent = (expected_profit / asking_price) * 100 if asking_price > 0 else 0

# Verdict logic
if roi_percent >= 18:
    verdict = "PROCEED"
    verdict_color = "green"
    risk = "Medium"
elif roi_percent >= 12:
    verdict = "REVIEW"
    verdict_color = "orange"
    risk = "High"
else:
    verdict = "REJECT"
    verdict_color = "red"
    risk = "Very High"

# OUTPUT
st.markdown("---")
st.subheader("AI Deal Verdict")

col1, col2 = st.columns(2)
with col1:
    st.metric("Recommended Strategy", "Fix & Flip")
    st.metric("Expected Profit", f"${expected_profit:,.0f}")
with col2:
    st.metric("ROI", f"{roi_percent:.1f}%")
    st.metric("Risk Level", risk)

st.markdown(f"### Verdict: :{verdict_color}[{verdict}]")

st.markdown("---")
st.subheader("Matched Investors")
st.write("✅ 27 active investors matched")
st.write("• Top ROI target: 18–22%")
st.write("• Average close time: 14 days")

st.markdown("---")
st.caption("⚠️ AI-assisted and non-binding. All transactions must be handled by a licensed real estate professional.")

FOOTER

st.markdown("---") st.caption("Demo App – AI Property Brokerage Bot")
