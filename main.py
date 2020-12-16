import time
import multiprocessing
from multiprocessing import Pool

from modules.fileIO import Csv
from modules.webdriver import Chrome

target_locations = [
    {'name': 'UberEats東京', 'url': 'https://maps.uedriver.info/maps/tokyo'},
    # {'name': 'UberEats千葉', 'url': 'https://maps.uedriver.info/maps/chiba'},
]
fileIO = Csv()
output_path = './out/out.csv'

def main(target_location):
    target_name = target_location.get('name')
    target_url = target_location.get('url')
    ch = Chrome()
    with ch.driver as driver:
        driver.get(target_url)
        time.sleep(4)
        driver.find_element_by_xpath(f'//*[@id="inspire"]/div[1]/header/div/div[4]/button[3]').click()
        time.sleep(1)
        driver.find_element_by_xpath(f'//*[@id="inspire"]/div[3]/div/div/div[7]/div/div[1]/div').click()
        time.sleep(1)
        driver.find_element_by_xpath(f'//*[@id="inspire"]/div[3]/div/div/header/div/button').click()
        time.sleep(1)
        driver.find_element_by_xpath(f'//*[@id="inspire"]/div[1]/header/div/div[1]/button').click()
        time.sleep(3)
        driver.find_element_by_xpath(f'//*[@id="amiShowStorelist"]').click()
        time.sleep(1)
        
        count = 0
        while(True):
            content_list = []
            try:
                content = driver.find_elements_by_xpath(f'//*[@class="cilist v-list-item v-list-item--link theme--light"]')[count]
            except Exception as e:
                print(e)
                break
            title = driver.find_elements_by_xpath(f'//*[@class="cilist v-list-item v-list-item--link theme--light"]/*[@class="v-list-item__content"]/*[@class="v-list-item__title"]')[count].get_attribute("innerText")
            location = driver.find_elements_by_xpath(f'//*[@class="cilist v-list-item v-list-item--link theme--light"]/*[@class="v-list-item__content"]/*[@class="v-list-item__subtitle"]')[count].get_attribute("innerText")
            print(title)
            content_list.append(title)
            print(location)
            content_list.append(location)
            fileIO.addContent(output_path, content_list)
            count += 1
            
        while(True):
            try:
                driver.find_element_by_xpath(f'//*[@class="v-pagination v-pagination--circle theme--light"]/li[9]/button').click()
            except Exception as e:
                print(e)
                break
            time.sleep(1)
            
            count = 0
            while(True):
                content_list = []
                try:
                    content = driver.find_elements_by_xpath(f'//*[@class="cilist v-list-item v-list-item--link theme--light"]')[count]
                except Exception as e:
                    print(e)
                    break
                title = driver.find_elements_by_xpath(f'//*[@class="cilist v-list-item v-list-item--link theme--light"]/*[@class="v-list-item__content"]/*[@class="v-list-item__title"]')[count].get_attribute("innerText")
                location = driver.find_elements_by_xpath(f'//*[@class="cilist v-list-item v-list-item--link theme--light"]/*[@class="v-list-item__content"]/*[@class="v-list-item__subtitle"]')[count].get_attribute("innerText")
                print(title)
                content_list.append(title)
                print(location)
                content_list.append(location)
                fileIO.addContent(output_path, content_list)
                count += 1
    return

if __name__ == "__main__":
    for target_location in target_locations:
        main(target_location)