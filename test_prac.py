import pytest
from playwright.sync_api import sync_playwright, Page

def test_dynamic1(page:Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")

    table=page.locator('//table[@class="table table-striped"]') #xpath for table

    rows = page.locator('//table[@class="table table-striped"]/tbody/tr').all()

    for row in rows:
        print(row.inner_text())
        process=row.locator("td").nth(0).inner_text()
        if process=="Chrome":
            cpu_load=row.locator("td:has-text('%')").inner_text()





    #     print(row.inner_text())

    # tds=page.locator('//table[@class="table table-striped"]/tbody/tr/td').all()
    #
    # for td in tds:
    #     print(td.inner_text())

