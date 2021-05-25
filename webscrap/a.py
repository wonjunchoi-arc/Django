class BeautifulSoup(object):
    title = ''
    def __init__(self, html_doc, parser):
        self.html_doc = html_doc
        self.parser = parser
    def prettyfy(self):
        print(self.html_doc)