from utils.summarize_utils.summ_utils import get_osid, map_terms
from utils.summarize_utils.headline_utils import get_condition

def get_headline(status,phase,osid, sid,condition):
    if status =='Recruiting':
        headline = "Initiation of " + \
                    '/'.join(phase.lower().split('|')) + ' '+ \
                        "trial " + \
                            get_osid(osid,sid)+ \
                                "for " + \
                                    get_condition(condition) + \
                                        " reported" 
        return map_terms(headline)
    elif status == 'Active, not recruiting':
        headline = "Planned " + \
                    '/'.join(phase.lower().split('|')) + ' '+ \
                        "trial " + \
                            get_osid(osid,sid)+ \
                                "for " + \
                                    get_condition(condition) + \
                                        " reported"
        return map_terms(headline)

    elif status =='Completed':
        headline = "Completion of " + \
                    '/'.join(phase.lower().split('|')) + ' '+ \
                        "trial " + \
                            get_osid(osid,sid)+ \
                                "for " + \
                                    get_condition(condition) + \
                                        " reported"
        return map_terms(headline)
    
    elif status =='Terminated':
        headline = "Termination of " + \
                    '/'.join(phase.lower().split('|')) + ' '+ \
                        "trial " + \
                            get_osid(osid,sid)+ \
                                "for " + \
                                    get_condition(condition) + \
                                        " reported"
        return map_terms(headline)

    elif status =='Withdrawn':
        headline = "Withdrawal of " + \
                    '/'.join(phase.lower().split('|')) + ' '+ \
                        "trial  " +\
                            get_osid(osid,sid)+ \
                                "for " + \
                                    get_condition(condition) + \
                                        " reported"
        return map_terms(headline)

    elif status =='Suspension':
        headline = "Suspension of " + \
                    '/'.join(phase.lower().split('|')) + ' '+ \
                        "trial " +\
                            get_osid(osid,sid)+ \
                                "for " + \
                                    get_condition(condition) + \
                                        " reported"
        return headline
    else:
        headline = "Ongoing " + \
                    '/'.join(phase.lower().split('|')) + ' '+ \
                        "trial " +\
                            get_osid(osid,sid)+ \
                                "for " + \
                                    get_condition(condition) + \
                                        " reported"
        return map_terms(headline)
