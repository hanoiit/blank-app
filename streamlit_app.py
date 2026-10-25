import streamlit as st

st.set_page_config(
    page_title="Website của tôi",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 Website Demo")
st.write("Chào mừng đến với website Streamlit của tôi!")

col1, col2 = st.columns(2)

with col1:
    st.header("Giới thiệu")
    st.write("Đây là nội dung giới thiệu.")

with col2:
    st.header("Dịch vụ")
    st.write("Đây là nội dung dịch vụ.")

img = 'https://images.pexels.com/photos/39457179/pexels-photo-39457179.jpeg'

st.image(img, caption="Cưỡi ngữa ngắm hoàng hôn")

audio = 'https://pixabay.com/vi/music/piano-solo-twilight-princess-496948/'

st.audio(audio, 'audio/wav')

# git add .
# git commit -m "Update homepage"
# git push origin main