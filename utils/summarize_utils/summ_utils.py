from utils.pharmap_utils.cid import CaseInsensitiveDict
import re



##==============================================================================
#load mapping terms
with open('utils/summarize_utils/map_terms.txt') as f:
  mt_dict = dict(x.rstrip().split(',', 1) for x in f)

##==============================================================================
#load number mapping terms to convert numbers in words appearing before weeks 
# to number 
with open('utils/summarize_utils/map_nums.txt') as f:
  num_dict = dict(x.rstrip().split(',', 1) for x in f)
##==============================================================================
## load stop words
with open('utils/summarize_utils/stopwords-en.txt','r',encoding='unicode_escape') as f:
  stopwords = f.read().split()
##==============================================================================
def get_first_word(alloc,masking,status):
  print('Getting first word..')
  if (alloc.lower()=='n/a' and masking.lower()=='none (open label)'):
    if status == 'Active, not recruiting':
      fw = 'An '
      start_word = 'It is in '
      result = start_word + fw.lower()
      return result
    elif status == 'Recruiting':
      fw = 'An '
      start_word = 'It is in '
      result = start_word + fw.lower()
      return result
    else:
      fw = 'An '
      result = fw
      return result
  else:
    if status == 'Active, not recruiting':
      fw = 'A '
      start_word = 'It is in '
      result = start_word + fw.lower()
      return result
    elif status == 'Recruiting':
      fw = 'A '
      start_word = 'It is in '
      result = start_word + fw.lower()
      return result
    else:
      fw = 'A '
      result = fw
      return result

##==============================================================================
#get masking type
def get_mask(masking):
  print('Getting mask..')
  # print('maskingentry:',masking)
  try:
    if masking.lower() == 'double':
      masking = 'double-blind, '
    elif masking.lower() == 'none (open label)':
      masking = 'open-label, '
    elif masking.lower() in 'quadruple':
      masking = 'quadruple-blind, ' 
    # print('....... ..... done..')  
    return str(masking)
  except:
    pass
##==============================================================================
#get study type
def get_stype(stype):
  print('Getting study type...')
  if stype.lower() == 'interventional':
    stype = 'interventional study '
  else:
    stype = 'observational study '
  # print('....... ....... done..')
  return stype  
##==============================================================================
# get intervention model
def get_imodel(imodel):
  print('Getting imodel...')
  if imodel.lower() is not None:
    res = imodel.lower() + ', '
    return res
  else:
    pass  
##==============================================================================
#get objective
def get_obj(otitle,bsumm, ddesc):
  print('Getting objective for..')
  # print(string)
  # keywords = ['purpose','objective','evaluated','aim','assess','pharmcokinetic',
  #             'pharmacodynamic','safety','immunogenecity']'Study to Evaluate'
  keywords = ['to Demonstrate', 
              'to Evaluate',
              'to Investigate',
              'to Assess',
              'to Determine',
              # 'Investigating',
              'Placebo','Purpose','aim','purpose','main purpose',
              'Aim','Objective', 'objective', 'Main Objective', 'Selection Study',
              'Main Purpose', 'Main Aim','Study', 'STUDY', 'study',
              'Ascending Multiple-dose','Adaptive','Dose Escalation',
              'assess', 'Bioavailability','investigate','Investigating'
              ]

  otitle_result = [ele for ele in keywords if(ele in otitle)]
  print('otitle_result:', otitle_result)
  bsumm_result = [ele for ele in keywords if(ele in bsumm.lower())]
  print('bsumm_result:', bsumm_result)
  ddesc_result = [ele for ele in keywords if(ele in ddesc.lower())]
  print('ddesc_result:',ddesc_result)
  # print(otitle_result)
  try:
    if len(otitle_result)>0:
      print('im in otitle')
      word = ''.join(otitle_result[0])
      print('word in otitle:', word)
      matched = [sentence + '.' for sentence in otitle.split('. ') if word in sentence]
      sobj = ''.join(matched)
      print('matched sobj',sobj)
      # result = re.sub(r'^.*?to', 'to', sobj)
      pattern=word+'(.*)'+'.'
      result = re.search(pattern, sobj)
      print('result of pattern search:',result)
      result = word+result.group(1)
      print('result group:',result)
      result = non_abbr(result)
      print('non-abbr result:',result)
      return result
    elif len(bsumm_result)>0:
      print('im in bsumm')
      # print(bsumm_result)
      word = ''.join(bsumm_result[0])
      # print(word)
      matched = [sentence + '.' for sentence in bsumm.split('. ') if word in sentence]
      sobj = ', '.join(matched)
      sobj = non_abbr(sobj)
      return sobj
    elif len(ddesc_result)>0:
      # print('im in ddesc')
      word = ''.join(ddesc_result[0])
      matched = [sentence + '.' for sentence in ddesc.split('. ') if word in sentence]
      sobj = ''.join(matched)
      sobj = non_abbr(sobj)
      return sobj
    else:
      sobj = 'No Objective Found'
      return sobj
  except:
      pass
  
##==============================================================================
# other study id extract
def get_osid(osid,sid):
  print('Getting Study Ids...')
  if None not in (osid,sid):
    if sid !='':
      osid = '(' + '; '.join(osid.split('|')) + '; '+ ', '.join(sid.split('|')) +') '
      # print('both not none:',osid)
      return osid
    elif osid is not None:
      osid_only = '(' + '; '.join(osid.split('|')) + ') '
      # print('sid is none:',osid_only)
      return osid_only
    elif osid is None and sid is not None:
      sid_only = '(' + '; '.join(sid.split('|')) + ') '
      # print('osid is none:',sid_only)
      # print('....... ....... done..')
      return sid_only
  else:
    pass

##==============================================================================
# get locations
def join_and(items):
  if len(items)>1:
    return ', '.join(items[:-1]) + ', and '+items[-1]
  else:
    return ', '.join(items)
    
def get_locs(locations):
  print('Getting Locations...')
  print(locations)
  print(len(locations))
  if locations !='':
    print('location is not empty')
    if '|' in locations:
      res = join_and(sorted(list(set(locations.split('|')))))
      print('inside location split if:', res)
    else:
      res = locations
      print('inside location split else:', res)
  else:
    res = locations
    print('outside location split else:', res)
  if res =='':
    pass
  else:  
    res = ' in ' + res +', '
  # print('....... ....... done..')
  return res  

##==============================================================================
# status extract
status_dict = {'Not yet recruiting':', is planned ',
              # 'Recruiting':', is active ',
              'Active, not recruiting':' (enrollment complete) ',
              'Completed' :', is complete ',
              'Terminated':', has been terminated',
              'Suspended' :', has been suspended',
              'Withdrawn' :', has been withdrawn'
              }
def get_status(status):
  print('Getting trial type...')
  search_key = status
  # print(search_key)
  try:
    res = [val for key, val in status_dict.items() if search_key in key]
    res = str(res).replace("['",'').replace("']",'')
      # print('....... ....... done..')
    return res
  except:
    pass

##==============================================================================
# lower non abbr word for ystop
def non_abbr(string):
  word = string.split(' ')
  my_list=[]
  try:
    for word in word:
      if word.isupper() == True:
        word = word.upper()
        my_list.append(word)
      else:
        word = word.lower()
        my_list.append(word)
    return ' '.join(my_list)
  except:
    pass
##==============================================================================
# reason for stop extract
def get_ystop(ystop):
  print('Getting ystop...')
  if ystop!='':
    ystop = non_abbr(ystop)
    ystop = ', '+ 'due to ' + ystop
    return ystop
  else:
    pass
##==============================================================================
#get age
def get_age(minage,maxage):
  # print('Getting age...')
  if maxage !='':
    age = 'aged between '+ minage+ ' and ' + maxage
  else:
    age = 'with minimum age of ' +minage
  # print('....... ....... done..')
  return age
##==============================================================================

# get link
def get_url(nctid,lupd):
  print('Cooking up final url...')
  urll='https://clinicaltrials.gov/ct2/show/'
  new_url= ' ('+ 'ClinicalTrials.gov, '+ lupd+', ' +urll+nctid + ')'
  return new_url
##==============================================================================
#map week numbers
def map_week_num(myText):
  obj = CaseInsensitiveDict(num_dict)
  pattern = re.compile(r'(?<!\w)(' + '|'.join(re.escape(key) for key in obj.keys()) + r')(?!\w)',flags=re.IGNORECASE)
  text = pattern.sub(lambda x: obj[x.group()], myText)
  # text = pattern.sub(lambda x: obj[x.group()], text)
  return text
##==============================================================================
#map terms
def map_terms(myText):
  obj = CaseInsensitiveDict(mt_dict)
  pattern = re.compile(r'(?<!\w)(' + '|'.join(re.escape(key) for key in obj.keys()) + r')(?!\w)',flags=re.IGNORECASE)
  text = pattern.sub(lambda x: obj[x.group()], myText)
  # text = pattern.sub(lambda x: obj[x.group()], text)
  return text
##==============================================================================
# adjust space, period, comma
def remove_period_spaces(text):
  text = text.replace('||','')
  text = text.replace('Korea, Republic of','S Korea')
  text = text.replace('[]','')
  text = text.replace(', This',', this')
  text = text.replace(') The',') the')
  text = text.replace('in The The','in the')
  text = text.replace('The','the')
  text = text.replace('the the','the')
  text = text.replace('this is a','')
  text = text.replace('.,',',')
  text = text.replace('., ',',')
  text = text.replace(',',', ')  
  text = text.replace("due to", "because of", 1)
  text = text.replace("male subjects", "male participants")
  text = text.replace("female subjects", "female participants")
  # text = text.capitalize()
  text=" ".join(text.split())
  return text
##==============================================================================
# remove duplicate words
def unique_list(text_str):
    l = text_str.split()
    temp = []
    for x in l:
        if x not in temp:
            temp.append(x)
    return ' '.join(temp)
#===============================================================================
#reposition the condition in the summary
def repos_condition(my_string):
  try:
    # print(my_string)
    subjects=re.search('with(.*),',my_string)
    # print(subjects.group(1))
    if subjects:   
      fs=subjects.group(1).split(',')[0]
      # print(fs)
    else:
      subjects=re.search('with(.*).',my_string)
      fs=subjects.group(1).split('.')[0]
    # print(subjects.group(1).split(',')[0])
    a=re.search(r"\d+\s+subjects\s",my_string)
    # print(a.group(0))
    r=re.sub(r"\d+\s+subjects\s",a.group(0)+"with"+fs+" ",my_string)
    # print(r)
    result=re.sub("with"+fs+",","",r)
    print("--------------")
    return result
  except:
    print("not found")

#================================================================================

#reposition the additional study_design words
def repos_study_design(text):
    try:
        result = re.search('subjects(.*)study', text.lower())
        if result:
            r = result.group(1)+'study'
            newtext= text.replace(r, '')
            try:
              idx = newtext.lower().index('phase')
              newtext = newtext[:idx] + result.group(1) + newtext[idx:]
              return newtext
            except:
              return text
        else:
            return text
    except:
        print("nothing happened")  
#================================================================================
#identify purpose issues
def purpose_issue(summary):
  flag_words = ['will also be evaluated','will be evaluated','No Objective Found','subjects), is', 'subjects, is complete']
  if any(word in summary for word in flag_words):
    return "Yes - Grammar/Endpoint related Mistakes in Summary"
  else:
    return "No"
#================================================================================
# duplicate words check
def dupe_check(text,rr_value,stopwords=stopwords):
  if rr_value == 'No':
    split_text = text.split(' ')
    clean_text = ' '.join(i for i in split_text if i.lower() not in (x.lower() for x in stopwords))
    words = clean_text.split()
    result = (len(words) > len(set(words)))
    if result ==True:
      return " Yes - Duplicate Words maybe found in Summary"
    else:
      return rr_value
  else:
    return rr_value
#================================================================================  
#count all cap words
def count_caps(summary,rr_value):
  if rr_value == 'No':
    match_length = len(' '.join(re.findall(r"\b[A-Z\s]+\b", summary)).split())
    if match_length > 10:
      res = 'Yes - Summary May Contain Lot of Words in Upper Case'
      return res
    else:
      return rr_value
  else:
    return rr_value
#================================================================================
#identify route/dose misses
def route_miss(summary,rr_value,int_dec):
    if rr_value == 'No':
      split_summ = summary.split(' ')
      clean_text = ' '.join(i for i in split_summ if i.lower() not in (x.lower() for x in stopwords))
      summ_list = clean_text.split()
      int_summ = int_dec.split(' ')
      clean_text = ' '.join(i for i in int_summ if i.lower() not in (x.lower() for x in stopwords))
      int_list = clean_text.split()
      if any(check in int_list for check in summ_list):
        return "No"
      else:
        return "Yes - Route/Dose info might have been missed"
    else:
      return rr_value

