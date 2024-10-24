from representatives.sewell import *
from representatives.pocan import *
from representatives.carl import *
from representatives.lamalfa import *
from representatives.radewagen import *

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

extraction_functions['https://carl.house.gov'] = {
            'extract_issues': carl_extract_issues,
            'extract_article_links': carl_extract_article_links,
            'extract_article': carl_extract_article
        }
extraction_functions['https://radewagen.house.gov'] = {
            'extract_issues': radewagen_extract_issues,
            'extract_article_links': radewagen_extract_article_links,
            'extract_article': radewagen_extract_article
        }
extraction_functions['https://lamalfa.house.gov'] = {
            'extract_issues': lamalfa_extract_issues,
            'extract_article_links': lamalfa_extract_article_links,
            'extract_article': lamalfa_extract_article
        }

