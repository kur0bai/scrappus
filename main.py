from colorama import Fore, Style
import argparse
import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class Functions:
    def get_content(url, is_dynamic=False):
        if is_dynamic:
            """
            If website is dynamic then we use selenium to extract data
            """
            options = Options()
            options.add_argument('--headless')
            driver = webdriver.Chrome(service=Service(
                ChromeDriverManager().install()))
            driver.get(url)
            time.sleep(3)
            content = driver.page_source
            driver.quit()
        else:
            pass


def main():
    """
    Show the main features arguments to choice when we need to scrapp something
    """
    parser = argparse.ArgumentParser(description="Universal Web Scrapper")
    parser.add_argument('url', help='Websites URL to extract data.')
    parser.add_argument('rules', help="JSON file with the extraction rules.")
    parser.add_argument('--dynamic', action='store_true',
                        help='If is a dynamic website, use selenium')
    parser.add_argument('--output', default='output.json',
                        help='Output file name')
    parser.add_argument(
        '--format', choices=['json', 'csv'], default='json', help='Output file extension')

    args = parser.parse_args()

    with open(args.rules, 'r', encoding='utf8') as file:
        rules = json.load(file)


def show_banner():
    """
    Main identifier banner
    """
    banner = [
        Fore.GREEN + " (                                           ",
        Fore.GREEN + " )\ )                                         ",
        Fore.GREEN + "(()/(     (       )                  (       ",
        Fore.GREEN + " /(_)) (  )(   ( /(  `  )   `  )    ))\  (   ",
        Fore.GREEN + "(_))   )\(()\  )(_)) /(/(   /(/(   /((_) )\  ",
        Fore.GREEN + "/ __| ((_)((_)((_)_ ((_)_\ ((_)_\ (_))( ((_) ",
        Fore.CYAN + "\__ \/ _|| '_|/ _` || '_ \)| '_ \)| || |(_-< ",
        Fore.CYAN + "|___/\__||_|  \__,_|| .__/ | .__/  \_,_|/__/ ",
        Fore.CYAN + "                    |_|    |_|               ",
        Style.RESET_ALL
    ]

    for line in banner:
        print(line)


if __name__ == '__main__':
    show_banner()
    main()

""" functions = functions.Functions()


options = [
    {"id": 1, "text": '1. Scrapp host'},
    {"id": 2, "text": '2. Exit'},
]

exit = False

while (exit is not True):
    for option in options:
        print(Fore.BLUE + option["text"])

    try:
        selected_option = int(input('Select option: '))
        functions.validate_option(selected_option)
    except Exception:
        print(Fore.RED + 'Is not a valid option')
        print('\n') """
