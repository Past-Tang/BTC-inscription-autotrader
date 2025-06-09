def get_extension_id(context):
    """
    获取 Manifest V3 扩展的ID
    :param context: 浏览器上下文
    :return: 扩展ID
    """
    try:
        if context.service_workers:
            background = context.service_workers[0]
        else:
            background = context.wait_for_event("serviceworker", timeout=10000)
        extension_id = background.url.split("/")[2]
        return extension_id
    except:
        return None


def Login_Wallet(context):
    """
        登录钱包页面的函数。
        :param context: 包含页面和追踪等信息的上下文对象。
        :return: 返回上下文对象、钱包页面对象和新打开的页面对象。
        """
    page = context.new_page()
    page.wait_for_timeout(3000)
    Wallet_page = next((page for page in context.pages if page.title() == "UniSat Wallet"), None)
    Wallet_page.fill('input[type="password"][placeholder="Password"]',
                     "mrgCxXDegURqgELYKHYcHdAhNBRMOO0usnV31be1iNEgNea1FmeyXdtMKZsRheFd")
    Wallet_page.get_by_text("Unlock").click()
    Wallet_page.get_by_text("Send").wait_for()

    element = Wallet_page.locator('xpath=//*[@id="root"]/div[1]/div/div[2]/div/div[1]/div[3]/div')
    element.wait_for(state="visible", timeout=30000)
    element.click()

    Wallet_page.wait_for_selector('div[data-id="list"]')
    list_div = Wallet_page.query_selector('div[data-id="list"]')
    task_list=[]
    if list_div:
        row_containers = list_div.query_selector_all('.row-container')
        for row in row_containers:
            account_name = row.query_selector('div:nth-child(2) > div:nth-child(1)').inner_text()  # Account名称
            address = row.query_selector('div:nth-child(2) > div:nth-child(2)').inner_text()  # 地址信息
            task_list.append([account_name, address])
        row_containers[0].query_selector('div:nth-child(2) > div:nth-child(1)').click() #钱包归一操作
    page.wait_for_timeout(1000)
    print("UniSat钱包与本次任务清单初始化完成",f'- 共计{len(task_list)}个子钱包.')
    return context, Wallet_page, page, task_list


# 钱包操作
def Next_wallet(Wallet_page,account_name, address):
    Wallet_page.wait_for_load_state("networkidle")
    element = Wallet_page.locator('xpath=//*[@id="root"]/div[1]/div/div[2]/div/div[1]/div[3]/div')
    element.wait_for(state="visible", timeout=30000)
    element.click()
    Wallet_page.wait_for_selector('div[data-id="list"]')
    list_div = Wallet_page.query_selector('div[data-id="list"]')
    if list_div:
        row_containers = list_div.query_selector_all('.row-container')
        for row in row_containers:
            name = row.query_selector('div:nth-child(2) > div:nth-child(1)').inner_text()  # Account名称
            if name == account_name:
                row.query_selector('div:nth-child(2) > div:nth-child(1)').click()
                break
    Wallet_page.get_by_text("Send").wait_for()
    Wallet_page.get_by_text(f"{account_name}").wait_for()
    print(f'已经切换到{account_name}钱包 - 验证成功')
    return True

