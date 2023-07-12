import streamlit as st

st.title("SEO Article Writer With CHATGPT")


def generate_article(keyword, writing_style, word_count):
    return "This is the article without making any API calls"


keyword = st.text_input("Enter a Keyword")
writing_style = st.selectbox("Select a writing style", ["Funny", "Sarcastic", "Academic"])
word_count = st.slider("Select the word count", min_value=300, max_value=100, value=300)
submit_button = st.button("Generate Article")

if submit_button:
    message = st.empty()
    message.text("Generating Article .. ")
    article = generate_article(keyword=keyword, writing_style=writing_style, word_count=word_count)
    message.text("")
    st.write(article)
    st.download_button(label="Download Article", data=article, file_name="article.txt", mime="text/txt")