import streamlit as st
from streamlit_option_menu import option_menu

selected_page = option_menu(
        menu_title="Significance of Creatures discussed in the Quran",
        options=["🐝 Wahi to Bee", "🐜 Ant", "🕷️ Spider in the Quran"],
        icons=["droplet-half", "bug", "shield-exclamation"],
        menu_icon="book",
        default_index=0,
        orientation="horizontal",
    )

if selected_page == "🐝 Wahi to Bee":
    st.title("🐝 The Bee in the Qur'an and Hadith")
    st.markdown("""
    Honey Bees are discussed in the 16th surah of the Quran: **Surah An-Nahl (The Bee)**.

    What Quran mentions about the bee is really honoring it.
    """)

    st.image("images/biological/wahi_to_bee.png")
    
    st.markdown("In this ayah, it is indicated that it is a special command of Allah for bees to make hives, in mountains, houses, and trees.")
    
    st.image("images/biological/shifa_for_people.png")

    st.markdown("""
    And the special thing about this is that there is healing for people in their drink, which means a bee is beneficial to the people by Allah's command.
    
    The last part of Ayah indicates that in this there is a sign for people who think.

    #### Now what signs the world has found till now.

    In a hadith of Prophet SAW, he said : 

    > **"By the One in whose hand is the soul of Muhammad, the believer is like a bee which eats that which is pure and wholesome and lays that which is pure and wholesome. When it lands on something, it does not break or ruin it."**

    The Prophet of Allah swears by his soul ﷺ. So, there is a great thing going on with this hadith, and things mentioned in this hadith.

    That *eats pure*, means that a believer earns halal, and avoids haram. It has two meanings:

    - He doesn't earn money by deceiving or exploiting someone.
    - What he eats is useful for himself and others because it is made halal and beneficial by Allah.

    The next part of hadith is about the results of halal and pure, which is also pure, and beneficial for people:

    - He always benefits others.
    - He wants similar for others as he wants for himself.

    The last part is:

    - He is not harmful to the people around him.
    - He deals with people with kindness, love, and compassion.
    - When he gains victory, he chooses mercy over vengeance if it benefits society.
    """)

elif selected_page == "🐜 Ant":
    st.title("🐜 The Ant in the Qur'an")
    st.markdown("""
    **Surah An-Naml (27:18–19)** narrates the famous story of Prophet Sulaiman (AS) and the ants:

    > **"Until, when they came upon the valley of the ants, an ant said, 'O ants, enter your dwellings that you not be crushed by Solomon and his soldiers while they perceive not.'"**

    """)
    
    st.image("images/biological/ants_valley.png")

    st.markdown("""
    This verse reflects the following:

    - Ants live in **organized societies**.
    - They **communicate** and **warn** each other.
    - The use of the female form in Arabic for the speaking ant aligns with modern science — **the worker ants are all female**.
    
    🧠 **Scientific Note:**
    Ants demonstrate highly structured communities, division of labor, communication, and cooperation — signs of intelligent design and communal order.
    """)

elif selected_page == "🕷️ Spider in the Quran":
    st.title("🕷️ The Spider in the Qur'an")
    st.markdown("""
    #### Fragile home of Spider
    **Surah Al-Ankabut (29:41)** mentions the spider:

    > **"The example of those who take protectors other than Allah is like that of the spider who builds a house; and indeed, the weakest of houses is the spider’s house – if they only knew."**
    """)

    st.image("images/biological/ankaboot.png")
    
    st.markdown("""
                🕸️ This verse compares false reliance with the fragility of a spider's web.

    🔬 **Scientific Discovery:**
    - The **spider’s web**, though strong relative to its size, is **structurally fragile as a home**.
    - **Female spiders** often expel or consume males after mating, showing social instability — a hidden wisdom in the verse’s symbolic depth.

    💡 **Reflection:**
    Trusting in anything other than Allah is like relying on a spider's web — fragile, deceptive, and unsupportive.
    """)
