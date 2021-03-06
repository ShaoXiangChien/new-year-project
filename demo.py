import streamlit as st
import base64
main_bg = "./背景.jpg"
main_bg_ext = "jpg"
option = st.sidebar.selectbox('選單', options=['主頁', 'Cast', '歌曲', '小說'])
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)

cast_texts = []
for i in range(4):
    with open(f'./cast_info/intro{i+1}.txt') as fh:
        cast_texts.append(fh.readlines())

with open('./lyrics.txt') as fh:
    lyrics = fh.read()
    lyrics = lyrics.split('\n')

with open('./novel.txt') as fh:
    novel = fh.read()


# st.title('Project Jadeite')
st.markdown('<h1 style="font-family:sans-serif; font-weight: bold; color:Black; font-size: 40px;">' +
            'Project Jadeite' + '</h1>', unsafe_allow_html=True)
st.write('\n\n')
st.write('\n\n')

if option == '主頁':
    st.image('./賀卡.png')
    st.markdown('<h2 style="font-family:sans-serif; font: bold; color:Black; font-size: 25px;">' +
                '點擊左上角箭頭展開選單就可以看到其他作品啦！' + '</h2>', unsafe_allow_html=True)

if option == 'Cast':
    st.header('Casting')
    title = ['Project Initiator', 'Illustrator', 'Vocal', 'Novelist']
    ig = ['critic_suika', 'yueling_tsai', 'Ericchien21']
    talent = ['Eve', '蔡岳陵', '艾瑞克簡', 'Jeffery']
    cols = [st.columns(2) for i in range(4)]
    for i in range(4):
        for j in range(5):
            cols[i][0].write('\n')
        cols[i][0].image(
            f'./cast_info/talent{i+1}.png', width=230, caption=talent[i])
        for j in range(3):
            cols[i][0].write('\n')
            cols[i][1].write('\n')

        tt = '<h2 style="font-family:sans-serif; font: bold; color:Black; font-size: 25px;">' + \
            title[i] + ' - ' + talent[i] + '</h2>'
        cols[i][1].markdown(tt, unsafe_allow_html=True)
        # cols[i][1].subheader(title[i])
        cols[i][1].write('\n')
        for line in cast_texts[i]:
            md = '<h3 style="font-family:sans-serif; font: bold; color:Black; font-size: 20px;">' + \
                line + '</h3>'
            cols[i][1].markdown(md, unsafe_allow_html=True)

        if i < 3:
            cols[i][1].caption('ig: ' + ig[i])
        for j in range(5):
            cols[i][1].write('\n')
        # if i == 1 or i == 2:
        #     for j in range(2):
        #         cols[1].write('\n')


if option == '歌曲':
    st.image('./賀卡.png')
    st.write('\n')
    # audio_file = open('./song.mp3', 'rb')
    # audio_bytes = audio_file.read()
    st.markdown('<h2 style="font-family:sans-serif; font: bold; color:Black; font-size: 25px;">' +
                '有些話想跟大家說～' + '</h2>', unsafe_allow_html=True)
    st.audio('https://drive.google.com/uc?export=download&id=1FEbwhWEXl8QvoJcmMSduNT1xIX6wQW2r', format='audio/ogg')
    st.markdown('<h2 style="font-family:sans-serif; font: bold; color:Black; font-size: 25px;">' +
                '歌曲音源' + '</h2>', unsafe_allow_html=True)
    st.audio('https://drive.google.com/uc?export=download&id=1aXo2MJAOE9J9mAYDzXHUGDdUMNKAEdU7', format='audio/ogg')
    st.subheader('\n中日歌詞\n')
    for i in range(0, len(lyrics), 2):
        try:
            ch = '<p style="font-family:sans-serif; font: bold; color:Black; font-size: 20px;">' + \
                lyrics[i] + '</p>'
            jp = '<p style="font-family:sans-serif; color:Gray; font-size: 15px;">' + \
                lyrics[i+1] + '</p>'
        except:
            continue
        st.markdown(ch, unsafe_allow_html=True)
        st.markdown(jp, unsafe_allow_html=True)

if option == '小說':
    for line in novel.split('\n'):
        md = '<p style="font-family:sans-serif; font: bold; color:Black; font-size: 20px;">' + \
            line + '</p>'
        st.markdown(md, unsafe_allow_html=True)
