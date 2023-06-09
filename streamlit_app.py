import streamlit as st
from streamlit_chat import message as st_message
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from translate import Translator
import nltk

nltk.download('punkt')
from nltk.tokenize import word_tokenize


# Function to load tokenizer and model from cache or download
@st.cache_resource
def get_models():
    model_name = 'facebook/blenderbot-400M-distill'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model


# Initialize chat history if it doesn't exist in session state
if 'history' not in st.session_state:
    st.session_state.history = []

# Set page configuration for the Streamlit app
st.set_page_config(page_title='Tagalog Chatbot', page_icon='🤖')
st.title('Tagalog Chatbot')

# Translator for English to Tagalog (Filipino) and vice versa
translator_en = Translator(from_lang='tl', to_lang='en')
translator_tl = Translator(from_lang='en', to_lang='tl')

foul_words = [
    'amputa', 'animal', 'bayag', 'betlog', 'bilat',
    'binibrocha', 'bobo', 'bogo', 'boto', 'brocha',
    'buang', 'burat', 'bwesit', 'bwisit', 'chupa',
    'demonyo', 'deputa', 'engot', 'etits', 'gaga',
    'gagi', 'gago', 'habal', 'hayup', 'hinampak',
    'hinayupak', 'hindot', 'hindutan', 'hudas', 'hindut',
    'hjakol', 'inutel', 'inutil', 'iyot', 'jakol',
    'kagaguhan', 'kagang', 'kantot', 'kantotan', 'kantut',
    'kantutan', 'kaululan', 'kayat', 'kiki', 'kikinginamo',
    'kingina', 'kupal', 'leche', 'leching', 'lechugas',
    'letse', 'lintik', 'nakakaburat', 'nimal', 'ogag',
    'olok', 'pakingshet', 'pakshet', 'pakyu', 'pekpek',
    'pek pek', 'pesteng yawa', 'pisteng yawa', 'poke', 'poki',
    'pokpok', 'pota', 'potang ina', 'potangina', 'puchanggala',
    'puchangina', 'puke', 'puki', 'pukinangina', 'puking',
    'punyeta', 'puta', 'putang ina', 'putang', 'putangina',
    'putanginamo', 'putaragis', 'putragis', 'puyet', 'ratbu',
    'salsal', 'shet', 'shunga', 'sira ulo', 'siraulo',
    'suso', 'susu', 'syet', 'tae', 'taena',
    'tamod', 'tang ina', 'tanga', 'tangina', 'taragis',
    'tarantado', 'tete', 'teti', 'timang', 'tinil',
    'tite', 'titi', 'tubol', 'tungaw', 'ulol',
    'ulul', 'ungas', 'utong', 'yawa']


# Function to filter out foul words
def filter_sentence(sentence):
    # Tokenize the sentence into individual words
    words = word_tokenize(sentence)

    # Initialize an empty list to store the filtered words
    filtered_words = []

    # Iterate over each word in the tokenized sentence
    index = 0
    while index < len(words):
        word = words[index]

        # Check if the word is in the foul words list
        if word.lower() in foul_words:
            # If the word is a bad word, replace it with asterisks of the same length
            filtered_words.append('*' * len(word))
        else:
            # If the word is not a bad word, keep it as it is
            filtered_words.append(word)

        # Check if the next word forms a phrase with a foul word
        next_index = index + 1
        if next_index < len(words):
            next_word = words[next_index]
            phrase = f"{word.lower()} {next_word.lower()}"
            if phrase in foul_words:
                filtered_words[-1] = '*' * len(phrase)
                index += 1

        index += 1

    # Join the filtered words back into a sentence
    filtered_sentence = ' '.join(filtered_words)

    return filtered_sentence


# Function to generate the chatbot's response
def generate_response(max_length=2048):
    tokenizer, model = get_models()
    user_message = st.session_state.input_text

    # Clear the input field after user submits a message
    st.session_state.input_text = ''

    # Translate user's message from Tagalog to English
    translation_en = translator_en.translate(user_message)

    # Encode translated message using the tokenizer
    inputs = tokenizer.encode(translation_en, return_tensors='pt')

    # Generate the chatbot's response
    result = model.generate(inputs, max_length=len(inputs[0]) + max_length, do_sample=False)
    message_bot = tokenizer.decode(result[0], skip_special_tokens=True)

    # Translate the response back to Tagalog
    translation_tl = translator_tl.translate(message_bot)

    filtered_sentence = filter_sentence(user_message)

    # Append user's message and chatbot's response to the chat history
    st.session_state.history.append({'message': filtered_sentence, 'is_user': True})
    st.session_state.history.append({'message': translation_tl, 'is_user': False})


# Display the chat history using streamlit_chat message component
for i, chat in enumerate(st.session_state.history):
    st_message(**chat, key=str(i))

# Add an empty space to create some separation
st.empty()

# Text input field for user interaction
input_placeholder = st.empty()
input_text = input_placeholder.text_input('Kausapin mo ako 😊', key='input_text', on_change=generate_response)

# Move the input field to the bottom by adding some vertical space
st.empty()
