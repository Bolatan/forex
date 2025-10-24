import os
from playwright.sync_api import sync_playwright, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Navigate to the local HTML file
    file_path = "file://" + os.path.abspath('index.html')
    page.goto(file_path)

    # Set viewport to a mobile size
    page.set_viewport_size({"width": 375, "height": 667})

    # Click the hamburger menu button
    hamburger_button = page.locator("#hamburger-menu")
    expect(hamburger_button).to_be_visible()
    hamburger_button.click()

    # Wait for the mobile navigation to be visible and take a screenshot
    mobile_nav = page.locator("#mobile-nav-container")
    expect(mobile_nav).to_be_visible()
    page.screenshot(path="jules-scratch/verification/verification.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
