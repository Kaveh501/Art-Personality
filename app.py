

import streamlit as st

# تنظیمات اولیه صفحه
st.set_page_config(page_title="Art Personality", layout="centered")

# زبان‌ها و ترجمه‌ها
langs = {
    "fa": {
        "page_title": "🎨 تست شخصیت هنری تو",
        "intro": "با چند تا سوال ساده، بفهم که چه نوع آرتیستی هستی!",
        "tool_q": "از چه ابزارهایی بیشتر استفاده می‌کنی؟",
        "tools": ["دیجیتال", "سنتی", "ترکیبی", "سه‌بعدی"],
        "inspire_q": "الهام‌بخش‌هات کیان؟",
        "inspires": ["طبیعت", "احساسات", "سیاست", "فانتزی"],
        "vibe_q": "آثارت چه حال و هوایی دارن؟",
        "vibes": ["تاریک", "آرام", "انرژی‌بخش", "آشفته"],
        "style_q": "سبک مورد علاقه‌ت چیه؟",
        "styles": ["سوررئال", "آبستره", "رئالیسم", "اکسپرسیونیسم"],
        "submit": "نتیجه تست",
        "result_title": "✨ رویاپرداز دیجیتال",
        "result_text": "تو ذهنی پر از ایده‌های خیال‌انگیز داری. دنیای تو پر از رنگ و نور و جادوئه!"
    },
    "en": {
        "page_title": "🎨 Your Artistic Personality Test",
        "intro": "Answer a few quick questions and find out your inner artist!",
        "tool_q": "What tools do you mostly use?",
        "tools": ["Digital", "Traditional", "Hybrid", "3D"],
        "inspire_q": "What inspires you?",
        "inspires": ["Nature", "Emotions", "Politics", "Fantasy"],
        "vibe_q": "What vibe do your artworks have?",
        "vibes": ["Dark", "Calm", "Energetic", "Chaotic"],
        "style_q": "What's your favorite art style?",
        "styles": ["Surreal", "Abstract", "Realism", "Expressionism"],
        "submit": "Show Result",
        "result_title": "✨ The Digital Dreamer",
        "result_text": "Your mind is full of surreal visions and magical ideas. You're born to create wonders!"
    }
}

# انتخاب زبان
lang_choice = st.selectbox("Language / زبان", ["فارسی", "English"])
lang = "fa" if lang_choice == "فارسی" else "en"
t = langs[lang]

# موزیک پس‌زمینه با iframe (مثلاً موزیک هنری یا لوفای)
st.markdown("""
<div style="text-align:center;">
<iframe src="https://open.spotify.com/embed/track/1HNkqx9Ahdgi1Ixy2xkKkL" width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
</div>
""", unsafe_allow_html=True)

# عنوان و معرفی
st.title(t["page_title"])
st.markdown(t["intro"])

# سوالات
tool = st.radio(t["tool_q"], t["tools"])
inspiration = st.radio(t["inspire_q"], t["inspires"])
vibe = st.radio(t["vibe_q"], t["vibes"])
style = st.radio(t["style_q"], t["styles"])

# تم رنگی داینامیک بر اساس vibe
theme_colors = {
    "تاریک": "#2e2e2e", "Dark": "#2e2e2e",
    "آرام": "#88c0d0", "Calm": "#88c0d0",
    "انرژی‌بخش": "#ff8800", "Energetic": "#ff8800",
    "آشفته": "#ff0066", "Chaotic": "#ff0066"
}

bg_color = theme_colors.get(vibe, "#ffffff")

# نمایش نتیجه
if st.button(t["submit"]):
    st.markdown(
        f"""
        <div style='background-color:{bg_color}; padding:20px; border-radius:10px; text-align:center;'>
            <h2>{t["result_title"]}</h2>
            <p style='font-size:18px'>{t["result_text"]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
