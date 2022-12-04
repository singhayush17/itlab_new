import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/90.0.4430.212 Safari/537.36',
'Accept-Language': 'en-US, en;q=0.5'})

# user define function
# Scrape the data

def getdata(url):
    r = requests.get(url, headers=HEADERS)
    return r.text

def html_code(url):

    # pass the url
    # into getdata function
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')

    # display html code
    return (soup)

url ="https://www.flipkart.com/sony-zv-e10l-mirrorless-camera-body-1650-mm-power-zoom-lens-vlog/p/itmed07cbb694444?pid=DLLG6G8U8P2NGEHG&lid=LSTDLLG6G8U8P2NGEHGGVZNLB&marketplace=FLIPKART&store=jek%2Fp31%2Ftrv&srno=b_1_1&otracker=hp_omu_Best%2Bof%2BElectronics_2_3.dealCard.OMU_Q5LU1U8PHMK6_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_2_NA_view-all_3&fm=neo%2Fmerchandising&iid=bcbff080-c21e-4657-a547-ef169105be65.DLLG6G8U8P2NGEHG.SEARCH&ppt=hp&ppn=homepage&ssid=sae541zqls0000001670131941010"

soup = html_code(url)

#print(soup)

def cus_data(soup):
    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""
    cus_list = []

    for item in soup.find_all("span", class_="a-profile-name"):
        data_str = data_str + item.get_text()
        cus_list.append(data_str)
        data_str = ""
    return cus_list

cus_res = cus_data(soup)
# print(cus_res)

def cus_rev(soup):
    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""

    for item in soup.find_all("div", class_="a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container"):
        data_str = data_str + item.get_text()
    result = data_str.split("\n")
    return (result)

rev_data = cus_rev(soup)
rev_result = []

for i in rev_data:
    if i == "":
        pass
    else:
        rev_result.append(i)
print((rev_result[0]))