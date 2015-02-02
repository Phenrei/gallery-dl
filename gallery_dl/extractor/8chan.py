from .common import BasicExtractor
from urllib.parse import unquote
import re

class Extractor(BasicExtractor):

    url_base = "https://8ch.net"
    thread_url_fmt = url_base + "/{0}/res/{1}.html"
    regex = r'>File: <a href="([^"]+)">([^<]+)\.[^<]+<.*?<span class="postfilename"( title="([^"]+)")?>([^<]+)<'

    def __init__(self, match, config):
        BasicExtractor.__init__(self, config)
        self.board, _, self.thread_id = match.group(1).split("/")
        self.category = "8chan"
        self.directory = self.board + "-" + self.thread_id

    def images(self):
        url  = self.thread_url_fmt.format(self.board, self.thread_id)
        text = self.request(url).text
        for match in re.finditer(self.regex, text):
            url, prefix, fullname, name = match.group(1, 2, 4, 5)
            if url.startswith("/"):
                url = self.url_base + url
            yield (url, prefix + "-" + unquote(fullname or name))
