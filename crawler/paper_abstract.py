import requests
import lxml.html

header_count = 8
header_start_index = 2


class PaperIntroduction:

    def __init__(self, title, category, link, abstract):
        self.__title = title
        self.__category = category
        self.__link = link
        self.__abstract = abstract

    def __str__(self) -> str:
        return "Paper['title': %s ; 'category': %s ; 'link': %s ; 'abstract': %s]" % (self.__title, self.__category,
                                                                                      self.__link, self.__abstract)


def get_html(url):
    mock_user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                      "Chrome/63.0.3239.132 Safari/537.36 "
    user_agent_header = "User-Agent"
    headers = {user_agent_header: mock_user_agent}
    response = requests.get(url, headers=headers)
    html = response.text
    return html


if __name__ == "__main__":
    selector = lxml.html.fromstring(get_html("https://dblp.uni-trier.de/db/conf/fast/fast2019.html"))

    html_headers = {}
    html_spans = {}
    papers = []
    for i in range(header_count):
        header_xpath = '//*[@id="main"]/header[%d]/h2' % (header_start_index + i)
        ul_xpath = '//*[@id="main"]/ul[%d]' % (header_start_index + i)
        html_headers[i] = selector.xpath(header_xpath)[0].text
        print('*************************************************')
        print(html_headers[i])

        html_ul = selector.xpath(ul_xpath)
        j = 1
        while True:
            span_xpath = ul_xpath + ('/li[%d]/cite/span[@class="title"]' % j)
            link_xpath = ul_xpath + ('/li[%d]/nav/ul/li[1]/div[1]/a' % j)
            html_span = selector.xpath(span_xpath)
            if html_span is None or len(html_span) == 0:
                break
            else:
                html_spans[j - 1] = html_span[0].text
                html_link = selector.xpath(link_xpath)[0].attrib['href']
                print(('%d. ' % j) + html_spans[j - 1] + " " + html_link)

                abstract_xpath = '//*[@role = "main"]/section/div[3]/article/div/div[2]/div[2]/div/p'
                paper_selector = lxml.html.fromstring(get_html(html_link))

                abstract_content = ""
                html_paras = paper_selector.xpath(abstract_xpath)
                if html_paras is not None and len(html_paras) != 0:
                    for index in range(len(html_paras)):
                        abstract_content += html_paras[index].text

                paper = PaperIntroduction(str(html_spans[j - 1]), str(html_headers[i]), str(html_link), abstract_content)
                papers.append(paper)
                j += 1

        print('*************************************************')

    for i in range(len(papers)):
        print(papers[i])
