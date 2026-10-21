from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Must be headless=True for GitHub Codespaces
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    # 1. Open the website
    page.goto("https://bootswatch.com/default/")
    
    print(f"Website: {page.title()}")
    
    # 2. Fill the Email (Locator Type 1: CSS selector / ID)
    page.locator("#exampleInputEmail1").fill("sabrina@example.com")
    
    # 3. Fill the Password (Locator Type 2: Unique ID selector to avoid strict mode violation)
    page.locator("#exampleInputPassword1").fill("Test@12345")
    
    # 4. Choose 3 in Example select (Locator Type 3: get_by_role)
    page.get_by_role("combobox", name="Example select").select_option("3")
    
    # 5. Choose 2 and 5 in Example multiple select (Locator Type 4: CSS class with nth index)
    page.locator("select.form-select").nth(2).select_option(["2", "5"])
    
    # 6. Write a message in the textarea
    page.locator("textarea.form-control").fill("My name is Sabrina Manahil Waseem and i am doing my STS lab 05 right now")
    
    # 7. Select the second radio button
    page.locator("#optionsRadios2").check()
    
    # 8. Tick the Default checkbox
    page.get_by_label("Default checkbox").check()
    
    # 9. Turn on the Default switch
    page.get_by_label("Default switch checkbox input").check()
    
    print("\nFORM RESULTS")
    print(f"Email: {page.locator('#exampleInputEmail1').input_value()}")
    print(f"Password: {page.locator('#exampleInputPassword1').input_value()}")
    print(f"Example select: {page.get_by_role('combobox', name='Example select').input_value()}")
    print(f"Multiple select: {page.locator('select.form-select').nth(2).evaluate('(el) => Array.from(el.selectedOptions).map(o => o.value)')}")
    print(f"Textarea: {page.locator('textarea.form-control').input_value()}")
    print(f"Second Radio Selected: {page.locator('#optionsRadios2').is_checked()}")
    print(f"Default Checkbox Checked: {page.get_by_label('Default checkbox').is_checked()}")
    print(f"Default Switch Checked: {page.get_by_label('Default switch checkbox input').is_checked()}")
    
    browser.close()