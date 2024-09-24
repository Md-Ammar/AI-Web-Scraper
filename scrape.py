import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_website(website):
    options = Options()
    # options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(website)

    html = driver.page_source
    driver.quit()
    
    return html

def extract_body_content(html):
    soup = BeautifulSoup(html, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]


scrape_website("https://www.techwithtim.net/")