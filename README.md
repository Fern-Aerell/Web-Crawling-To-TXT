  # Web Crawling To TXT

  <p align="center">
    <img src="designs/icon/icon.png" alt="icon" width="250" height="250">
  </p>

  Proyek ini adalah sebuah aplikasi web crawling asynchronous yang ditulis dalam bahasa Python. Aplikasi ini dapat melakukan crawling pada sebuah situs web, mengumpulkan URL yang valid, dan mengekstrak konten dari setiap URL tersebut.

  ## Fitur

  - Crawling URL secara asynchronous dalam domain yang sama
  - Ekstraksi konten teks dari setiap halaman web
  - Penyimpanan hasil crawling dalam format TXT
  - Pembersihan teks yang diekstrak

  ## Persyaratan

  Untuk menjalankan aplikasi ini, Anda memerlukan:

  - Python 3.x
  - Beberapa library Python yang dapat diinstal menggunakan pip:
    - aiohttp
    - beautifulsoup4
    - lxml

  Anda dapat menginstal semua dependensi dengan menjalankan:


  pip install aiohttp beautifulsoup4 lxml


  ## Penggunaan

  Untuk menjalankan aplikasi, gunakan perintah berikut di terminal:


  python webcrawling2txt.py <base_url> <output_file>


  Dimana:
  - `<base_url>` adalah URL dasar situs web yang ingin Anda crawl
  - `<output_file>` adalah nama file output (tanpa ekstensi .txt)

  Contoh:


  python webcrawling2txt.py https://www.example.com hasil_crawling


  Hasil crawling akan disimpan dalam file TXT dengan nama `hasil_crawling.txt`.

  ## Struktur Proyek

  - `webcrawling2txt.py`: File utama yang berisi semua fungsi untuk melakukan web crawling
    - `clean_text()`: Fungsi untuk membersihkan teks yang diekstrak
    - `crawl_url()`: Fungsi asynchronous untuk melakukan crawling URL
    - `crawl_website()`: Fungsi utama yang menjalankan proses crawling dan menyimpan hasilnya
    - `main()`: Fungsi untuk menangani argumen command line dan menjalankan crawling

  ## Catatan

  - Pastikan untuk mematuhi kebijakan dan persyaratan layanan dari situs web yang Anda crawl.
  - Gunakan aplikasi ini dengan bijak dan bertanggung jawab.
  - Aplikasi ini menggunakan asyncio dan aiohttp untuk melakukan crawling secara asynchronous, yang dapat meningkatkan kinerja pada situs web dengan banyak halaman.

  ## Kontribusi

  Kontribusi untuk proyek ini sangat diterima. Jika Anda memiliki saran atau perbaikan, silakan buat pull request atau buka issue.

  ## Lisensi

  [MIT License](LICENSE)