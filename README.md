# Scrappy\_AI

An **AI-powered web scraper** that extracts, cleans, and parses website data using **Selenium, BeautifulSoup, and Google Gemini API**. Built with a **Streamlit interface** for simplicity.


## Features

* **Scrape any website** using Selenium.
* **Extract & clean body content** (removes scripts, styles, etc.).
* ✂**Split large DOM content** into manageable chunks.
* **AI-powered parsing** with Google Gemini API.
* **Streamlit UI** for easy interaction.

## Tech Stack

* **Python 3.9+**
* [Streamlit](https://streamlit.io/)
* [Selenium](https://www.selenium.dev/)
* [BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/)
* [Google Gemini API](https://ai.google.dev/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)


## Project Structure

```
Scrappy_AI/
│-- main.py          # Streamlit app
│-- scrape.py        # Website scraping & cleaning functions
│-- parser.py        # AI parsing using Gemini
│-- requirements.txt # Dependencies
│-- .env.example     # Environment variables template
```


## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/Scrappy_AI.git
cd Scrappy_AI
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Setup Environment Variables:**

* Create a `.env` file in the project root.
* Add your Gemini API key:

```env
API_KEY=your_google_gemini_api_key_here
```

5. **Install ChromeDriver:**

* Download the correct [ChromeDriver](https://sites.google.com/chromium.org/driver/) for your Chrome version.
* Place it in the project folder as `chromedriver.exe`.


## Usage

Run the Streamlit app:

```bash
streamlit run main.py
```

### Workflow:

1. Enter a website URL.
2. Click **Scrape Website** → view extracted DOM.
3. Describe what you want to parse (e.g., *Extract all email addresses*).
4. Click **Parse Content** → AI extracts requested data.


## Demo

<p align="center">
  <img src="Scrappy_AL/Demo.gif" width="450" alt="AI web scrapper demo" />
</p>


## Notes

* The free Gemini API has usage limits → avoid scraping huge websites in one go.
* Selenium may require Chrome to be installed on your system.
* Works best with structured websites.


## Acknowledgements

* [Streamlit](https://streamlit.io/)
* [Selenium](https://www.selenium.dev/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
* [Google Gemini API](https://ai.google.dev/)


### ⭐ If you like this project, give it a star on GitHub!
