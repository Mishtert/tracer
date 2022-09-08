import stanza
import streamlit as st

# @st.cache(suppress_st_warning=True)
def call_nlp_pipeline():
# stanza.download('en', package='mimic', processors={'ner': 'bc5cdr'}, model_dir='/stanmodels')
    nlp = stanza.Pipeline('en', package='mimic', processors={'ner': 'bc5cdr'}, model_dir='./stanmodels')
    return nlp


