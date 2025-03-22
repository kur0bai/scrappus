from colorama import Fore, Style
import functions
import argparse


def main():
    """
    Show the main features arguments to choice when we need to scrapp something
    """
    parser = argparse.ArgumentParser(description="Universal Web Scrapper")
    parser.add_argument('url', help='Websites URL to extract data.')
    parser.add_argument('rules', help="JSON file with the extraction rules.")
    parser.add_argument('--dynamic', action='store_true', help='If is a dynamic website, use selenium')
    parser.add_argument('--output', default='output.json', help='Output file name')
    parser.add_argument('--format', choices=['json', 'csv'], default='json', help='Output file extension')


def show_banner():
    """
    Main identifier banner
    """
    banner = [
        Fore.GREEN    + " (                                           ",
        Fore.GREEN  + " )\ )                                         ",
        Fore.GREEN + "(()/(     (       )                  (       ",
        Fore.GREEN   + " /(_)) (  )(   ( /(  `  )   `  )    ))\  (   ",
        Fore.GREEN+ "(_))   )\(()\  )(_)) /(/(   /(/(   /((_) )\  ",
        Fore.GREEN   + "/ __| ((_)((_)((_)_ ((_)_\ ((_)_\ (_))( ((_) ",
        Fore.CYAN  + "\__ \/ _|| '_|/ _` || '_ \)| '_ \)| || |(_-< ",
        Fore.CYAN    + "|___/\__||_|  \__,_|| .__/ | .__/  \_,_|/__/ ",
        Fore.CYAN + "                    |_|    |_|               ",
        Style.RESET_ALL  
    ]
    
    for line in banner:
        print(line)


functions = functions.Functions()

    
options = [
    {"id": 1, "text": '1. Scrapp host'},
    {"id": 2, "text": '2. Exit'},
]    

exit = False

while(exit is not True):
    for option in options:
        print(Fore.BLUE + option["text"])
        
    try:    
        selected_option = int(input('Select option: '))
        functions.validate_option(selected_option)
    except Exception: 
        print(Fore.RED + 'Is not a valid option')
        print('\n')    




    