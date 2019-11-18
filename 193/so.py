import requests
import bs4

cached_so_url = 'https://bit.ly/2IMrXdp'


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    result = []
    html = requests.get(url).text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    q_div = soup.find("div", id="questions", class_="flush-left")
    for q in q_div.children:
        if isinstance(q, bs4.Tag):
            views_str = q.find(class_="views")["title"]
            views = int(views_str.rstrip(" views").replace(",", ""))
            if views < 1000000:
                continue
            votes = int(q.find(class_="vote-count-post").strong.text)
            question = q.find(class_="question-hyperlink").text
            result.append((question, votes))
    return sorted(result, key=lambda x: x[1], reverse=True)
