from scraping.utils.scraping_utils import get_html

def harris_extract_issues(issues_html, base_link):
    issues_list_element = issues_html.find(class_='evo-content')
    issue_elements = issues_list_element.find_all(class_='evo-media-object')
    issues = []
    for issue_element in issue_elements:
        a_el = issue_element.find(class_='media-body').find('a')
        issue = {
            'name': a_el.text.strip(),
            'link': base_link + a_el['href']
        }
        issues.append(issue)
    return issues

def harris_extract_article_links(issue, base_link):
    print(issue)
    articles_page = get_html(issue['link'])
    articles_links = []
    while True:
        articles_container = articles_page.find(class_='evo-view-wrapper')
        article_elements = articles_container.find_all(class_='evo-views-row')

        for article_element in article_elements:
            body = article_element.find(class_='media-body')
            if body is None:
                continue
            # date = cells[1].text.strip()
            # article_name = cells[3].text.strip()
            article_href = base_link + body.find('a')['href'].strip()
            articles_links.append(article_href)
        
        try:
            next_page_btn = articles_page.find(class_='page__content').find(class_='pagination').find('li', class_='pager__item--next')
        except AttributeError as e:
            next_page_btn = None
        if next_page_btn is None:
            break
        next_page_btn = next_page_btn.find('a')
        
        next_page_link = issue['link'] + next_page_btn['href']
        print(next_page_link)
        articles_page = get_html(next_page_link)

    return articles_links

def harris_extract_article(article_link):
    try:
        article_page = get_html(article_link['link'])
        article_element = article_page.find(class_='evo-content')
        title = article_element.find('h1').span.text.strip()
        date = article_element.find(class_='row').div.text.strip()
        text_element = article_element.find(class_='evo-press-release__body')
        if text_element is None:
            text_element = article_element.find(class_='evo-in-the-news__body')
        text = text_element.get_text().strip()
    except AttributeError as e:
        print('Error on: ', article_link)
        return None
    return {'issue': article_link['issue'], 'title': title, 'date': date, 'text': text}