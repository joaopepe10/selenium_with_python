import os
import re
import tempfile
import time
from ffmpegaudiorecord import start_recording
from audiotranser import transcribe_audio
from touchtouch import touch
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from a_selenium_iframes_crawler import Iframes
from operagxdriver import start_opera_driver
import random
import rapidfuzz
import undetected_chromedriver as uc
import pandas as pd
from time import sleep
import pytesseract
from PrettyColorPrinter import add_printer
import numpy as np
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

operaPath = r"C:\Users\João Pedro\AppData\Local\Programs\Opera GX\opera.exe"
driverPath = r"C:\operadriver_win64\operadriver.exe"

getiframes = lambda: Iframes(
    driver,
    By,
    WebDriverWait,
    expected_conditions,
    seperator_for_duplicated_iframe="Ç",
    ignore_google_ads=True,
)


def print_elementos():
    driver.switch_to.default_content()
    iframes = getiframes()
    for ini, iframe in enumerate(iframes.iframes):
        try:
            print(f"Frame: {ini} -----------------------------------")
            iframes.switch_to(iframe)
            elemethods = driver.find_elements(By.CSS_SELECTOR, "*")
            print(f"Iframe: {iframe}")
            for ele in elemethods:
                print(ele)
                print(f"{ele.text=}")
                print(f"{ele.tag_name=}")
        except Exception as fe:
            print(fe)
            continue


def get_screenshot_tesser(minlen=2):
    with ScreenshotOfOneMonitor(
            monitor=0, ascontiguousarray=True
    ) as screenshots_monitor:
        img5 = screenshots_monitor.screenshot_one_monitor()
    df = pytesseract.image_to_data(img5, output_type="data.frame")
    df = df.dropna(subset="text")
    df = df.loc[df.text.str.len() > minlen].reset_index(drop=True)
    return df

def buscaElemento():
    didweclick = False
    while not didweclick:
        driver.switch_to.default_content()
        iframes = getiframes()
        for ini, iframe in enumerate(iframes.iframes):
            try:
                print(f"Frame: {ini} -----------------------------------")
                if """[title="reCAPTCHA"]""" not in iframe:
                    continue
                iframes.switch_to(iframe)
                elemethods = driver.find_elements(By.CSS_SELECTOR, "span")
                print(f"Iframe: {iframe}")
                for ele in elemethods:
                    try:
                        print(ele)
                        try:
                            ele.click()
                            didweclick = True
                            break
                        except Exception:
                            continue

                    except Exception:
                        pass
                if didweclick:
                    break
            except Exception as fe:
                print(fe)
                continue

driver = start_opera_driver(
    opera_browser_exe=operaPath,
    opera_driver_exe=driverPath,
    userdir="c:\\operabrowserprofile3",
    arguments=(
        "--no-sandbox",
        "--test-type",
        "--no-default-browser-check",
        "--no-first-run",
        "--incognito",
        "--start-maximized",
    ),
)
driver.get(r"https://jurisprudencia.trt15.jus.br/")
sleep(5)
buscaElemento()


