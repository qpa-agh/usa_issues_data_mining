from utils.scraping_utils import get_html

def bost_extract_issues(issues_html, base_link):
    issues_list_element = issues_html.find(class_='toc-list')
    issue_elements = issues_list_element.find_all(class_='content')
    issues = []
    for issue_element in issue_elements:
        a_el = issue_element.find(class_='header').find('a')
        issue = {
            'name': a_el.text.strip(),
            'link': base_link + a_el['href']
        }
        issues.append(issue)
    return issues

def bost_extract_article_links(issue, base_link):
    print(issue)
    articles_page = get_html(issue['link'])
    articles_links = []
    while True:
        try:
            articles_container = articles_page.find(id='content').find(class_='recordsContainer')
            article_elements = articles_container.find_all('tbody')
            article_groups = articles_container.find_all('table', class_='recordList')
        except AttributeError as e:
            return []
        article_elements = []
        for article_group in article_groups:
            article_elements.extend(article_group.find('tbody').find_all('tr')) 

        for article_element in article_elements:
            body = article_element.find(class_='recordListTitle')
            if body is None:
                continue
            # date = cells[1].text.strip()
            # article_name = cells[3].text.strip()
            article_href = base_link + body.find('a')['href'].strip()
            articles_links.append(article_href)
        
        try:
            navs = articles_page.find_all(class_='navbar')
            if len(navs) == 2:
                next_page_btn = navs[1].find('a', string='Next >')
            else:
                next_page_btn = navs[0].find('a', string='Next >')
        except AttributeError as e:
            next_page_btn = None
        if next_page_btn is None or next_page_btn['href'] == '#':
            break
        
        next_page_link = issue['link'] + '?' + next_page_btn['href'].split('?')[-1]
        print(next_page_link)
        articles_page = get_html(next_page_link)

    return articles_links

def bost_extract_article(article_link):
    try:
        article_page = get_html(article_link['link'])
        article_element = article_page.find(id='page-body')
        title = article_element.find('h1', class_='title').a.text.strip()
        date = article_element.find(class_='date').text.strip()
        text = article_element.find(class_='content').get_text().strip()
    except AttributeError as e:
        print('Error on: ', article_link)
        print(e)
        return None
    return {'issue': article_link['issue'], 'title': title, 'date': date, 'text': text}
