# Web Crawling To TXT

<p align="center">
  <img src="designs/icon/icon.png" alt="icon" width="250" height="250">
</p>

This project is an asynchronous web crawling application written in Python. The application can crawl a website, collect valid URLs, and extract content from each URL.

## Features

- Asynchronous URL crawling within the same domain  
- Text content extraction from each web page  
- Saving crawl results in TXT format  
- Cleaning extracted text  

## Requirements

To run this application, you need:

- Python 3.x  
- Several Python libraries that can be installed using pip:  
  - aiohttp  
  - beautifulsoup4  
  - lxml  

You can install all dependencies by running:

```sh
pip install aiohttp beautifulsoup4 lxml
```

## Usage

To run the application, use the following command in the terminal:

```sh
python webcrawling2txt.py <base_url> <output_file>
```

Where:  
- `<base_url>` is the base URL of the website you want to crawl  
- `<output_file>` is the output file name (without the .txt extension)  

Example:

```sh
python webcrawling2txt.py https://www.example.com crawl_results
```

The crawl results will be saved in a TXT file named `crawl_results.txt`.

## Project Structure

- `webcrawling2txt.py`: Main file containing all functions for web crawling  
  - `clean_text()`: Function to clean the extracted text  
  - `crawl_url()`: Asynchronous function for crawling URLs  
  - `crawl_website()`: Main function that performs crawling and saves the results  
  - `main()`: Function to handle command-line arguments and run the crawling process  

## Notes

- Make sure to comply with the policies and terms of service of the websites you crawl.  
- Use this application responsibly and ethically.  
- This application uses asyncio and aiohttp for asynchronous crawling, which improves performance on websites with many pages.  

## Contribution

Contributions to this project are welcome. If you have suggestions or improvements, feel free to submit a pull request or open an issue.  

## License

[MIT License](LICENSE)  
