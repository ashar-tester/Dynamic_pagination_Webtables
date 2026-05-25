import pytest
from playwright.sync_api import sync_playwright, Page

def test_dynamic(page:Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")

    table=page.locator('//table[@class="table table-striped"]') #xpath for table

    rows = page.locator('//table[@class="table table-striped"]/tbody/tr').all()


    for row in rows:

        elements=row.locator("td").nth(0).inner_text()
        el1=row.locator("td").all()
        for el2 in el1:
            print(el2.inner_text())
        #print(el2)
        if elements == "Chrome":
            cpu_load=row.locator("td:has-text('%')").inner_text()

            break


    #print("CPU Load=", cpu_load)
    page.wait_for_timeout(2000)
