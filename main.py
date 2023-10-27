import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="SAT and IELTS Tutor", page_icon=":fire:", layout="wide")


def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load CSS
st.markdown(
    """
    <style>
    .container {
        padding: 20px;
        background-color: #f7f7f7;
        border-radius: 10px;
        margin: 10px 0;
    }
    .header {
        font-size: 28px;
    }
    .subheader {
        font-size: 20px;
    }
    .image-container {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Loading assets
lottie = load_lottie("https://lottie.host/43d9ebf8-5ad1-4e71-95e7-c3a3b573258b/itfSaLxjUL.json")
img = Image.open("images/aizada.jpg")
img1 = Image.open("images/dias.jpg")

# Header section
with st.container():
    st.header("Hello, I am Anuar :wave:")
    st.title("SAT and IELTS tutor")
# My own results
with st.container():
    st.write("---")
    left, right = st.columns(2)
    with left:
        st.subheader("My Achievements")
        st.write("##")
        st.write("- IELTS - 8.0 (Listening - 8.5, Reading - 8.5, Writing and Speaking - 7)")
        st.write("- SAT - 1470 (Math - 790, Reading/Writing - 680)")
        st.write("- NUET - 174 (Math - 96, Critical Thinking - 78)")
    with right:
        st_lottie(lottie, height=500, key='education')
# October cases
with st.container():
    st.write("---")
    st.header("October cases:")
    st.write("##")
    image, text = st.columns((1, 2))
    with image:
        st.image(img, caption="Aizada")
    with text:
        st.subheader("Aizada's Success")
        st.write("##")
        st.write("In just one month, Aizada achieved a remarkable SAT score improvement.")
        st.write("Her total SAT score increased from 1220 (670 in math and 550 in EBRW) to 1480.")
        st.write("This success opened doors to prestigious universities.")
    st.write("---")
    image, text = st.columns((1, 2))
    with image:
        st.image(img1, caption="Dias")
    with text:
        st.subheader("Dias's Success")
        st.write("##")
        st.write("In 1.5 months, Dias increased his SAT score from 990 (480 in EBRW and 510 in math) to 1380.")
        st.write("This quick improvement is a testament to his determination and our focused tutoring sessions.")
        st.write("It opened doors to better opportunities and reinforced his belief in his abilities.")



# Contact
with st.container():
    st.write("---")
    st.header("Sign up for a free trial lesson")
    st.write("##")

    st.subheader("Contact Information")
    name = st.text_input("Your name")
    telegram_id = st.text_input("Your Telegram ID")
    if st.button("Send"):
        st.success("Your information has been submitted!")

