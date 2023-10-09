
# import time
# from typing import io, re
#
# from operagxdriver import is_binary_patched
# from selenium import webdriver
# from selenium.webdriver.chrome import service
# from selenium.webdriver.common.by import By
#
# def patch_exe(executable_path):
#     if is_binary_patched(executable_path=executable_path):
#         return True
#     start = time.perf_counter()
#     with io.open(executable_path, "r+b") as fh:
#         content = fh.read()
#         # match_injected_codeblock = re.search(rb"{window.*;}", content)
#         match_injected_codeblock = re.search(rb"\{window\.cdc.*?;\}", content)
#         if match_injected_codeblock:
#             target_bytes = match_injected_codeblock[0]
#             new_target_bytes = (
#                 b'{console.log("undetected chromedriver 1337!")}'.ljust(
#                     len(target_bytes), b" "
#                 )
#             )
#             new_content = content.replace(target_bytes, new_target_bytes)
#             if new_content == content:
#
#                 print(
#                     "something went wrong patching the driver binary. could not find injection code block"
#                 )
#             else:
#                 print(
#                     "found block:\n%s\nreplacing with:\n%s"
#                     % (target_bytes, new_target_bytes)
#                 )
#             fh.seek(0)
#             fh.write(new_content)
#     print(
#         "patching took us {:.2f} seconds".format(time.perf_counter() - start)
#     )
#
# operaPath = r"C:\Users\João Pedro\AppData\Local\Programs\Opera GX\opera.exe"
# driverPath = r"C:\operadriver_win64\operadriver.exe"
#
# webdriver_service = service.Service(driverPath)
# webdriver_service.start()
#
# options = webdriver.ChromeOptions()
# options.binary_location = r"C:\Users\João Pedro\AppData\Local\Programs\Opera GX\opera.exe"
# options.add_experimental_option('w3c', True)
#
# driver = webdriver.Remote(webdriver_service.service_url, options=options)
#
# driver.get("https://www.google.com")
# teste = driver.find_element(By.NAME, 'q')
# teste.send_keys('operadriver\n')
#
# time.sleep(5)
# driver.quit()