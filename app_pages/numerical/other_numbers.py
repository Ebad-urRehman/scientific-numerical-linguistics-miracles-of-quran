import streamlit as st
import pandas as pd

from utilities import normalize_arabic_letters, remove_global_duplicates, remove_harakat, sum_of_sur_and_verses

st.header("Numerical Patterns Describing Content")

quran = pd.read_csv("The Quran Dataset.csv")

with st.sidebar:
    option = st.radio(
        "Select an option:",
        ["Even and odd numbers", "The Chapter-Verse Matrix", "Surah Kausar Number 10"]
    )

if option == "Even and odd numbers":
    st.markdown("## 🔢 Importance of Even and Odd Numbers")

    # Mathematics section
    st.markdown("""
    ### 🧮 In Mathematics

    - **Even numbers** are divisible by 2 (e.g., 2, 4, 6, ...)  
    → Represent **balance**, **symmetry**, and **pairing**.

    - **Odd numbers** are not divisible by 2 (e.g., 1, 3, 5, ...)  
    → Represent **individuality**, **uniqueness**, and often **mystery**.
    """)

    # Quran section
    st.markdown("""
    ### 📖 In the Qur’an

    #### 1. **Allah swears by Even and Odd**
    > _"By the even and the odd!"_  
    > **(Qur’an 89:3 — Surah Al-Fajr)**
    """)
    
    st.image("images/numerical/even_and_odd.png")
    
    st.markdown("""
    - Shows divine attention to **balance and structure**.
    - Scholars interpret it in layers:
    - **Even** = pairs (male/female, heaven/earth)
    - **Odd** = Tawḥīd (Oneness of Allah)

    #### 2. **Allah is One (Witr)**
    > The Prophet ﷺ said:  
    > _“Allah is One (Witr), and He loves odd numbers.”_  
    
    Full Hadith
    >There are ninety-nine names of Allah; he who commits them to memory would get into Paradise. Verily, Allah is Odd (He is one, and it is an odd number) and He loves odd number. And in the narration of Ibn 'Umar (the words are):" He who enumerated them."
    > **(Sahih Muslim, 2677)**

    This indicates a divine preference for **oddness**, especially in worship:
    - Witr prayer is 1 or 3 rak‘ahs
    - Tawaf is done **7** times
    - Stoning the devil: odd number of stones
    """)

    # Table of symbolic meanings
    data = {
        "Concept": ["Male & Female", "Tawḥīd (Oneness)", "Creation in Pairs", "Allah’s Unity", "Balance of opposites"],
        "Even ↔ Odd": ["Paired (Even)", "Singular (Odd)", "Even (Qur’an 51:49)", "Odd (Witr)", "Even ↔ Odd"]
    }
    df = pd.DataFrame(data)

    st.markdown("### 🧠 Symbolic Concepts")
    st.table(df)

elif option == "The Chapter-Verse Matrix":
    st.header("Chapter Verse Matrix")
    st.write("Insight : Even, and Odd numbers from chapter-verse sum column seperately add up to sum of verse numbers and sum of chapter numbers")
    st.image("images/numerical/chapter_verse_matrix.png")
    st.header("Proof")
    st.subheader("Calculating total number of Ayah, and Chapters, and their sums")

    surahs_sum, total_ayahs = sum_of_sur_and_verses()
    surah_nos = [i for i in range(1, 115)] # surah numbers list
    ayah_nos = [quran[quran['surah_no'] == i]['total_ayah_surah'].iloc[0] for i in surah_nos]
    chap_verse_sum = [surah_no + ayah_no for surah_no, ayah_no in zip(surah_nos, ayah_nos)]

    surah_verse_df = pd.DataFrame({
    "Surah Number": surah_nos,
    "Total Verses": ayah_nos,
    "Chapter-Verse Sum" : chap_verse_sum
})
    st.dataframe(surah_verse_df)


    st.info(f"Sum of above two columns {surahs_sum} {total_ayahs}")

    st.subheader("Now compute Even and Odd numbers wrt Chapter-Verse Sum Column")

    even_odd_list = ["Even" if chap_verse_sum[i] % 2 == 0 else "Odd" for i in range(len(chap_verse_sum))]

    # adding even odd columns to surah_verse_df
    surah_verse_df["Even Odd"] = even_odd_list

    st.dataframe(surah_verse_df)

    # Calculating even and odd surahs
    even_surahs = surah_verse_df[surah_verse_df['Even Odd'] == 'Even']
    odd_surahs = surah_verse_df[surah_verse_df['Even Odd'] == 'Odd']
    
    st.markdown(f"#### Count of Even Surah Number : {len(even_surahs)}")
    st.markdown(f"#### Count of Odd Surah Number : {len(odd_surahs)}")
    st.markdown(f"#### Count of Even Surah Number = Count of Odd Surah Number = {len(odd_surahs)}")

    st.divider()

    st.markdown("##### Writing even and odd counts in seperate columns")
    surah_verse_df['Only Even'] = [surah_verse_df['Chapter-Verse Sum'].iloc[i] if even_odd_list[i] == "Even" else 0 for i in range(len(even_odd_list))]
    surah_verse_df['Only Odd'] = [surah_verse_df['Chapter-Verse Sum'].iloc[i] if even_odd_list[i] == "Odd" else 0 for i in range(len(even_odd_list))]
    st.dataframe(surah_verse_df)

    st.write("Adding them up...")
    
    st.code(f"""Surah's Sum : {sum(surah_nos)}
Ayah's sum : {sum(ayah_nos)}
Sum of Odd numbers in Chapter-Verse Sum : {sum(surah_verse_df["Only Odd"])}
Sum of Even numbers in Chapter-Verse Sum : {sum(surah_verse_df["Only Even"])}""")
    

elif option == "Surah Kausar Number 10":
    st.subheader("Surah Kausar analysis")

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
        st.image("images/numerical/surah_kausar_unique_letter_count.jpeg", caption="Unique letters in Surah Al-Kausar")
        
        lettersayah1 = remove_harakat(normalize_arabic_letters("".join(ayah1).replace(" ", "")))
        lettersayah2 = remove_harakat(normalize_arabic_letters("".join(ayah2).replace(" ", "")))
        lettersayah3 = remove_harakat(normalize_arabic_letters("".join(ayah3).replace(" ", "")))
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
        st.image("images/numerical/surah_kausar_alif_count.jpeg", caption="Alif count in Surah Al-Kausar")

        st.info(f"Alif count in ayah 1: {lettersayah1.count('ا')}")
        st.info(f"Alif count in ayah 2: {lettersayah2.count('ا')}")
        st.info(f"Alif count in ayah 3: {lettersayah3.count('ا')}")
        st.info(f"Total alif count: {lettersayah1.count('ا') + lettersayah2.count('ا') + lettersayah3.count('ا')}")
        st.warning("Note: According to most scholars, the letter Hamza (ء) is considered equivalent to Alif (ا) in script and is counted as Alif (ا) throughout this analysis.")
    st.success("These subtleties show the Qur'an's linguistic depth and structural design, no one other than Allah can create a single verse like that.")