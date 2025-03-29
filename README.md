
# Scrappus :space_invader:

A flexible, Dockerized web scraper that supports both static and dynamic websites using Selenium (Chrome or Firefox). Extraction is rule-based via JSON, and supports multiple output formats like JSON and CSV.
Scrappus is developed in **python**. If you want to learn about web scrapping you can check this [article](https://medium.com/@joerosborne/intro-to-web-scraping-build-your-first-scraper-in-5-minutes-1c36b5c4b110), you need to know basics or HTML5 tags to define the **rules.json** file who includes the specifications to start getting the data from the target.

---
## 📦 Features

- Supports static and JavaScript-rendered (dynamic) websites
- Rule-based scraping via JSON file
- Output to JSON or CSV
- Dockerized for easy setup
- Supports Chrome and Firefox headless modes

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/kur0bai/scrappus.git
cd scrappus
```

### 2. Create your rules

Feed the ***rules.json*** file with the required or desired rules to extract data, for example:
```
{
	"title": "h3",
	"description": "meta[name='description']",
	"modules": "div[class='container']",
	"links": "a[href]"
}
```

### 3. Run in Docker or traditional way

Docker: 
- Create an image: `docker build -t scrappus .`
- Execute it: ``docker run --rm scrappus "https://example.com" "rules.json"  --output output.json --dynamic``

Traditional:

- Install requirements (python virtual enviroment recommended): `pip install requirements.txt`
- Run the script using: `python3 main.py` to see the help commands.

Easy right? :fish_cake:
***You should see the results on the output file you defined before.***


### Important:  :pushpin:
I want to clarify that this tool is open to modifications if necessary for the usefulness of those who are interested. However, I am not responsible if it is used for malicious purposes, as it is not the idea. Use it under your own responsibility.
Without further ado I hope this can help your projects.
