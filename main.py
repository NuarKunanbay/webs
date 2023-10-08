import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title = "SAT and IELTS tutor", page_icon = ":fire:", layout = "wide")

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


#loading assets
lottie =load_lottie("https://lottie.host/43d9ebf8-5ad1-4e71-95e7-c3a3b573258b/itfSaLxjUL.json")
img = Image.open("images/aizada.jpg")
img1 = Image.open("images/dias.jpg")


#header section
with st.container():
    st.header("Hello, I am Anuar :wave:")
    st.title("SAT and IELTS tutor")

with st.container():
    st.write("---")
    left, right = st.columns(2)
    with left:

        st.header("My own results are:")
        st.write("##")
        st.write("- IELTS - 8.0 (Listening - 8.5, Reading - 8.5, Writing and Speaking - 7)")
        st.write("- SAT - 1470 (mathematics - 790, reading/writing - 680) ")
        st.write("- NUET - 174 (mathematics - 96, critical thinking - 78)")
        st.write("---")
        st.header("I invite all motivated students to individual and group lessons.")
        st.write("##")
        st.write("My educational program is based on my personal experience of successful preparation.My students have achieved impressive results, improving their exam scores from 1100 to 1500 points. Successful cases of my students confirm the effectiveness of my methodology.")
        st.write(" - During the teaching process, I also use artificial intelligence tools to optimize the lesson plan and schedule to ensure that each student receives the most effective learning.")
        st.write(" - I have 1 year of teaching experience (over 500 working hours), and I strive to make lessons interesting and effective. My goal is to help you succeed in your studies.")
        st.write(" - If you are looking for a teacher with proven methods, an individual approach, and the use of artificial intelligence for lesson planning, I am ready to help you! ")



    with right:
        st_lottie(lottie, height = 800, key = 'education')

with st.container():
    st.write("---")
    st.header("Successful cases:")
    st.write("##")
    image, text = st.columns((1,2))
    with image:
        st.image(img)

    with text:
        st.header("Aizada, a determined student, found me online with an initial SAT score of 1220 (670 in math and 550 in EBRW).")
        st.write("##")
        st.write(" In just one month of dedicated hard work and my guidance as her SAT tutor, she achieved remarkable progress.")
        st.write("We honed her math skills to perfection, resulting in a score of 800. On the EBRW section, we worked extensively on reading comprehension and grammar, boosting her score to 650.")
        st.write("---")
        st.header("Aizada's total SAT score increased from 1220 to an impressive 1450, a testament to her determination and our focused tutoring sessions.")
        st.write("##")
        st.write("Her success not only opened doors to prestigious universities but also reinforced her belief that she can achieve anything she sets her mind to.")

with st.container():
    st.write("---")
    st.write("##")
    image, text = st.columns((1,2))

    with image:
        st.image(img1)
        st.write("##")

    with text:
        st.header("Dias, a hard-working student, approached me with an initial SAT score of 990 (480 in EBRW and 510 in math).")
        st.write("##")
        st.write("In just 1.5 months of dedicated hard work and under my guidance as his SAT tutor, he achieved remarkable progress.")
        st.write("We focused on refining his math skills and strategies, resulting in a score of 720.")
        st.write("On the EBRW section, we worked extensively on reading comprehension and grammar, boosting his score to 650")
        st.write('---')
        st.header("Dias's total SAT score increased from 990 to an impressive 1370 in this relatively short time frame.")
        st.write('##')
        st.write('This quick improvement is a proof to his determination and our focused tutoring sessions. His success not only opened doors to better opportunities but also reinforced his belief in his own abilities.')

# contacts

with st.container():
    st.write("---")

    st.header('Sign up for the free trial lesson')
    st.write("##")

    contact = """
    <form action="https://formsubmit.co/kunanbaevanuar79@gmail.com" method="POST">
     <input type = "hidden" name = "_captcha" value = "false">
     <input type="text" name="name" placeholder = "Your name" required>
     <input type="text" name="telegram_id" placeholder = "Your telegram id" required>
     <button type="submit">Send</button>
    </form>
    """
    left, right = st.columns(2)
    with left:
        st.markdown(contact, unsafe_allow_html=True)
    with right:
        st.empty()





