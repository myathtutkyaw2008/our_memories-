import streamlit as st

# App Header
st.title("💖 Our Special Memories 💖")

# လုံခြုံရေးအတွက် Password (သို့) Pin နံပါတ် ခံခြင်း
password = st.text_input("ကျေးဇူးပြု၍ လျှို့ဝှက်နံပါတ် (Pin) ထည့်ပါ:", type="password")

# ကိုယ်နဲ့ သူ သတ်မှတ်ထားမယ့် Password (ဥပမာ - 1234 ဒါမှမဟုတ် နှစ်ယောက်သားအထူးနေ့စွဲ)
CORRECT_PIN = "2008" 

if password == CORRECT_PIN:
    st.success("ဝင်ရောက်ခွင့် ပြုပါပြီ! ✨")
    
    # Menu Selection (Albums)
    menu = st.radio("Albums များကို ရွေးချယ်ပါ:", ["🎵 Music Album", "👦 My Photos", "👧 Her Photos", "💌 Memories & Notes"])

    if menu == "🎵 Music Album":
        st.header("🎵 Music Collection")
        st.write("ကိုယ် ဆိုပြတီးပြဖူးတဲ့ သီချင်းလေးများ... (နောင်မှ ထည့်မည်)")

    elif menu == "👦 My Photos":
        st.header("👦 My Photos Album")
        st.write("ကိုယ့်ရဲ့ ဓာတ်ပုံလေးများ... (နောင်မှ ထည့်မည်)")

    elif menu == "👧 Her Photos":
        st.header("👧 Her Photos Album")
        st.write("သူ့ရဲ့ ဓာတ်ပုံလေးများ... (နောင်မှ ထည့်မည်)")

    elif menu == "💌 Memories & Notes":
        st.header("💌 Memories & Notes")
        st.write("နှစ်ယောက်သားရဲ့ အမှတ်တရများ...")
        
        # စာအသစ်ထပ်ရေးရန် Box
        new_note = st.text_area("မှတ်စုအသစ် ရေးရန်:")
        if st.button("Save Memory"):
            if new_note:
                st.success("မှတ်စုကို သိမ်းဆည်းပြီးပါပြီ!")
            else:
                st.warning("ကျေးဇူးပြု၍ စာအရင်ရေးပါ။")

elif password:
    st.error("လျှို့ဝှက်နံပါတ် မှားယွင်းနေပါသည်။")
else:
    st.info("ကျေးဇူးပြု၍ လျှို့ဝှက်နံပါတ်ကို ထည့်သွင်းပါ။")
  
