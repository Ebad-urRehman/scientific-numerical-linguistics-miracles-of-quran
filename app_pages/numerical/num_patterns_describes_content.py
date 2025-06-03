import base64
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

from utilities import find_letters_count_in_range, find_words_count_in_range

st.header("Numerical Patterns Describing Content")

quran = pd.read_csv("The Quran Dataset.csv")

option = option_menu(
        "Select an Option",
        ["Placement of Surah 'The Iron'", 
         "Creation of man and number of chromosomes pattern"],
        icons=["book", "layers", "dna"],  # Optional: add relevant icons
        menu_icon="cast",  # Optional: main sidebar icon
        default_index=0,
        orientation="horizontal"
    )
if option == "Surah Kahf mentioning 300 years":
        st.header("📜 Surah Al-Kahf: Numerical Miracle of 300 Years")
        start, end = 12, 26
        surah = 18
        # getting word count from first occurence of "لَبِثُو" to "مِائَةٍ" before "سِنِيۡنَ"
        words_before_300 = find_words_count_in_range(quran, surah, start, end, skip_first_words=8, skip_last_words=18)
        st.info(words_before_300)


    
    
elif option == "Placement of Surah 'The Iron'":
    pass
elif option == "Creation of man and number of chromosomes pattern":
    pdf_url = "https://dn721607.ca.archive.org/0/items/chromosome-numbers-in-the-holy-quran_202006/Chromosome%20numbers%20in%20the%20Holy%20Quran.pdf"

    st.components.v1.html(f"""
        <iframe src="{pdf_url}" width="100%" height="1000px"">
        </iframe>
    """, height=1000)


