# import streamlit as st

# word_counts_options = ["Angels and Devils", "World and Hereafter", "Days, Month, and Years Count"]

# st.title("Word Count Balance, or ratio shows something")
# with st.sidebar:
#     selected = st.radio("Select an option to display", word_counts_options, index=0, key="word_counts")
# st.markdown("## Word Counts & Ratios")
# st.markdown(
#     """
#     This page explores the word counts and ratios of specific terms in the Quran, highlighting the balance and harmony in their usage.
    
#     - **Angels and Devils**: The Quran mentions angels 88 times and devils 88 times, showing a perfect balance.
#     - **World and Hereafter**: The terms 'world' and 'hereafter' are mentioned 115 times each, emphasizing their equal importance.
#     - **Days, Month, and Years Count**: The Quran mentions 'day' 365 times, 'month' 12 times, and 'year' 19 times, reflecting a consistent numerical pattern.
    
#     These examples illustrate the Quran's intricate numerical structure and its profound significance.
#     """
# )

# if selected == "Angels and Devils":
#     st.markdown("### Angels and Devils")
#     st.markdown(
#         """
#         The Quran mentions **angels** 88 times and **devils** 88 times, showing a perfect balance in their representation.
        
#         - **Angels**: 88 occurrences
#         - **Devils**: 88 occurrences
        
#         This balance highlights the duality of good and evil in the Quranic narrative.
#         """
#     )
# elif selected == "World and Hereafter":
#     st.markdown("### World and Hereafter")
#     st.markdown(
#         """
#         The terms **world** and **hereafter** are mentioned 115 times each, emphasizing their equal importance in the Quran.
        
#         - **World**: 115 occurrences
#         - **Hereafter**: 115 occurrences
        
#         This balance underscores the Quran's focus on both the temporal and eternal aspects of existence.
#         """
#     )
# elif selected == "Days, Month, and Years Count":
#     st.markdown("### Days, Month, and Years Count")
#     st.markdown(
#         """
#         The Quran mentions **day** 365 times, **month** 12 times, and **year** 19 times, reflecting a consistent numerical pattern.
        
#         - **Day**: 365 occurrences
#         - **Month**: 12 occurrences
#         - **Year**: 19 occurrences
        
#         This numerical harmony illustrates the Quran's intricate structure and its profound significance in understanding time.
#         """
#     )

import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Qur'anic Word Counts & Ratio Miracles")
st.markdown("Explore mathematically balanced word frequencies and linguistic patterns in the Qur’an that point to deeper meaning and divine authorship.")

# Word Frequencies
word_counts = {
    "Qul (Say)": 332,
    "Qālū (They said)": 332,
    "Month (Shahr)": 12,
    "Prayer (Salawat)": 5,
    "Iblīs": 11,
    "Seek Refuge (A‘ūdhu)": 11,
    "Angels (Malāʾikah)": 88,
    "Devil (Shayṭān)": 88,
    "Life (Ḥayāh)": 145,
    "Death (Mawt)": 145,
    "World (Dunyā)": 115,
    "Hereafter (Ākhirah)": 115
}

# Section 1: Table
st.subheader("📋 Verified Word Frequencies in the Qur’an")
st.write("Below is a list of select words and how many times they appear in the Qur’an:")

st.table(word_counts)

# Section 2: Bar Chart
st.subheader("📈 Frequency Comparison")

fig, ax = plt.subplots()
ax.bar(word_counts.keys(), word_counts.values(), color='teal')
plt.xticks(rotation=45, ha='right')
plt.title("Word Frequencies in the Qur’an")
plt.tight_layout()
st.pyplot(fig)

# Section 3: Ratio Analysis
st.subheader("🧮 Ratio Patterns and Miracles")

st.markdown("""
**1. "Qul" vs "Qālū"**  
- Both appear exactly **332 times** — a perfect dialogue symmetry.

**2. "Angels" vs "Devil"**  
- *Malāʾikah* (Angels): 88 times  
- *Shayṭān* (Devil): 88 times  
- Symbolizing the constant balance in moral struggle.

**3. "Life" vs "Death"**  
- *Ḥayāh* (Life): 145 times  
- *Mawt* (Death): 145 times  
- A reflection of divine balance between birth and end.

**4. "World" vs "Hereafter"**  
- *Dunyā*: 115 times  
- *Ākhirah*: 115 times  
- Emphasizing the equal significance of this life and the next.

**5. "Sea" vs "Land"**  
- *Sea* is mentioned **32 times**  
- *Land* is mentioned **13 times**  
- Total = 45  
- Sea ratio = 32/45 ≈ **71.11%**  
- Land ratio = 13/45 ≈ **28.89%**

This matches the actual **Earth surface composition**: ~**71% water** and **29% land** — a stunning alignment with science.
""")

# Section 4: Pie Chart for Sea vs Land
st.subheader("🌍 Earth’s Surface Ratio in the Qur’an")

labels = ['Sea (32)', 'Land (13)']
sizes = [32, 13]
colors = ['#3399ff', '#99cc66']
explode = (0.1, 0)

fig2, ax2 = plt.subplots()
ax2.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)
ax2.axis('equal')
st.pyplot(fig2)

st.info("🌊 The Qur’an’s mention of ‘Sea’ and ‘Land’ aligns with Earth’s actual surface ratio — something not measurable by humans in the 7th century.")

# Footer
st.caption("✨ Built to reflect the perfect balance of the Divine Word.")
