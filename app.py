import streamlit as strlit
import datetime

strlit.set_page_config(
    page_title="RTI & Legal Assistant - Satish Pradhan",
    page_icon="⚖️",
    layout="centered"
)

# मोबाईलच्या ॲप्ससारखी सुंदर रंगीबेरंगी आणि चमचमीत बटणांसाठी CSS डिझाइन
strlit.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .header-box {
        background: #ffffff;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 15px;
    }
    .header-box h1 {
        font-size: 20px;
        font-weight: bold;
        color: #00A86B;
        margin-bottom: 5px;
    }
    .tag-box {
        background: linear-gradient(90deg, #fff3e0, #ffe0b2);
        padding: 6px 12px;
        border-radius: 20px;
        display: inline-block;
        font-size: 13px;
        font-weight: bold;
        color: #e65100;
        border: 1px dashed #ffa726;
        margin-bottom: 10px;
    }
    
    /* मोबाईलच्या होमस्क्रीनसारखी ४x४ ग्रिड रचना व चमचमीत रंग */
    .app-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        margin-bottom: 15px;
    }
    .app-btn {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 12px 5px;
        border-radius: 18px;
        color: white;
        text-align: center;
        font-weight: bold;
        font-size: 12px;
        cursor: pointer;
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
        transition: 0.2s;
        text-decoration: none;
        border: none;
        width: 100%;
    }
    .app-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        color: white;
    }
    
    /* प्रत्येक बटनासाठी वेगळा रंगीबेरंगी आणि गोल्डन लुक */
    .btn-rti { background: linear-gradient(135deg, #00b09b, #96c93d); }
    .btn-appeal { background: linear-gradient(135deg, #ff9966, #ff5e62); }
    .btn-comm { background: linear-gradient(135deg, #232526, #414345); border: 1px solid #ffd700; }
    .btn-ai { background: linear-gradient(135deg, #4e54c8, #8f94fb); }
    .btn-court { background: linear-gradient(135deg, #7f00ff, #e100ff); }
    .btn-comp { background: linear-gradient(135deg, #cb356b, #bd3f32); }
    .btn-aff { background: linear-gradient(135deg, #f2994a, #f2c94c); }
    .btn-cons { background: linear-gradient(135deg, #00c6ff, #0072ff); }

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
        <div class="tag-box">⚡ घरसल्या एका मिनिटात अर्ज तयार करा</div>
        <p style="font-size: 12px; color: #555; margin:0;">👤 सतीश अशोक प्रधान | 📱 ८६६८२३५३९५ | छत्रपती संभाजीनगर</p>
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
        if strlit.button("🚀 ॲप सुरू करा"):
            if len(mob) == 10 and mob.isdigit():
                strlit.session_state.is_logged_in = True
                strlit.session_state.user_mobile = mob
                strlit.rerun()
            else:
                strlit.error("कृपया अचूक १० अंकी नंबर टाका.")
else:
    if "active_module" not in strlit.session_state:
        strlit.session_state.active_module = "rti"

    strlit.markdown("### 🎛️ सेवा निवडा (मोबाईल डिझाइन):")

    # ==============================================================================
    # मोबाईलच्या होमस्क्रीनसारखी चमचमीत रंगीबेरंगी बटने (वर ४, खाली ४)
    # ==============================================================================
    
    col1, col2, col3, col4 = strlit.columns(4)
    with col1:
        if strlit.button("📄\nजोडपत्र 'अ'"): strlit.session_state.active_module = "rti"
    with col2:
        if strlit.button("⚖️\nप्रथम अपील"): strlit.session_state.active_module = "first_appeal"
    with col3:
        if strlit.button("🏛️\nमाहिती आयोग"): strlit.session_state.active_module = "commission"
    with col4:
        if strlit.button("✨\nAI चॅट"): strlit.session_state.active_module = "ai_chat"

    col5, col6, col7, col8 = strlit.columns(4)
    with col5:
        if strlit.button("📜\nकोर्ट याचिका"): strlit.session_state.active_module = "court"
    with col6:
        if strlit.button("📣\nशासकीय तक्रार"): strlit.session_state.active_module = "complaint"
    with col7:
        if strlit.button("✏️\nप्रतिज्ञापत्र"): strlit.session_state.active_module = "affidavit"
    with col8:
        if strlit.button("🛒\nग्राहक मंच"): strlit.session_state.active_module = "consumer"

    strlit.write("---")

    # ================= मॉड्यूल्सची अंमलबजावणी =================

    if strlit.session_state.active_module == "rti":
        strlit.subheader("📄 जोडपत्र 'अ' - माहिती अधिकार अर्ज")
        dept = strlit.text_input("जन माहिती अधिकारी, विभाग व पत्ता:")
        subject = strlit.text_input("माहितीचा विषय:")
        details = strlit.text_area("माहितीचा तपशील:")
        if strlit.button("मसुदा तयार करा"):
            draft = f"""
**माहिती अधिकाराचा अर्ज (जोडपत्र 'अ')**
प्रति, जन माहिती अधिकारी, {dept}
विषय: {subject}
१. माहितीचा तपशील: {details}
**अर्जदार:** सतीश अशोक प्रधान, छत्रपती संभाजीनगर | दिनांक: {datetime.date.today().strftime('%d/%m/%Y')}
            """
            strlit.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    elif strlit.session_state.active_module == "ai_chat":
        strlit.subheader("✨ आकांक्षा AI कायदेशीर सल्लागार (चॅट बॉट)")
        strlit.info("💡 इथे तुम्ही RTI, कायदे, किंवा कोणत्याही शासकीय प्रक्रियेबद्दल प्रश्न विचारू शकता.")
        
        if "messages" not in strlit.session_state:
            strlit.session_state.messages = []

        for message in strlit.session_state.messages:
            with strlit.chat_message(message["role"]):
                strlit.markdown(message["content"])

        if prompt := strlit.chat_input("तुमचा कायदेशीर किंवा RTI बद्दलचा प्रश्न येथे विचारပါ။"):
            strlit.session_state.messages.append({"role": "user", "content": prompt})
            with strlit.chat_message("user"):
                strlit.markdown(prompt)

            with strlit.chat_message("assistant"):
                if "आरटीआय" in prompt or "rti" in prompt.lower() or "माहिती" in prompt:
                    ai_response = "माहिती अधिकार कायदा २००५ कलमानुसार आपण कोणत्याही शासकीय विभागाकडून नियमानुसार माहिती मागू शकता. प्रथम 'जोडपत्र अ' वापरून अर्ज दाखल करावा."
                elif "अपील" in prompt:
                    ai_response = "जर ३० दिवसांत माहिती मिळाली नाही, तर संबंधित अपिलीय अधिकारी यांच्याकडे 'प्रथम अपील' दाखल करू शकता."
                else:
                    ai_response = f"सतीशजी, तुमच्या '{prompt}' या प्रश्नासंदर्भात योग्य कायदेशीर प्रक्रिया पार पाडण्यासाठी वरील योग्य मसुदा निवडा."
                
                strlit.markdown(ai_response)
                strlit.session_state.messages.append({"role": "assistant", "content": ai_response})

    elif strlit.session_state.active_module == "first_appeal":
        strlit.subheader("⚖️ प्रथम अपील अर्ज (कलम १९)")
        fa_dept = strlit.text_input("प्रथम अपिलीय अधिकारी व पत्ता:")
        reason = strlit.text_area("अपिलाचे कारण:")
        if strlit.button("प्रथम अपील तयार करा"):
            draft = f"**प्रथम अपील अर्ज**\nप्रति, {fa_dept}\nकारण: {reason}\n**अपीलार्थी:** सतीश अशोक प्रधान, छत्रपती संभाजीनगर"
            strlit.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    elif strlit.session_state.active_module == "commission":
        strlit.subheader("🏛️ राज्य माहिती आयोग")
        comm_details = strlit.text_area("तक्रार तपशील:")
        if strlit.button("आयोग अर्ज तयार करा"):
            draft = f"**द्वितीय अपील - राज्य माहिती आयोग**\nतपशील: {comm_details}\n**अर्जदार:** सतीश अशोक प्रधान, छत्रपती संभाजीनगर"
            strlit.markdown(f"<div class='a4-container'>{draft}</div>", unsafe_allow_html=True)

    elif strlit.session_state.active_module == "court":
        strlit.subheader("📜 कोर्ट याचिका मसुदा")
        facts = strlit.text_area("हकीकत:")
        if strlit.button("याचिका तयार करा"):
            strlit.markdown(f"<div class='a4-container'><b>कोर्ट याचिका मसुदा:</b> {facts}<br><b>याचिकाकर्ता:</b> सतीश अशोक प्रधान</div>", unsafe_allow_html=True)

    elif strlit.session_state.active_module == "complaint":
        strlit.subheader("📣 शासकीय तक्रार अर्ज")
        comp = strlit.text_area("तक्रारीचा विषय व तपशील:")
        if strlit.button("तक्रार तयार करा"):
            strlit.markdown(f"<div class='a4-container'><b>शासकीय तक्रार:</b> {comp}<br><b>तक्रारदार:</b> सतीश अशोक प्रधान, छत्रपती संभाजीनगर</div>", unsafe_allow_html=True)

    elif strlit.session_state.active_module == "affidavit":
        strlit.subheader("✏️ प्रतिज्ञापत्र")
        aff = strlit.text_area("घोषणा मुद्दे:")
        if strlit.button("प्रतिज्ञापत्र तयार करा"):
            strlit.markdown(f"<div class='a4-container'><b>प्रतिज्ञापत्र:</b> {aff}<br><b>घोषणाकर्ता:</b> सतीश अशोक प्रधान</div>", unsafe_allow_html=True)

    elif strlit.session_state.active_module == "consumer":
        strlit.subheader("🛒 ग्राहक मंच तक्रार")
        cons = strlit.text_area("फसवणूक तपशील व भरपाई:")
        if strlit.button("ग्राहक मंच अर्ज तयार करा"):
            strlit.markdown(f"<div class='a4-container'><b>ग्राहक मंच अर्ज:</b> {cons}<br><b>तक्रारदार:</b> सतीश अशोक प्रधान</div>", unsafe_allow_html=True)
