import streamlit as st
import Langchain_helper

st.set_page_config(
    page_title = "2026 Restaurant Generator",
    page_icon = "🍴",
    layout="centered"
)
st.title(" AI Restaurant Idea Generator")
st.markdown("""
            Select a cuisine from the sidebar, and our AI will dream up a **unique restaurant name** and a **signature menu** for you!
            """)

st.sidebar.markdown("🍽️")
st.sidebar.title("Configuration")

cuisine = st.sidebar.selectbox(
    "Choose a Cuisine",
    ("Indian", "Mexican", "American", "Russian", "Italian","South Indian", "Arabic")
)
if cuisine:
    with st.spinner(f" Chef Sushant is creating {cuisine} ideas..."):
        try:
            response = Langchain_helper.generate_restaurant_name_and_items(cuisine)
            st.divider()
            st.markdown(f"### Recommended Name:")
            st.success(f"** {response['restaurant_name']}**")

            st.markdown(f"### Signature Menu:")
            menu_items=response[ "menu_items" ].split(",")

            for item in menu_items:
                st.write(f" {item.strip()}")
            
        except Exception as e:
            st.error("Something went wrong. Please check your API key or model setting.")
            st.exception(e)
