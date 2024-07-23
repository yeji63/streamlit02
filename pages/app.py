import streamlit as st

# data = [1,2,3]
url = 'https://naver.com'

# 입력화면 - HTML/CSS/JS 로 최종적으로 변환
val1 = st.button("고양이")
val2 = st.button("강아지")
val3 = st.button("토끼")

# 동작
if val1:
    st.image("./data/cat.jpg")
elif val2:
    st.image("./data/dog.png")
elif val3:
    st.image("./data/rabbit.png")

# 출력
st.write(val1)
# # . : 현재경로
# st.image("./data/cat.jpg")
# st.image("./data/dog.png")

# st.download_button("Download file", data)
# st.link_button("Go to gallery", url)
# st.page_link("app.py", label="Home")
# st.data_editor("Edit data", data)
# st.checkbox("I agree")
# st.toggle("Enable")
# st.radio("Pick one", ["cats", "dogs"])
# st.selectbox("Pick one", ["cats", "dogs"])
# st.multiselect("Buy", ["milk", "apples", "potatoes"])
# st.slider("Pick a number", 0, 100)
# st.select_slider("Pick a size", ["S", "M", "L"])
# st.text_input("First name")
# st.number_input("Pick a number", 0, 10)
# st.text_area("Text to translate")
# st.date_input("Your birthday")
# st.time_input("Meeting time")
# st.file_uploader("Upload a CSV")
# st.camera_input("Take a picture")
# st.color_picker("Pick a color")

# # Use widgets' returned values in variables:
# # for i in range(int(st.number_input("Num:"))):
# #     foo()
# # if st.sidebar.selectbox("I:",["f"]) == "f":
# #     b()
# my_slider_val = st.slider("Quinn Mallory", 1, 88)
# st.write('slider_val')

# # Disable widgets to remove interactivity:
# st.slider("Pick a number", 0, 100, disabled=True)


# # 함수, 변수 등을 통해 입력받은 값을 출력하기 위한 값으로 제어


# # 출력화면 - HTML/CSS/JS 로 최종적으로 변환 
# st.write("Most objects") # df, err, func, keras!
# st.write(["st", "is <", 3]) # see *
# # st.write_stream(my_generator)
# # st.write_stream(my_llm_stream)

# st.text("Fixed width text")
# st.markdown("_Markdown_") # see *
# st.latex(r""" e^{i\pi} + 1 = 0 """)
# st.title("My title")
# st.header("My header")
# st.subheader("My sub")
# st.code("for i in range(8): foo()")
# st.html("<p>Hi!</p>")