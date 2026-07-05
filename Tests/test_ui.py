import pytest
import re

from playwright.sync_api import Page, expect

@pytest.mark.ui

def test_bank_login(page: Page):

    #Arrange
    page.goto('https://demo.applitools.com/')

    #Act
    page.locator('id=username').fill('melissa')
    page.locator('id=password').fill('i<test')
    page.locator('id=log-in').click()

    #Assert
    expect(page.get_by_text('Add account')).to_be_visible()
    expect(page.get_by_text('Make Payment')).to_be_visible()






