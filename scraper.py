import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig

async def main():
    browser_config = BrowserConfig(verbose=True) # verbose for logging

    run_config = CrawlerRunConfig(
      word_count_threshold=10,        # Minimum words per content block
      exclude_external_links=True,    # Remove external links
      remove_overlay_elements=True,   # Remove popups/modals
      process_iframes=True            # Process iframe content
      )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://www.eu-startups.com/directory/wpbdp_category/luxembourg-based-startups/",
            config=run_config
        )
        print(result.markdown)

asyncio.run(main())


