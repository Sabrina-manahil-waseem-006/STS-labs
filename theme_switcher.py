import os
from playwright.sync_api import sync_playwright

with open("sample.txt", "w") as f:
    f.write("Sample file content for upload test.")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    page.goto("https://bootswatch.com/default/")
    
    # Click the Themes dropdown using text/role-agnostic locator
    page.get_by_text("Themes", exact=True).click()
    page.get_by_role("link", name="Darkly").click()
    
    page.wait_for_url("**/darkly/*")
    
    new_url = page.url
    print(f"New Page URL: {new_url}")
    assert "darkly" in new_url.lower(), "Error: URL does not contain 'darkly'"
    print("URL check passed: Contains 'darkly'.")
    
    page.locator("input[type='file']").first.set_input_files("sample.txt")
    print("File uploaded successfully.")
    
    textarea_locator = page.locator("textarea.form-control")
    textarea_locator.click()
    page.keyboard.type("Sabrina")
    
    print(f"\nTextarea Element: {textarea_locator}")
    print(f"Textarea Value: {textarea_locator.input_value()}")
    
    browser.close()

if os.path.exists("sample.txt"):
    os.remove("sample.txt")