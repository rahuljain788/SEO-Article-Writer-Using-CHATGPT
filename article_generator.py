import streamlit as st
import openai

openai.api_key = "Key"

st.title("SEO Article Writer With CHATGPT")


def generate_article(word, writing_style, word_count):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [
            {'role':'user', 'content':f'Write an SEO optimized word article about {word}'},
            {'role':'user', 'content':f'This article should be in style {writing_style}'},
            {'role': 'user', 'content': f'The article lenght should be {word_count}'}
        ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content

    print(result)
    return result


keyword = st.text_input("Enter a Keyword")
writing_style = st.selectbox("Select a writing style", ["Funny", "Sarcastic", "Academic"])
word_count = st.slider("Select the word count", min_value=300, max_value=100, value=300)
submit_button = st.button("Generate Article")

if submit_button:
    message = st.empty()
    message.text("Generating Article .. ")
    article = generate_article(word=keyword, writing_style=writing_style, word_count=word_count)
    message.text("")
    st.write(article)
    st.download_button(label="Download Article", data=article, file_name="article.txt", mime="text/txt")