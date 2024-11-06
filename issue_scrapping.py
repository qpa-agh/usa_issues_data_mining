import pandas as pd
from utils.scraping_utils import get_html, parrarelize_processes
from wrappers import extract_articles
from representatives.collection import extraction_functions

if __name__ == "__main__":
    rep_df = pd.read_csv('data\chosen_representatives.csv')

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
    for name, state, party, committee, link in zip(rep_df['name'], rep_df['state'], rep_df['party'], rep_df['committee'], rep_df['page_link']):
        if link in extraction_functions and not (link in skip_list):
            page_functions = extraction_functions[link]
            # print(link)
            jobs.append([link, page_functions['extract_issues'], page_functions['extract_article_links'], page_functions['extract_article']])
            additional_info.append([name, state, party, committee]) 

    articles = [] 
    for id, result in parrarelize_processes(extract_articles, jobs, n_executors=5):
        for rep_article in result:
            rep_article['representative_name'] = additional_info[id][0]
            rep_article['representative_state'] = additional_info[id][1]
            rep_article['representative_party'] = additional_info[id][2]
            rep_article['representative_committee'] = additional_info[id][3]
        articles.extend(result)

    articles_df = pd.DataFrame.from_dict(articles)
    articles_df

    articles_df.to_csv('data/articles2.csv')
