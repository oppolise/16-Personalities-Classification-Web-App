import streamlit as st
import pandas as pd
import joblib

# ตั้งค่าหน้าเว็บให้มี layout กว้างขึ้น
st.set_page_config(layout="wide")

# โหลดโมเดล Scikit-learn
model = joblib.load("knn_model.pkl")

# โหลด dataset และลบคอลัมน์สุดท้าย (คลาส)
df = pd.read_csv("16P.csv", encoding='latin1')
columns = df.columns.tolist()
columns = columns[1:-1]  # ลบคอลัมน์สุดท้าย

# สร้าง dictionary เพื่อเก็บข้อมูล input ของผู้ใช้
input_data = {}

# ชื่อของ personalities ตามลำดับที่โมเดลให้ผลลัพธ์
personality_names = ['ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'ESTP', 'INFJ', 'INFP', 'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP']

# ลักษณะนิสัยของแต่ละบุคลิกภาพ
personality_descriptions = {
    'ENFJ': 'เป็นผู้นำที่มีเสน่ห์ ชอบช่วยเหลือผู้อื่นและมีความมุ่งมั่นในการทำให้โลกดีขึ้น',
    'ENFP': 'มีความคิดสร้างสรรค์ ชอบสำรวจแนวคิดใหม่ๆ และมองหาความหมายในทุกสิ่ง',
    'ENTJ': 'เป็นคนมั่นใจ ชอบการจัดการและวางแผน มุ่งเน้นไปที่การตัดสินใจอย่างชัดเจน',
    'ENTP': 'ชอบท้าทายและถกเถียงในเชิงเหตุผล เปิดรับแนวคิดใหม่ๆ และเป็นนักแก้ปัญหาที่ดี',
    'ESFJ': 'ชอบสนับสนุนผู้อื่น เอาใจใส่และเป็นมิตร เป็นคนที่เชื่อถือได้',
    'ESFP': 'สนุกสนาน ชอบทำให้คนรอบข้างมีความสุข มีความเป็นธรรมชาติและเต็มไปด้วยพลัง',
    'ESTJ': 'มีความสามารถในการจัดการ และชอบทำงานที่มีระบบและระเบียบ',
    'ESTP': 'มีพลังในการแก้ปัญหาและการตัดสินใจ ชอบทดลองและปรับเปลี่ยนสิ่งต่างๆ',
    'INFJ': 'เป็นนักคิดในเชิงลึก มีความเห็นอกเห็นใจและตั้งใจที่จะทำให้โลกดีขึ้น',
    'INFP': 'เป็นคนมีจิตใจอ่อนโยน มีความเชื่อในความดีงามและชอบช่วยเหลือผู้อื่น',
    'INTJ': 'มีความคิดเชิงกลยุทธ์ ชอบการวางแผนและการสร้างสรรค์สิ่งใหม่ๆ',
    'INTP': 'ชอบคิดวิเคราะห์ในเชิงนามธรรม มีความสงสัยและตั้งคำถามกับสิ่งต่างๆ',
    'ISFJ': 'เอาใจใส่และชอบช่วยเหลือผู้อื่น เป็นคนที่เชื่อถือได้และชอบความเป็นระเบียบ',
    'ISFP': 'ชอบการแสดงออกทางศิลปะ มีความเงียบสงบแต่มีความคิดสร้างสรรค์',
    'ISTJ': 'มีความรับผิดชอบและเป็นระเบียบ ชอบทำงานที่มีความชัดเจนและมั่นคง',
    'ISTP': 'ชอบการทดลองและแก้ปัญหาโดยใช้ทักษะทางปฏิบัติ มีแนวคิดเชิงกลไก'
}

# สร้างตัวเลือกสำหรับคำตอบ
answer_options = {
    -3: "ไม่เห็นด้วยอย่างยิ่ง",
    -2: "ไม่เห็นด้วยปานกลาง",
    -1: "ไม่เห็นด้วยเล็กน้อย",
    0: "เป็นกลาง",
    1: "เห็นด้วยเล็กน้อย",
    2: "เห็นด้วยปานกลาง",
    3: "เห็นด้วยอย่างยิ่ง"
}

# เพิ่ม CSS สำหรับการจัดรูปแบบ
st.markdown("""
    <style>
        /* สไตล์สำหรับพื้นหลังและสีหลัก */
        .main {
            background-color: #1E1E1E;
            color: #FFFFFF;
            padding: 20px;
        }
        
        /* สไตล์สำหรับข้อคำถาม */
        .question-container {
            background-color: #2D2D2D;
            padding: 25px;
            border-radius: 10px;
            margin: 20px 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .question-text {
            font-size: 18px;
            color: #E0E0E0;
            margin-bottom: 20px;
            line-height: 1.5;
        }
        
        .question-number {
            color: #4B9CD3;
            font-weight: bold;
            margin-right: 10px;
        }
        
        /* สไตล์สำหรับตัวเลือกคำตอบ */
        .stRadio > div[role='radiogroup'] {
            background-color: #363636;
            padding: 10px;
            border-radius: 8px;
        }
        
        .stRadio > div[role='radiogroup'] > div {
            padding: 12px 15px;
            margin: 5px 0;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        
        .stRadio > div[role='radiogroup'] > div:hover {
            background-color: #404040;
        }
        
        /* สไตล์สำหรับปุ่มส่งคำตอบ */
        .stButton > button {
            background-color: #4B9CD3;
            color: white;
            padding: 15px 30px;
            border-radius: 25px;
            border: none;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s;
            font-weight: bold;
            width: 200px;
        }
        
        .stButton > button:hover {
            background-color: #357ABD;
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
        }
        
        /* สไตล์สำหรับส่วนหัว */
        .header {
            text-align: center;
            padding: 30px 0;
            margin-bottom: 40px;
        }
        
        .header-title {
            color: #4B9CD3;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 15px;
        }
        
        .header-subtitle {
            color: #B0B0B0;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# ส่วนแสดงผลหน้าเว็บ
st.markdown("<div class='header'>", unsafe_allow_html=True)
st.markdown("<h1 class='header-title'>แบบทดสอบบุคลิกภาพ 16 Personalities</h1>", unsafe_allow_html=True)
st.markdown("<p class='header-subtitle'>กรุณาเลือกคำตอบที่ตรงกับความคิดเห็นของคุณมากที่สุด</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# สร้างฟอร์ม
with st.form("personality_test"):
    for i, col in enumerate(columns, 1):
        st.markdown(f"""
            <div class='question-container'>
                <div class='question-text'>
                    <span class='question-number'>{i}.</span>
                    {col}
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if df[col].dtype == 'object':
            unique_values = df[col].unique().tolist()
            input_data[col] = st.radio(
                "",
                options=unique_values,
                key=f"q_{col}",
                horizontal=False,
                label_visibility="collapsed"
            )
        else:
            input_data[col] = st.radio(
                "",
                options=list(answer_options.keys()),
                format_func=lambda x: answer_options[x],
                horizontal=False,
                key=f"q_{col}",
                label_visibility="collapsed"
            )

    # จัดการปุ่มส่งคำตอบ
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        submit_button = st.form_submit_button(
            "ส่งคำตอบ",
            use_container_width=True
        )

# ส่วนแสดงผลลัพธ์
if submit_button:
    st.markdown("<div class='result-container'>", unsafe_allow_html=True)
    input_list = [input_data[col] for col in columns]
    prediction = model.predict([input_list])
    predicted_personality = personality_names[int(prediction[0])]
    
    st.markdown("<h3 style='text-align: center; color: #4B9CD3; margin-top: 40px;'>ผลการวิเคราะห์บุคลิกภาพของคุณ</h3>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center; color: #FFFFFF; margin: 20px 0;'>{predicted_personality}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #E0E0E0; padding: 20px;'>{personality_descriptions[predicted_personality]}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
