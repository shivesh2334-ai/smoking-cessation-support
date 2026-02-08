import streamlit as st

st.set_page_config(
    page_title="Smoking Cessation Support",
    page_icon="🚭",
    layout="centered"
)

st.title("🚭 Smoking Cessation Support Tool")
st.caption("Evidence-based guidance for quitting tobacco")

# -----------------------------
# ASK: Tobacco Use
# -----------------------------
st.header("1️⃣ Tobacco Use Assessment")

smoker = st.radio(
    "Have you used tobacco products in the past year?",
    ["Yes", "No"]
)

if smoker == "No":
    st.success("Great! Staying tobacco-free is one of the best things you can do for your health.")
    st.stop()

cigs_per_day = st.number_input(
    "How many cigarettes do you smoke per day?",
    min_value=0,
    max_value=60,
    value=10
)

time_to_first = st.selectbox(
    "How soon after waking do you smoke your first cigarette?",
    [
        "Within 5 minutes",
        "6–30 minutes",
        "31–60 minutes",
        "After 60 minutes"
    ]
)

# Heaviness of Smoking Index (simplified)
dependence_score = 0
dependence_score += 2 if cigs_per_day >= 20 else 1 if cigs_per_day >= 10 else 0
dependence_score += 2 if time_to_first == "Within 5 minutes" else 1 if time_to_first == "6–30 minutes" else 0

st.markdown("**Nicotine Dependence Level:**")
if dependence_score >= 3:
    st.error("High dependence")
elif dependence_score == 2:
    st.warning("Moderate dependence")
else:
    st.success("Low dependence")

# -----------------------------
# ADVISE: Clear Advice
# -----------------------------
st.header("2️⃣ Clinical Advice")

st.info(
    "Stopping smoking is the **single most important action** you can take to improve your health.\n\n"
    "It’s never too late to benefit from quitting."
)

benefits = st.multiselect(
    "What matters most to you about quitting?",
    [
        "Better health",
        "Saving money",
        "Family and children",
        "Freedom from addiction",
        "Better breathing and stamina"
    ]
)

if benefits:
    st.success(f"Quitting will directly help with: **{', '.join(benefits)}**")

# -----------------------------
# CONNECT: Treatment Offer
# -----------------------------
st.header("3️⃣ Treatment & Support")

ready = st.radio(
    "Are you willing to take action toward quitting?",
    ["Yes, I want to quit", "Not ready, but open to reducing", "Not interested right now"]
)

# READY TO QUIT
if ready == "Yes, I want to quit":
    st.subheader("✅ Quit Plan")

    quit_date = st.date_input("Select a quit date (within 2–4 weeks)")

    st.markdown("### Recommended Treatment")
    st.checkbox("Nicotine Replacement Therapy (Patch, Gum, Lozenge)", value=True)
    st.checkbox("Prescription medications (Varenicline / Bupropion)")
    st.checkbox("Behavioral counseling")

    st.markdown("### Behavioral Support")
    st.write("- Telephone quitlines")
    st.write("- App-based or web-based counseling")
    st.write("- Regular follow-up and monitoring")

    st.success("You have taken an important step. Support + medication gives the best success rates.")

# NOT READY BUT OPEN
elif ready == "Not ready, but open to reducing":
    st.subheader("🔄 Harm Reduction Approach")

    st.write(
        "You don’t need to quit all at once. Reducing smoking and using nicotine replacement "
        "can help move you toward quitting when you’re ready."
    )

    st.checkbox("Cut down number of cigarettes per day")
    st.checkbox("Use nicotine replacement to reduce cravings")
    st.checkbox("Set a future quit date")

# NOT INTERESTED
else:
    st.subheader("💬 Motivational Support")

    st.write(
        "Quitting is a process. Even thinking about it today increases the chance of quitting later."
    )

    st.info("Whenever you’re ready, effective treatments and support are available.")

# -----------------------------
# Resources
# -----------------------------
st.header("📞 Support Resources")

st.markdown(
    """
    - **Quitline (India / International):** Local tobacco cessation services  
    - **Web tools:** https://www.smokefree.gov  
    - **Tip:** Make your home and car completely smoke-free
    """
)

st.caption("This tool follows evidence-based smoking cessation guidelines (updated 2025–26).")
