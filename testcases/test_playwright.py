import os.path
import time

from playwright.sync_api import Page, expect, Browser,sync_playwright


# def test_first_example(page:Page):
#     #page.set_viewport_size({"width": 1920, "height": 1080})
#     page.goto("https://magic-data-fe-dev.webelight.co.in/sign-up")
#     title = page.title()
#     print(page.title())
#     print(title)
#     assert "No-Code ETL Platform Frontend" in title
#     page.wait_for_timeout(2000)
#     page.goto("http://gmail.com")
#     page.wait_for_timeout(2000)
#     page.go_back()
#     page.wait_for_timeout(2000)
#     page.go_forward()
#     page.wait_for_timeout(2000)
#     page.reload()

# def test_finding_elements(page):
#     page.goto("http://gmail.com")
#     #id, xpath, css, name, className, tagName, linkText, partialLinkText
#     #page.locator("[name='identifier']").fill("trainer@way2automation.com")
#     page.get_by_label("Email or phone",exact=True).fill("trainer@way2automation.com")
#     #page.locator("button:has-text('Next')").click()
#     page.locator("button").filter(has_text="Next").click()
#     page.get_by_label("Enter your password").fill("sdfsdfsf",timeout=10000)
#     time.sleep(2)
#     page.locator("//*[@id='passwordNext']/div/button/span").click()
#
#     error_message = page.locator("//*[@id='yDmH0d']/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[2]/div[2]/span").inner_text()
#     print(error_message)
#
#     assert "Wrong password" in error_message
#     page.wait_for_timeout(2000)
#
# def test_handling_dropdown(page):
#     page.goto("https://www.wikipedia.org/")
#     #page.select_option("select",label="Eesti") #index, text
#     #page.select_option("select", value="hi")
#     page.select_option("select", index=0)
#     page.wait_for_timeout(5000)
#
#     dropdown = page.locator("select")
#     options = dropdown.locator("option").all()
#
#  #   block2 = page.locator("block2")
#   #  block2.locator("#abc").nth(1).click()
#
#     print(f"Total values are : {len(options)}")
#
#     for option in options:
#         text = option.inner_text()
#         lang = option.get_attribute("lang")
#         print(f"{text}---{lang}")

def test_handling_links(page):
    page.goto("https://www.wikipedia.org/")

    block = page.locator("//*[@id='www-wikipedia-org']/footer/nav")
    links = block.locator("a").all()

    print(f"Total values are : {len(links)}")

    for link in links:
        text = link.inner_text()
        url = link.get_attribute("href")
        print(f"{text}---{url}")

# def test_checkboxes(page):
#     page.goto("http://tizag.com/htmlT/htmlcheckboxes.php")
#
#     block = page.locator("//table/tbody/tr/td/div[4]")
#     checkboxes = block.locator("[name='sports']")
#     checkboxes_count = checkboxes.count()
#     print(checkboxes_count)
#
#     for i in range(checkboxes_count):
#         checkboxes.nth(i).click()
#
# def test_assertions(page):
#     page.goto("http://tizag.com/htmlT/htmlcheckboxes.php")
#
#     expect(page).to_have_url("http://tizag.com/htmlT/htmlcheckboxes.php")
#     print("URL Assertion passed")
#
#     expect(page).not_to_have_url("error")
#     print("No errors on the page hence passed")
#
#     expect(page).to_have_title("HTML Tutorial - Checkboxes")
#     print("Title assertion passed")
#
#
#     link = page.locator("//*[@id='menu']/a[19]")
#     expect(link).to_have_text("HTML - Tags")
#     print("Text assertion passed")
#
#
#     checkbox = page.locator("//div[4]/input[1]")
#     expect(checkbox).to_be_visible()
#     print("Checkbox is visible")
#
#     checkbox.click()
#
#     expect(checkbox).to_be_checked()
#     print("Checkbox is checked")
#
# def test_webtables(page):
#     page.goto("https://money.rediff.com/indices/nse/NIFTY-50?src=moneyhome_nseIndices")
#
#
#     row_count = page.locator(".index-data-wrapper > table > tbody > tr").count()
#     print("Row count is : ",row_count)
#
#
#     col_count = page.locator(".index-data-wrapper > table > tbody > tr:nth-child(1) > td").count()
#     print("Col count is : ",col_count)
#
#     text = page.locator(".index-data-wrapper > table > tbody > tr:nth-child(2) > td:first-child")
#     expect(text).to_contain_text("Adani")
#     print(text.inner_text())
#
#
#
#     all_inner_text = page.locator(".index-data-wrapper > table > tbody > tr").all_inner_texts()
#
#     for table_text in all_inner_text:
#         print(table_text)
#
# def test_shadowroot(page):
#     page.goto("chrome://downloads/")
#
#     page.locator("#searchInput").fill("Rahul")
#
# def test_mouseover(page):
#     page.goto("https://www.way2automation.com/")
#
#     page.locator("//*[@id='menu-item-27580']/a/span[2]").hover()
#     page.locator("//*[@id='menu-item-27592']/a/span[2]").click()
#
# def test_slider(page):
#     page.goto("https://jqueryui.com/resources/demos/slider/default.html")
#
#     slider = page.locator("//*[@id='slider']/span")
#
#     page.wait_for_timeout(3000)
#
#     bounding_box = slider.bounding_box()
#
#     start_x = bounding_box["x"] + bounding_box["width"] / 2
#     start_y = bounding_box["y"] + bounding_box["height"] / 2
#
#     page.mouse.move(start_x,start_y)
#
#     page.mouse.down()
#
#     page.mouse.move(start_x +400, start_y)
#
#     page.mouse.up()
#
#
# def test_resizable(page):
#     page.goto("https://jqueryui.com/resources/demos/resizable/default.html")
#
#     slider = page.locator("//*[@id='resizable']/div[3]")
#
#     page.wait_for_timeout(3000)
#
#     bounding_box = slider.bounding_box()
#
#     start_x = bounding_box["x"] + bounding_box["width"] / 2
#     start_y = bounding_box["y"] + bounding_box["height"] / 2
#
#     page.mouse.move(start_x,start_y)
#
#     page.mouse.down()
#
#     page.mouse.move(start_x +400, start_y+400)
#
#     page.mouse.up()
#
#
# def test_droppable(page):
#     page.goto("https://jqueryui.com/resources/demos/droppable/default.html")
#
#     draggable = page.locator("#draggable")
#     droppable = page.locator("#droppable")
#
#     page.wait_for_timeout(3000)
#
#     draggable_box = draggable.bounding_box()
#     droppable_box = droppable.bounding_box()
#
#     page.mouse.move(
#
#         draggable_box["x"] + draggable_box["width"] / 2,
#         draggable_box["y"] + draggable_box["height"] / 2
#
#     )
#
#     page.mouse.down()
#
#     page.mouse.move(
#
#         droppable_box["x"] + droppable_box["width"] / 2,
#         droppable_box["y"] + droppable_box["height"] / 2
#
#     )
#
#     page.mouse.up()
#
# def test_resizable(page):
#     page.goto("https://deluxe-menu.com/popup-mode-sample.html")
#
#     page.locator("//p[2]/img").click(button="right")
#
# def test_alert(page):
#
#
#     def dialog_handler(dialog):
#         page.wait_for_timeout(2000)
#         print(dialog.message)
#         dialog.accept()
#
#     page.on("dialog",dialog_handler)
#
#     page.goto("https://mail.rediff.com/cgi-bin/login.cgi")
#
#     page.locator("[type='submit']").click()
#
#
# def test_iframe(page):
#     page.goto("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit",timeout=60000)
#     page.wait_for_timeout(2000)
#     frame = page.frame_locator("#iframeResult")
#     frame.locator("#fname").clear()
#     frame.locator("#fname").fill("Rahul")
#
#     frame.locator("#lname").clear()
#     frame.locator("#lname").fill("Arora")
#
#     frame.locator("[type='submit']").click()
#
# def test_tabs_and_popups(page):
#     page.goto("https://sso.teachable.com/secure/673/identity/sign_up/otp",timeout=60000)
#
#     with page.expect_popup() as popup_info:
#         page.locator("text=Privacy").nth(0).click()
#
#     popup = popup_info.value
#     popup.locator("//*[@id='header-sign-up-btn']").click()
#     popup.locator("#name").fill("trainer@way2automation.com")
#
#     page.wait_for_timeout(3000)
#     popup.close()
#
#     page.wait_for_timeout(3000)
#
#
# def test_javascript(page):
#     page.goto("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit",timeout=60000)
#     page.wait_for_timeout(2000)
#     frame = page.frame_locator("#iframeResult")
#     frame.locator("#fname").clear()
#     frame.locator("#fname").fill("Rahul")
#
#     frame.locator("#lname").clear()
#     frame.locator("#lname").fill("Arora")
#
#     frame.locator("[type='submit']").evaluate("(element) =>{element.style.border = '3px solid red';}")
#
#     frame.locator("[type='submit']").screenshot(path="screenshot/element.png")
#
#     page.wait_for_timeout(3000)
#
#
#     page.screenshot(path="screenshot/page.png")
#     #frame.locator("[type='submit']").click()
#
#
# def test_http_authentication(page,browser: Browser):
#     context = browser.new_context(
#         http_credentials={"username":"admin","password":"admin"}
#     )
#
#     page = context.new_page()
#
#
#     page.goto("https://the-internet.herokuapp.com/basic_auth", timeout=60000)
#
#
# def test_file_upload(page):
#     page.goto("https://www.way2automation.com/way2auto_jquery/registration.php#load_box", timeout=60000)
#
#
#     page.locator("#register_form > fieldset:nth-child(9) > input[type=file]").set_input_files("C:\\Users\\way2automation\\Downloads\\ufb.jpg")
#
# def test_multiple_file_upload(page):
#     page.goto("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_fileupload_multiple", timeout=60000)
#
#     frame = page.frame_locator("#iframeResult")
#
#     frame.locator("#myFile").set_input_files([
#         "C:\\Users\\way2automation\\Desktop\\createaccount.png",
#         "C:\\Users\\way2automation\\Desktop\\misc.png"
#     ])
#
#
# def test_multiple_file_upload(page):
#     page.goto("https://www.selenium.dev/downloads/", timeout=60000)
#
#
#     with page.expect_download() as download_info:
#         page.locator("body > div.container-fluid.td-default.td-outer > main > div:nth-child(5) > div.col-sm-6.py-3.ps-0.pe-3 > div > div > p:nth-child(1) > a").click()
#
#     download = download_info.value
#
#
#     project_directory = os.path.join(os.path.dirname(os.getcwd()),"downloads")
#     os.makedirs(project_directory,exist_ok=True)
#
#     file_path = os.path.join(project_directory,"selenium.jar")
#     download.save_as(file_path)
#
#     print(f"file downloaded to : {file_path}")
#
# def test_multiple_file_upload():
#     with sync_playwright() as p:
#         request_context = p.request.new_context()
#         response = request_context.get("http://localhost:8080/api/users/1")
#
#         assert response.status == 200, f"Unexpected status code : {response.status}"
#
#         print(f"status code {response.status}")
#         print(f"Response body : {response.text()}")
#
#         json_response = response.json()
#
#         print(json_response.get("firstName"))
#
#         assert json_response.get("firstName") == "Rahul1", f"Expected 'Rahul' but got {json_response.get('firstName')}"
#
# def test_multiple_file_upload():
#     with sync_playwright() as p:
#         request_context = p.request.new_context()
#         response = request_context.post("http://localhost:8080/api/users", data={"email":"Trump@way2automation.com", "firstName":"Donald", "lastName":"Trump"},
#                              headers={"Content-Type":"application/json"})
#
#         print(f"status code {response.status}")
#
#         assert response.status == 201, f"Unexpected status code : {response.status}"
#
#         print(f"Response body : {response.text()}")
