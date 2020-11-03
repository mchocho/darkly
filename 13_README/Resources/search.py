import sys
import requests
from bs4 import BeautifulSoup

def crawl(url, files):
    request = requests.get(url)
    if (request.status_code != 200):
        return files
    print(url)
    soup = BeautifulSoup(request.text, "html.parser")
    links = soup.find_all("a")
    links.reverse()

    for link in links:
        linkURL = link["href"]

        if (linkURL != "../" and linkURL != "README"):
            newDir = url + linkURL
            files = crawl(newDir, files)
        elif linkURL == "README":
            fileURL = url + "README"
            fileRequest = requests.get(fileURL)
            
            if fileRequest.status_code == 200 and fileRequest.text not in files:
                files.append(fileRequest.text)
        
        if (len(files) == 8):
            break;
    return files

if (len(sys.argv) == 1):
    print("Please enter the url to crawl.")
    sys.exit()

url = sys.argv[1] + ".hidden/"
files = list()
files = crawl(url, files)
    
for elem in files:
    print("\t-", elem)
