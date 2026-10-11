from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="GCC LaunchOS | India GCC Entry Intelligence",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit's default page gutters so the embedded product can use the
# available browser width instead of sitting inside a narrow centered column.
st.markdown(
    """
    <style>
      [data-testid="stAppViewContainer"] { overflow-x: hidden; }
      [data-testid="stMainBlockContainer"] {
        max-width: 100% !important;
        width: 100% !important;
        padding: 0 !important;
      }
      /* Hide Streamlit's host toolbar so its Share/star/edit/GitHub icons do not
         overlap the embedded GCC LaunchOS interface. */
      [data-testid="stHeader"],
      [data-testid="stToolbar"],
      [data-testid="stDecoration"],
      [data-testid="stStatusWidget"],
      #MainMenu,
      footer { visibility: hidden !important; height: 0 !important; display: none !important; }
      iframe[title="streamlit.components.v1.html"] {
        display: block;
        width: 100% !important;
        border: 0 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_PATH = Path(__file__).parent / "index.html"
if not HTML_PATH.exists():
    st.error("Prototype file not found. Ensure index.html is in the same repository folder as app.py.")
    st.stop()

html = HTML_PATH.read_text(encoding="utf-8")

# Make the actual product fill the available viewport. The original HTML's
# 1450px content cap and centered margins made it appear undersized in Streamlit.
html = html.replace("max-width:1450px;margin:auto", "max-width:none;width:100%;margin:0")
html = html.replace("@media(max-width:1000px)", "@media(max-width:700px)")
html = html.replace("body{margin:0;", "html,body{width:100%;min-height:100%;margin:0;padding:0}body{margin:0;")
html = html.replace(".app{display:grid;grid-template-columns:245px 1fr;min-height:100vh}", ".app{display:grid;grid-template-columns:245px minmax(0,1fr);width:100%;min-height:100vh}")

# Extra height keeps longer pages scrollable inside the embedded app.
components.html(html, height=2400, scrolling=True)
