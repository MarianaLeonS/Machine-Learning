/streamlit_app
    /pages
        __init__.py   # This can be empty; it just marks 'pages' as a Python package directory
        home.py       # This will contain the code for the "Home" page
        learn.py      # This will contain the code for the "Learn" page
        test.py       # This will contain the code for the "Test" page
    streamlit_app.py           # This is the main app file

import streamlit as st
from pages import home, learn, test

PAGES = {
    "Home": home,
    "Learn": learn,
    "Test": test
}

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()
