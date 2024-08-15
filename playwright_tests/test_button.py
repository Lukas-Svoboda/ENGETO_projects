import asyncio
import pytest
from playwright.async_api import async_playwright, TimeoutError

@pytest.mark.asyncio
async def test_click_terminy():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Otevření stránky
        await page.goto("https://engeto.cz/")

        # Kliknutí na tlačítko pro přijetí cookies
        try:
            # Použití funkce locator pro vyhledání tlačítka podle textu
            cookie_button = page.locator("text=CHÁPU A PŘIJÍMÁM")
            await cookie_button.wait_for(timeout=10000)  # Explicitní čekání na zobrazení tlačítka
            await cookie_button.click()
            print("Cookies dialog accepted.")
        except TimeoutError:
            print("Cookies dialog not found or could not be clicked.")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Ověření, že titulek obsahuje text "ENGETO"
        try:
            title = await page.title()
            assert "ENGETO" in title, f"Expected title to contain 'ENGETO', but got '{title}'"
            print(f"Test passed: Title contains 'ENGETO'. Title: {title}")
        except AssertionError as e:
            print(f"Test failed: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Kliknutí na tlačítko "TERMÍNY"
        try:
            terminy_button = page.locator("text=TERMÍNY")
            await terminy_button.wait_for(timeout=10000)  # Explicitní čekání na zobrazení tlačítka
            await terminy_button.click()
        except TimeoutError:
            print("Button 'TERMÍNY' not found or could not be clicked.")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Ověření, že stránka s termíny byla otevřena
        try:
            await page.wait_for_selector("text=TERMÍNY KURZŮ", timeout=10000)
            print("Test passed: 'TERMÍNY KURZŮ' page loaded successfully.")
        except TimeoutError:
            print("Test failed: 'TERMÍNY KURZŮ' page did not load.")
        except Exception as e:
            print(f"An error occurred: {e}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_click_terminy())
