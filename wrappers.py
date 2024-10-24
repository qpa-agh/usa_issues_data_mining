from utils.scraping_utils import get_html

def extract_issues_wrapper(rep_link, extract_issues):
    issues_link = rep_link + 'issues'
    issues_html = get_html(issues_link)
    if issues_html is None:
        return []
    
    issues = extract_issues(issues_html, rep_link)
    return issues

def extract_article_links_wrapper(base_link, issues, extract_article_links):
    article_links = []
    for issue in issues:
        issue_article_links = extract_article_links(issue, base_link)
        if issue_article_links is not None:
            article_links.extend([{'issue': issue['name'], 'link': article_link} for article_link in issue_article_links])
    return article_links

def extract_articles_wrapper(article_links, extract_articles):
    articles = []
    for article_link in article_links:
        print(article_link)
        article = extract_articles(article_link)
        if article is not None:
            articles.append(article)
    return articles

def extract_articles(rep_link, extract_issues, extract_article_links, extract_article):
    print(rep_link)
    if rep_link[-1] != '/':
        rep_link += '/'
    issues = extract_issues_wrapper(rep_link, extract_issues)
    article_links = extract_article_links_wrapper(rep_link, issues, extract_article_links)
    articles = extract_articles_wrapper(article_links, extract_article)
    return articles