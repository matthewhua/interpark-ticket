import random
import string
import logging

import nodriver as uc
from infodemo import *

logging.basicConfig(level=30)

months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]


async def main():
    driver = await uc.start(browser_executable_path=BrowserPath)
    tab = await driver.get("https://x.com/")

    # wait for text to appear instead of a static number of seconds to wait
    # this does not always work as expected, due to speed.
    print('finding the "create account" button')
    create_account = await tab.find("css-1jxf684 r-dnmrzs r-1udh08x r-3s2u2q r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-a023e6 r-rjixqe", best_match=True)

    print('"create account" => click')
    await create_account.click()

    print("finding the email input field")
    email = await tab.select("input[type=email]")

    # sometimes, email field is not shown, because phone is being asked instead
    # when this occurs, find the small text which says "use email instead"
    if not email:
        use_email_instead_ = await tab.find("use email instead")
        # and click it
        await use_email_instead_.click()

        # now find the email field again
        email = await tab.select("input[type=email]")

    randstr = lambda k: "".join(random.choices(string.ascii_letters, k=k))

    # send keys to email field
    print('filling in the "email" input filed')
    await email.send_keys("".join([randstr(8), "@", randstr(8), "com"]))

    # find the name input filed
    print("finding the name input filed")
    name = await tab.select("input[type=text]")

    # again, send random text
    print('filling in the "name" input filed')
    await name.send_keys(randstr(8))

    # since there are 3 select fields on the tab, we can use unpacking
    # to assign each field
    print('finding the "month" , "day" and "year" fields in 1 go')
    sel_month, sel_day, sel_year = await tab.select_all("select")

    # await sel_month.focus()
    print('filling in the "month" input field')
    await sel_month.send_keys(random.choice(months))

    # await sel_day.focus()
    # i don't want to bother with month-lengths and leap years
    print('filling in the "day" input field')
    await sel_day.send_keys(random.randint(0, 28))

    # await sel_year.focus()
    print('filling in the "year" input field')
    await sel_year.send_keys(random.randint(1900, 2022))

    await tab

    # let's handle the cookie nag as well
    cookie_bar_accept = await tab.find("accept all", best_match=True)
    if cookie_bar_accept:
        await cookie_bar_accept.click()

    await tab.sleep(1)

    next_btn = await tab.find(text="next", best_match=True)
    print('clicking the "next" button')
    await next_btn.mouse_click()

    # just wait for same button, before we continue
    await tab.select("[role=button]")

    print('finding "sign up" button')
    signup_btn = await tab.find("sign up", best_match=True)
    # we need the second  one
    print('clicking the "sign up" button')
    await signup_btn.mouse_click()

    print('the rest of the "implementation" is out of scope')

    # further implementation is out of scope
    await tab.sleep(10)
    driver.stop()

    # verification code per mail

if __name__ == "__main__":
    # since asyncio.run never worked (for me)
    # i use
    uc.loop().run_until_complete(main())



