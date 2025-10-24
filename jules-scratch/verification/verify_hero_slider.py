from playwright.sync_api import sync_playwright
import os

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    filepath = "file://" + os.path.abspath("index.html").replace("\\", "/")
    page.goto(filepath)
    hero_section = page.locator("#home")
    hero_section.screenshot(path="jules-scratch/verification/verification.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
