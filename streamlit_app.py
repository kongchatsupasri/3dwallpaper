#%%
import streamlit as st
import math
from PIL import Image, ImageDraw, ImageFont
#%%
head_col1, head_col2 = st.columns([3, 1])

with head_col2:
    language = st.radio(label = 'select language', 
                              options = ('th', 'en'),
                              index = 0,
                              horizontal = True,
                              label_visibility = 'hidden')

input_col1, input_col2 = st.columns(2)
with input_col1: 
    if language == 'th':
        width = st.number_input('ความกว้าง (เมตร)', step = 0.1, min_value = 0.0, value = 0.0)
    else:
        width = st.number_input('width (meters)', step = 0.1, min_value = 0.0, value = 0.0)
with input_col2:
    if language == 'th':
        height = st.number_input('ความสูง (เมตร)', step = 0.1, min_value = 0.0, value = 0.0)
    else:
        height = st.number_input('height (meters)', step = 0.1, min_value = 0.0, value = 0.0)


def ปัดเศษ(input):
    return math.floor(input * 1000000) / 1000000

wh = ปัดเศษ(width * height) 

x_pieces = math.ceil(ปัดเศษ(width) * 2.0)
y_pieces = math.ceil(ปัดเศษ(height) * 2.0) 

total_wallpaper = math.ceil(x_pieces * y_pieces)

if language == 'th':
    st.subheader(f'จำนวนแผ่นที่ต้องใช้ = {total_wallpaper}')
else:
    st.subheader(f'total wallpaper = {total_wallpaper}')

panel = Image.open('white_wp.jpeg')
panel = panel.resize((100, 100))

new_image = Image.new('RGB', (x_pieces*panel.size[0], y_pieces* panel.size[1]), (250,250,250))

if 0 in [x_pieces, y_pieces]:
    pass
else:
    for j in range(y_pieces):
        for i in range(x_pieces):

            new_image.paste(panel,(i * panel.size[0] , j * panel.size[1]))
            # new_image.paste(image,(image.size[0],0))

    draw = ImageDraw.Draw(new_image)  
    draw.rectangle([(0,0),(width * 200, height * 200)],outline="#0000ff", width = 5)
    # new_image = new_image.crop((0,0, width * 200, height * 200))

    st.image(new_image)
