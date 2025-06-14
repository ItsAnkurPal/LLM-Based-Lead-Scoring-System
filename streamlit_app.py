# streamlit_app.py

import streamlit as st
import requests

st.title("🔍 AI Lead Scorer")

with st.form("lead_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    company = st.text_input("Company")
    title = st.text_input("Title")
    inquiry = st.text_area("Inquiry Message")
    source = st.selectbox("Source", ["Demo Request", "LinkedIn", "Cold Email", "Website"])
    industry = st.text_input("Industry")
    location = st.text_input("Location")
    submit = st.form_submit_button("Score Lead")

if submit:
    lead_data = {
        "name": name,
        "email": email,
        "company": company,
        "title": title,
        "inquiry": inquiry,
        "source": source,
        "industry": industry,
        "location": location
    }

    with st.spinner("Scoring lead..."):
        try:
            res = requests.post("http://localhost:8000/score", json=lead_data)
            if res.status_code == 200:
                data = res.json()
                st.success(f"🎯 Score: {data['score']} ({data['category']})")
                st.info(f"💡 Explanation: {data['explanation']}")
            else:
                st.error("Error from API")
        except Exception as e:
            st.error(f"API request failed: {e}")
