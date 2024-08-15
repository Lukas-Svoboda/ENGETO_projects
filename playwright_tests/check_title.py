import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_page_title():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        url = 'https://engeto.cz/prehled-kurzu/'
        expected_title_selector = "//main[@class='container-child']//h1"
        expected_title_text = "KURZY PROGRAMOVÁNÍ"

        try:
            # Navigace na URL
            await page.goto(url)
            print(f"Navigated to URL: {url}")

            # Wait for the element to be visible
            await page.wait_for_selector(expected_title_selector)
            print(f"Selector found: {expected_title_selector}")

            # Získání textu z elementu pomocí selektoru
            actual_title_text = (await page.locator(expected_title_selector).inner_text()).strip()
            print(f"Actual Title Text: '{actual_title_text}'")

            # Ověření, zda text odpovídá očekávané hodnotě
            assert actual_title_text == expected_title_text, f"Expected title text '{expected_title_text}', but got '{actual_title_text}'"
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise
        finally:
            await browser.close()