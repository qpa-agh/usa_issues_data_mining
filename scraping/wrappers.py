from scraping.utils.scraping_utils import get_html, parrarelize_threads

def extract_issues_wrapper(rep_link, extract_issues):
    issues_link = rep_link + 'issues'
    issues_html = get_html(issues_link)
    if issues_html is None:
        return []
    
    issues = extract_issues(issues_html, rep_link)
    return issues

def extract_issues_wrapper_proofed(rep_link, extract_issues):
    try:
        issues_link = rep_link + 'issues'
        issues_html = get_html(issues_link)
        if issues_html is not None:
            return extract_issues(issues_html, rep_link)
    except BaseException as e:
        print(rep_link, 'error:', e)
    return []

def extract_article_links_wrapper(base_link, issues, extract_article_links):
    article_links = []
    additional_information = [[issue['name']] for issue in issues]
    jobs = [[issue, base_link] for issue in issues]
    for id, issue_article_links in parrarelize_threads(extract_article_links, jobs):
        if issue_article_links is not None:
            article_links.extend([{'issue': additional_information[id][0], 'link': article_link} for article_link in issue_article_links])
    return article_links

def extract_articles_wrapper(article_links, extract_articles):
    articles = []
    jobs = [[article_link] for article_link in article_links]
    additional_information = [[article_link] for article_link in article_links]
    for id, article in parrarelize_threads(extract_articles, jobs):
        print(additional_information[id][0])
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

def extract_articles_proofed(rep_link, extract_issues, extract_article_links, extract_article):
    try:
        print(rep_link)
        if rep_link[-1] != '/':
            rep_link += '/'
        issues = extract_issues_wrapper(rep_link, extract_issues)
        article_links = extract_article_links_wrapper(rep_link, issues, extract_article_links)
        articles = extract_articles_wrapper(article_links, extract_article)
        return articles
    except BaseException as e:
        print(rep_link, 'error:', e)
    return []