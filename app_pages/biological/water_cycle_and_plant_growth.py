import streamlit as st



st.markdown("""
### Measured Water Distribution
Water is the primary source of life, life can't exist without water, the concentration of water is balanced like all other things.
In Quran Allah Says : 

""")

st.image("images/biological/measured_water.png")

st.markdown("""

The phrase **"in due measure" (bi qadar)** emphasizes **balance** — an exact, regulated quantity of water. Today, scientists recognize that the Earth’s **hydrological cycle** is **finely tuned** to sustain ecosystems without overflowing or drying up — from rainfall to evaporation to condensation and return. 


### Heavy clouds
Humans precieve clouds to be light wieghted till before the discovery of science that clouds are heavy. Quran is explaining formation of massive clouds precisely 1440+ years ago.

""")

st.image("images/biological/cloud_formation.png")

st.header("🌧️ Stages of Rain Formation in the Qur'an and Science")

# rain_stages = [
#     {
#         "title": "1️⃣ Evaporation",
#         "ayah": "وَأَرْسَلْنَا ٱلرِّيَـٰحَ لَوَٰقِحَ فَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَسْقَيْنَـٰكُمُوهُ ۖ وَمَآ أَنتُمْ لَهُۥ بِخَـٰزِنِينَ\n\n\n**“And We sent the winds as fertilizing agents, and We sent down water from the sky and gave it to you to drink—and you are not its retainers.”**\n— *Surah Al-Hijr (15:22)*",
#         "explanation": "🌡️ **Scientific View:** Sunlight causes water from oceans, lakes, and rivers to evaporate into vapor.\n💡 **Qur'anic Insight:** The winds act as agents that initiate this process, fertilizing the clouds."
#     },
#     {
#         "title": "2️⃣ Condensation",
#         "ayah": "اَلَمۡ تَرَ اَنَّ اللّٰهَ يُزۡجِىۡ سَحَابًا ثُمَّ يُؤَلِّفُ بَيۡنَهٗ ثُمَّ يَجۡعَلُهٗ رُكَامًا فَتَرَى الۡوَدۡقَ يَخۡرُجُ مِنۡ خِلٰلِهٖ​ۚ \n\n“Do you not see that Allāh drives clouds? Then He brings them together; then He makes them into a mass, and you see the rain emerge from within it..\n\n\n — Saheeh International\n\n\n**",
#         "explanation": "🌬️ **Scientific View:** Water vapor cools and condenses on dust particles to form clouds.\n\n💡Qur'anic Insight:** Allah drives and gathers the clouds into heaps—describing condensation and cloud formation."
#     },
#     {
#         "title": "3️⃣ Cloud Growth",
#         "ayah": "وَهُوَ ٱلَّذِى يُرْسِلُ ٱلرِّيَـٰحَ بُشْرًۭا بَيْنَ يَدَىْ رَحْمَتِهِۦ ۖ حَتَّىٰٓ إِذَآ أَقَلَّتْ سَحَابًۭا ثِقَالًۭا\n**“And it is He who sends the winds as good tidings before His mercy, until, when they have carried heavy clouds...”**\n— *Surah Al-A'raf (7:57)*",
#         "explanation": "☁️ **Scientific View:** As clouds gather more condensed vapor, they become dense and heavy.\n💡 **Qur'anic Insight:** The term *heavy clouds* perfectly aligns with the scientific threshold before rainfall begins."
#     },
#     {
#         "title": "4️⃣ Precipitation (Rainfall)",
#         "ayah": "فَتَرَى ٱلْوَدْقَ يَخْرُجُ مِنْ خِلَـٰلِهِۦ\n**“And you see the rain emerge from within it...”**\n— *Surah An-Nur (24:43)*",
#         "explanation": "🌧️ **Scientific View:** When clouds become saturated, water droplets fall due to gravity.\n💡 **Qur'anic Insight:** The verse describes this exact moment—rain falling from cloud masses."
#     },
#     {
#         "title": "5️⃣ Earth Revived",
#         "ayah": "وَٱللَّهُ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَسْمَعُونَ\n**“And Allah sends down rain from the sky and gives life thereby to the earth after its lifelessness. Indeed in that is a sign for people who listen.”**\n— *Surah An-Nahl (16:65)*",
#         "explanation": "🌱 **Scientific View:** Rain nourishes soil, supports plant growth, and sustains ecosystems.\n💡 **Qur'anic Insight:** The revival of barren land through rain is highlighted as a divine sign."
#     }
# ]

rain_stages = [
    {
        "title": "1️⃣ Evaporation",
        "ayah": "وَأَرْسَلْنَا ٱلرِّيَـٰحَ لَوَٰقِحَ فَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَسْقَيْنَـٰكُمُوهُ ۖ وَمَآ أَنتُمْ لَهُۥ بِخَـٰزِنِينَ\n\n“**And We sent the winds as fertilizing agents, and We sent down water from the sky and gave it to you to drink—and you are not its retainers.**”\n\n— *Surah Al-Hijr (15:22)*",
        "explanation": "🌡️ **Scientific View:** Sunlight causes water from oceans, lakes, and rivers to evaporate into vapor.\n\n💡 **Qur'anic Insight:** The winds act as agents that initiate this process, fertilizing the clouds."
    },
    {
        "title": "2️⃣ Condensation",
        "ayah": "اَلَمۡ تَرَ اَنَّ اللّٰهَ يُزۡجِىۡ سَحَابًا ثُمَّ يُؤَلِّفُ بَيۡنَهٗ ثُمَّ يَجۡعَلُهٗ رُكَامًا فَتَرَى الۡوَدۡقَ يَخۡرُجُ مِنۡ خِلٰلِهٖ​ۚ\n\n“**Do you not see that Allāh drives clouds? Then He brings them together; then He makes them into a mass, and you see the rain emerge from within it.**”\n\n— *Surah An-Nur (24:43)*",
        "explanation": "🌬️ **Scientific View:** Water vapor cools and condenses on dust particles to form clouds.\n\n💡 **Qur'anic Insight:** Allah drives and gathers the clouds into heaps—describing condensation and cloud formation."
    },
    {
        "title": "3️⃣ Cloud Growth",
        "ayah": "وَهُوَ ٱلَّذِى يُرْسِلُ ٱلرِّيَـٰحَ بُشْرًۭا بَيْنَ يَدَىْ رَحْمَتِهِۦ ۖ حَتَّىٰٓ إِذَآ أَقَلَّتْ سَحَابًۭا ثِقَالًۭا\n\n“**And it is He who sends the winds as good tidings before His mercy, until, when they have carried heavy clouds...**”\n\n— *Surah Al-A'raf (7:57)*",
        "explanation": "☁️ **Scientific View:** As clouds gather more condensed vapor, they become dense and heavy.\n\n💡 **Qur'anic Insight:** The term *heavy clouds* perfectly aligns with the scientific threshold before rainfall begins."
    },
    {
        "title": "4️⃣ Precipitation (Rainfall)",
        "ayah": "فَتَرَى ٱلْوَدْقَ يَخْرُجُ مِنْ خِلَـٰلِهِۦ\n\n“**And you see the rain emerge from within it...**”\n\n— *Surah An-Nur (24:43)*",
        "explanation": "🌧️ **Scientific View:** When clouds become saturated, water droplets fall due to gravity.\n\n💡 **Qur'anic Insight:** The verse describes this exact moment—rain falling from cloud masses."
    },
    {
        "title": "5️⃣ Earth Revived",
        "ayah": "وَٱللَّهُ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّقَوْمٍۢ يَسْمَعُونَ\n\n“**And Allah sends down rain from the sky and gives life thereby to the earth after its lifelessness. Indeed in that is a sign for people who listen.**”\n\n— *Surah An-Nahl (16:65)*",
        "explanation": "🌱 **Scientific View:** Rain nourishes soil, supports plant growth, and sustains ecosystems.\n\n💡 **Qur'anic Insight:** The revival of barren land through rain is highlighted as a divine sign."
    }
]


for stage in rain_stages:
    with st.expander(stage["title"]):
        st.markdown(f"📖 **Qur'anic Ayah:**\n\n{stage['ayah']}")
        st.markdown(f"🔍 **Explanation:**\n\n{stage['explanation']}")