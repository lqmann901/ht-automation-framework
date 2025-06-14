from playwright.sync_api import sync_playwright

class DriverFactory:
    @staticmethod
    def get_browser(browser_type = "chromium", headless=True):
        playwright = sync_playwright().start() #Start Playwright
        if not playwright:
            raise Exception("Playwright failed to start")
        
        # Launch the browser based on the specified type
        if browser_type == "chromium":
            browser = playwright.chromeium.launch(headless=headless) #headless = True means no GUI
        elif browser_type == "firefox":
            browser = playwright.firefox.launch(headless=headless)
        elif browser_type == "webkit":
            browser = playwright.webkit.launch(headless=headless)
        else:
            raise Exception(f"Unsupported browser type: {browser_type}")
        context= browser.new_context
        page = context.new_page() # Create a new page in the browser context
        return playwright, browser, context, page # Return the created objects
    