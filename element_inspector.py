from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    print(f"Loaded Website: {page.title()}\n")
    
    print("1. Heading 3 Heading")
    loc_h3_getby = page.get_by_role("heading", name="Heading 3", exact=True)
    print(f"get_by_role count: {loc_h3_getby.count()}")
    loc_h3_getby.highlight()
    
    loc_h3_css = page.locator("h3:has-text('Heading 3')")
    print(f"CSS selector count: {loc_h3_css.count()}")
    loc_h3_css.highlight()
    
    print("\n2. Large Button")
    loc_btn_getby = page.get_by_role("button", name="Large button")
    print(f"get_by_role count: {loc_btn_getby.count()}")
    loc_btn_getby.highlight()
    
    loc_btn_css = page.locator("button.btn-lg, a.btn-lg").first
    print(f"CSS selector count: {loc_btn_css.count()}")
    loc_btn_css.highlight()
    
    print("\n3. Disabled Input")
    loc_input_getby = page.get_by_placeholder("Disabled input")
    print(f"get_by_placeholder count: {loc_input_getby.count()}")
    loc_input_getby.highlight()
    
    loc_input_css = page.locator("input.form-control[disabled]")
    print(f"CSS selector count: {loc_input_css.count()}")
    loc_input_css.highlight()
    
    print("\n4. Home Link in Blue Navigation Bar")
    loc_nav_getby = page.locator(".navbar.bg-primary").get_by_role("link", name="Home")
    print(f"get_by chain count: {loc_nav_getby.count()}")
    loc_nav_getby.highlight()
    
    loc_nav_xpath = page.locator("//nav[contains(@class, 'bg-primary')]//a[contains(text(), 'Home')]")
    print(f"XPath selector count: {loc_nav_xpath.count()}")
    loc_nav_xpath.highlight()
    
    print("\n5. Third Source Title Citation")
    loc_cite_getby = page.get_by_text("Source Title").nth(2)
    print(f"get_by_text count (nth=2): {loc_cite_getby.count()}")
    loc_cite_getby.highlight()
    
    loc_cite_xpath = page.locator("(//cite[@title='Source Title'])[3]")
    print(f"XPath selector count (3rd): {loc_cite_xpath.count()}")
    loc_cite_xpath.highlight()
    
    print("\nAll locators successfully verified and highlighted!")
    browser.close()