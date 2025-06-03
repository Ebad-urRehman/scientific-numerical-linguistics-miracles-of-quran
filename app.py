import streamlit as st

st.set_page_config(page_title="AyatVerse", layout="wide")

# Define App Pages
pages = {
    "Home": [
        st.Page("app_pages/home/00-home.py", title="Home", icon=":material/home:"),
        st.Page("app_pages/home/points_to_consider.py", title="⚠️ Points to Consider"),
        st.Page("app_pages/chatbot.py", title="Chatbot"),
    ],
    "Numerical Miracles": [
        st.Page("app_pages/numerical/intro.py", title="🔢 Intro to Numerical Miracles"),
        st.Page("app_pages/numerical/word_count.py", title="📊 Word Counts & Ratios"),
        # st.Page("app_pages/numerical/huroof.py", title="🧩 Muqattaʿāt Encoding"),
        st.Page("app_pages/numerical/primes.py", title="🧮 Prime Numbers & Patterns"),
        st.Page("app_pages/numerical/num_patterns_describes_content.py", title="📐 Numerical Patterns describes content"),
        st.Page("app_pages/numerical/math_org_prove_and_challenge.py", title="⚖️📖 Challenge of Quran Math Harmony"),
        st.Page("app_pages/numerical/other_numbers.py", title="🔎 Numerical Patterns"),
    ],

    "Biological Miracles": [
    st.Page("app_pages/biological/water_cycle_and_plant_growth.py", title="💧 Water Cycle & Plant Growth"),
    st.Page("app_pages/biological/lessons_from_char_of_animals.py", title="🐾 Lessons from Animal Behavior"),
    st.Page("app_pages/biological/creation_in_pairs.py", title="👥 Creation in Pairs"),
    st.Page("app_pages/biological/embrology.py", title="🧬 Embryology in the Qur'an"),
    st.Page("app_pages/biological/creating_phases_of_humans.py", title="👴 Phases of Human Creation"),
],

"Cosmology & Astronomy": [
    # 🌌 Cosmology & Astronomy
    st.Page("app_pages/physics/cosmology/Allah_and_the_cosmos.py", title="🌌 Allah and the Cosmos"),  # 🌌
    st.Page("app_pages/physics/cosmology/big_bang_and_expansion.py", title="🌌 Big Bang & Expanding Universe"),  # 🌌
    st.Page("app_pages/physics/cosmology/iron_from_space.py", title="🪨🚀 Iron Sent from Space"),  # 🪨🚀
    st.Page("app_pages/physics/cosmology/blackholes_and_portals.py", title="🕳️ Black Holes & Cosmic Portals"), # 🕳️
    st.Page("app_pages/physics/cosmology/knocking_stars_pulsars.py", title="✨ Knocking Stars (Pulsars)"),  # ✨
    st.Page("app_pages/physics/cosmology/seven_heavens.py", title="☁️ Seven Heavens & Orbits"),  # ☁️
    st.Page("app_pages/physics/cosmology/revolving_around_center.py", title="🪐 Single Center"),  # 🪐
    st.Page("app_pages/physics/cosmology/universe_creation_in_pairs.py", title="👥 Creation in Pairs"),  # 👥
],

"Time, Space & Relativity": [
    # 🕰️ Time, Space & Relativity
    st.Page("app_pages/physics/time/mi'raj_and_time_dilation.py", title="🕰️ Mi'raj & Time Dilation"),  # 🕰️
    st.Page("app_pages/physics/time/angels_speed_of_light.py", title="⚡ Angels & Speed of Light"),  # ⚡
],
"Earth & Environmental Physics": [
    # 🌍 Earth & Environmental Physics
    st.Page("app_pages/physics/earths_environment/barrier_between_waters.py", title="🌊 Salt & Fresh Water Barrier"),  # 🌊
    st.Page("app_pages/physics/earths_environment/mountains_as_pegs.py", title="🏔️ Mountains as Pegs"),  # 🏔️
    st.Page("app_pages/physics/earths_environment/earth_shape_rotation.py", title="🌐 Spherical Earth & Rotation"),  # 🌐
],

# "Biological - 👤 Human Physical Miracles": [

#     # 👤 Human Physical Miracles
#     st.Page("app_pages/physics/human/fingerprints_identity.py", title="Fingerprints & Identity"),  # 🧬
#     st.Page("app_pages/physics/human/resurrection_locusts.py", title="Resurrection Like Locusts"),  # 🪳
# ]

    # "Psychological & Historical": [
    #     st.Page("app_pages/psychological/01-patterns.py", title="Psychological Patterns", icon=":material/psychology_alt:"),
    #     st.Page("app_pages/psychological/02-history.py", title="Historical Predictions", icon=":material/history_edu:")
    # ],
    # "Vision & Purpose": [
    #     st.Page("app_pages/home/01-purpose.py", title="Why This App?", icon=":material/visibility:"),
    #     st.Page("app_pages/home/02-mindset.py", title="Building a Muslim Mindset", icon=":material/self_improvement:")
    # ]
}

# Build and run navigation
pg = st.navigation(pages)
pg.run()