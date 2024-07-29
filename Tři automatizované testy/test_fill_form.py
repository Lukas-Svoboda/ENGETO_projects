from playwright.sync_api import sync_playwright

def test_form_submission():
    with sync_playwright() as p:
        # Spuštění prohlížeče
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Otevření stránky
        page.goto("https://test-intro.engeto.com/")
        
        # Čekání na načtení stránky
        page.wait_for_load_state("networkidle")
        
        # Vyplnění políčka "First Name"
        page.fill('input[name="firstname"]', 'Lukáš')
        
        # Vyplnění políčka "City"
        page.fill('input[name="city"]', 'Brno')
        
        # Kliknutí na tlačítko pro odeslání
        page.click('input[type="submit"]')
        
        # Zavření prohlížeče
        browser.close()

if __name__ == "__main__":
    test_form_submission()
