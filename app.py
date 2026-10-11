from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="GCC LaunchOS | India GCC Entry Intelligence",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state="collapsed",
)

HTML_PATH = Path(__file__).parent / "index.html"

if not HTML_PATH.exists():
    st.error("Prototype file not found. Make sure index.html is in the same GitHub repository as app.py.")
    st.stop()

html = HTML_PATH.read_text(encoding="utf-8")

# Streamlit embeds HTML in an iframe. The original prototype switches to a
# compact top-navigation layout below 1000px; Streamlit's iframe can report a
# narrower viewport than the visible browser window. Lower that breakpoint so
# the intended desktop left-sidebar layout remains visible on desktop screens.
html = html.replace("@media(max-width:1000px)", "@media(max-width:700px)")

# Embed the self-contained HTML prototype. The prototype's own CSS and JavaScript
# provide its interface; Streamlit is only being used as the hosting shell.
components.html(html, height=1800, scrolling=True)
