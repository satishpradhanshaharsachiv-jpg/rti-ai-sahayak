import streamlit as strlit
import datetime

strlit.set_page_config(
    page_title="RTI & Legal Assistant - Satish Pradhan",
    page_icon="⚖️",
    layout="centered"
)

# CSS डिझाइन आणि स्टाइलिंग
strlit.markdown("""
    <style>
    .stApp {
        background: #f8f9fa;
    }
    .header-box {
        background: #ffffff;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    .header-box h1 {
        font-size: 22px;
        font-weight: bold;
        color: #00A86B;
        margin-bottom: 5px;
    }
    .tag-box {
        background: #fff8e1;
        padding: 5px 12px;
        border-radius: 20px;
        display: inline-block;
        font-size: 12px;
        font-weight: bold;
        color: #f57f17;
        border: 1px dashed #ffb300;
        margin-bottom: 8px;
    }
    
    /* बटनांची रचना सुधारण्यासाठी स्टायलिंग */
    div.stButton > button {
        width: 100% !important;
        height: 85px !important;
        border-radius: 16px !important;
        border: none !important;
        color: white !important;
        font-size: 13px !important;
        font-weight: bold !important;
        white-space: pre-line !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15) !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 15px rgba(0,0,0,0.25) !important;
    }
    
    /* प्रत्येक बटनाचे कस्टम कलर्स (स्क्रीनशॉटप्रमाणे) */
    div.stButton > button[data-testid="baseButton-secondary"]:nth-child(1) { background: linear-gradient(135deg, #00b09b, #96c93d); }
    
    .a4-container {
        background-color: #ffffff;
        border: 2px dashed #1e3c72;
        padding: 20px;
        border-radius: 12px;
        color: #111827;
        font-size: 14px;
        line-height: 1.7;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# हेडर भाग
strlit.markdown("""
    <div class="header-box">
        <h1>⚖️ RTI AI महा-सहाय्यक</h1>
        <div class="tag-box">⚡ घरबसल्या एका मिनिटात अर्ज तयार करा</div>
        <p style="font-size: 11px; color: #666; margin:0;">👤 सतीश अशोक प्रधान | 📱 ८६६८२३५३९५ | छत्रपती संभाजीनगर</p>
    </div>
""", unsafe_allow_html=True)

# कायमस्वरूपी लॉगिन सत्र
if "is_logged_in" not in strlit.session_state:
    strlit.session_state.is_logged_in = False

if not strlit.session_state.is_logged_in:
    strlit.markdown("<h3 style='text-align: center; color: #1e3c72;'>🔐 सुरक्षित मोबाईल प्रवेश</h3>", unsafe_allow_html=True)
    c1, c2, c3 = strlit.columns([1, 3, 1])
    with c2:
        mob = strlit.text_input("मोबाईल नंबर प्रविष्ट करा:", placeholder="8668235395", max_chars=10)
        if strlit.button("🚀 ॲप सुरू करा", key="login_btn"):
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
    # स्क्रीनशॉटनुसार ४x४ ग्रिड बटन्स
    # ==============================================================================
    
    col1, col2, col3, col4 = strlit.columns(4)
    with col1:
        if strlit.button("📄\nजोडपत्र 'अ'", key="btn_rti"):
            strlit.session_state.active_module = "rti"
    with col2:
        if strlit.button("⚖️\nप्रथम अपील", key="btn_fa"):
            strlit.session_state.active_module = "first_appeal"
    with col3:
        if strlit.button("🏛️\nमाहिती आयोग", key="btn_comm"):
            strlit.session_state.active_module = "commission"
    with col4:
        if strlit.button("✨\nAI चॅट", key="btn_ai"):
            strlit.session_state.active_module = "ai_chat"

    col5, col6, col7, col8 = strlit.columns(4)
    with col5:
        if strlit.button("📜\nकोर्ट याचिका", key="btn_court"):
            strlit.session_state.active_module = "court"
    with col6:
        if strlit.button("📣\nशासकीय तक्रार", key="btn_comp"):
            strlit.session_state.active_module = "complaint"
    with col7:
        if strlit.button("✏️\nप्रतिज्ञापत्र", key="btn_aff"):
            strlit.session_state.active_module = "affidavit"
    with col8:
        if strlit.button("🛒\nग्राहक मंच", key="btn_cons"):
            strlit.session_state.active_module = "consumer"

    strlit.write("---")

    # ================= मॉड्यूल्सची अंमलबजावणी =================

    if strlit.session_state.active_module == "rti":
        strlit.subheader("📄 जोडपत्र 'अ' - माहिती अधिकार अर्ज")
        dept = strlit.text_input("जन माहिती अधिकारी, विभाग व पत्ता:")
        subject = strlit.text_input("माहितीचा विषय:")
        details = strlit.text_area("माहितीचा तपशील:")
        if strlit.button("मसुदा तयार करा", key="gen_rti"):
            draft = f"""
**माहिती अधिकाराचा अर्ज (जोडपत्र 'अ')**

प्रति, 
जन माहिती अधिकारी, 
{dept}

विषय: {subject}

१. माहितीचा तपशील: 
{details}

**अर्जदार:** सतीश अशोक प्रधान, छत्रपती संभाजीनगर | दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}
            """
            strlit.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    elif strlit.session_state.active_module == "ai_chat":
        strlit.subheader("✨ AI कायदेशीर सल्लागार")
        
        if "messages" not in strlit.session_state:
            strlit.session_state.messages = []

        for message in strlit.session_state.messages:
            with strlit.chat_message(message["role"]):
                strlit.markdown(message["content"])

        if prompt := strlit.chat_input("तुमचा कायदेशीर किंवा RTI बद्दलचा प्रश्न येथे विचार..."):
            strlit.session_state.messages.append({"role": "user", "content": prompt})
            with strlit.chat_message("user"):
                strlit.markdown(prompt)

            with strlit.chat_message("assistant"):
                if "आरटीआय" in prompt or "rti" in prompt.lower() or "माहिती" in prompt:
                    ai_response = "माहिती अधिकार कायदा २००५ नुसार आपण माहिती मागवू शकता. प्रथम 'जोडपत्र अ' वापरून अर्ज दाखल करा."
                elif "अपील" in prompt:
                    ai_response = "३० दिवसांत माहिती न मिळाल्यास प्रथम अपिलीय अधिकाऱ्यांकडे अर्ज करा."
                else:
                    ai_response = f"सतीशजी, तुमच्या '{prompt}' या प्रश्नासाठी योग्य कायदेशीर पर्याय निवडा."
                
                strlit.markdown(ai_response)
                strlit.session_state.messages.append({"role": "assistant", "content": ai_response})

    elif strlit.session_state.active_module == "first_appeal":
        strlit.subheader("⚖️ प्रथम अपील अर्ज (कलम १९)")
        fa_dept = strlit.text_input("प्रथम अपिलीय अधिकारी व पत्ता:")
        reason = strlit.text_area("अपिलाचे कारण:")
        if strlit.button("प्रथम अपील तयार करा", key="gen_fa"):
            draft = f"**प्रथम अपील अर्ज**\n\nप्रति, {fa_dept}\n\nकारण: {reason}\n\n**अपीलार्थी:** सतीश अशोक प्रधान, छत्रपती संभाजीनगर"
            strlit.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    elif strlit.session_state.active_module == "commission":
        strlit.subheader("🏛️ राज्य माहिती आयोग")
        comm_details = strlit.text_area("तक्रार तपशील:")
        if strlit.button("आयोग अर्ज तयार करा", key="gen_comm"):
            draft = f"**द्वितीय अपील - राज्य माहिती आयोग**\n\nतपशील: {comm_details}\n\n**अर्जदार:** सतीश अशोक प्रधान, छत्रपती संभाजीनगर"
            strlit.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    elif strlit.session_state.active_module == "court":
        strlit.subheader("📜 कोर्ट याचिका मसुदा")
        facts = strlit.text_area("हकीकत:")
        if strlit.button("याचिका तयार करा", key="gen_court"):
            strlit.markdown(f"<div class='a4-container'><b>कोर्ट याचिका मसुदा:</b><br>{facts}<br><br><b>याचिकाकर्ता:</b> सतीश अशोक प्रधान</div>", unsafe_allow_html=True)

    elif strlit.session_state.active_module == "complaint":
        strlit.subheader("📣 शासकीय तक्रार अर्ज")
        comp = strlit.text_area("तक्रारीचा विषय व तपशील:")
        if strlit.button("तक्रार तयार करा", key="gen_comp"):
            strlit.markdown(f"<div class='a4-container'><b>शासकीय तक्रार:</b><br>{comp}<br><br><b>तक्रारदार:</b> सतीश अशोक प्रधान, छत्रपती संभाजीनगर</div>", unsafe_allow_html=True)

    elif strlit.session_state.active_module == "affidavit":
        strlit.subheader("✏️ प्रतिज्ञापत्र")
        aff = strlit.text_area("घोषणा मुद्दे:")
        if strlit.button("प्रतिज्ञापत्र तयार करा", key="gen_aff"):
            strlit.markdown(f"<div class='a4-container'><b>प्रतिज्ञापत्र:</b><br>{aff}<br><br><b>घोषणाकर्ता:</b> सतीश अशोक प्रधान</div>", unsafe_allow_html=True)

    elif strlit.session_state.active_module == "consumer":
        strlit.subheader("🛒 ग्राहक मंच तक्रार")
        cons = strlit.text_area("फसवणूक तपशील व भरपाई:")
        if strlit.button("ग्राहक मंच अर्ज तयार करा", key="gen_cons"):
            strlit.markdown(f"<div class='a4-container'><b>ग्राहक मंच अर्ज:</b><br>{cons}<br><br><b>तक्रारदार:</b> सतीश अशोक प्रधान</div>", unsafe_allow_html=True)
