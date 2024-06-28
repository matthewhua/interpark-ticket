import asyncio
import nodriver as uc
from infodemo import *

async def main():
    browser = await uc.start()
    page = await browser.get('https://www.nowsecure.nl')

    await page.save_screenshot()
    await page.get_content()
    await page.scroll_down(150)
    elems = await page.select_all('*[src]')
    for elem in elems:
        await elem.flash()

    page2 = await browser.get('https://twitter.com', new_tab=True)
    page3 = await browser.get('https://github.com/ultrafunkamsterdam/nodriver', new_window=True)

    for e in (page, page2, page3):
        await e.bring_to_front()
        await e.scroll_down(200)
        await e     # wait for events to be processed
        await e.reload()
        if e != page3:
            await e.close()


if __name__ == '__main__':


    # since asyncio.run never worked (for me)
    uc.loop().run_until_complete(main())