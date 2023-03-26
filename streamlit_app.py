#%%
import streamlit as st
import math
from PIL import Image, ImageDraw, ImageFont
#%%
head_col1, head_col2 = st.columns([3, 1])

with head_col2:
    language_radio = st.radio(label = 'select language', 
                              options = ('th', 'en'),
                              index = 0,
                              horizontal = True,
                              label_visibility = 'hidden')

input_col1, input_col2 = st.columns(2)
with input_col1: 
    width = st.number_input('width (meters)', step = 0.1)
with input_col2:
    height = st.number_input('height (meters)', step = 0.1)


def ปัดเศษ(input):
    return math.floor(input * 1000000) / 1000000

wh = ปัดเศษ(width * height) 

total_wallpaper = math.ceil(wh * 4.0)
st.subheader(f'total wallpaper = {total_wallpaper}')

x_pieces = math.ceil(ปัดเศษ(width) * 2.0)
y_pieces = math.ceil(ปัดเศษ(height) * 2.0) 

st.write(f'horizontal_pieces = {x_pieces}', type(x_pieces))
st.write(f'vertical_pieces = {y_pieces}', type(y_pieces))

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
    draw.text((10, 10), "Hello", fill=(255,0,0,128))

    st.image(new_image, caption = 'caption')