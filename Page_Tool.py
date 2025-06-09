def wait_for_text_to_disappear(page, text, timeout=10000):
    """
    等待指定文本消失
    :param page: 页面对象
    :param text: 要等待消失的文本
    :param timeout: 超时时间，默认为10秒
    """
    page.wait_for_function(
        f'document.querySelector("body").innerText.includes("{text}") === false',
        timeout=timeout
    )

