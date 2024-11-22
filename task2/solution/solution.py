import csv
import asyncio 
import aiohttp
from collections import defaultdict
from bs4 import BeautifulSoup


dc = defaultdict(int)
flag = True 

async def get_animals_in_page(soup: BeautifulSoup): 
    global flag
    parent_div = soup.find(id="mw-pages")
    items_div = parent_div.find_all("div", class_="mw-category-group")
    for div in items_div:
        items_li = div.find_all("a", title=True)
        s = items_li[0].get("title")[0]
        if 1040 > ord(s) or ord(s) > 1071:
            flag = False 
        else:
            dc[s] += len(items_li) 


async def get_next_page_url(soup: BeautifulSoup):
    url = soup.find(id="mw-pages").find_all("a", recursive=False)[-1].get("href")
    return url 


async def fetch_url(session, url: str):
    async with session.get(url) as r:
        html = await r.text()
        soup = BeautifulSoup(html, features="html.parser")
        await get_animals_in_page(soup)
        return soup

async def main():
    base_url = "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту"
    pages = {base_url}
    async with aiohttp.ClientSession() as session:
        while pages and flag:
            tasks = []
            while pages:
                u = pages.pop()
                tasks.append(fetch_url(session, u))
            for finished_task in asyncio.as_completed(tasks):
                soup = await finished_task
                new_postfix = await get_next_page_url(soup)
                new_url = base_url + new_postfix[new_postfix.find("&"):]
                pages.add(new_url)
                
    write_to_csv()

def write_to_csv():
    with open("res.csv", mode="w", newline="") as f:
        writer = csv.writer(f)
        for a in dc:
            data = [a, dc[a]]
            writer.writerow(data)

if __name__ == "__main__":
    asyncio.run(main())
