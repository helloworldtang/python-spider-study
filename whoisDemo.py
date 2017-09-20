import urllib.request
import urllib.error


def download(url):
    print('Downloading:', url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print('Download error:', e.code)
        if hasattr(e, "reason"):
            print('Download error:', e.reason)
        html = None
    return html


print(download('http://baidu.com'))
