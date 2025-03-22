from colorama import Fore, Style
import argparse
import json
import csv
import time
import requests
import threading
import sys
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

####################
# UI FUNCTIONS #
####################


class Spinner:
    """
    Function to show and hide spinner animation
    """

    def __init__(self, message="Loading"):
        self.spinner = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.message = message
        self.running = False
        self.thread = None

    def start(self):
        if self.running:
            return  # avoid multiple threading

        self.running = True
        self.thread = threading.Thread(target=self._animate, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()  # wait until ends

        # clean
        sys.stdout.write("\r" + " " * (len(self.message) + 4) + "\r")
        sys.stdout.flush()

    def _animate(self):
        """execute spinner animation."""
        while self.running:
            for frame in self.spinner:
                if not self.running:
                    break
                sys.stdout.write(f"\r{self.message} {frame} ")
                sys.stdout.flush()
                time.sleep(0.1)  # speed

####################
# MAIN FUNCTIONS #
####################


class Functions:
    def get_content(self, url, is_dynamic=False):
        if is_dynamic:
            """
            If website is dynamic then we use selenium to extract data
            """
            options = Options()
            options.add_argument("--headless")
            driver = webdriver.Chrome(service=Service(
                ChromeDriverManager().install()), options=options)
            driver.get(url)
            time.sleep(3)
            content = driver.page_source
            driver.quit()
        else:
            """
            Using simple request for static websites
            """
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            content = response.text
        return content

    def parse_content(self, content, rules):
        soup = BeautifulSoup(content, "html.parser")
        extracted_data = {}

        for key, selector in rules.items():
            elements = soup.select(selector)
            extracted_data[key] = [element.text.strip()
                                   for element in elements] if elements else None
        return extracted_data

    def save_data(self, data, output_format, output_file):
        if output_format == 'json':
            with open(output_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        elif output_format == 'csv':
            with open(output_file, 'w', newline="", encoding='utf8') as file:
                writer = csv.writer(file)
                writer.writerow(data.keys())
                writer.writerows(zip(*data.values()))


def main():
    """
    Show the main features arguments to choice when we need to scrapp something
    """
    parser = argparse.ArgumentParser(description="Universal Web Scrapper")
    parser.add_argument('url', help='Websites URL to extract data.')
    parser.add_argument('rules', help="JSON file with the extraction rules.")
    parser.add_argument('--dynamic', default=False, action='store_true',
                        help='If is a dynamic website, use selenium')
    parser.add_argument('--output', default='output.json',
                        help='Output file name')
    parser.add_argument(
        '--format', choices=['json', 'csv'], default='json', help='Output file extension')

    args = parser.parse_args()

    functions = Functions()

    try:
        spinner = Spinner(Fore.CYAN + 'Reading rules file')
        spinner.start()

        with open(args.rules, 'r', encoding='utf8') as file:
            rules = json.load(file)

        spinner.stop()

        spinner = Spinner(Fore.CYAN + 'Scrapping Web data')
        spinner.start()

        content = functions.get_content(args.url, args.dynamic)

        spinner.stop()

        extracted_data = functions.parse_content(content, rules)
        functions.save_data(extracted_data, args.format, args.output)
        print(Fore.GREEN + 'Finished!!')
        print(Fore.GREEN + f'Data saved in {args.output}')
    except Exception as ex:
        print(Fore.RED + f'\nSomething went wrong, please try again.',)
        print(Fore.YELLOW + f'Error: ' + Fore.RED + f'{ex}')
        Style.RESET_ALL


def show_banner():
    """
    Main identifier banner
    """
    banner = [
        Fore.GREEN + r" (                                           ",
        Fore.GREEN + r" )\ )                                         ",
        Fore.GREEN + r"(()/(     (       )                  (       ",
        Fore.GREEN + r" /(_)) (  )(   ( /(  `  )   `  )    ))\  (   ",
        Fore.GREEN + r"(_))   )\(()\  )(_)) /(/(   /(/(   /((_) )\  ",
        Fore.GREEN + r"/ __| ((_)((_)((_)_ ((_)_\ ((_)_\ (_))( ((_) ",
        Fore.CYAN + r"\__ \/ _|| '_|/ _` || '_ \)| '_ \)| || |(_-< ",
        Fore.CYAN + r"|___/\__||_|  \__,_|| .__/ | .__/  \_,_|/__/ ",
        Fore.CYAN + r"                    |_|    |_|               ",
        Style.RESET_ALL
    ]

    for line in banner:
        print(line)


if __name__ == '__main__':
    show_banner()
    main()
