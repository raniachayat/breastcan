import streamlit as st 
import json 
import os 
from datetime import datetime 
from fpdf import FPDF 
from io import BytesIO 
from breast_cancer import select_breast_therapy

# ------------------ Page Settings ------------------
st.set_page_config(page_title="BreastCan App", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #fff0f5;
        }
        .stButton>button {
            background-color: #e91e63;
            color: white;
            font-weight: bold;
        }
        .stTextInput>div>div>input {
            background-color: white;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------ Utility Functions ------------------
def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f)

def user_exists(username):
    users = load_users()
    return username in users


def register_user(username, password):
    users = load_users()
    if username in users:
        return False
    users[username] = password
    save_users(users)
    return True

def authenticate_user(username, password):
    users = load_users()
    return username in users and users[username] == password

def clean_text(text):
    return text.encode('latin-1', 'ignore').decode('latin-1')

# ------------------ Session Init ------------------
for key in [
    "logged_in", "username", "last_recommendation", "patient_name", "patient_id",
    "receptor_status", "tumor_characteristics", "stage", "surgery_possible",
    "oncotype_score", "patient_context", "mutations", "prior_therapies",
    "current_page"
]:
    if key not in st.session_state:
        st.session_state[key] = None if key != "logged_in" else False

# Default page is "home"
if st.session_state.current_page is None:
    st.session_state.current_page = "home"

# ------------------ Home Page ------------------
# ------------------ Home Page ------------------
def home_page():
    # Full page styling for background and layout
    st.markdown("""
        <style>
            /* Make background cover the entire app */
            .stApp {
                background: linear-gradient(to bottom right, #ffe6f0, #fff0f5);
                padding-top: 50px;
                padding-bottom: 50px;
            }
            /* Center all content */
            .home-container {
                text-align: center;
            }
            .home-title {
                font-size: 60px;
                font-weight: bold;
                color: #e91e63;
                margin-bottom: 10px;
            }
            .home-subtitle {
                font-size: 24px;
                color: #ff6699;
                margin-bottom: 40px;
            }
            /* Buttons styling */
            div[data-testid="stHorizontalBlock"] button {
                background-color: #e91e63 !important;
                color: white !important;
                font-size: 18px !important;
                font-weight: bold !important;
                padding: 12px 30px !important;
                border-radius: 15px !important;
                border: none !important;
                cursor: pointer !important;
            }
            div[data-testid="stHorizontalBlock"] button:hover {
                background-color: #d81b60 !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # Content container
    st.markdown('<div class="home-container">', unsafe_allow_html=True)
    
    # Optional ribbon image if exists
    if os.path.exists("pink_ribbon.png"):
        st.image("pink_ribbon.png", width=100)

    # Title and subtitle
    st.markdown('<div class="home-title">BreastCan</div>', unsafe_allow_html=True)
    st.markdown('<div class="home-subtitle">Your Breast Cancer Therapy Assistant</div>', unsafe_allow_html=True)
    
    # Buttons in columns
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login"):
            st.session_state.current_page = "login"
    with col2:
        if st.button("Sign Up"):
            st.session_state.current_page = "signup"

    st.markdown('</div>', unsafe_allow_html=True)


def signup_page():
    st.title("Sign Up for BreastCan App")
    if st.button("← Return to Home"):
        st.session_state.current_page = "home"
        return

    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")

    if st.button("Sign Up"):
        if not new_username.strip() or not new_password.strip():
            st.warning("Please fill out both fields.")
        elif user_exists(new_username):
            st.warning("Username already exists.")
        else:
            if register_user(new_username, new_password):
                st.success("Account created successfully. You can now log in.")
            else:
                st.warning("Something went wrong. Please try again.")


def login_page():
    st.title("Login to BreastCan App")
    if st.button("← Return to Home"):
        st.session_state.current_page = "home"
        return

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not username.strip() or not password.strip():
            st.warning("Please fill out both fields.")
        elif authenticate_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Logged in successfully!")
            st.session_state.current_page = "main"
        else:
            st.warning("Invalid username or password.")


# ------------------ Main Form ------------------
def main_form():
    st.title("Breast Cancer Therapy Recommendation")
    st.subheader("Patient Information")
    patient_id = st.text_input("Patient ID")
    patient_name = st.text_input("Patient Name")
    # Clinical Inputs
    receptor_status = {
        "ER": st.selectbox("Estrogen Receptor (ER)", ["positive", "negative"]),
        "PR": st.selectbox("Progesterone Receptor (PR)", ["positive", "negative"]),
        "HER2": st.selectbox("HER2 Status", ["positive", "negative"]),
    }
    tumor_characteristics = {
        "tumor_size_cm": st.number_input("Tumor Size (cm)", min_value=0.0),
        "tumor_grade": st.selectbox("Tumor Grade", [1, 2, 3]),
        "node_status": st.selectbox("Node Status", ["N0", "N1"]),
        "ki67": st.selectbox("Ki-67", ["low", "high"]),
        "lvi": st.checkbox("Lymphovascular Invasion (LVI)?"),
    }
    stage = st.selectbox("Tumor Stage", ["I", "II", "III", "IV"])
    surgery_possible = st.checkbox("Is Surgery Possible?", value=True)
    oncotype_score = st.number_input("Oncotype DX Score", min_value=0, step=1)
    patient_context = {
        "age": st.number_input("Patient Age", min_value=0, step=1),
        "pregnant": st.checkbox("Is the patient pregnant?"),
        "performance_status": st.slider("ECOG Performance Status", 0, 5),
        "menopausal_status": st.selectbox("Menopausal Status", ["premenopausal", "postmenopausal"]),
    }
    st.subheader("Mutation Selection (max 2)")
    mutation_options = list(select_breast_therapy.__globals__["mutation_therapies"].keys())
    selected_mutations = st.multiselect("Select up to 2 mutations", mutation_options, max_selections=2)
    prior_therapies = []
    for m in selected_mutations:
        used = st.checkbox(f"Has preferred therapy for {m} already been used?")
        if used:
            info = select_breast_therapy.__globals__["mutation_therapies"][m]
            prior_therapies.append(info["preferred_therapy"])
    generate = st.button("Generate Recommendation")
    if generate:
        inputs = {
            "receptor_status": receptor_status,
            "tumor_characteristics": tumor_characteristics,
            "stage": stage,
            "surgery_possible": surgery_possible,
            "genomic_score": {"oncotype_dx_score": oncotype_score},
            "patient_context": patient_context,
            "mutations": selected_mutations,
            "prior_therapies": prior_therapies,
        }
        recommendation = select_breast_therapy(inputs)
        st.session_state.last_recommendation = recommendation
        st.session_state.patient_name = patient_name
        st.session_state.patient_id = patient_id
        st.session_state.receptor_status = receptor_status
        st.session_state.tumor_characteristics = tumor_characteristics
        st.session_state.stage = stage
        st.session_state.surgery_possible = surgery_possible
        st.session_state.oncotype_score = oncotype_score
        st.session_state.patient_context = patient_context
        st.session_state.mutations = selected_mutations
        st.session_state.prior_therapies = prior_therapies
    if st.session_state.last_recommendation:
        st.markdown(f"### Recommendation for {st.session_state.patient_name}")
        st.code(st.session_state.last_recommendation, language="markdown")
        if st.button("Generate Report"):
            buffer, filename = generate_pdf_report()
            st.download_button("Download Report", data=buffer, file_name=filename, mime="application/pdf")

# ------------------ PDF Export ------------------
def generate_pdf_report():
    class PDF(FPDF):
        def header(self):
            if os.path.exists("pink_ribbon.png"):
                self.image("pink_ribbon.png", 10, 8, 15)
            self.set_font("Arial", "B", 14)
            self.set_text_color(233, 30, 99)
            self.cell(0, 10, "Breast Cancer Therapy Report", ln=True, align="C")
            self.set_draw_color(233, 30, 99)
            self.line(10, 20, 200, 20)
            self.ln(10)

        def footer(self):
            self.set_y(-15)
            self.set_font("Arial", "I", 8)
            self.set_text_color(128)
            self.cell(0, 10, f"Page {self.page_no()}", align="C")

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)
    pdf.set_text_color(0)
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    pdf.cell(0, 10, f"Date: {date_str}", ln=True)
    pdf.cell(0, 10, f"Doctor: Dr. {st.session_state.username}", ln=True)
    pdf.cell(0, 10, f"Patient: {st.session_state.patient_name} (ID: {st.session_state.patient_id})", ln=True)
    pdf.set_text_color(233, 30, 99)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Clinical Inputs", ln=True)
    pdf.set_text_color(0)
    pdf.set_font("Arial", size=11)
    r = st.session_state.receptor_status
    t = st.session_state.tumor_characteristics
    c = st.session_state.patient_context
    pdf.multi_cell(0, 8, f"Receptor Status: ER = {r['ER']}, PR = {r['PR']}, HER2 = {r['HER2']}")
    pdf.multi_cell(0, 8, f"Stage: {st.session_state.stage} | Surgery Possible: {'Yes' if st.session_state.surgery_possible else 'No'}")
    pdf.multi_cell(0, 8, f"Oncotype DX Score: {st.session_state.oncotype_score}")
    pdf.multi_cell(0, 8, f"Tumor Size: {t['tumor_size_cm']} cm | Grade: {t['tumor_grade']}, Node: {t['node_status']}, Ki-67: {t['ki67']}, LVI: {'Yes' if t['lvi'] else 'No'}")
    pdf.multi_cell(0, 8, f"Patient Age: {c['age']} | Pregnant: {'Yes' if c['pregnant'] else 'No'}, ECOG: {c['performance_status']}, Menopausal Status: {c['menopausal_status']}")
    if st.session_state.mutations:
        pdf.multi_cell(0, 8, "Mutations: " + ", ".join(st.session_state.mutations))
    if st.session_state.prior_therapies:
        pdf.multi_cell(0, 8, "Prior Therapies Used: " + ", ".join(st.session_state.prior_therapies))
    pdf.ln(5)
    pdf.set_text_color(233, 30, 99)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Final Recommendation", ln=True)
    pdf.set_text_color(0)
    pdf.set_font("Arial", size=11)
    pdf.set_fill_color(255, 235, 245)
    for line in st.session_state.last_recommendation.split("\n"):
        pdf.multi_cell(0, 8, clean_text(line), fill=True)
    pdf_data = pdf.output(dest="S").encode("latin1")
    buffer = BytesIO(pdf_data)
    filename = f"report_{st.session_state.patient_name.replace(' ', '_')}_{st.session_state.patient_id}.pdf"
    return buffer, filename

# ------------------ Logout ------------------
def logout():
    for key in st.session_state:
        st.session_state[key] = None
    st.session_state.logged_in = False
    st.success("Logged out.")

# ------------------ App Routing ------------------
if not st.session_state.logged_in:
    if st.session_state.current_page == "home":
        home_page()
    elif st.session_state.current_page == "login":
        login_page()
    elif st.session_state.current_page == "signup":
        signup_page()
else:
    with st.sidebar:
        st.image("logo.png", width=200)
        st.title("BreastCan App")
        st.write(f"Logged in as: **{st.session_state.username}**")
        if st.button("Logout"):
            logout()
    main_form()
