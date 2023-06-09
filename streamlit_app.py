#%%
import streamlit as st
import math
from PIL import Image, ImageDraw, ImageFont
#%%
d = {'wh': {
        'width': {'th': 'ความกว้าง (เมตร)', 'en': 'width (meters)'},
        'height': {'th': 'ความสูง (เมตร)', 'en': 'height (meters)'}
    },
    'pic': {
        'white diamond': 'white_diamond.jpg', 
        'black diamond': 'black_diamond.jpg', 
        'silver': 'silver.jpg',
        'yellow bright': 'yellow_bright.jpg',
        'electric green': 'electric_green.jpg', 
        'fresh blue': 'fresh_blue.jpg', 
        'red festive': 'red_festive.jpg', 
        'pink sakura': 'pink_sakura.jpg',
        'wood grain': 'wood_grain.jpg', 
        'estella': 'estella.jpg'
    },
    'pieces': {
        'th': 'จำนวนแผ่นที่ต้องใช้ = ', 
        'en': f'Total = '
    },
    'select_error': {
        'th': 'กรุณาเลือก 1 - 2 ลาย', 
        'en': 'please select 1 - 2 design.'
    }
    }

st.cache(persist = True)
def pic_generate(design_ls, x_pieces, y_pieces):
    panel = Image.open(d['pic'][design_ls[0]])
    panel = panel.resize((100, 100))
    new_image = Image.new('RGB', (x_pieces*panel.size[0], y_pieces* panel.size[1]), (250,250,250))

    if 0 in [x_pieces, y_pieces]:
        pass
    else:
        for j in range(y_pieces):
            if j == 0:
                first_panel = design_ls[0]
            else:
                if first_panel == design_ls[0]:
                    design_ls = design_ls[::-1]
                first_panel = design_ls[0]

            for i in range(x_pieces):
                panel = Image.open(d['pic'][design_ls[0]])
                panel = panel.resize((100, 100))
                new_image.paste(panel,(i * panel.size[0] , j * panel.size[1]))
                design_ls = design_ls[::-1]
    return new_image

st.cache(persist = True)
def ปัดเศษ(input):
    return math.floor(input * 1000000) / 1000000

head_col1, head_col2 = st.columns([3, 1])

st.markdown("""
    <style>
    .stRadio [role=radiogroup]{
        align-items: right;
        justify-content: right;
    }
    </style>
""",unsafe_allow_html=True)

with head_col2:
    language = st.radio(label = 'select language', 
                              options = ('th', 'en'),
                              index = 0,
                              horizontal = True,
                              label_visibility = 'hidden')

input_col1, input_col2 = st.columns(2)
with input_col1: 
    width = st.number_input(d['wh']['width'][language], step = 0.1, min_value = 0.0, value = 1.0)
with input_col2:
    height = st.number_input(d['wh']['height'][language], step = 0.1, min_value = 0.0, value = 1.0)

st.markdown("""
    <style>
    .stRadio [role=radiogroup]{
        align-items: left;
        justify-content: left;
    }
    </style>
""",unsafe_allow_html=True)

selected_ls = st.multiselect(
    'select design',
    d['pic'].keys(),
    ['fresh blue', 'yellow bright'])
design_ls = [x for x in selected_ls if x != 0]

if len(design_ls) > 2 or len(design_ls) < 1:
    st.markdown(f"<h3 style='text-align: center;'>{d['select_error'][language]}</h1>", unsafe_allow_html=True)
else:
    wh = ปัดเศษ(width * height) 

    x_pieces = math.ceil(ปัดเศษ(width) * 2.0)
    y_pieces = math.ceil(ปัดเศษ(height) * 2.0) 

    total_wallpaper = math.ceil(x_pieces * y_pieces)

    st.markdown(f"<h2 style='text-align: center;'>{d['pieces'][language]} {total_wallpaper}</h2>", unsafe_allow_html=True)

    img = pic_generate(design_ls = design_ls, x_pieces = x_pieces, y_pieces = y_pieces)
    draw = ImageDraw.Draw(img)  
    draw.rectangle([(0,0),(width * 200, height * 200)],outline="#cf2f17", width = 7)
    # new_image = new_image.crop((0,0, width * 200, height * 200))

    st.image(img)
    # if language == 'th':
    #     st.write('**หมายเหตุ: ลายบนตัวแผ่นไม่สมมาตร')
    # else:
    #     st.write("**Note: Wall panel's pattern is asymmetrical.")

    st.markdown('#')
    st.write(f'''
    <div style="text-align:center">
        <a target="_blank" href="https://shopee.co.th/stardust287#product_list">
            <button style = "
                fontWeight: 400;
                padding: 0.25rem 0.75rem;
                borderRadius: 0.25rem;
                margin: 2px;
                lineHeight: 1.6;
                width: auto;
                userSelect: none;
                backgroundColor: #FFFFFF;
                border: 1px solid rgba(49, 51, 63, 0.2);
                ">
                    Shopee
            </button>
        </a>
        <a target="_blank" href="https://www.lazada.co.th/shop/cozy-homey/?spm=a2o4m.pdp_revamp.seller.1.98a651bftDfSmn&itemId=4585163215&channelSource=pdp">
            <button style = "
                fontWeight: 400;
                padding: 0.25rem 0.75rem;
                borderRadius: 0.25rem;
                margin: 2;
                lineHeight: 1.6;
                width: auto;
                userSelect: none;
                backgroundColor: #FFFFFF;
                border: 1px solid rgba(49, 51, 63, 0.2);
                ">
                    Lazada
            </button>
        </a>
    </div>
        ''',
        unsafe_allow_html=True)

    st.markdown('#')   
    st.markdown('<div style="text-align: right;">© cozy-homey 2023</div>', unsafe_allow_html=True)
