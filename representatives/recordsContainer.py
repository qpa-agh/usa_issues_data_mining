from utils.scraping_utils import get_html

def recordsContainer_extract_issues(issues_html, base_link):
    issues_list_element = issues_html.find(class_='issues-group')
    issue_elements = issues_list_element.find_all(class_='issues-group-item')
    issues = []
    for issue_element in issue_elements:
        issue = {
            'name': issue_element.text.strip(),
            'link': base_link + issue_element.a['href']
        }
        issues.append(issue)
    return issues

def recordsContainer_extract_article_links(issue, base_link):
    articles_page = get_html(issue['link'])
    articles_links = []
    while True:
        articles_container = articles_page.find(class_='recordsContainer')
        if articles_container is None:
            print('skipped issues==>', issue['link'])
            return articles_links
        article_groups = articles_container.find_all('table', class_='recordList')

        article_elements = []
        for article_group in article_groups:
            article_elements.extend(article_group.find('tbody').find_all('tr')) 

        for article_element in article_elements:
            cells = list(article_element.children)
            # date = cells[1].text.strip()
            # article_name = cells[3].text.strip()
            article_href = base_link + cells[3].a['href'].strip()
            articles_links.append(article_href)
        next_page_btn = articles_page.find('a', string='Next >')
        if next_page_btn is None or next_page_btn['href'] == '#':
            break
        next_page_link = base_link + next_page_btn['href']
        print(next_page_link)
        articles_page = get_html(next_page_link)

    return articles_links

def recordsContainer_extract_article(article_link):
    try:
        article_page = get_html(article_link['link'])
        article_element = article_page.find('article')
        title = article_element.find(class_='title').text.strip()
        date = article_element.find(class_='date').text.strip()
        text = article_element.find(class_='post-content').get_text().strip()
    except AttributeError as e:
        print('Error on: ', article_link)
        return None
    return {'issue': article_link['issue'], 'title': title, 'date': date, 'text': text}