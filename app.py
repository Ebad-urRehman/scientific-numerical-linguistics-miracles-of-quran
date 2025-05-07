import streamlit as st
from streamlit_option_menu import option_menu

# Set page config
st.set_page_config(page_title="Qur'an Miracles Explorer", layout="wide")

# Main navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=[
            "Home",
            "Scientific Miracles",
            "Linguistic Miracles",
            "Numerical Patterns",
            "Unnoticed Subtleties",
            "Discover New Patterns"
        ],
        icons=["house", "microscope", "chat-text", "123", "lightbulb", "search"],
        menu_icon="cast",
        default_index=0
    )

# Pages
if selected == "Home":
    st.title("📖 Qur'an Miracles Explorer")
    st.markdown("""
    Welcome to our exhibition project! This app showcases:
    - **Scientific Miracles**
    - **Linguistic Wonders**
    - **Numerical Patterns**
    - **Unnoticed Subtleties**

    Future version will help discover new miracles using technology!
    """)

elif selected == "Scientific Miracles":
    st.header("🔬 Scientific Miracles in the Qur’an")

    st.subheader("1. Embryology in the Qur'an")
    st.markdown("""
    **Verse**: *Surah Al-Mu’minun (23:12–14)*  
    **Arabic**:  
    `وَلَقَدْ خَلَقْنَا ٱلْإِنسَـٰنَ مِن سُلَـٰلَةٍۢ مِّن طِينٍۢ ...`  
    **Translation**:  
    _"We created man from an extract of clay... then We made the drop into a clinging clot, and We made the clot into a lump, and We made the lump bones, and We covered the bones with flesh..."_

    **Scientific Insight**:  
    This verse describes the stages of embryonic development with remarkable accuracy: sperm-drop → clinging clot → lump → bones → flesh. Modern embryology confirms these stages with ultrasound imaging and embryological data.

    **Reference**: Keith L. Moore, Embryologist, acknowledged the resemblance of Qur’anic descriptions to scientific knowledge.
    """)

    st.markdown("---")

    st.subheader("2. The Big Bang and Expansion of the Universe")
    st.markdown("""
    **Verse**: *Surah Al-Anbiya (21:30)*  
    **Arabic**:  
    `أَوَلَمْ يَرَ ٱلَّذِينَ كَفَرُوٓا۟ أَنَّ ٱلسَّمَـٰوَٰتِ وَٱلْأَرْضَ كَانَتَا رَتْقًۭا فَفَتَقْنَـٰهُمَا...`  
    **Translation**:  
    _"Do not the disbelievers see that the heavens and the earth were a joined entity, then We split them apart..."_

    **Scientific Insight**:  
    This is a clear reference to the **Big Bang**, the widely accepted theory of how the universe began as a single point and expanded outward.

    **Reference**: Supported by Edwin Hubble’s discovery in 1929 that the universe is expanding.

    """)

    st.markdown("---")

    st.subheader("3. Iron Sent Down from the Sky")
    st.markdown("""
    **Verse**: *Surah Al-Hadid (57:25)*  
    **Arabic**:  
    `... وَأَنزَلْنَا ٱلْحَدِيدَ فِيهِ بَأْسٌۭ شَدِيدٌۭ ...`  
    **Translation**:  
    _"...and We sent down iron, in which is strong material and benefits for mankind..."_

    **Scientific Insight**:  
    The Qur’an says iron was “sent down”, which puzzled classical scholars. Modern science confirms that **iron is not native to Earth**—it arrived via meteorites from supernova explosions, which forged iron in the stars.

    **Reference**: NASA & Astrophysics: Iron forms in massive stars and is delivered to planets through cosmic collisions.

    """)

    st.success("These verses, revealed over 1400 years ago, align with modern science—yet were spoken in an age with no scientific tools.")


elif selected == "Linguistic Miracles":
    st.header("🗣️ Linguistic Miracles in the Qur’an")

    st.subheader("1. Inimitability (I'jaz) of the Qur'an")
    st.markdown("""
    The Qur'an challenges mankind to produce even a single Surah like it (Surah Al-Baqarah 2:23).  
    Despite being brief, Surah Al-Kawthar (3 verses) is rich in rhythm, depth, and eloquence—unmatched by Arabic literature.

    **Example**:  
    _"إِنَّا أَعْطَيْنَاكَ الْكَوْثَرَ"_ – Its rhythmic beauty, concise structure, and layered meanings make it impossible to replicate.
    """)

    st.subheader("2. Perfect Word Choice")
    st.markdown("""
    Arabic has multiple synonyms for many words, yet the Qur'an always uses the most contextually and emotionally appropriate one.

    **Example**:  
    The word _“بصر”_ (vision) is used when referring to external sight, while _“نظر”_ is used when deeper contemplation is meant.
    """)

    st.subheader("3. Gender-Consistent Verbs")
    st.markdown("""
    Arabic verbs change with gender. In Surah Al-Shams (91:8), the soul is grammatically feminine:
    
    _"فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَاهَا"_  
    The verb is correctly conjugated to match. This level of grammar accuracy is consistent throughout.
    """)

    st.success("The Qur'an's linguistic perfection stunned even the most eloquent Arabs of its time.")


elif selected == "Numerical Patterns":
    st.header("🔢 Numerical Patterns in the Qur’an")

    st.subheader("1. Word Pair Counts")
    st.markdown("""
    - **"Day" (يوم)** appears **365** times → Number of days in a year  
    - **"Month" (شهر)** appears **12** times → Months in a year  
    - **"Angels" and "Devils"** each appear **88** times  
    - **"Life" (الحياة)** and **"Death" (الموت)** both occur **145** times  
    """)

    st.subheader("2. Symmetry in Word Placement")
    st.markdown("""
    The middle verse of the Qur'an is **Surah Al-Kahf (18:19)**, and that verse talks about **time**—"how long did you remain?"  
    This mirroring of theme and position is mathematically elegant.

    """)

    st.subheader("3. Balanced Contrasts")
    st.markdown("""
    - “World” (الدنيا) and “Hereafter” (الآخرة): **115** times each  
    - “Reward” and “Punishment”: Same count  
    These contrasts show intended balance—not random chance.
    """)

    st.info("These word counts are preserved across centuries and manuscripts, hinting at divine preservation.")


elif selected == "Unnoticed Subtleties":
    st.header("🧠 Unnoticed Linguistic and Structural Subtleties")

    st.subheader("1. Chiastic (Mirror) Structures")
    st.markdown("""
    Many Surahs are **chiastic** – meaning the structure mirrors around a central theme.

    **Example**: Surah Al-Baqarah**  
    - Begins and ends with guidance & belief  
    - Middle focuses on **changing Qibla** — spiritual direction

    This complex structure holds throughout, showing deep design.
    """)

    st.subheader("2. Selective Use of Letters")
    st.markdown("""
    In Surah Yusuf, the word **“king” (ملك)** is used, not **“Pharaoh (فرعون)”**, because Yusuf lived under kings of Egypt—not the Pharaohs.  
    But in Musa's story, **Pharaoh** is used consistently.

    This shows **historical accuracy** in word selection.
    """)

    st.subheader("3. Sound and Meaning Harmony")
    st.markdown("""
    Verses often use **harsh sounds** when talking about punishment and **soft sounds** for mercy.

    **Example**:  
    _"فَسَوْفَ نُيَسِّرُهُ لِلْيُسْرَىٰ"_ (We will ease him toward ease)  
    The verse itself sounds easy and smooth.
    """)

    st.success("Such subtleties are hard to notice but deepen one’s awe of the Qur’an.")


elif selected == "Discover New Patterns":
    st.header("🔍 Discover New Patterns (Coming Soon)")
    st.markdown("""
    Planned tools:
    - Arabic NLP to analyze roots, frequency, and positions
    - Pattern mining and symmetrical phrase detection
    - Community-sourced discoveries
    """)
