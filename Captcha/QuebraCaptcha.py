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
from selenium.webdriver.common.by import By

add_printer(1)
import mousekey

mkey = mousekey.MouseKey()
mkey.enable_failsafekill("ctrl+e")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from fast_ctypes_screenshots import (
    ScreenshotOfOneMonitor,
)


def move_mouse(
        x,
        y,
        variationx=(-5, 5),
        variationy=(-5, 5),
        up_down=(0.2, 0.3),
        min_variation=-10,
        max_variation=10,
        use_every=4,
        sleeptime=(0.009, 0.019),
        linear=90,
):
    mkey.left_click_xy_natural(
        int(x) - random.randint(*variationx),
        int(y) - random.randint(*variationy),
        delay=random.uniform(*up_down),
        min_variation=min_variation,
        max_variation=max_variation,
        use_every=use_every,
        sleeptime=sleeptime,
        print_coords=True,
        percent=linear,
    )

def get_screenshot_tesser(minlen=2):
    with ScreenshotOfOneMonitor(
            monitor=0, ascontiguousarray=True
    ) as screenshots_monitor:
        img5 = screenshots_monitor.screenshot_one_monitor()
    df = pytesseract.image_to_data(img5, output_type="data.frame")
    df = df.dropna(subset="text")
    df = df.loc[df.text.str.len() > minlen].reset_index(drop=True)
    return df


if __name__ == "__main__":
    servico = Service(ChromeDriverManager().install())
    # options = uc.ChromeOptions()
    # options.add_argument("--headless")
    # userdir = "C:/chromeprofiletest"
    # options.add_argument(f"--user-data-dir={userdir}")
    # driver = uc.Chrome(options=options)
    driver = webdriver.Chrome(service=servico)
    driver.maximize_window()
    driver.get(r"https://sia.estacio.br/sianet/Logon")
    sleep(3)
    df = get_screenshot_tesser(minlen=2)
    df = pd.concat(
        [
            df,
            pd.DataFrame(
                rapidfuzz.process_cpp.cdist(["Nao", "sou", "robé"], df.text.to_list())
            ).T.rename(columns={0: "nao", 1: "sou", 2:"robe"}),
        ],
        axis=1,
    )

    try:
        vamosClicar = np.diff(df.loc[(df.nao == df.nao.max()) & (df.nao > 80) | (df.sou == df.sou.max()) & (df.sou > 80) | (
                    df.robe == df.robe.max()) & (df.robe > 80)][:3].index)[0] == 1
    except Exception:
        vamosClicar = False

    if vamosClicar:
        x, y = df.loc[df.nao == df.nao.max()][['left', 'top']].__array__()[0]
        move_mouse(
            x,
            y,
            variationx=(-5, 5),
            variationy=(-5, 5),
            up_down=(0.2, 0.3),
            min_variation=-10,
            max_variation=10,
            use_every=4,
            sleeptime=(0.009, 0.019),
            linear=90,
        )
        sleep(5)
        btnAudio = driver.find_element(By.CSS_SELECTOR, "div.rc-footer > #recaptcha-audio-button")
        btnAudio.click()