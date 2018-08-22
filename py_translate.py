from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import argparse

Languages = ('ta', 'mn', 'tl', 'cy', 'kn', 'sn', 'ko', 'ar', 'km', 'bs', 'la', 'cs', 'rw', 'ne', 'sq', 'sw', 'sm', 'mi', 'co', 'hy', 'el', 'st', 'tk', 'ha', 'it', 'sd', 'af', 'sr', 'es', 'bn', 'th', 'is', 'ka', 'ht', 'so', 'ga', 'fr', 'hi', 'ig', 'pt', 'tg', 'ro', 'pl', 'vi', 'en', 'lv', 'mk', 'hr', 'mt', 'te', 'lt', 'ru', 'id', 'iw', 'gl', 'sv', 'ms', 'sl', 'zh-TW', 'ug', 'zh', 'mr', 'fi', 'si', 'xh', 'jw', 'fy', 'pa', 'ku', 'ps', 'hu', 'ml', 'no', 'gd', 'eu', 'or', 'ceb', 'fa', 'bg', 'lb', 'kk', 'et', 'gu', 'lo', 'yi', 'su', 'da', 'am', 'ur', 'hmn', 'de', 'tr', 'tt', 'eo', 'yo', 'sk', 'zu', 'nl', 'be', 'ky', 'haw', 'uk', 'ca', 'zh-CN', 'my', 'uz', 'mg', 'ny', 'ja', 'az')

parser = argparse.ArgumentParser(description = "Translate everything!")
parser.add_argument('--source-language', required = True, choices = Languages, help="Specify the source language!")
parser.add_argument('--destination-language', required = True, choices = Languages, help="Specify the destination language!")
parser.add_argument('-tobetranslated', required = True, help="What do you need translating?")
args = parser.parse_args()

if args.source_language == args.destination_language:
	raise SystemExit("You need different source and destination language!")

driver = webdriver.Firefox()

#https://translate.google.com/#en/hu/

driver.get(f"https://translate.google.com/#{args.source_language}/{args.destination_language}/")

TranslateElement = "//input[@id='gt-submit']"
InputElement = "//textarea[@id='source']"
OutPutElement = "//div[@id='gt-res-dir-ctr']"

TranslateButton = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(TranslateElement))
InputBox = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(InputElement))

InputBox.send_keys(args.tobetranslated)

TranslateButton.click()

sleep(3)

ResultElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(OutPutElement))

print(f"#### Result <{args.source_language}> -> <{args.destination_language}>")
print(ResultElement.text)
print("####")

driver.quit()
