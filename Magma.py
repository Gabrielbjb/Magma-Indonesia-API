import aiohttp, asyncio
from bs4 import BeautifulSoup

async def link(link):
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resp:
            return await resp.text()

def magmalevelonly():
    result = {}
    web = asyncio.run(link('https://magma.esdm.go.id/v1/gunung-api/tingkat-aktivitas'))
    HTMLResult = ((BeautifulSoup(web, "html.parser").find_all('div',  class_= "table-responsive")[0]).find('tbody'))
    linkcheck = 0
    judul2 = ""
    url = []
    def ceking(HTMLResult):
            for ip in HTMLResult.find_all('a', class_="tx-inverse tx-14 tx-medium d-block"):
                judul = ip.get_text(strip=True)
                if judul in j.get_text(strip=True):
                    return False, judul
            return True, judul2
    def checkinglink(k):
        for l in k.find_all('a', href=True, class_=False):
            url.append(l['href'])
    for i in HTMLResult.find_all('tr'):
        for j in i.find_all('td'):
            tes, judul = ceking(HTMLResult)
            checkinglink(j)
            judul2 = judul
            if tes and not (j.get_text(strip=True)).isnumeric():
                gunung = (j.get_text(strip=True)).replace("Lihat laporan","").split(" - ")
                result[judul2][gunung[0]] = {"location":gunung[1],"link":url[linkcheck]}
                linkcheck += 1
            elif tes == False:
                result[judul2] = {}
    return result

def magmadetail():
    result = magmalevelonly()
    for i in result:
        for j in result[i]:
            detailresult = {}
            web = asyncio.run(link(result[i][j]["link"]))
            HTMLResult = BeautifulSoup(web, "html.parser").find('div', class_="col-lg-12")
            titleanddate = (HTMLResult.find('h5', class_="card-title tx-dark tx-medium mg-b-10").get_text(strip=True)).split(", ")
            detailresult["title"] = titleanddate[0]
            detailresult["date"] = titleanddate[1]
            detailresult["period"] = titleanddate[2].replace("periode ","")
            detailresult["author"] = (HTMLResult.find('p', class_="card-subtitle tx-normal mg-b-15").get_text(strip=True)).split(",  ")[1]
            detailresult["location"] = HTMLResult.find('p', class_="col-lg-6 pd-0").get_text(strip=True)
            try:
                asyncio.run(link(HTMLResult.find('img', class_="img-fluid")['src']))
                detailresult["image"] = None
            except:
                detailresult["image"] = HTMLResult.find('img', class_="img-fluid")['src']
            detailresult["visual_observation"] = (HTMLResult.find('div', class_="media-body").find('p')).get_text(strip=True)
            detailresult["other_description"] = (HTMLResult.find('div', class_="media pd-30").find('p')).get_text(strip=True)
            sameclass = HTMLResult.find_all('div', class_="card pd-30")
            detailresult["climatology"] = (sameclass[0].find('p')).get_text(strip=True)
            detailresult["seismic_observation"] = (sameclass[1].find('p')).get_text(strip=True)
            detailresult["recommendation"] = (((sameclass[2].find('p')).get_text(strip=True, separator='\n')).split("\n"))
            result[i][j]["detail"] = detailresult
    return result
