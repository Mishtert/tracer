from utils.summarize_utils.summ_utils import *
from utils.summarize_utils.ctwrap import ClinicalTrials
import pandas as pd

# get data
def get_data(study_id_list):
    # print(study_id_list)
    ct = ClinicalTrials()
    
    fields=['NCTId','OfficialTitle','BriefSummary','DetailedDescription','LocationCountry',
            'OrgStudyId','SecondaryId','Condition','InterventionName',
            'DesignInterventionModel','BriefTitle','Phase', 'DesignAllocation', 
            'DesignMasking','OverallStatus', 'WhyStopped','EnrollmentCount', 'LastUpdatePostDate',
            'InterventionDescription']


    column_names = ['Rank','NCTId','OfficialTitle','BriefSummary','DetailedDescription',
                    'LocationCountry' ,'OrgStudyId','SecondaryId','Condition','InterventionName',
                    'DesignInterventionModel', 'BriefTitle','Phase','DesignAllocation', 
                    'DesignMasking', 'OverallStatus', 'WhyStopped','EnrollmentCount',
                    'LastUpdatePostDate','InterventionDescription']
    my_list =[]
    for ncid in study_id_list:
        nct_fields = ct.get_study_fields(
            search_expr= ncid,
            fields=fields,
            fmt="csv",
        )
        my_list.append(nct_fields[1:])
    flat_list = [item for sublist in my_list for item in sublist]
    d= [dict(zip(column_names, l)) for l in flat_list ]
    data = pd.DataFrame(d).fillna('')
    print('Data reading complete..')
    return data


def get_summ(status, alloc, masking, phase, imodel, osid, sid, locations,pcount,otitle, bsumm,ddesc,ystop,nctid,lupd):
  locs = get_locs(locations)
  print(status)

  if alloc.lower()!='n/a'and ystop =='' and pcount !='0' and status =='':
    print('first if - im inside alloc is not na & ystop is none')
    ostmt = get_first_word(alloc,masking,status) +              \
            alloc.lower() + ', ' +                              \
            get_mask(masking) +                                 \
            get_imodel(imodel) +                                \
            '/'.join(phase.lower().split('|')) + ' '+                                \
            get_osid(osid,sid)+                                 \
            'study ' +                                          \
            get_locs(locations) +                               \
            ' in ' + pcount + ' subjects '+                     \
            get_obj(otitle,bsumm,ddesc) +                       \
            get_status(status) +                                \
            get_url(nctid,lupd)
    ostmt = repos_study_design(remove_period_spaces(map_terms(map_week_num(ostmt))))
    return ostmt
  
  if alloc.lower()!='n/a'and ystop =='' and pcount !='0' and status =='Active, not recruiting' :
    print('second if - im inside alloc is not na & ystop is none')
    ostmt = get_first_word(alloc,masking,status) +              \
            alloc.lower() + ', ' +                              \
            get_mask(masking) +                                 \
            get_imodel(imodel) +                                \
            '/'.join(phase.lower().split('|')) + ' '+                                \
            get_osid(osid,sid)+                                 \
            'study ' +                                          \
            get_locs(locations) +                               \
            get_status(status) +                                \
            ' in ' + pcount + ' subjects '+                     \
            get_obj(otitle,bsumm,ddesc) +                       \
            get_url(nctid,lupd)
    ostmt = repos_study_design(remove_period_spaces(map_terms(map_week_num(ostmt))))
    # ostmt = unique_list(ostmt)
    return ostmt
  if alloc.lower()!='n/a'and ystop =='' and pcount !='0' and status !='':
    print('third if - im inside alloc is not na & ystop is none')
    ostmt = get_first_word(alloc,masking,status) +              \
            alloc.lower() + ', ' +                              \
            get_mask(masking) +                                 \
            get_imodel(imodel) +                                \
            '/'.join(phase.lower().split('|')) + ' '+                                \
            get_osid(osid,sid)+                                 \
            'study ' +                                          \
            get_locs(locations) +                               \
            ' in ' + pcount + ' subjects '+                     \
            get_obj(otitle,bsumm,ddesc) +                       \
            get_status(status) +                                \
            get_url(nctid,lupd)
    ostmt = repos_study_design(remove_period_spaces(map_terms(map_week_num(ostmt)))      )
    # ostmt = unique_list(ostmt)
    return ostmt
  if alloc.lower()=='n/a' and ystop =='' and pcount !='0':
    print('fourth if - im alloc is na and ystop is none')
    ostmt = get_first_word(alloc,masking,status) +              \
            get_mask(masking) +                                 \
            get_imodel(imodel) +                                \
            '/'.join(phase.lower().split('|')) + ' '+                                \
            get_osid(osid,sid)+                                 \
            'study ' +                                          \
            get_locs(locations) +                               \
            ' in ' + pcount + ' subjects '+                     \
            get_obj(otitle,bsumm,ddesc) +                       \
            get_status(status) +                                \
            get_url(nctid,lupd)
    print(ostmt)
    ostmt = repos_study_design(remove_period_spaces(map_terms(map_week_num(ostmt))))
    # ostmt = unique_list(ostmt)
    return ostmt
    
  if alloc.lower()=='n/a' and ystop !='' and pcount !='0':
    print('fifth if - im in alloc na;  ystop not none; pcount not 0')
    ostmt = get_first_word(alloc,masking,status) +              \
            get_mask(masking) +                                 \
            get_imodel(imodel) +                                \
            '/'.join(phase.lower().split('|')) + ' '+                                \
            get_osid(osid,sid)+                                 \
            'study ' +                                          \
            get_locs(locations) +                               \
            ' in ' + pcount + ' subjects '+                     \
            get_obj(otitle,bsumm,ddesc) +                       \
            get_status(status) +                                \
            get_ystop(ystop) +                                  \
            get_url(nctid,lupd)
    ostmt = repos_study_design(remove_period_spaces(map_terms(map_week_num(ostmt))))
    # ostmt = unique_list(ostmt)
    return ostmt
    
  if alloc.lower()!='n/a' and ystop !='' and pcount !='0':
    print('sixth if - im alloc not na and ystop is not none')
    ostmt = get_first_word(alloc,masking,status) +              \
            alloc.lower() + ', ' +                              \
            get_mask(masking) +                                 \
            get_imodel(imodel) +                                \
            '/'.join(phase.lower().split('|')) + ' '+                                \
            get_osid(osid,sid)+                                 \
            'study ' +                                          \
            get_locs(locations) +                               \
            ' in ' + pcount + ' subjects '+                     \
            get_obj(otitle,bsumm,ddesc) +                       \
            get_status(status) +                                \
            get_ystop(ystop) +                                  \
            get_url(nctid,lupd)
    ostmt = repos_study_design(remove_period_spaces(map_terms(map_week_num(ostmt))))
    # ostmt = unique_list(ostmt)
    return ostmt

  if alloc.lower()!='n/a' and ystop !='' and pcount =='0':
    print('seventh if - im alloc not na and ystop is not none')
    print(ystop)
    ostmt = get_first_word(alloc,masking,status) +              \
            alloc.lower() + ', ' +                              \
            get_mask(masking) +                                 \
            get_imodel(imodel) +                                \
            '/'.join(phase.lower().split('|')) + ' '+                                \
            get_osid(osid,sid)+                                 \
            'study ' +                                          \
            get_locs(locations) +                               \
            get_obj(otitle,bsumm,ddesc) +                       \
            get_status(status) +                                \
            get_ystop(ystop) +                                  \
            get_url(nctid,lupd)
    ostmt = repos_study_design(remove_period_spaces(map_terms(map_week_num(ostmt))))
    # ostmt = unique_list(ostmt)
    return ostmt

  if alloc.lower()=='n/a' and ystop !='' and pcount =='0':
    print('eigth if - im alloc not na and ystop is not none')
    ostmt = get_first_word(alloc,masking,status) +              \
            get_mask(masking) +                                 \
            get_imodel(imodel) +                                \
            '/'.join(phase.lower().split('|')) + ' '+                                \
            get_osid(osid,sid)+                                 \
            'study ' +                                          \
            get_locs(locations) +                               \
            get_obj(otitle,bsumm,ddesc) +                       \
            get_status(status) +                                \
            get_ystop(ystop) +                                  \
            get_url(nctid,lupd)
    ostmt = repos_study_design(remove_period_spaces(map_terms(map_week_num(ostmt))))
#     ostmt = unique_list(ostmt)
    return ostmt   

