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

def magmaeruption(page = 1):
    result = {}
    web = asyncio.run(link("https://magma.esdm.go.id/v1/gunung-api/informasi-letusan"))
    HTMLResult = BeautifulSoup(web, "html.parser") 
    pageHTML = int(HTMLResult.find('div', class_="ui pagination menu").find_all('a')[7].get_text(strip=True))+1
    if page == "all":
        totalpage = pageHTML
    elif isinstance(page, int):
        if page < 0:
            totalpage = 1
        elif page > pageHTML:
            totalpage = pageHTML
        else:
            totalpage = page
    else:
        totalpage = 1
    month = {"Januari":"January","Februari":"February","Maret":"March","April":"April","Mei":"May","Juni":"June","Juli":"July","Agustus":"August","September":"September","Oktober":"October","November":"November","Desember":"December"}
    day = {"Senin":"Monday","Selasa":"Tuesday","Rabu":"Wednesday","Kamis":"Thursday","Jumat":"Friday","Sabtu":"Saturday","Minggu":"Sunday"}
    judul = ""
    checking = 0
    while checking < totalpage:
        web = asyncio.run(link(f"https://magma.esdm.go.id/v1/gunung-api/informasi-letusan?page={checking+1}"))
        HTMLResult = BeautifulSoup(web, "html.parser") 
        content = HTMLResult.find_all('div', class_="timeline-item")
        for i in content:
            if len(i.attrs['class']) >= 2:
                date = ((i.find('p', class_="timeline-date")).get_text(strip=True).split(", "))[1].split(" ")
                if date[0] in list(day.keys()):
                    date = (i.get_text(strip=True).split(", ")[2]).split(" ")
                date[1] = str(list(month.keys()).index(date[1])+1)
                judul = f"{date[1]}-{date[0]}-{date[2]}"
                if judul not in result:
                    result[judul] = {}
            else:
                clock = i.find('div', class_="timeline-time").get_text().split(" ")

                if clock[1] in result[judul].keys():
                    result[judul][clock[1]].update({clock[0]: {"volcano_name": i.find('p', class_="timeline-title").get_text()}})
                else:
                    result[judul][clock[1]] = {clock[0]:{"volcano_name": i.find('p', class_="timeline-title").get_text()}}
                result[judul][clock[1]][clock[0]].update({"author": i.find_next(class_="timeline-author").get_text().replace("Dibuat oleh ","")})
                result[judul][clock[1]][clock[0]].update({"information": i.find('p', class_="timeline-text").get_text(strip=True).replace("  ","")})
                result[judul][clock[1]][clock[0]].update({"image": i.find('img', class_="bd img-fluid")['src']})
                result[judul][clock[1]][clock[0]].update({"detail": i.find('a', class_="btn btn-sm btn-outline-primary")['href']})
        checking += 1
    return result


def magmadetail():
    result = magmalevelonly()
    for i in result:
        for j in result[i]:
            detailresult = {}
            web = asyncio.run(link(result[i][j]["link"]))
            HTMLResult = BeautifulSoup(web, "html.parser").find('div', class_="col-lg-12")
            detailresult["title"] = HTMLResult.find('h5', class_="card-title tx-dark tx-medium mg-b-10").get_text(strip=True)
            detailresult["author"] = (HTMLResult.find('p', class_="card-subtitle tx-normal mg-b-15").get_text(strip=True)).split(", ")[1]
            detailresult["location"] = HTMLResult.find('p', class_="col-lg-6 pd-0").get_text(strip=True)
            try:
                asyncio.run(link(HTMLResult.find('img', class_="img-fluid")['src']))
                detailresult["image"] = None
            except:
                detailresult["image"] = HTMLResult.find('img', class_="img-fluid")['src']
            detailresult["visual_observation"] = (HTMLResult.find('div', class_="media-body").find('p')).get_text(strip=True)
            detailresult["other_description"] = (HTMLResult.find('div', class_="media pd-30").find('p')).get_text(strip=True)
            sameclass = HTMLResult.find_all('div', class_="card pd-30")
            detailresult["climatology"] = sameclass[0].get_text(strip=True)
            detailresult["seismic_observation"] = sameclass[1].get_text(strip=True)
            detailresult["recommendation"] = sameclass[2].get_text(strip=True)
            result[i][j]["detail"] = detailresult
    return result
