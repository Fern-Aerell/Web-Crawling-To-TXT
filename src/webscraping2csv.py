import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import csv
import tqdm
import sys

def crawl_url(base_url):
    """
    Melakukan crawling pada URL yang diberikan dan mengumpulkan semua URL yang valid.

    Args:
        base_url (str): URL dasar yang akan di-crawl.

    Returns:
        list: Daftar URL yang berhasil di-crawl.

    Fungsi ini melakukan crawling pada URL dasar yang diberikan, mengikuti tautan
    internal dalam domain yang sama, dan mengumpulkan semua URL yang valid.
    Fungsi ini menggunakan pendekatan breadth-first search untuk melakukan crawling.
    """
    kunjungan = set()
    url_dalam_antrian = set()
    antrian = [base_url]
    url_dalam_antrian.add(base_url)
    base_domain = urlparse(base_url).netloc

    with tqdm.tqdm(total=len(antrian), desc="Crawling URLs", unit="url") as pbar:
        while antrian:
            url = antrian.pop(0)

            if url in kunjungan or '#' in url:
                continue

            if urlparse(url).netloc != base_domain:
                continue

            kunjungan.add(url)

            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.RequestException:
                pbar.update(1)
                continue

            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a'):
                href = link.get('href')
                absolut_url = urljoin(url, href)

                if absolut_url.startswith('http') and urlparse(absolut_url).netloc == base_domain and '#' not in absolut_url and absolut_url not in url_dalam_antrian:
                    try:
                        check_response = requests.head(absolut_url)
                        check_response.raise_for_status()
                        antrian.append(absolut_url)
                        url_dalam_antrian.add(absolut_url)
                    except requests.RequestException:
                        continue

            pbar.update(1)
            pbar.total = len(antrian) + pbar.n

    return list(kunjungan)

def get_url_content(url):
    """
    Mengambil konten teks dari URL yang diberikan.

    Args:
        url (str): URL halaman web yang akan diambil kontennya.

    Returns:
        str: Konten teks dari halaman web, atau None jika gagal mengambil konten.

    Fungsi ini mengambil konten teks dari URL yang diberikan menggunakan
    requests dan BeautifulSoup. Jika terjadi kesalahan saat mengambil
    atau memproses konten, fungsi akan mengembalikan None.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        content = ' '.join(soup.stripped_strings)
        return content
    except requests.RequestException:
        return None

def webscraping(base_url, output_file):
    """
    Fungsi utama untuk melakukan web scraping dan menyimpan hasilnya ke file CSV.

    Args:
        base_url (str): URL dasar situs web yang akan di-scrape.
        output_file (str): Nama file output (tanpa ekstensi .csv).

    Fungsi ini melakukan proses web scraping dengan langkah-langkah berikut:
    1. Melakukan crawling pada URL dasar untuk mendapatkan daftar URL valid.
    2. Mengambil konten dari setiap URL valid.
    3. Menyimpan hasil (URL dan konten) ke dalam file CSV.

    Hasil scraping disimpan dalam format CSV dengan dua kolom:
    "Daftar URL" dan "Isi Konten Di Dalam URL".
    """
    valid_urls = crawl_url(base_url)

    with open(f"{output_file}.csv", 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Daftar URL", "Isi Konten Di Dalam URL"])
        
        for valid_url in tqdm.tqdm(valid_urls, desc="Mengumpulkan data", unit="data"):
            content = get_url_content(valid_url)
            if content is not None:
                writer.writerow([valid_url, content])

    print("Data telah terkumpul!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Penggunaan: python webscraping.py <base_url> <output_file>")
        sys.exit(1)
    
    base_url = sys.argv[1]
    output_file = sys.argv[2]
    webscraping(base_url, output_file)