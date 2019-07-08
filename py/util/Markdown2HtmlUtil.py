import markdown
import os.path as op
from bs4 import BeautifulSoup


class Markdown2Html:

    def __init__(self, css_file=None):
        """
        初始化 Markdown2Html 类，可传入特定 css 文件作为样式
        """
        self.headTag = '<head><meta charset="utf-8" /></head>'
        if css_file:
            self.set_style(css_file)

    def set_style(self, css_file=None):
        """
        设置样式表文件
        """
        if css_file is None:
            self.headTag = '<head><meta charset="utf-8" /></head>'
        else:
            with open(css_file, 'r') as f:
                css = f.read()
                self.headTag = self.headTag[:-7] + f'<style  type="text/css">{css}</style>' + self.headTag[-7:]

    def convert(self, infile, outfile=None, prettify=False):
        """
        转换文件
        """
        if not op.isfile(infile):
            print('请输入正确的 markdown 文件路径！')
            return

        if outfile is None:
            outfile = op.splitext(infile)[0] + '.html'

        with open(infile, 'r', encoding='utf8') as f:
            markdown_text = f.read()

        raw_html = self.headTag + markdown.markdown(markdown_text, output_format='html5', extensions=['extra'])

        if prettify:
            pretty_html = BeautifulSoup(raw_html, 'html5lib').prettify()
            with open(outfile, 'w', encoding='utf8') as f:
                f.write(pretty_html)
        else:
            with open(outfile, 'w', encoding='utf8') as f:
                f.write(raw_html)


if __name__ == '__main__':
    m2h = Markdown2Html('github.css')
    input_markdown_file_path = 'C:\\Users\\lyh\\PycharmProjects\\Python-learn\\py\\util\\Cinder.md'
    output_html_file_path = 'C:\\Users\\lyh\\PycharmProjects\\Python-learn\\py\\util\\Cinder.html'
    m2h.convert(input_markdown_file_path, output_html_file_path)
