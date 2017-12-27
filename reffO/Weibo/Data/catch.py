from goose3 import Goose
from goose3.text import StopWordsChinese
url  = 'http://news.sina.com.cn/c/nd/2017-11-28/doc-ifypathz7124001.shtml'
g = Goose({'stopwords_class': StopWordsChinese})
article = g.extract(url=url)
print(article.cleaned_text[:150])