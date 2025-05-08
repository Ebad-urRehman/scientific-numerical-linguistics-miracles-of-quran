import streamlit as st
from streamlit_option_menu import option_menu

from other_pages.home import display_home
from other_pages.linguistic_miracles import display_linguistic_miracles
from other_pages.numerical_patterns import display_numerical_miracles
from other_pages.scientific_miracles import display_scientific_miracles
from other_pages.subtleties import display_interesting_subtleties

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
            "Interesting Subtleties",
            "Discover New Patterns"
        ],
        icons=["house", "microscope", "chat-text", "123", "lightbulb", "search"],
        menu_icon="cast",
        default_index=0
    )

# Pages
if selected == "Home":
    display_home()  

elif selected == "Scientific Miracles":
    display_scientific_miracles()

elif selected == "Linguistic Miracles":
    display_linguistic_miracles()

elif selected == "Numerical Patterns":
    display_numerical_miracles()

elif selected == "Interesting Subtleties":
    display_interesting_subtleties()

elif selected == "Discover New Patterns":
    st.header("🔍 Discover New Patterns (Coming Soon)")
    st.markdown("""
    Planned tools:
    - Arabic NLP to analyze roots, frequency, and positions
    - Pattern mining and symmetrical phrase detection
    - Community-sourced discoveries
    """)
