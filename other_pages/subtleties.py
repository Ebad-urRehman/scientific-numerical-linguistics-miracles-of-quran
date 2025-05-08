import streamlit as st
import pandas as pd

from utilities import remove_harakat

quran = pd.read_csv("The Quran Dataset.csv")  

def display_interesting_subtleties():
    st.header("🧠 Interesting Linguistic and Structural Subtleties")

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

    st.subheader("4. Surah Kausar analysis")

    st.markdown("""
    Surah Al-Kausar (Chapter 108) is the shortest chapter in the Qur'an, consisting of only three verses.
    It is often cited as a linguistic miracle due to its brevity and depth of meaning.
    The chapter is named after the word "Kausar," which means "abundance" or "plenty." It emphasizes the blessings and abundance bestowed upon the Prophet Muhammad (peace be upon him).
    """)

    st.markdown("""
    **Significance of number 10 in surah kausar**
    - The chapter consists of 10 words in Arabic.
    - Every verse has 10 unique letters.
    - The chapter has 10 unique letters in total.
    """)
    kausar_ayat = quran[quran['surah_name_en'] == 'The Abundance']
    ayah1 = kausar_ayat[quran['ayah_no_surah'] == 1]['ayah_ar'].to_string().split()[1:]
    ayah2 = kausar_ayat[quran['ayah_no_surah'] == 2]['ayah_ar'].to_string().split()[1:]
    ayah3 = kausar_ayat[quran['ayah_no_surah'] == 3]['ayah_ar'].to_string().split()[1:]
    
    with st.expander("Click to see the word count of each verse"):
        st.info("Word count in Surah Al-Kausar:")
        st.info(f"{ayah1}, {len(ayah1)}")
        st.info(f"{ayah2}, {len(ayah2)}")
        st.info(f"{ayah3}, {len(ayah3)}")
        st.info(f"{len(ayah1)} + {len(ayah2)} + {len(ayah3)} = {len(ayah1) + len(ayah2) + len(ayah3)}")

    with st.expander("Click to see the letter count of each verse"):
        st.info("Letter count in Surah Al-Kausar:")
        lettersayah1 = remove_harakat("".join(ayah1).replace(" ", ""))
        lettersayah2 = remove_harakat("".join(ayah2).replace(" ", ""))
        lettersayah3 = remove_harakat("".join(ayah3).replace(" ", ""))
        st.info(f"Letters in ayah 1 : {ayah1}, {len(set(lettersayah1))}")
        st.info(f"Letters in ayah 2 : {ayah2}, {len(set(lettersayah2))}")
        st.info(f"Letters in ayah 3 :  {ayah3}, {len(set(lettersayah3))}")
    st.success("These subtleties show the Qur'an's linguistic depth and structural design, hinting at divine authorship.")