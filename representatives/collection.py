from representatives.sewell import *
from representatives.pocan import *

extraction_functions = {
    'https://sewell.house.gov/': 
        {
            'extract_issues': sewell_extract_issues,
            'extract_article_links': sewell_extract_article_links,
            'extract_article': sewell_extract_article
        },
    'https://pocan.house.gov':
        {
            'extract_issues': pocan_extract_issues,
            'extract_article_links': pocan_extract_article_links,
            'extract_article': pocan_extract_article
        }
}