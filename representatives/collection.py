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
from representatives.moylan import *
from representatives.bost import *
from representatives.mrvan import *
from representatives.millermeeks import *
from representatives.davids import *
from representatives.mann import *
from representatives.comer import *
from representatives.scalise import *
from representatives.ruppersberger import *
from representatives.harris import *
from representatives.scholten import *
from representatives.craig import *
from representatives.wagner import *
from representatives.zinke import *
from representatives.flood import *
from representatives.amodei import *
from representatives.pappas import *
from representatives.norcross import *
from representatives.mace import *

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
# extraction_functions['https://moylan.house.gov'] = { no articles
#             'extract_issues': moylan_extract_issues,
#             'extract_article_links': moylan_extract_article_links,
#             'extract_article': moylan_extract_article
#         }

extraction_functions['https://bost.house.gov/'] = {
            'extract_issues': bost_extract_issues,
            'extract_article_links': bost_extract_article_links,
            'extract_article': bost_extract_article
        }

extraction_functions['https://mrvan.house.gov'] = {
            'extract_issues': mrvan_extract_issues,
            'extract_article_links': mrvan_extract_article_links,
            'extract_article': mrvan_extract_article
        }
extraction_functions['https://millermeeks.house.gov/'] = {
            'extract_issues': millermeeks_extract_issues,
            'extract_article_links': millermeeks_extract_article_links,
            'extract_article': millermeeks_extract_article
        }
extraction_functions['https://davids.house.gov/'] = {
            'extract_issues': davids_extract_issues,
            'extract_article_links': davids_extract_article_links,
            'extract_article': davids_extract_article
        }
extraction_functions['https://mann.house.gov'] = {
            'extract_issues': mann_extract_issues,
            'extract_article_links': mann_extract_article_links,
            'extract_article': mann_extract_article
        }
extraction_functions['https://comer.house.gov/'] = {
            'extract_issues': comer_extract_issues,
            'extract_article_links': comer_extract_article_links,
            'extract_article': comer_extract_article
        }
extraction_functions['https://scalise.house.gov/'] = {
            'extract_issues': scalise_extract_issues,
            'extract_article_links': scalise_extract_article_links,
            'extract_article': scalise_extract_article
        }
extraction_functions['https://ruppersberger.house.gov'] = {
            'extract_issues': ruppersberger_extract_issues,
            'extract_article_links': ruppersberger_extract_article_links,
            'extract_article': ruppersberger_extract_article
        }
extraction_functions['https://harris.house.gov/'] = {
            'extract_issues': harris_extract_issues,
            'extract_article_links': harris_extract_article_links,
            'extract_article': harris_extract_article
        }
extraction_functions['https://scholten.house.gov'] = {
            'extract_issues': scholten_extract_issues,
            'extract_article_links': scholten_extract_article_links,
            'extract_article': scholten_extract_article
        }
extraction_functions['https://craig.house.gov'] = {
            'extract_issues': craig_extract_issues,
            'extract_article_links': craig_extract_article_links,
            'extract_article': craig_extract_article
        }
# extraction_functions['https://finstad.house.gov/'] = { no artivcles :c
#             'extract_issues': finstad_extract_issues,
#             'extract_article_links': finstad_extract_article_links,
#             'extract_article': finstad_extract_article
#         }
# extraction_functions['https://benniethompson.house.gov/'] = {no artivcles :c
#             'extract_issues': benniethompson_extract_issues,
#             'extract_article_links': benniethompson_extract_article_links,
#             'extract_article': benniethompson_extract_article
#         }
extraction_functions['https://wagner.house.gov'] = {
            'extract_issues': wagner_extract_issues,
            'extract_article_links': wagner_extract_article_links,
            'extract_article': wagner_extract_article
        }
extraction_functions['https://zinke.house.gov'] = {
            'extract_issues': zinke_extract_issues,
            'extract_article_links': zinke_extract_article_links,
            'extract_article': zinke_extract_article
        }
extraction_functions['https://flood.house.gov/'] = {
            'extract_issues': flood_extract_issues,
            'extract_article_links': flood_extract_article_links,
            'extract_article': flood_extract_article
        }
extraction_functions['https://amodei.house.gov'] = {
            'extract_issues': amodei_extract_issues,
            'extract_article_links': amodei_extract_article_links,
            'extract_article': amodei_extract_article
        }
extraction_functions['https://pappas.house.gov'] = {
            'extract_issues': pappas_extract_issues,
            'extract_article_links': pappas_extract_article_links,
            'extract_article': pappas_extract_article
        }
extraction_functions['https://norcross.house.gov'] = {
            'extract_issues': norcross_extract_issues,
            'extract_article_links': norcross_extract_article_links,
            'extract_article': norcross_extract_article
        }
extraction_functions['https://mace.house.gov'] = {
            'extract_issues': mace_extract_issues,
            'extract_article_links': mace_extract_article_links,
            'extract_article': mace_extract_article
        }
