import streamlit as st
# import base64
# main_bg = "./賀卡bg.png"
# main_bg_ext = "png"

option = st.sidebar.selectbox('選單', options=['主頁', '歌曲', '小說'])
# st.markdown(
#     f"""
#     <style>
#     .reportview-container {{
#         background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

with open('./lyrics.txt') as fh:
    lyrics = fh.read()
    lyrics = lyrics.split('\n')

with open('./novel.txt') as fh:
    novel = fh.read()


st.title('Project Jadeite')
st.write('\n\n')
st.write('\n\n')

if option == '主頁':
    st.image('./賀卡.png')


if option == '歌曲':
    st.image('./賀卡.png')
    st.write('\n')
    audio_file = open('song.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
    for i in range(0, len(lyrics), 2):
        ch = lyrics[i]
        try:
            jp = '<p style="font-family:sans-serif; color:Gray; font-size: 15px;">' + \
                lyrics[i+1] + '</p>'
        except:
            continue
        st.write(ch)
        st.markdown(jp, unsafe_allow_html=True)

if option == '小說':
    for line in novel.split('\n'):
        st.write(line)
