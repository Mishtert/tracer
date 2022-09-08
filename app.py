import streamlit as st

import meta
import fitz
import requests
from bs4 import BeautifulSoup

from best_seller import get_items
from pharmap_url import get_link_mapped
from summarize import get_summary_app
from utils.results_utils import get_brief, ReadPDFFile, PopulateDict
from utils.utils import load_image_from_local, local_css, pure_comma_separation, remote_css
from examples import CATEGORY_LIST, LINK_LIST, STUDY_LIST, FILE_LIST

with open("bestseller.html", "r") as f:
	html_content = f.read()

# html_content[:500]





def main():
	st.set_page_config(
		page_title="Tracer",
		page_icon="‍👻",
		layout="wide",
		initial_sidebar_state="expanded"
	)
	remote_css("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&family=Poppins:wght@600&display=swap")
	local_css("asset/css/style.css")

	col1, col2 = st.columns([5, 5])
	with col2:
		# st.image(load_image_from_local("asset/images/main_logo.png"), width=300)
		# st.markdown("Discover --> Extract --> Sense --> Decide --> Render", unsafe_allow_html=True)
		st.image(load_image_from_local("asset/images/task_theme.png"), width=500)
		with st.expander("Design & Development", expanded=True):
			st.markdown(meta.SIDEBAR_INFO, unsafe_allow_html=True)

		with st.expander("What does Tracer do?", expanded=True):
			st.markdown(meta.STORY, unsafe_allow_html=True)

		st.markdown(meta.CONCEPT_INFO, unsafe_allow_html=True)
		st.image(load_image_from_local("asset/images/side_bar.png"), width=600)

	with col1:
		st.markdown(meta.HEADER_INFO, unsafe_allow_html=True)

		st.markdown(meta.CHEF_INFO, unsafe_allow_html=True)

		# st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>',
		#          unsafe_allow_html=True)
		#
		# st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>',
		#          unsafe_allow_html=True)

		choose = st.radio("Choose Task", (
		                                  "Get Therapy Area Mapped for Given Disease/s",
		                                  "Generate Summary for Clinical Trials",
		                                  "Generate Financial Brief for given 10-Q file"))

		if choose == 'Get Therapy Area Mapped for Given Disease/s':

			prompts = list(LINK_LIST.keys()) + ["Custom"]
			prompt = st.selectbox(
				'Examples (select from this list)',
				prompts,
				# index=len(prompts) - 1,
				index=0
			)

			if prompt == "Custom":
				prompt_box = ""
			else:
				prompt_box = LINK_LIST[prompt]

			items = st.text_area(
				'Selected Sample Webpage Link: ',
				prompt_box,
			)
			# items = pure_comma_separation(items, return_list=False)
			entered_items = st.empty()
			result_button = st.button('Get Therapy Areas!')

			st.markdown(
				"<hr />",
				unsafe_allow_html=True
			)

			if result_button:
				get_link_mapped(items)

		if choose == 'Generate Summary for Clinical Trials':

			prompts = list(STUDY_LIST.keys()) + ["Custom"]
			prompt = st.selectbox(
				'Examples (select from this list)',
				prompts,
				# index=len(prompts) - 1,
				index=0
			)

			if prompt == "Custom":
				prompt_box = ""
			else:
				prompt_box = STUDY_LIST[prompt]

			items = st.text_area(
				'Selected Sample Study ID (Clinical Trial.Gov): ',
				prompt_box,
			)
			# items = pure_comma_separation(items, return_list=False)
			# st.write(items)
			entered_items = st.empty()
			result_button = st.button('Get Summary!')

			st.markdown(
				"<hr />",
				unsafe_allow_html=True
			)

			if result_button:
				headline_output, summary_output = get_summary_app(items)

				# headline = f"""
				# <p class="story-box font-body">{headline_output}</p>
				# """
				# summary = f"""
				# <p class="story-box font-body">{summary_output}</p>
				# """
				# st.markdown(summary, unsafe_allow_html=True)

				# st.write(headline_output)
				st.write(summary_output)

		if choose == 'Generate Financial Brief for given 10-Q file':

			prompts = list(FILE_LIST.keys()) + ["Custom"]
			prompt = st.selectbox(
				'Examples (select from this list)',
				prompts,
				# index=len(prompts) - 1,
				index=0
			)
			if prompt == "Custom":
				file = st.file_uploader("Choose a file")
				uploaded_file  = open(file, 'rb')
				doc = fitz.open(uploaded_file)
				result_button = st.button('Get Earnings Brief!')

				st.markdown(
					"<hr />",
					unsafe_allow_html=True
				)
				print("before custom result button")
				if result_button and uploaded_file is not None:
					with st.spinner("Generating Brief..."):
						DictText = {}
						Extracttext = ReadPDFFile(doc, 19, "(Dollars in millions except per share amounts)", "")
						DictText = PopulateDict(Extracttext, DictText)
						Extracttext = ReadPDFFile(doc, 20, "Overview (continued)",
						                          "Results may not sum due to rounding")
						DictText = PopulateDict(Extracttext, DictText)
						Extracttext = ReadPDFFile(doc, 21, "(Dollars in millions)", "Three months ended")
						DictText = PopulateDict(Extracttext, DictText)
						# st.write(DictText)
						st.write(get_brief(DictText))

			else:
				prompt_box = FILE_LIST[prompt]

				items = st.text_area(
					'Selected File Name: ',
					prompt_box,
				)
				# items = pure_comma_separation(items, return_list=False)
				# st.write(items)
				entered_items = st.empty()
				result_button = st.button('Get Earnings Brief!')

				st.markdown(
					"<hr />",
					unsafe_allow_html=True
				)

				if result_button:
					uploaded_file = open("asset/data/TF-Q1'22-10Q.pdf", 'rb')
					doc = fitz.open(uploaded_file)
					with st.spinner("Generating Brief..."):
						DictText = {}
						Extracttext = ReadPDFFile(doc, 19, "(Dollars in millions except per share amounts)", "")
						DictText = PopulateDict(Extracttext, DictText)
						Extracttext = ReadPDFFile(doc, 20, "Overview (continued)",
						                          "Results may not sum due to rounding")
						DictText = PopulateDict(Extracttext, DictText)
						Extracttext = ReadPDFFile(doc, 21, "(Dollars in millions)", "Three months ended")
						DictText = PopulateDict(Extracttext, DictText)
						# st.write(DictText)
						st.write(get_brief(DictText))


if __name__ == '__main__':
	main()
