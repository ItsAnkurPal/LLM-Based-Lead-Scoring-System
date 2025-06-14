import streamlit as st
from scoring import get_lead_score
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Lead Scorer")

st.title(" LLM-based Lead Scoring System")
st.markdown("Evaluate lead quality using Gemini LLM")

# Lead Input Form
with st.form("lead_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    company = st.text_input("Company")
    title = st.text_input("Job Title")
    industry = st.selectbox("Industry", ["SaaS", "E-Commerce", "Finance", "Healthcare", "Other"])
    location = st.text_input("Location")
    source = st.selectbox("Source Channel", ["Demo Request", "LinkedIn", "Cold Email", "Web Form"])
    inquiry = st.text_area("Inquiry Message")

    submitted = st.form_submit_button("Get Lead Score")

# Handle submission
if submitted:
    if not all([name, email, company, title, industry, location, source, inquiry]):
        st.warning("Please fill all the fields.")
    else:
        with st.spinner("Scoring the lead..."):
            lead = {
                "name": name,
                "email": email,
                "company": company,
                "title": title,
                "industry": industry,
                "location": location,
                "source": source,
                "inquiry": inquiry
            }
            result = get_lead_score(lead)

        # Show results
        st.success(f" Score: {result['score']} ({result['category']})")
        st.markdown(f"** Explanation:** {result['explanation']}")
