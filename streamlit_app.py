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
