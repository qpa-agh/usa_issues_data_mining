import pandas as pd
from utils.scraping_utils import get_html, parrarelize_processes
from wrappers import extract_articles_proofed
from representatives.evo import evo_extract_issues, evo_extract_article_links, evo_extract_article
from representatives.recordsContainer import recordsContainer_extract_issues, recordsContainer_extract_article_links, recordsContainer_extract_article

if __name__ == "__main__":
    recordsContainer_df = pd.read_csv('data/recordsContainer_representatives.csv')
    evo_df = pd.read_csv('data/evo_representatives.csv')
    
    recordsContainer_df = recordsContainer_df[recordsContainer_df['issues_catched'].isna() != True]
    evo_df = evo_df[evo_df['issues_catched'].isna() != True]
    
    jobs = []
    additional_info = []
    skip_list = ['https://pocan.house.gov', 
                 'https://sewell.house.gov/', 
                 'https://carl.house.gov', 
                 'https://radewagen.house.gov', 
                 'https://lamalfa.house.gov', 
                 'https://boebert.house.gov', 
                 'https://larson.house.gov/', 
                 'https://soto.house.gov', 
                 'https://gaetz.house.gov',
                 'https://bishop.house.gov/',
                 'https://bost.house.gov/',
                 'https://mrvan.house.gov',
                 'https://millermeeks.house.gov/',
                 'https://davids.house.gov/',
                 'https://mann.house.gov',
                 'https://comer.house.gov/',
                 'https://scalise.house.gov/',
                 'https://ruppersberger.house.gov',
                 'https://harris.house.gov/',
                 'https://scholten.house.gov',
                 'https://craig.house.gov',
                 'https://wagner.house.gov',
                 'https://zinke.house.gov',
                 'https://flood.house.gov/',
                 'https://amodei.house.gov',
                 'https://pappas.house.gov',
                 'https://norcross.house.gov',
                 'https://mace.house.gov',
                  ]
    for name, state, party, committee, link in zip(evo_df['representative_name'], evo_df['representative_state'], evo_df['representative_party'], evo_df['representative_committee'], evo_df['link']):
        if not (link in skip_list):
            jobs.append([link, evo_extract_issues, evo_extract_article_links, evo_extract_article])
            additional_info.append([name, state, party, committee]) 
    for name, state, party, committee, link in zip(recordsContainer_df['representative_name'], recordsContainer_df['representative_state'], recordsContainer_df['representative_party'], recordsContainer_df['representative_committee'], recordsContainer_df['link']):
        if not (link in skip_list):
            jobs.append([link, recordsContainer_extract_issues, recordsContainer_extract_article_links, recordsContainer_extract_article])
            additional_info.append([name, state, party, committee])

    articles = [] 
    for id, result in parrarelize_processes(extract_articles_proofed, jobs, n_executors=10):
        for rep_article in result:
            rep_article['representative_name'] = additional_info[id][0]
            rep_article['representative_state'] = additional_info[id][1]
            rep_article['representative_party'] = additional_info[id][2]
            rep_article['representative_committee'] = additional_info[id][3]
        articles.extend(result)

    articles_df = pd.DataFrame.from_dict(articles)
    articles_df

    articles_df.to_csv('data/articles_blind.csv')
