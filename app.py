import streamlit as strlit
import datetime

strlit.set_page_config(
    page_title="RTI AI महा-सहाय्यक - सतीश प्रधान",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# चमचमीत आणि आकर्षक गोल्डन मोबाईल CSS डिझाइन
strlit.markdown("""
    <style>
    /* मुख्य पार्श्वभूमी */
    .stApp {
        background: linear-gradient(180deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: #ffffff;
    }
    
    /* हेडर बॉक्स */
    .header-box {
        background: rgba(255, 255, 255, 0.08);
        padding: 10px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #ffd700;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.2);
        margin-bottom: 12px;
    }
    .header-box h1 {
        font-size: 18px;
        font-weight: bold;
        color: #ffd700;
        margin-bottom: 3px;
        text-shadow: 0 0 8px rgba(255,215,0,0.6);
    }
    .tag-box {
        background: linear-gradient(90deg, #ff8c00, #e52e71);
        padding: 3px 8px;
        border-radius: 12px;
        display: inline-block;
        font-size: 10px;
        font-weight: bold;
        color: #ffffff;
        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
    }
    
    /* ४x३ मोबाईल ग्रिड बटनांचे चमचमीत CSS */
    div.stButton > button {
        width: 100% !important;
        height: 70px !important;
        border-radius: 12px !important;
        font-size: 11px !important;
        font-weight: bold !important;
        white-space: pre-line !important;
        color: #ffffff !important;
        border: 1.5px solid #ffd700 !important; /* प्रीमियम गोल्डन बॉर्डर */
        box-shadow: 0 4px 10px rgba(0,0,0,0.5), inset 0 1px 1px rgba(255,255,255,0.4) !important;
        transition: all 0.2s ease-in-out !important;
        padding: 2px !important;
    }
    
    div.stButton > button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 0 12px #ffd700 !important;
    }
    
    /* १-१२ प्रत्येक बटनाचा वेगवेगळा चमचमीत ग्रेडियंट रंग */
    div.stButton > button[key="b1"] { background: linear-gradient(135deg, #11998e, #38ef7d) !important; }
    div.stButton > button[key="b2"] { background: linear-gradient(135deg, #FF416C, #FF4B2B) !important; }
    div.stButton > button[key="b3"] { background: linear-gradient(135deg, #8A2387, #E94057) !important; }
    div.stButton > button[key="b4"] { background: linear-gradient(135deg, #f7b731, #fa8231) !important; }
    
    div.stButton > button[key="b5"] { background: linear-gradient(135deg, #654ea3, #eaafc8) !important; }
    div.stButton > button[key="b6"] { background: linear-gradient(135deg, #00B4DB, #0083B0) !important; }
    div.stButton > button[key="b7"] { background: linear-gradient(135deg, #f12711, #f5af19) !important; }
    div.stButton > button[key="b8"] { background: linear-gradient(135deg, #56ab2f, #a8e063) !important; }

    div.stButton > button[key="b9"] { background: linear-gradient(135deg, #4776E6, #8E54E9) !important; }
    div.stButton > button[key="b10"] { background: linear-gradient(135deg, #614385, #516395) !important; }
    div.stButton > button[key="b11"] { background: linear-gradient(135deg, #e1eec3, #f05053) !important; }
    div.stButton > button[key="b12"] { background: linear-gradient(135deg, #16A085, #F4D03F) !important; }

    /* A4 ड्राफ्ट कंटेनर */
    .a4-container {
        background-color: #ffffff;
        border: 2px dashed #ffd700;
        padding: 15px;
        border-radius: 10px;
        color: #000000;
        font-size: 13px;
        line-height: 1.6;
        box-shadow: 0 4px 15px rgba(255,215,0,0.2);
        margin-top: 10px;
    }
    
    /* अतिरिक्त मेन्यू लपवणे */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# चमकदार हेडर भाग
strlit.markdown("""
    <div class="header-box">
        <h1>⚖️ RTI AI महा-सहाय्यक</h1>
        <div class="tag-box">⚡ एका क्लिकवर सर्व कायदेशीर मसुदे</div>
        <p style="font-size: 10px; color: #ffd700; margin-top: 3px; margin-bottom:0;">👤 सतीश अशोक प्रधान | 📱 ८६६८२३५३९५</p>
    </div>
""", unsafe_allow_html=True)

# लॉगिन सत्र चेकिंग
if "is_logged_in" not in strlit.session_state:
    strlit.session_state.is_logged_in = False

if not strlit.session_state.is_logged_in:
    strlit.markdown("<h4 style='text-align: center; color: #ffd700;'>🔐 सुरक्षित मोबाईल प्रवेश</h4>", unsafe_allow_html=True)
    c1, c2, c3 = strlit.columns([0.2, 3, 0.2])
    with c2:
        mob = strlit.text_input("मोबाईल नंबर टाका:", placeholder="8668235395", max_chars=10)
        if strlit.button("🚀 ॲप सुरू करा", key="b_login"):
            if len(mob) == 10 and mob.isdigit():
                strlit.session_state.is_logged_in = True
                strlit.session_state.user_mobile = mob
                strlit.rerun()
            else:
                strlit.error("कृपया अचूक १० अंकी नंबर टाका.")
else:
    if "active_module" not in strlit.session_state:
        strlit.session_state.active_module = "rti"

    # ==============================================================================
    # उभे ४ आणि आडवे ३ (४x३ = १२ बटनांची सुंदर मोबाईल रचना)
    # ==============================================================================
    
    # ओळ १
    c1, c2, c3, c4 = strlit.columns(4)
    with c1:
        if strlit.button("📄\nजोडपत्र 'अ'", key="b1"): strlit.session_state.active_module = "rti"
    with c2:
        if strlit.button("⚖️\nप्रथम अपील", key="b2"): strlit.session_state.active_module = "first_appeal"
    with c3:
        if strlit.button("🏛️\nमाहिती आयोग", key="b3"): strlit.session_state.active_module = "commission"
    with c4:
        if strlit.button("✨\nAI चॅट", key="b4"): strlit.session_state.active_module = "ai_chat"

    # ओळ २
    c5, c6, c7, c8 = strlit.columns(4)
    with c5:
        if strlit.button("📜\nकोर्ट याचिका", key="b5"): strlit.session_state.active_module = "court"
    with c6:
        if strlit.button("📣\nशासकीय तक्रार", key="b6"): strlit.session_state.active_module = "complaint"
    with c7:
        if strlit.button("✏️\nप्रतिज्ञापत्र", key="b7"): strlit.session_state.active_module = "affidavit"
    with c8:
        if strlit.button("🛒\nग्राहक मंच", key="b8"): strlit.session_state.active_module = "consumer"

    # ओळ ३ (नवीन अतिरिक्त ४ सेवा)
    c9, c10, c11, c12 = strlit.columns(4)
    with c9:
        if strlit.button("📑\nग्रामपंचायत", key="b9"): strlit.session_state.active_module = "grampanchayat"
    with c10:
        if strlit.button("🏢\nमहापालिका", key="b10"): strlit.session_state.active_module = "corporation"
    with c11:
        if strlit.button("🚔\nपोलीस तक्रार", key="b11"): strlit.session_state.active_module = "police"
    with c12:
        if strlit.button("📋\nइतर अर्ज", key="b12"): strlit.session_state.active_module = "other"

    strlit.write("---")

    # ================= मॉड्यूल्सचे कामकाज =================

    if strlit.session_state.active_module == "rti":
        strlit.markdown("#### 📄 जोडपत्र 'अ' - माहिती अधिकार अर्ज")
        dept = strlit.text_input("विभाग व पत्ता:")
        subject = strlit.text_input("माहितीचा विषय:")
        details = strlit.text_area("माहितीचा तपशील:")
        if strlit.button("मसुदा तयार करा", key="m1"):
            draft = f"**माहिती अधिकाराचा अर्ज (जोडपत्र 'अ')**\n\n**प्रति,** जन माहिती अधिकारी, {dept}\n\n**विषय:** {subject}\n\n**१. माहितीचा तपशील:** {details}\n\n**अर्जदार:** सतीश अशोक प्रधान | दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}"
            strlit.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    elif strlit.session_state.active_module == "ai_chat":
        strlit.markdown("#### ✨ AI कायदेशीर सल्लागार")
        prompt = strlit.chat_input("तुमचा प्रश्न विचारा...")
        if prompt:
            strlit.info(f"तुमचा प्रश्न: {prompt}")
            strlit.success("सतीशजी, कायदेशीर सहाय्यासाठी वरील पर्यायांतून योग्य अर्ज निवडून मसुदा तयार करा.")

    elif strlit.session_state.active_module == "police":
        strlit.markdown("#### 🚔 पोलीस ठाणे तक्रार अर्ज")
        station = strlit.text_input("पोलीस ठाण्याचे नाव:")
        comp_details = strlit.text_area("तक्रारीचा तपशील:")
        if strlit.button("तक्रार अर्ज तयार करा", key="m11"):
            draft = f"**प्रति,** ठाणे अंमलदार साहेब, {station}\n\n**विषय:** कायदेशीर कारवाई बाबत तक्रार अर्ज.\n\n**तपशील:** {comp_details}\n\n**तक्रारदार:** सतीश अशोक प्रधान, छत्रपती संभाजीनगर"
            strlit.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    else:
        strlit.markdown(f"#### ⚙️ निवडलेली सेवा: {strlit.session_state.active_module.upper()}")
        st_text = strlit.text_area("अर्जाचा तपशील व मुद्दे प्रविष्ट करा:")
        if strlit.button("मसुदा तयार करा", key="m_gen"):
            draft = f"**अर्ज / तक्रार मसुदा**\n\n**तपशील:** {st_text}\n\n**अर्जदार:** सतीश अशोक प्रधान, छत्रपती संभाजीनगर"
            strlit.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)
