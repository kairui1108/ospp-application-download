import time
import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from get_urls import get_map


base_dir = "E:\\python\\pdfdownload\\total\\"


def init_browser_on_window():
    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('prefs', {
        "download.default_directory": base_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    })
    return_browser = webdriver.Chrome(options=options)
    return_browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
    })
    return return_browser


def download(browser, pro_id, dir_name):

    sub_dir = None
    try:
        sub_dir = os.path.join(base_dir, dir_name)
        os.makedirs(sub_dir, exist_ok=True)
    except:
        sub_dir = "AAA"
    browser.execute_cdp_cmd('Page.enable', {})
    browser.execute_cdp_cmd('Network.enable', {})
    browser.execute_cdp_cmd('Page.setDownloadBehavior', {
        'behavior': 'allow',
        'downloadPath': sub_dir
    })
    # 访问指定的URL
    url = "https://summer-ospp.ac.cn/previewPdf/" + str(pro_id)
    browser.get(url)
    time.sleep(5)

    # 获取id为content的元素
    content_element = browser.find_element(By.ID, "ifm")
    pdf_url = content_element.get_attribute("src")
    browser.get(pdf_url)
    print(dir_name + "  下载完成... ...")
    time.sleep(3)


if __name__ == "__main__":
    b = init_browser_on_window()
    # download(b, 1974, "NebulaGraph Exchange 提供批量删除能力")
    map_dict = get_map()
    for key in map_dict:
        download(b, map_dict[key], key)
