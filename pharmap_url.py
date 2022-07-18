import streamlit as st
import pandas as pd
# import utils.pharmap_utils.layout as lt
from utils.pharmap_utils.batutils import *
# import stanza

import requests
# import os.path
import io
# import PyPDF2
from pypdf.pdf import PdfFileReader
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from bs4.element import Comment

# from utils.pharmap_utils.dtxutils import *
# from utils.pharmap_utils.dictutils import *

from utils.pharmap_utils.stanzautils import *


# @st.cache(show_spinner=True)
def get_ner(contents):
	print('inside get ner')
	content_list = []
	st.write('Reading the page...')
	nlp = call_nlp_pipeline()
	doc = nlp(contents.strip())
	st.write('Getting disease names...')
	for ent in doc.entities:
		if ent.type == 'DISEASE':
			content_list.append(ent.text.replace('\n', ''))
	content_list = list(set(content_list))
	print('got the disease names', content_list)
	st.write('Got the disease names...')
	return content_list


def get_ta_mapped_url(content_list):
	print('inside get_ta_mapped')
	st.write(content_list)
	# content_list = content_list
	st.write('Trying to get Mesh Name..')
	print('Trying to get Mesh Name..')
	ta_list = []
	ta = []
	for condition_text in content_list:
		# print("printing inside the for loop",condition_text)
		ta = non_url_flow(condition_text)
		# print(ta)
		ta_list.append(ta)
	# print(ta_list)
	flat_list = [item for sublist in ta_list for item in sublist]
	ta = list(set(flat_list))
	print("Outside the loop", ta)
	return ta


def check_pdf_html(url):
	r = requests.get(url)
	content_type = r.headers.get('content-type')
	print(content_type)
	if 'application/pdf' in content_type:
		ext = 'pdf'
	elif 'text/html' in content_type:
		ext = 'html'
	else:
		ext = ''
		print('Unknown type: {}'.format(content_type))
	print(ext)
	return ext


# @st.cache
def get_disease_html(u):
	print('inside get disease html')
	# u="https://www.exelixis.com/pipeline/"
	# "https://www.roche.com/dam/jcr:22160102-e04d-4484-ae3b-0f474105647e/en/diaq321.pdf"
	url = Request(u, headers={'User-Agent': 'Mozilla/5.0'})
	html = urlopen(url).read()
	soup = BeautifulSoup(html, features="html.parser")
	for script in soup(["script", "style"]):
		script.extract()
	for footer in soup.findAll('header'):
		footer.decompose()
	for footer in soup.findAll('footer'):
		footer.decompose()
	text = soup.get_text()
	lines = (line.strip() for line in text.splitlines())
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	text = '\n'.join(chunk for chunk in chunks if chunk)
	# st.write(text)
	result = get_ner(text)
	return result


# @st.cache(persist=True,show_spinner=True)
def get_disease_pdf(url):
	st.write('get pdf disease')
	r = requests.get(url)
	f = io.BytesIO(r.content)
	reader = PdfFileReader(f)
	# pnum = reader.getNumPages()
	# p_num = []
	data = []
	df = pd.DataFrame()
	content_list = []
	pnum = 2
	for p in range(pnum):
		contents = reader.getPage(p).extractText()
		content_list = get_ner(contents)
		# doc = nlp(contents.strip())
		# for ent in doc.entities:
		#     if ent.type=='DISEASE':
		#         content_list.append(ent.text.replace('\n',''))
		# content_list = list(set(content_list))
		# print(content_list)
		# p_num = [p+1]
		# print('pagenum',p_num)
		# print('values',content_list)
		a_dictionary = {'pno:': [p + 1],
		                'conditions': content_list
		                }
		content_list = []
		# print('a_dictionary',a_dictionary)
		data.append(a_dictionary)
	f.close()
	df = df.append(data, True)
	return df


def get_link_mapped(url):
		# st.write(url)
		# 	url = 'https://www.gene.com/medical-professionals/pipeline'
			try:
				get = check_pdf_html(url)
			# st.write(get)
			except:
				get = 'invalid URL'
			if get == 'pdf':
				# st.write('inside pdf')
				pdf_mapped_df = get_disease_pdf(url)
				st.dataframe(pdf_mapped_df)
			elif get == 'html':
				# st.write('inside html')
				# st.write(url)
				# print('html')
				content_list = get_disease_html(url)
				ta = get_ta_mapped_url(content_list)
				st.write(ta)

			elif get == 'invalid URL':
				print('invalid')

