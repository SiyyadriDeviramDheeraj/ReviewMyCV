import streamlit as st
import PyPDF2

st.set_page_config(page_title="ReviewMyCV", layout="wide")

st.markdown("""
<style>
    /* Hide Streamlit elements */
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    header {visibility:hidden;}

    /* Main App Background */
    .stApp {
        background-color: #f8fff8;
    }

    /* Professional Container */
    .main-container {
        max-width: 900px;
        margin: auto;
        padding: 40px;
        background-color: white;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }

    /* Input Styling */
    textarea, .stFileUploader {
        border-radius: 12px !important;
        border: 1px solid #e0e0e0 !important;
    }

    /* Parrot Green Button */
    .stButton>button {
        background-color: #39ff14;
        color: #000;
        font-weight: bold;
        border-radius: 10px;
        width: 100%;
        border: none;
        height: 50px;
        transition: 0.3s transform ease;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        background-color: #32e612;
        color: #000;
    }

    /* Custom Progress Bar Color */
    .stProgress > div > div > div > div {
        background-color: #39ff14;
    }

    /* Metric Card Styling */
    [data-testid="stMetricValue"] {
        color: #1b5e20;
    }
</style>
""", unsafe_allow_html=True)

# Title Section
st.markdown("<h1 style='text-align: left; color: #000000;'>ReviewMyCV</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #666;'>Optimize your application with logic-driven skill matching.</p>",
            unsafe_allow_html=True)


col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.subheader("1. Your Resume")
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    resume_text = ""
    if uploaded_file:
        reader = PyPDF2.PdfReader(uploaded_file)
        for page in reader.pages:
            resume_text += page.extract_text()
        st.success("Resume loaded successfully!")

with col_right:
    st.subheader("2. Job Details")
    job_desc = st.text_area("Paste Job Description", height=150, placeholder="Paste the full job post here...")
    st.info("**Tip:** Paste the full technical requirements to ensure the matching logic detects all specific frameworks and tools.")

st.markdown("---")


SKILL_MAP = {
    "Python": ["python", "py", "pandas", "numpy", "django", "flask"],
    "Java": ["java", "spring boot", "maven", "hibernate", "jsp"],
    "SQL": ["sql", "mysql", "postgresql", "oracle", "nosql", "database", "mongodb"],
    "Machine Learning": ["machine learning", "ml", "ai", "artificial intelligence", "scikit-learn", "tensorflow",
                         "pytorch"],
    "Frontend": ["react", "react.js", "frontend", "javascript", "js", "html", "css", "tailwind"],
    "Cloud/DevOps": ["aws", "azure", "gcp", "docker", "kubernetes", "cloud", "ec2", "s3"],
    "Soft Skills": ["communication", "teamwork", "leadership", "agile", "scrum", "problem solving"]
}

if st.button("Run Match Analysis"):
    if not resume_text or not job_desc:
        st.error("Please provide both a Resume and a Job Description.")
    else:
        job_text_lower = job_desc.lower()
        resume_text_lower = resume_text.lower()

        required_categories = []
        matched_categories = []
        missing_categories = []

        # Logic Engine
        for category, synonyms in SKILL_MAP.items():
            # Check if this skill category is mentioned in the Job Description
            if any(syn in job_text_lower for syn in synonyms):
                required_categories.append(category)
                # Check if it also exists in the Resume
                if any(syn in resume_text_lower for syn in synonyms):
                    matched_categories.append(category)
                else:
                    missing_categories.append(category)


        if not required_categories:
            st.warning("No specific technical keywords detected in the Job Description. Please try a more detailed JD.")
        else:

            score = int((len(matched_categories) / len(required_categories)) * 100)

            if score >= 75:
                fit_level = "Strong Match"
                fit_color = "green"
            elif score >= 50:
                fit_level = "Moderate Match"
                fit_color = "orange"
            else:
                fit_level = "Needs Improvement"
                fit_color = "red"


            st.markdown(f"### Analysis Results")
            m1, m2, m3 = st.columns(3)
            m1.metric("Match Score", f"{score}%")
            m2.metric("Skills Found", f"{len(matched_categories)}/{len(required_categories)}")
            m3.markdown(f"**Fit Level:**\n#### :{fit_color}[{fit_level}]")

            st.progress(score / 100)


            res_col1, res_col2 = st.columns(2)

            with res_col1:
                with st.expander(" Matched Skills", expanded=True):
                    if matched_categories:
                        for s in matched_categories:
                            st.write(f"✔️ {s}")
                    else:
                        st.write("No direct matches found.")

            with res_col2:
                with st.expander(" Missing Skills", expanded=True):
                    if missing_categories:
                        for s in missing_categories:
                            st.markdown(f"<span style='color:#e74c3c;'>✘ {s}</span>", unsafe_allow_html=True)
                    else:
                        st.success("You have all the required skill categories!")


            st.markdown("---")
            st.subheader(" Optimize Your Resume with AI")
            st.write("Copy the pre-engineered prompt below into your preferred AI model to generate a tailored action plan:")

            ai_prompt = f"""
            Act as a Senior Tech Recruiter. Analyze my resume against this Job Description.
            1. Evaluate project relevance for this specific role.
            2. Suggest 3 specific bullet points to add to my resume to close the gaps: {', '.join(missing_categories)}.
            3. Generate 5 behavioral interview questions based on my background.

            [RESUME TEXT]:
            {resume_text}

            [JOB DESCRIPTION]:
            {job_desc}
            """
            st.code(ai_prompt, language="markdown")

st.markdown("---")
st.caption("Privacy First: All processing is done locally. No data is saved.")