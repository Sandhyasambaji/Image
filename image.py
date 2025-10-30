import streamlit as st

tab1, tab2, tab3 = st.tabs(["Home", "About", "Contact"])

col1, col2, col3 = st.columns(3)

# --- FLOWERS SECTION ---
with col1:
    st.header("Flowers")
    with st.expander("Beautiful Flowers"):
        img_col1, img_col2 = st.columns(2)
        with img_col1:
            st.image("http://getwallpapers.com/wallpaper/full/5/f/b/967407-gorgerous-beautiful-flowers-wallpaper-1920x1080-ipad-pro.jpg", width=150)
        with img_col2:
            st.image("https://tse4.mm.bing.net/th/id/OIP.ZFLxuj_j5RVmO658GvMsEwHaFi?pid=Api&P=0&h=180", width=150)

# --- ANIMALS SECTION ---
with col2:
    st.header("Animals")
    with st.expander("Cute Animals"):
        img_col1, img_col2 = st.columns(2)
        with img_col1:
            st.image("https://tse4.mm.bing.net/th/id/OIP.Jlh-TlckEek5sqlqHcalLQHaE8?pid=Api&P=0&h=180", width=150)
        with img_col2:
            st.image("https://tse4.mm.bing.net/th/id/OIP.3J2q-ML2eSU3xPhgV4ez0AHaE8?pid=Api&P=0&h=180", width=150)

# --- SPACE SECTION ---
with col3:
    st.header("Space")
    with st.expander("Amazing Space Images"):
        img_col1, img_col2 = st.columns(2)
        with img_col1:
            st.image("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa", width=150)
        with img_col2:
            st.image("https://images.unsplash.com/photo-1462331940025-496dfbfc7564", width=150)
