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
    st.text_input("Nhập vào giá trị")

with col2:
    st.header("Dịch vụ")
    st.write("Đây là nội dung dịch vụ.")
    st.date_input("Ngày tháng")

img = 'https://images.pexels.com/photos/39457179/pexels-photo-39457179.jpeg'

st.image(img, caption="Cưỡi ngữa ngắm hoàng hôn")

audio = 'https://www.pexels.com/vi-vn/download/video/18069094/'

st.audio(audio, 'audio/mp3')

videos = "https://www.pexels.com/vi-vn/download/video/18069094/"

video1 = 'https://www.youtube.com/watch?v=4az1HtZWT40'

st.video(video1, format='video/mp4')

st.video(videos, format='video/mp4')

with st.form(key="My Form"):
    st.write("Hello World")
    submitted = st.form_submit_button("Submited")
    if submitted:
        st.write("Done")

list_options = ['Green', 'Yellow', 'Red', 'Blue', 'Pink']

options = st.multiselect("Select your color: ", list_options)

st.write("Your selections: ")

for i in range(len(options)):
    st.write(options[i])

selectBoxs = ('Email', 'Điện thoại bàn', 'Điện thoại di động')

selectBox = st.selectbox('Chọn phương thức liên lạc?', selectBoxs)

st.write('Bạn đã chọ: ', selectBox)
# git add .
# git commit -m "Update homepage"
# git push origin main