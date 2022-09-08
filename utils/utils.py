from PIL import Image
import json
import streamlit as st


def load_image_from_local(image_path, image_resize=None):
	image = Image.open(image_path)

	if isinstance(image_resize, tuple):
		image = image.resize(image_resize)
	return image


# # reading the nct_ta dictionary
# with open('asset/data/input_sentence.json') as f:
# 	data = f.read()
# sample_sentences = json.loads(data)  # load dict
# print(sample_sentences)

def unique_list(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def pure_comma_separation(list_str, return_list=True):
	r = unique_list([item.strip() for item in list_str.lower().split(",") if item.strip()])
	if return_list:
		return r
	return ", ".join(r)



def local_css(css_path):
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def remote_css(css_url):
    st.markdown(f'<link href="{css_url}" rel="stylesheet">', unsafe_allow_html=True)