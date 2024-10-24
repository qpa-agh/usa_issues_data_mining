# %%
import pandas as pd
from utils.scraping_utils import get_html, parrarelize_processes
from wrappers import extract_articles
from representatives.collection import extraction_functions

if __name__ == "__main__":
    # %%
    rep_df = pd.read_csv('data\chosen_representatives.csv')
    rep_df.tail(78)

    # %%
    # extraction_functions['https://carl.house.gov'] = {
    #             'extract_issues': carl_extract_issues,
    #             'extract_article_links': carl_extract_article_links,
    #             'extract_article': carl_extract_article
    #         }


    # %%
    # articles = []
    # skip_list = []#['https://pocan.house.gov', 'https://sewell.house.gov/', 'https://carl.house.gov', 'https://radewagen.house.gov']
    # for name, state, party, committee, link in zip(rep_df['name'], rep_df['state'], rep_df['party'], rep_df['committee'], rep_df['page_link']):
    #     if link in extraction_functions and not (link in skip_list):
    #         page_functions = extraction_functions[link]
    #         print(link)
    #         rep_articles = extract_articles(link, page_functions['extract_issues'], page_functions['extract_article_links'], page_functions['extract_article'])
    #         for rep_article in rep_articles:
    #             rep_article['representative_name'] = name
    #             rep_article['representative_state'] = state
    #             rep_article['representative_party'] = party
    #             rep_article['representative_committee'] = committee
    #         articles.extend(rep_articles)

    # %%
    jobs = []
    additional_info = []
    skip_list = ['https://pocan.house.gov', 'https://sewell.house.gov/', 'https://carl.house.gov', 'https://radewagen.house.gov', 'https://lamalfa.house.gov']#, 'https://boebert.house.gov']
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

    # %%
    articles_df = pd.DataFrame.from_dict(articles)
    articles_df

    # %%
    articles_df.to_csv('data/articles2.csv')

    # %%
    articles_df['representative_name'].value_counts()

    # %%
    articles_df['issue'].value_counts()


