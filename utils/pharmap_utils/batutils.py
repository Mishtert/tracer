from utils.pharmap_utils.dtxutils import *
from utils.pharmap_utils.dictutils import *
import streamlit as st

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def flow(c_text, ct_text):
    # print('inside flow function')
    if c_text:
        # print('if 1')
        c_text = c_text.lower().strip()
        c_text = remove_stopwords(replace_text(split_values(c_text)))
        c_text = gb_2_us(c_text, gb_2_us_dict)
        c_text = fix_text_with_dict(c_text,repl_dict)
        mesh_term_list = c_text.split(',')
        l2_map = type_extract(mesh_term_list)
        if l2_map:
            ta_map = list(set(map(mesh_to_ta_dict.get, l2_map)))
            # print(ta_map)
            return ta_map
    if ct_text:
        # print(ct_text)
        # print("inside first ct if")
        ct_text = ct_text.lower().strip()
        ct_text = remove_stopwords(replace_text(split_values(ct_text)))
        ct_text = gb_2_us(ct_text,gb_2_us_dict)
        # print("ct text before dict replacement:",ct_text)
        ct_text = fix_text_with_dict(ct_text,repl_dict)
        # print("ct text after dict replacement:",ct_text)
        mesh_term_list = ct_text.split(',')
        # print(mesh_term_list)
        l2_map = type_extract(mesh_term_list)
        if l2_map:
            ta_map = list(set(map(mesh_to_ta_dict.get, l2_map)))
            # print(ta_map)
            return ta_map
        if not ct_text:
            # print(ct_text)
            # print("inside second ct if")
            ct_text = ct_text.lower().strip()
            ct_text = remove_stopwords(replace_text(split_values(ct_text)))
            ct_text = gb_2_us(ct_text,gb_2_us_dict)
            ct_text = fix_text_with_dict(ct_text,repl_dict)
            # print("ct text after dict replacement:",ct_text)
            mesh_term_list = ct_text.split(', ')
            l2_map = type_extract(mesh_term_list)
            if l2_map:
                ta_map = list(set(map(mesh_to_ta_dict.get, l2_map)))
                # print(ta_map)
                return ta_map
        if not ct_text:
            ct_text = ct_text.lower().strip()
            ct_text = remove_stopwords(replace_text(split_values(ct_text)))
            ct_text = gb_2_us(ct_text,gb_2_us_dict)
            # print("ct text before dict replacement:",ct_text)
            ct_text = fix_text_with_dict(ct_text,repl_dict)
            # print("ct text after dict replacement:",ct_text)
            mesh_term_list = ct_text.split('/')
            # print(ct_text)
            l2_map = type_extract(mesh_term_list)
            if l2_map:
                ta_map = list(set(map(mesh_to_ta_dict.get, l2_map)))
                # print(ta_map)
                return ta_map
        if not ct_text:
            # print("inside second elif for ct text")
            ct_text = ct_text.lower().strip()
            ct_text = remove_stopwords(replace_text(split_values(ct_text)))
            ct_text = gb_2_us(ct_text,gb_2_us_dict)
            # print("ct text before dict replacement:",ct_text)
            ct_text = fix_text_with_dict(ct_text,repl_dict)
            # print("ct text after dict replacement:",ct_text)
            mesh_term_list = ct_text.split('./')
            # print(mesh_term_list)
            l2_map = type_extract(mesh_term_list)
            if l2_map:
                ta_map = list(set(map(mesh_to_ta_dict.get, l2_map)))
                # print(ta_map)
                return ta_map
        if not ct_text:
            # print("inside second elif for ct text")
            ct_text = ct_text.lower().strip()
            ct_text = remove_stopwords(replace_text(split_values(ct_text)))
            ct_text = gb_2_us(ct_text,gb_2_us_dict)
            # print("ct text before dict replacement:",ct_text)
            ct_text = fix_text_with_dict(ct_text,repl_dict)
            # print("ct text after dict replacement:",ct_text)
            mesh_term_list = ct_text.split(',')
            # print(mesh_term_list)
            l2_map = type_extract(mesh_term_list)
            if l2_map:
                ta_map = list(set(map(mesh_to_ta_dict.get, l2_map)))
                # print(ta_map)
                return ta_map
        if not ct_text:
            # print("inside second elif for ct text")
            ct_text = ct_text.lower().strip()
            ct_text = remove_stopwords(replace_text(split_values(ct_text)))
            ct_text = gb_2_us(ct_text,gb_2_us_dict)
            ct_text = ''.join(ct_text.split(','))
            ct_text = ''.join(ct_text.split('.'))
            # print("ct text before dict replacement:",ct_text)
            ct_text = fix_text_with_dict(ct_text,repl_dict)
            # print("ct text after dict replacement:",ct_text)
            mesh_term_list = ct_text.split(' ,')
            # print(mesh_term_list)
            l2_map = type_extract(mesh_term_list)
            if l2_map:
                ta_map = list(set(map(mesh_to_ta_dict.get, l2_map)))
                # print(ta_map)
                return ta_map
        # if not c_text:
        #     # print("inside second elif for ct text")
        #     c_text = c_text.lower().strip()
        #     c_text = remove_stopwords(replace_text(split_values(c_text)))
        #     c_text = gb_2_us(c_text,gb_2_us_dict)
        #     c_text = ''.join(c_text.split(','))
        #     c_text = ''.join(c_text.split('.'))
        #     # print("ct text before dict replacement:",c_text)
        #     c_text = fix_text_with_dict(c_text,repl_dict)
        #     # print("ct text after dict replacement:",c_text)
        #     mesh_term_list = c_text.split(' ,')
        #     # print(mesh_term_list)
        #     l2_map = type_extract(mesh_term_list)
        #     if l2_map:
        #         ta_map = list(set(map(mesh_to_ta_dict.get, l2_map)))
        #         # print(ta_map)
        #         return ta_map
        if not c_text:
            # print("inside second elif for ct text")
            c_text = c_text.lower().strip()
            c_text = remove_stopwords(replace_text(split_values(c_text)))
            c_text = gb_2_us(c_text,gb_2_us_dict)
            # print("ct text before dict replacement:",c_text)
            c_text = fix_text_with_dict(c_text,repl_dict)
            # print("ct text after dict replacement:",c_text)
            mesh_term_list = c_text.split(' ')
            # print(mesh_term_list)' ,'
            l2_map = type_extract(mesh_term_list)
            if l2_map:
                ta_map = list(set(map(mesh_to_ta_dict.get, l2_map)))
                # print(ta_map)
                return ta_map
        if not ct_text:
            # print("inside second elif for ct text")
            ct_text = ct_text.lower().strip()
            ct_text = remove_stopwords(replace_text(split_values(ct_text)))
            ct_text = gb_2_us(ct_text,gb_2_us_dict)
            # print("ct text before dict replacement:",ct_text)
            ct_text = fix_text_with_dict(ct_text,repl_dict)
            # print("ct text after dict replacement:",ct_text)
            mesh_term_list = ct_text.split(' ')
            # print(mesh_term_list)' ,'
            l2_map = type_extract(mesh_term_list)
            if l2_map:
                ta_map = list(set(map(mesh_to_ta_dict.get, l2_map)))
                # print(ta_map)
                return ta_map
        
    return []

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def non_url_flow(ct_text):
    if ct_text:
        # print('inside non_url_flow')
        # print("inside first ct if")
        ct_text = ct_text.lower().strip()
        ct_text = remove_stopwords(replace_text(split_values(ct_text)))
        ct_text = gb_2_us(ct_text,gb_2_us_dict)
        # print("ct text before dict replacement:",ct_text)
        ct_text = fix_text_with_dict(ct_text,repl_dict)
        # print("ct text after dict replacement:",ct_text)
        mesh_term_list = ct_text.split(',')
        # print(mesh_term_list)
        l2_map = type_extract(mesh_term_list)
        if l2_map:
            ta_map = list(set(map(mesh_to_ta_dict.get, l2_map)))
            print(ta_map)
            return ta_map
        if not ct_text:
            # print(ct_text)
            # print("inside second ct if")
            ct_text = ct_text.lower().strip()
            ct_text = remove_stopwords(replace_text(split_values(ct_text)))
            ct_text = gb_2_us(ct_text,gb_2_us_dict)
            ct_text = fix_text_with_dict(ct_text,repl_dict)
            # print("ct text after dict replacement:",ct_text)
            mesh_term_list = ct_text.split(', ')
            l2_map = type_extract(mesh_term_list)
            if l2_map:
                ta_map = list(set(map(mesh_to_ta_dict.get, l2_map)))
                # print(ta_map)
                return ta_map
        if not ct_text:
            # print("inside third ct if")
            ct_text = ct_text.lower().strip()
            ct_text = remove_stopwords(replace_text(split_values(ct_text)))
            ct_text = gb_2_us(ct_text,gb_2_us_dict)
            # print("ct text before dict replacement:",ct_text)
            ct_text = fix_text_with_dict(ct_text,repl_dict)
            # print("ct text after dict replacement:",ct_text)
            mesh_term_list = ct_text.split('/')
            # print(ct_text)
            l2_map = type_extract(mesh_term_list)
            if l2_map:
                ta_map = list(set(map(mesh_to_ta_dict.get, l2_map)))
                # print(ta_map)
                return ta_map
        if not ct_text:
            # print("inside fourth if for ct text")
            ct_text = ct_text.lower().strip()
            ct_text = remove_stopwords(replace_text(split_values(ct_text)))
            ct_text = gb_2_us(ct_text,gb_2_us_dict)
            # print("ct text before dict replacement:",ct_text)
            ct_text = fix_text_with_dict(ct_text,repl_dict)
            # print("ct text after dict replacement:",ct_text)
            mesh_term_list = ct_text.split('./')
            # print(mesh_term_list)
            l2_map = type_extract(mesh_term_list)
            if l2_map:
                ta_map = list(set(map(mesh_to_ta_dict.get, l2_map)))
                # print(ta_map)
                return ta_map
        if not ct_text:
            # print("inside fifth if for ct text")
            ct_text = ct_text.lower().strip()
            ct_text = remove_stopwords(replace_text(split_values(ct_text)))
            ct_text = gb_2_us(ct_text,gb_2_us_dict)
            # print("ct text before dict replacement:",ct_text)
            ct_text = fix_text_with_dict(ct_text,repl_dict)
            # print("ct text after dict replacement:",ct_text)
            mesh_term_list = ct_text.split(',')
            # print(mesh_term_list)
            l2_map = type_extract(mesh_term_list)
            if l2_map:
                ta_map = list(set(map(mesh_to_ta_dict.get, l2_map)))
                # print(ta_map)
                return ta_map
        if not ct_text:
            # print("inside sixth elif for ct text")
            ct_text = ct_text.lower().strip()
            ct_text = remove_stopwords(replace_text(split_values(ct_text)))
            ct_text = gb_2_us(ct_text,gb_2_us_dict)
            ct_text = ''.join(ct_text.split(','))
            ct_text = ''.join(ct_text.split('.'))
            # print("ct text before dict replacement:",ct_text)
            ct_text = fix_text_with_dict(ct_text,repl_dict)
            # print("ct text after dict replacement:",ct_text)
            mesh_term_list = ct_text.split(' ,')
            # print(mesh_term_list)
            l2_map = type_extract(mesh_term_list)
            if l2_map:
                ta_map = list(set(map(mesh_to_ta_dict.get, l2_map)))
                # print(ta_map)
                return ta_map
        if not ct_text:
            # print("inside seventh if for ct text")
            ct_text = ct_text.lower().strip()
            ct_text = remove_stopwords(replace_text(split_values(ct_text)))
            ct_text = gb_2_us(ct_text,gb_2_us_dict)
            # print("ct text before dict replacement:",ct_text)
            ct_text = fix_text_with_dict(ct_text,repl_dict)
            # print("ct text after dict replacement:",ct_text)
            mesh_term_list = ct_text.split(' ')
            # print(mesh_term_list)' ,'
            l2_map = type_extract(mesh_term_list)
            if l2_map:
                ta_map = list(set(map(mesh_to_ta_dict.get, l2_map)))
                print(ta_map)
                return ta_map
        
    return []