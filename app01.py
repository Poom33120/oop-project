import streamlit as st

def convert_year(year, era):
    if era == 'ค.ศ.':
        return year - 543
    elif era == 'ร.ศ.':
        return year - 2324
    elif era == 'ฮ.ศ.':
        return year - 1164
    elif era == 'จ.ศ.':
        return year - 1181

def get_year_label(era):
    if era == 'ค.ศ.':
        return 'ปี ค.ศ.'
    elif era == 'ร.ศ.':
        return 'ปี ร.ศ.'
    elif era == 'ฮ.ศ.':
        return 'ปี ฮ.ศ.'
    elif era == 'จ.ศ.':
        return 'ปี จ.ศ.'

def main():
    st.title("แปลงปี พ.ศ. เป็นปีต่างๆ")
    
    # เพิ่มรูปภาพ
    st.image("image2.jpg", use_column_width=True)

    # สร้างช่องใส่ปีและเลือกประเภทปี
    year = st.number_input("ปี (พ.ศ.):", min_value=1, value=2565)
    era = st.selectbox("เลือกประเภทปี:", ['ค.ศ.', 'ร.ศ.', 'ฮ.ศ.', 'จ.ศ.'])

    # คำนวณปี
    converted_year = convert_year(year, era)
    
    # แสดงผลลัพธ์
    st.write(f"ปี {year} เป็น{get_year_label(era)}: {converted_year}")

if __name__ == "__main__":
    main()





