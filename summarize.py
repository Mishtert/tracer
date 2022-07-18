import streamlit as st
from tqdm import tqdm

from utils.summarize_utils.summ_utils import count_caps, dupe_check, purpose_issue, route_miss

tqdm.pandas()

# Warning message configuration
import logging, sys

logging.disable(sys.maxsize)
import warnings

warnings.filterwarnings('ignore')

# pwd

from utils.summarize_utils.summwrap import get_data, get_summ
from utils.summarize_utils.headlinewrap import get_headline
import pandas as pd

# import numpy as np

pd.set_option('display.max_colwidth', 800)


# study_id_list = [
#  'NCT04545554'
# ]
def get_summary_app(study_id):
    study_id_list = study_id.split(",")
    print(study_id.split(","))
    df = get_data(study_id_list)
    df.head(2)
    df['LastUpdatePostDate'] = pd.to_datetime(df['LastUpdatePostDate']).dt.strftime('%d %b %Y')

    df['summary'] = df.progress_apply(lambda x: get_summ(
        x['OverallStatus'],
        x['DesignAllocation'],
        x['DesignMasking'],
        x['Phase'],
        x['DesignInterventionModel'],
        x['OrgStudyId'],
        x['SecondaryId'],
        x['LocationCountry'],
        x['EnrollmentCount'],
        x['OfficialTitle'],
        x['BriefSummary'],
        x['DetailedDescription'],
        x['WhyStopped'],
        x['NCTId'],
        x['LastUpdatePostDate']
    ),
                                      axis=1
                                      )

    df['headline'] = df.progress_apply(lambda x: get_headline(
        x['OverallStatus'],
        x['Phase'],
        x['OrgStudyId'],
        x['SecondaryId'],
        x['Condition']
    ),
                                       axis=1
                                       )

    df['Review_Required'] = df['summary'].apply(lambda summary: purpose_issue(summary))
    df['Review_Required'] = df.apply(lambda row: dupe_check(row['summary'], row['Review_Required']), axis=1)
    df['Review_Required'] = df.apply(lambda row: count_caps(row['summary'], row['Review_Required']), axis=1)
    df['Review_Required'] = df.apply(
        lambda row: route_miss(row['summary'], row['Review_Required'], row['InterventionDescription']), axis=1)
    final_df = df[['NCTId', 'summary', 'Review_Required', 'headline']]
    ids = df['NCTId'].to_markdown()
    summary_output = df['summary'].to_markdown()
    headline_output = df['headline'].to_markdown()

    return headline_output, summary_output
# df[['OverallStatus','Phase','OrgStudyId','SecondaryId','Condition','headline']]

# df.head()
# df.to_csv('summary_output_sample.csv',index=False, encoding='UTF-8')
