from feedgen.feed import FeedGenerator
import get_articles
import datetime


    
def generateFeed(fg_id, fg_title, fg_description, articles):
    fg = FeedGenerator()
    fg.id(fg_id)
    fg.title(fg_title)
    fg.link(href='http://example.com', rel='alternate')
    fg.description(fg_description)
    articles.reverse()
    for article in articles:
        fe = fg.add_entry()
        fe.id(article.ahref)
        fe.title(article.title)
        fe.link(href=article.ahref)
    atomfeed = fg.atom_str(pretty=True)
    rssfeed  = fg.rss_str(pretty=True)
    fg.atom_file(f'{fg_title}-atom.xml')
    fg.rss_file(f'{fg_title}-rss.xml')
    now = datetime.datetime.now()
    print(f"{now} - fetched {fg_title}")


if __name__ == "__main__":
    urls = ["https://tjarnikova.github.io/cti.html","https://skvrnami.github.io/log/"]
    generateFeed('001','Unoficial tjarnikova RSS',"Unoficial tjarnikova RSS created by Martin K.", get_articles.get_articles(urls[0],"tjan"))
    generateFeed('002','Unoficial skvrnami RSS',"Unoficial skvrnami RSS created by Martin K.", get_articles.get_articles(urls[1],"skvrnami"))

