
import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get the absolute path to the index.html file
        file_path = os.path.abspath('index.html')

        # Go to the local HTML file
        page.goto(f'file://{file_path}')

        # Take a screenshot of the hero section
        hero_element = page.query_selector('.hero')
        if hero_element:
            hero_element.screenshot(path='jules-scratch/verification/hero_section.png')
        else:
            print("Hero section not found.")

        browser.close()

if __name__ == "__main__":
    run()
