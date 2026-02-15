import streamlit as st
from openai import OpenAI

# Get API key from Streamlit secrets
api_key = st.secrets["KEY"]
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="AI Trip Planner", page_icon="🌍")

st.title("🌍 AI World Trip Planner")
st.write("Plan your trip anywhere in the world in seconds!")

# ----------------------
# USER INPUT
# ----------------------

country = st.text_input("Country you want to visit")

col1, col2 = st.columns(2)

with col1:
    origin = st.text_input("Departure City")
    days = st.number_input("Number of Travel Days", min_value=1, max_value=30)

with col2:
    budget = st.text_input("Total Budget (USD)")
    food = st.selectbox(
        "Food Preference",
        ["No Preference", "Vegetarian", "Vegan", "Halal", "Local Cuisine"]
    )

travel_style = st.selectbox(
    "Travel Style",
    ["Luxury", "Mid-range", "Backpacking", "Adventure", "Relaxed"]
)

# ----------------------
# GENERATE PLAN
# ----------------------

if st.button("Generate Travel Plan ✈️"):

    if not country:
        st.warning("Please enter a country.")
    else:
        prompt = f"""
        Create a detailed travel plan:

        Country: {country}
        Departure City: {origin}
        Number of days: {days}
        Budget: {budget}
        Food preference: {food}
        Travel style: {travel_style}

        Include:
        - Suggested cities
        - Day-by-day itinerary
        - Budget breakdown
        - Estimated flight cost range
        - Visa information
        - Best time to visit
        - Local transport suggestions
        """

        with st.spinner("Planning your trip..."):

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
            )

            plan = response.choices[0].message.content

        st.success("Your Trip Plan is Ready! 🎉")
        st.markdown(plan)


