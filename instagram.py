import requests, re

def downloadImage(url):
    r = requests.get(url)
    with open('images/test.jpg','wb') as f:
        f.write(r.content)

def isInstagramUrl(url):
    # Here, we haven't considered the case that there might be loads of text along with an instagram url.
    pattern = '(.*?)instagram.com/p/(.*?)\/'
    if(re.match(pattern,url)):
        return True
    else:
        return False
def getImageLink(url):
    regular_expression = '\<meta property=\"og:image\" content\=\"(.*?)\"'
    # via some regex, we can also get the caption of the image
    response = requests.get(url)
    if(response.ok):
        htmlData = response.text
        image_url = re.findall(regular_expression,htmlData)
        image_url = (''.join(image_url)).rstrip()
    return image_url

if __name__ == '__main__':
    print(isInstagramUrl('https://www.instagram.com/'))
    print(isInstagramUrl('https://www.instagram.com/p/B3uih6LHfZ7/'))
