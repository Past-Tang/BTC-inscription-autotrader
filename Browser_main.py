from playwright.sync_api import sync_playwright, Playwright
import os
import time
import shutil
from Context_Tool import *
from Page_Tool import *

# 上下文目录
USER_DATA_DIR = os.path.join(os.path.dirname(__file__), "chrome_user_data")
EXTENSION_PATH = os.path.join(os.path.dirname(__file__), "unisat-chrome-mv3-v1.3.4")

def handle_popup(page):
    """
    处理弹出窗口
    :param page: 弹出窗口的页面对象
    """
    if "chrome-extension://" in page.url:
        page.wait_for_load_state("networkidle")
        if "Signature request" in page.content():
            div_selector = 'div[style*="background-color: rgb(227, 187, 95); height: 40px;"] div:has-text("Sign")'
            page.wait_for_selector(div_selector, state="visible")
            page.click(div_selector)
            return
        elif "Sign Transaction" in page.content():
            div_selector = 'div[style*="background-color: rgb(227, 187, 95); height: 40px;"] div:has-text("Sign")'
            page.wait_for_selector(div_selector, state="visible")
            page.click(div_selector)
            return
        elif "Connect with UniSat Wallet" in page.content():
            connect_element = page.locator(
                'div[style="font-size: 14px; line-height: normal; font-family: Inter-Bold; color: rgb(0, 0, 0); text-align: center; user-select: none; flex-shrink: 1; flex-grow: 0; z-index: 2; padding-left: 4px; padding-right: 4px;"]').first
            connect_element.wait_for(state="visible", timeout=30000)
            connect_element.click()
            return

def run(playwright: Playwright):
    """
    主运行函数
    :param playwright: Playwright实例
    """
    context = playwright.chromium.launch_persistent_context(
        USER_DATA_DIR,
        headless=False,
        args=[
            '--disable-blink-features=AutomationControlled',
            f"--disable-extensions-except={EXTENSION_PATH}",
            f"--load-extension={EXTENSION_PATH}",
        ],
        ignore_default_args=['--enable-automation']
    )
    context.on("page", handle_popup)

    context, Wallet_page, page, task_list = Login_Wallet(context)

    page.goto("https://magiceden.io/runes/UNCOMMON%E2%80%A2GOODS")
    time.sleep(2)
    [p.close() for p in context.pages if p.url == 'about:blank']
    Sell_page = next((page for page in context.pages if "Bitcoin" in page.title()), None)
    Sell_page.bring_to_front()

    print(task_list)
    for i in task_list:
        if Next_wallet(Wallet_page, i[0], i[1]) == True:
            time.sleep(2)
            Sell_page.evaluate('''
                const targetDiv = document.querySelector('div[data-test-id="wallet-balance"]');
                if (targetDiv) {
                    targetDiv.click();
                }
                const elements = document.querySelectorAll('p.tw-flex.tw-items-center');
                const logoutButton = Array.from(elements).find(el => el.textContent.trim() === 'Log out');
                if (logoutButton) {
                    logoutButton.click();
                }
            ''')
            time.sleep(2)
            if 'data-test-id="wallet-connect-button"' in page.content():
                log_out_button = Sell_page.locator('span.typography--button-secondary:has-text("Log out")')
                if log_out_button.is_visible():
                    log_out_button.click()
                Sell_page.wait_for_selector('div.tw-hidden.md\\:tw-flex', state="visible")
                Sell_page.click('div.tw-hidden.md\\:tw-flex')
                Sell_page.click('span:has-text("UniSat")')
                wait_for_text_to_disappear(Sell_page, 'Connect Wallet', timeout=20000)
                print("网站登录钱包成功")
                sell_button = Sell_page.locator(
                    'div.tw-text-sm.tw-text-light-gray-400.tw-flex.tw-items-end.tw-transition.tw-cursor-pointer.tw-shrink-0.hover\\:tw-opacity-80 >> text=Sell')
                sell_button.click()
                print("点击了 'Sell' 按钮")

    input("按回车继续")

    context.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)