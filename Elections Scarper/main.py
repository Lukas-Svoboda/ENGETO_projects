"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Lukáš Svoboda
email: lukas.svobo1@seznam.cz
"""

import sys
import requests
from bs4 import BeautifulSoup
import csv


def check_arguments():
    if len(sys.argv) != 3:
        print("\n[!] Chyba: Je nutné zadat 2 argumenty:\n- odkaz na územní celek\n- jméno výstupního souboru (např. vysledky.csv)\n")
        sys.exit(1)
    if "volby.cz" not in sys.argv[1]:
        print("\n[!] Chyba: První argument musí být platný odkaz na volby.cz!\n")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]


def get_soup(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def get_municipalities(main_soup):
    municipalities = []
    table = main_soup.find("table", class_="table")
    rows = table.find_all("tr")[2:]

    for row in rows:
        cells = row.find_all("td")
        if len(cells) >= 2:
            code = cells[0].text.strip()
            name = cells[1].text.strip()
            link = cells[0].find("a")["href"]
            municipalities.append((code, name, "https://www.volby.cz/pls/ps2017nss/" + link))
    return municipalities


def get_results(muni_url):
    muni_soup = get_soup(muni_url)

    registered = muni_soup.find("td", headers="sa2").text.replace('\xa0', '').strip()
    envelopes = muni_soup.find("td", headers="sa3").text.replace('\xa0', '').strip()
    valid = muni_soup.find("td", headers="sa6").text.replace('\xa0', '').strip()

    party_votes = []
    tables = muni_soup.find_all("table")
    for table in tables[1:]:
        rows = table.find_all("tr")[2:]
        for row in rows:
            cells = row.find_all("td")
            if len(cells) > 1:
                votes = cells[2].text.replace('\xa0', '').strip()
                party_votes.append(votes)

    return registered, envelopes, valid, party_votes


def write_csv(file_name, headers, data_rows):
    with open(file_name, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data_rows)


def main():
    base_url, output_file = check_arguments()
    main_soup = get_soup(base_url)
    municipalities = get_municipalities(main_soup)

    headers = ["code", "location", "registered", "envelopes", "valid"]
    sample_muni_url = municipalities[0][2]
    sample_registered, sample_envelopes, sample_valid, sample_votes = get_results(sample_muni_url)

    party_count = len(sample_votes)
    party_headers = [f"party_{i+1}" for i in range(party_count)]
    headers.extend(party_headers)

    data_rows = []
    for code, name, muni_url in municipalities:
        registered, envelopes, valid, votes = get_results(muni_url)
        row = [code, name, registered, envelopes, valid] + votes
        data_rows.append(row)

    write_csv(output_file, headers, data_rows)
    print(f"\n[SUCCESS] Data byla úspěšně uložena do souboru '{output_file}'.\n")


if __name__ == "__main__":
    main()

