from representatives.sewell import *
from representatives.pocan import *
from representatives.carl import *
from representatives.lamalfa import *
from representatives.radewagen import *
from representatives.boebert import *
from representatives.larson import *
from representatives.soto import *
from representatives.gaetz import *
from representatives.bishop import *

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
extraction_functions['https://boebert.house.gov'] = {
            'extract_issues': boebert_extract_issues,
            'extract_article_links': boebert_extract_article_links,
            'extract_article': boebert_extract_article
        }
extraction_functions['https://larson.house.gov/'] = {
            'extract_issues': larson_extract_issues,
            'extract_article_links': larson_extract_article_links,
            'extract_article': larson_extract_article
        }
extraction_functions['https://soto.house.gov'] = {
            'extract_issues': soto_extract_issues,
            'extract_article_links': soto_extract_article_links,
            'extract_article': soto_extract_article
        }
extraction_functions['https://gaetz.house.gov'] = {
            'extract_issues': gaetz_extract_issues,
            'extract_article_links': gaetz_extract_article_links,
            'extract_article': gaetz_extract_article
        }
extraction_functions['https://bishop.house.gov/'] = {
            'extract_issues': bishop_extract_issues,
            'extract_article_links': bishop_extract_article_links,
            'extract_article': bishop_extract_article
        }

