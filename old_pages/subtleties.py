import streamlit as st
import pandas as pd

from utilities import remove_global_duplicates, remove_harakat

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

    selected_surah = st.selectbox("Select a Surah to explore its numerical patterns, and miracles :", ["Surah Al-Baqarah", "Surah Al-Kahf", "Surah Al-Mulk", "Surah Al-Kausar"])

    if selected_surah == "Surah Al-Kausar":
            
        st.subheader("4. Surah Kausar analysis")

        st.markdown("""
        Surah Al-Kausar (Chapter 108) is the shortest chapter in the Qur'an, consisting of only three verses.
        It is often cited as a linguistic miracle due to its depth of meaning.
        The chapter is named after the word "Kausar," which means "abundance" or "plenty." It emphasizes the blessings and abundance bestowed upon the Prophet Muhammad (peace be upon him) on the day of Judgement.
        Beside this It is also a chapter of **numerical miracles**. 
        """)

        st.markdown("""
        **Significance of number 10 in surah kausar**
        - The chapter consists of 10 words in Arabic.
        - Every verse has 10 unique letters.
        - This chapter has 10 such letters that doesn't repeat themselves in any verse.
        - Most repeated letter in this chapter is **alif (ا)** which appears 10 times.
        - Each verse of this chapter ends with the letter **ra (ر)**, which is the 10th letter of the Arabic alphabet.
                    """)
        kausar_ayat = quran[quran['surah_name_en'] == 'The Abundance']
        ayah1 = kausar_ayat[quran['ayah_no_surah'] == 1]['ayah_ar'].to_string().split()[1:]
        ayah2 = kausar_ayat[quran['ayah_no_surah'] == 2]['ayah_ar'].to_string().split()[1:]
        ayah3 = kausar_ayat[quran['ayah_no_surah'] == 3]['ayah_ar'].to_string().split()[1:]
        
        with st.expander("Click to see the word count of each verse"):
            st.subheader("Word count in Surah Al-Kausar:")
            st.info(f"{ayah1}, {len(ayah1)}")
            st.info(f"{ayah2}, {len(ayah2)}")
            st.info(f"{ayah3}, {len(ayah3)}")
            st.info(f"{len(ayah1)} + {len(ayah2)} + {len(ayah3)} = {len(ayah1) + len(ayah2) + len(ayah3)}")

        with st.expander("Click to see the letter count of each verse"):
            st.subheader("Letter count in Surah Al-Kausar:")

            st.header("Visual Explanation")
            st.image("images/surah_kausar_unique_letter_count.jpeg", caption="Unique letters in Surah Al-Kausar")
            
            lettersayah1 = remove_harakat("".join(ayah1).replace(" ", ""))
            lettersayah2 = remove_harakat("".join(ayah2).replace(" ", ""))
            lettersayah3 = remove_harakat("".join(ayah3).replace(" ", ""))
            st.info(f"Unique Letters in ayah 1 : {set(lettersayah1)}, {len(set(lettersayah1))}")
            st.info(f"Unique Letters in ayah 2 : {set(lettersayah2)}, {len(set(lettersayah2))}")
            st.info(f"Unique Letters in ayah 3 :  {set(lettersayah3)}, {len(set(lettersayah3))}")

        with st.expander("Click to see letters that doesn't repeat themselves in any ayah"):
            st.subheader("Letters that appear once in every ayah: ")

            # find letters that appear once in every ayah
            lettersayah_list = [lettersayah1, lettersayah2, lettersayah3]
            non_repeated_letters = remove_global_duplicates(lettersayah_list)

            st.info(f"Non-repeated letters in all ayahs: {non_repeated_letters}")
            st.info(f"Non-repeated letters in ayah 1: {set(non_repeated_letters[0])}, {len(non_repeated_letters[0])}")
            st.info(f"Non-repeated letters in ayah 2: {set(non_repeated_letters[1])}, {len(non_repeated_letters[1])}")
            st.info(f"Non-repeated letters in ayah 3: {set(non_repeated_letters[2])}, {len(non_repeated_letters[2])}")
            st.info(f"Total non-repeated letters: {len(non_repeated_letters[0]) + len(non_repeated_letters[1]) + len(non_repeated_letters[2])}")

        with st.expander("Click to see alif count in each verse"):
            st.subheader("Alif count in Surah Al-Kausar:")
            st.header("Visual Explanation")
            st.image("images/surah_kausar_alif_count.jpeg", caption="Alif count in Surah Al-Kausar")

            st.info(f"Alif count in ayah 1: {lettersayah1.count('ا')}")
            st.info(f"Alif count in ayah 2: {lettersayah2.count('ا')}")
            st.info(f"Alif count in ayah 3: {lettersayah3.count('ا')}")
            st.info(f"Total alif count: {lettersayah1.count('ا') + lettersayah2.count('ا') + lettersayah3.count('ا')}")
            st.warning("Note : hamza (ء) is counted as alif (ا) in the whole anlaysis.")
        st.success("These subtleties show the Qur'an's linguistic depth and structural design, no one other than Allah can create a single verse like that.")