from utils.pharmap_utils.meshutils import nct_to_mesh_term, mesh_term_to_id, df_mesh, df_mesh_ct
from utils.pharmap_utils.cid import CaseInsensitiveDict
from utils.pharmap_utils.dictutils import *
import re
import streamlit as st


# mesh list extract
def meshtrm_lst_xtract(nct_value):
	try:
		mesh_term = nct_to_mesh_term[nct_value]
		mesh_term_list = list(mesh_term)
		return mesh_term_list
	except:
		pass


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
# type extract fun
def type_extract(mesh_term_list):
	mesh_term_list = [mesh_term_list] if isinstance(mesh_term_list, str) else mesh_term_list
	# print('mesh_term_list: ',mesh_term_list)

	# l2_map_lst=[]
	uid_lst = []
	if mesh_term_list is not None:
		for val in mesh_term_list:
			# print('value inside uid forloop:',val)
			try:
				# print('Inside get uid')
				uid = mesh_term_to_id[val]
				uid_lst.append(uid)
				# print(uid_lst)
				if uid_lst is None:
					uid_lst = []
			except:
				pass
				# print('error in get uid list')

				# get mesh num
		mesh_num_xtract_lst = []

		for val in uid_lst:
			try:
				# print('Inside get mesh num')
				mesh_num_xtract = df_mesh.loc[df_mesh['ui'] == val, 'mesh_number'].iloc[0]
				mesh_num_xtract_lst.append(mesh_num_xtract)
				# print(mesh_num_xtract_lst)
				if ',' in mesh_num_xtract_lst[0]:
					mesh_num_xtract_lst = mesh_num_xtract_lst[0].split(", ")
					# print('mesh_num_xtract_lst after spltting',mesh_num_xtract_lst)
			except:
				pass
				# print('error in get mesh num')

		# mesh number extract l2
		l2_map_lst = []
		for val in mesh_num_xtract_lst:
			# print('Inside l2map for loop',val)
			search_value = val[:3]
			# print('printing search value:',search_value)
			try:
				l2_map = df_mesh.loc[df_mesh['mesh_number'] == search_value, 'name'].iloc[0]
				# print(l2_map)
				l2_map_lst.append(l2_map)
				# print(l2_map_lst)
				if l2_map_lst is None:
					l2_map_lst = []
			except:
				pass

		l2_map_lst = list(set(l2_map_lst))
		# print('finaloutput',l2_map_lst)
		return l2_map_lst


def split_values(col_val):
	# """split words seperated by special characters"""
	# print(col_val)
	if col_val != '':
		char_list = ['|', ',', '/', '.', ';', './', ',/', '/ ', ' /']
		# res = ' '.join([ele for ele in char_list if(ele in col_val)])
		res = [ele for ele in char_list if (ele in col_val)]
		# print('printing string of found char',res)
		colstring = str(col_val)
		f_res = []
		try:
			while len(res) > 0:
				res = res[-1]
				f_res = colstring.split(''.join(res))
				# print(f_res)
				# return f_res
				f_res = [x for x in f_res if x is not None]
				return ', '.join(f_res)
		except:
			pass
		else:
			return col_val


def map_entry_terms(myText):
	obj = CaseInsensitiveDict(entry_dict)
	pattern = re.compile(r'(?<!\w)(' + '|'.join(re.escape(key) for key in obj.keys()) + r')(?!\w)', flags=re.IGNORECASE)
	text = pattern.sub(lambda x: obj[x.group()], myText)
	# text = pattern.sub(lambda x: obj[x.group()], text)
	return text.strip().split('/')


def remove_none(some_list):
	some_list = [some_list] if isinstance(some_list, str) else some_list
	if some_list is not None:
		some_list = list(filter(lambda x: x != None, some_list))
		return some_list


def retain_all_ta(some_list):
	some_list = [some_list] if isinstance(some_list, str) else some_list
	# some_list.split(',')
	value = 'all_ta'
	#   print(value)
	if some_list is not None:
		if value in some_list:
			some_list = [value]
			return some_list
		else:
			return some_list


def unique_list(l):
	l = map(str.strip, l)  # remove whitespace from list element
	# print(l)
	ulist = []
	[ulist.append(x) for x in l if x not in ulist]
	return ulist


def split_for_type_extract(my_list, char):
	# print('entering the function:',my_list)
	try:
		my_list = [my_list] if isinstance(my_list, str) else my_list
		if my_list is not None:
			# print(my_list)
			my_list = list(map(lambda x: x.split(char)[0], my_list))
			# my_list = [x for x in my_list if x is not None]
			return my_list
	except:
		pass


def special_ask(col_value):
	col_value = col_value.lower()
	if col_value == 'obesity':
		ta_list = 'met'
		return ta_list.split()
	elif col_value == 'healthy subject':
		ta_list = 'all_ta'
		return ta_list.split()
	elif col_value == 'healthy subjects':
		ta_list = 'all_ta'
		return ta_list.split()
	elif col_value == 'healthy participants':
		ta_list = 'all_ta'
		return ta_list.split()
	elif col_value == 'healthy participant':
		ta_list = 'all_ta'
		return ta_list.split()
	elif col_value == 'inflammation':
		ta_list = 'ai'
		return ta_list.split()
	else:
		pass


def remove_stopwords(query):
	stopwords = ['acute-on-chronic', 'acute', 'chronic',
	             'diseases of the', '-19', '- 19', '19', '.']
	if query is not None:
		querywords = query.split()
		resultwords = [word for word in querywords if word.lower() not in stopwords]
		result = ' '.join(resultwords)
		return result
	else:
		''


def gb_2_us(text, mydict):
	try:
		for us, gb in mydict.items():
			text = text.replace(gb, us)
			return text
	except:
		return ''


def fix_text_with_dict(text, mydict):
	text = ','.join([repl_dict.get(i, i) for i in text.split(', ')])
	return text


def replace_text(mytext):
	cancer = ['cancer', 'neoplasm', 'carcinoma', 'lymphoma', 'adenoma', 'myoma', 'meningioma',
	          'malignancy', 'tumor', 'malignancies', 'chemotherapy']
	# fracture = ['fractures', 'fracture']
	heart_failure = ['heart failure', 'cardiac']
	ectomy = 'prostatectomy'
	covid = 'covid'
	transplant = 'transplant'
	healthy = 'healthy'
	park = 'parkinson'
	allergy = ['allergy', 'allergic']
	virus = 'virus'
	cornea = ['cornea', 'eye', 'ocular', 'macular']
	vaccine = 'vaccines'
	ureter = 'ureter'
	mutation = 'mutation'
	stemcell = 'stem cells'
	behavior = ['behavior', 'depressive', 'depression', 'anxiety', 'satisfaction', 'grief']
	molar = ['molar', 'dental', 'maxillary']
	diet = 'diet'
	biopsy = 'biopsy'
	physiology = 'physiology'
	infection = ['infection', 'bacteremia', 'fungemia']
	preg = ['pregnancy', 'pregnant', 'labor', 'birth']
	imaging = ['x-ray', 'imaging', 'mri']
	surgery = 'surgery'
	angina = 'angina'
	use_disorder = ['use disorder', 'obsessive', 'panic', 'posttraumatic stress',
	                'post-traumatic stress', 'schizophrenia']

	if mytext:
		try:
			if any(text in mytext.lower() for text in cancer):
				mytext = 'neoplasms'
				return mytext
			if any(text in mytext.lower() for text in heart_failure):
				mytext = 'cardiovascular diseases'
				return mytext
			if covid in mytext.lower():
				mytext = 'covid-19'
				return mytext
			if ectomy in mytext.lower():
				mytext = 'urogenital surgical procedures'
				return mytext
			if transplant in mytext.lower():
				mytext = 'body regions'
				return mytext
			if healthy in mytext.lower():
				mytext = 'healthy volunteers'
				return mytext
			if any(text in mytext.lower() for text in allergy):
				mytext = 'immune system diseases'
				return mytext
			if park in mytext.lower():
				mytext = 'parkinson disease'
				return mytext
			if park in mytext.lower():
				mytext = 'immune system diseases'
				return mytext
			if virus in mytext.lower():
				mytext = 'viruses'
				return mytext
			if any(text in mytext.lower() for text in cornea):
				mytext = 'eye diseases'
				return mytext
			if vaccine in mytext.lower():
				mytext = 'vaccines'
				return mytext
			if ureter in mytext.lower():
				mytext = 'ureter'
				return mytext
			if mutation in mytext.lower():
				mytext = 'mutation'
				return mytext
			if stemcell in mytext.lower():
				mytext = 'stem cells'
				return mytext
			if any(text in mytext.lower() for text in behavior):
				mytext = 'behavior'
				return mytext
			if any(text in mytext.lower() for text in molar):
				mytext = 'molar'
				return mytext
			if diet in mytext.lower():
				mytext = 'diet'
				return mytext
			if biopsy in mytext.lower():
				mytext = 'biopsy'
				return mytext
			if physiology in mytext.lower():
				mytext = 'physiology'
				return mytext
			if any(text in mytext.lower() for text in infection):
				mytext = 'infections'
				return mytext
			if any(text in mytext.lower() for text in preg):
				mytext = 'reproductive and urinary physiological phenomena'
				return mytext
			if any(text in mytext.lower() for text in imaging):
				mytext = 'diagnosis'
				return mytext
			if surgery in mytext.lower():
				mytext = 'medicine'
				return mytext
			if angina in mytext.lower():
				mytext = 'angina pectoris'
				return mytext
			if any(text in mytext.lower() for text in use_disorder):
				mytext = 'mental disorders'
				return mytext
			else:
				return mytext
		except:
			return ''


# For studies in CTgov 
def is_nct(col_value):
	# Returns mesh term list based on NCT ID
	val = col_value[:3]
	if val == 'NCT':
		try:
			if col_value in df_mesh_ct.values:
				mesh_term_list = meshtrm_lst_xtract(col_value)
				l2map = type_extract(mesh_term_list)
				return l2map
		except:
			pass
	else:
		'Study Not in Database, Please enter condition or conditions treated'
	return


# For studies not in CTgov
def is_not_nct(col_value):
	# Returns mesh term list based on NCT ID
	# Returns disease type l2 tag in Mesh dictionary
	if col_value is not None:
		mesh_term_list = col_value
		l2map = type_extract(mesh_term_list)
		return l2map
	else:
		None
	return
