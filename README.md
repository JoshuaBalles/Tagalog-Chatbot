# Tagalog Chatbot

This is a Python script for a Tagalog Chatbot built using the Streamlit framework and the Hugging Face Transformers library. The chatbot is capable of engaging in conversations with users in Tagalog and providing responses in Tagalog as well.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

-   streamlit
-   transformers
-   translate
-   nltk

You can install these dependencies by running the following command:
`pip install streamlit transformers translate nltk` 

Additionally, download the required NLTK resources by running the following command:
`python -m nltk.downloader punkt` 

## Usage

To run the chatbot, execute the following command:
`streamlit run chatbot.py` 

This will start a Streamlit app and open it in your web browser. The app will display a chat interface where you can interact with the chatbot.

## Features

### Translation

The chatbot utilizes the `translate` library to translate messages between English and Tagalog. It automatically translates user inputs from Tagalog to English before generating a response and translates the chatbot's response from English to Tagalog before displaying it to the user.

### Foul Word Filtering

The script includes a function to filter out foul words from user inputs. The function replaces any detected foul words with asterisks of the same length. The list of foul words can be customized by modifying the `foul_words` variable in the script.

### Chat History

The chatbot keeps track of the conversation history using the Streamlit session state. Each message, whether from the user or the chatbot, is stored in the history and displayed in the chat interface.

## Customization

You can customize the behavior and appearance of the chatbot by modifying the script. Here are some possible customizations:

-   **Model Selection**: The script currently uses the "facebook/blenderbot-400M-distill" model for generating responses. You can change the model by modifying the `model_name` variable in the `get_models` function.
    
-   **Language Translation**: If you want to change the translation languages or use a different translation library, you can modify the translator initialization in the script.
    
-   **Styling**: You can modify the Streamlit app's page title, icon, and other visual aspects by changing the relevant arguments in the `st.set_page_config` function.
    

## License

This script is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Acknowledgements

-   This script utilizes the [Streamlit](https://streamlit.io/) framework for building the user interface.
-   It also uses the [Hugging Face Transformers](https://huggingface.co/transformers/) library for language translation and sequence-to-sequence modeling.
-   The foul word filtering functionality is implemented using the [NLTK](https://www.nltk.org/) library for natural language processing.

## Disclaimer

Please note that the foul word filtering functionality in this chatbot is not foolproof and may not catch all offensive language. It is recommended to use additional moderation mechanisms to ensure a safe and respectful environment.
