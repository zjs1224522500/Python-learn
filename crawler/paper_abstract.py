import os

import requests
import lxml.html

header_count = 8
header_start_index = 2
start_page = "https://dblp.uni-trier.de/db/conf/fast/fast2019.html"
output_file_name = ""


class PaperIntroduction:

    def __init__(self, title, category, link, abstract):
        self.__title = title
        self.__category = category
        self.__link = link
        self.__abstract = abstract

    def __str__(self) -> str:
        return "Paper['title': %s ; 'category': %s ; 'link': %s ; 'abstract': %s]" % (self.__title, self.__category,
                                                                                      self.__link, self.__abstract)

    def get_title(self) -> str:
        return self.__title

    def get_category(self) -> str:
        return self.__category

    def get_link(self) -> str:
        return self.__link

    def get_abstract(self) -> str:
        return self.__abstract


def get_html(url):
    mock_user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                      "Chrome/63.0.3239.132 Safari/537.36 "
    user_agent_header = "User-Agent"
    headers = {user_agent_header: mock_user_agent}
    response = requests.get(url, headers=headers)
    html = response.text
    return html


def get_papers(page):
    selector = lxml.html.fromstring(get_html(page))

    html_headers = {}
    html_spans = {}
    papers = []
    for i in range(header_count):
        header_xpath = '//*[@id="main"]/header[%d]/h2' % (header_start_index + i)
        ul_xpath = '//*[@id="main"]/ul[%d]' % (header_start_index + i)
        html_headers[i] = selector.xpath(header_xpath)[0].text
        print('*************************************************')
        print(html_headers[i])

        j = 1
        while True:
            span_xpath = ul_xpath + ('/li[%d]/cite/span[@class="title"]' % j)
            link_xpath = ul_xpath + ('/li[%d]/nav/ul/li[1]/div[1]/a' % j)
            html_span = selector.xpath(span_xpath)
            if html_span is None or len(html_span) == 0:
                break
            else:
                html_spans[j - 1] = html_span[0].text
                html_link_ele = selector.xpath(link_xpath)
                if html_link_ele is None or len(html_link_ele) <= 0:
                    break
                html_link = html_link_ele[0].attrib['href']
                paper_title = ('%d. ' % j) + html_spans[j - 1]
                print(paper_title + " " + html_link)

                abstract_xpath = '//*[@role = "main"]/section/div[3]/article/div/div[2]/div[2]/div/p'
                paper_selector = lxml.html.fromstring(get_html(html_link))

                abstract_content = ""
                html_paras = paper_selector.xpath(abstract_xpath)
                if html_paras is not None and len(html_paras) != 0:
                    for index in range(len(html_paras)):
                        abstract_content += str(html_paras[index].text + "\n")

                paper = PaperIntroduction(str(paper_title), str(html_headers[i]), str(html_link),
                                          abstract_content)
                papers.append(paper)
                j += 1

        print('*************************************************')
    return papers


def format_data(paperlist):
    result = ""
    for i in range(len(paperlist)):
        paper_title = paperlist[i].get_title()
        if paper_title.startswith("1."):
            result += "### %s \n\n" % paperlist[i].get_category()
        result += "#### %s \n" % paper_title
        result += "- [Source](%s) \n\n" % paperlist[i].get_link()
        result += "##### Abstract \n"
        abstract_str = paperlist[i].get_abstract()
        if abstract_str.__contains__("\n"):
            list_str = abstract_str.split("\n")
            for index in range(len(list_str)):
                if list_str[index] is not None and len(list_str[index]) > 2:
                    result += "- %s \n\n" % list_str[index]
        else:
            result += "- %s \n\n" % abstract_str
    return result


def write_file(file_name, content):
    cwd = os.getcwd()
    path = cwd + '/' + file_name
    output_file = open(path, 'a+', encoding="utf-8")
    print("Start write file, please wait!")
    output_file.write(content)
    output_file.close()
    print("Write completed")


if __name__ == "__main__":
    # papers19 = get_papers(start_page)
    # write_file("fast19.md", format_data(papers19))
    # papers18 = get_papers("https://dblp.uni-trier.de/db/conf/fast/fast2018.html")
    # write_file("fast18.md", format_data(papers18))
    urls = ["https://dblp.uni-trier.de/db/conf/fast/fast2017.html",
            "https://dblp.uni-trier.de/db/conf/fast/fast2016.html",
            "https://dblp.uni-trier.de/db/conf/fast/fast2015.html"]
    file_names = ["fast17.md", "fast16.md", "fast15.md"]
    for i in range(len(urls)):
        papers = get_papers(urls[i])
        write_file(file_names[i], format_data(papers))

