import codecs
import markdown

input_markdown_file_path = "Cinder.md"
output_html_file_path = "Cinder.html"
# 读取 markdown 文本
input_file = codecs.open(input_markdown_file_path, mode="r", encoding="utf-8")
text = input_file.read()

# 转为 html 文本
html = markdown.markdown(text)

# 保存为文件
output_file = codecs.open(output_html_file_path, mode="w", encoding="utf-8")
output_file.write(html)
