"""Scrape gun data from Enter the Gungeon wiki."""
import json
import utils
from bs4 import BeautifulSoup

page_fetcher = utils.PageFetcher("config/urls.json")
guns_page = page_fetcher.fetch_guns_page()

guns_parser = BeautifulSoup(guns_page, "html.parser")

table = guns_parser.find("table", {"class": "wikitable"})

guns = []
for row in table.find_all("tr")[1:]:
    gun_path = row.find_all("td")[1].find("a")["href"]

    gun_page = page_fetcher.fetch_page_by_path(gun_path)
    gun_parser = BeautifulSoup(gun_page, "html.parser")

    info_table = gun_parser.find("table", {"class": "infoboxtable"})
    
    gun = {
        "name": info_table.find("th").text.strip(),
        "type": info_table.find("td").text.strip(),
        "description": info_table.find_all("td")[1].text.strip(),
        "damage": info_table.find_all("td")[2].text.strip(),
        "reload_time": info_table.find_all("td")[3].text.strip(),
        "ammo_capacity": info_table.find_all("td")[4].text.strip(),
        "fire_rate": info_table.find_all("td")[5].text.strip(),
        "range": info_table.find_all("td")[6].text.strip(),
    }
    guns.append(gun)

with open("data/guns.json", "w", encoding="utf-8") as f:
    json.dump(guns, f, ensure_ascii=False, indent=2)
