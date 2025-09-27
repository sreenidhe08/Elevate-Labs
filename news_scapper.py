import requests
from bs4 import BeautifulSoup
def scrape_headlines(url):
    response = requests.get(url)
    if response.status_code!=200:
        print("Failed to retrieve the webpage.")
        return
    soup=BeautifulSoup(response.text,'html.parser')
    headlines=soup.find_all('h2') #Assuming headlines are in <h2> tags

    with open("headlines.txt",'w',encoding="utf-8") as f:
        for headline in headlines:
            f.write(headline.get_text().strip()+'\n')
    print("Headlines saved")

if __name__=="__main__":
    url="https://indianexpress.com"
    scrape_headlines(url)