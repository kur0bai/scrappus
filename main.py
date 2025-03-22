from colorama import Fore, Style
import functions

ascii_art_colored = [
    Fore.GREEN    + " (                                           ",
    Fore.GREEN  + " )\ )                                         ",
    Fore.GREEN + "(()/(     (       )                  (       ",
    Fore.GREEN   + " /(_)) (  )(   ( /(  `  )   `  )    ))\  (   ",
    Fore.GREEN+ "(_))   )\(()\  )(_)) /(/(   /(/(   /((_) )\  ",
    Fore.GREEN   + "/ __| ((_)((_)((_)_ ((_)_\ ((_)_\ (_))( ((_) ",
    Fore.CYAN  + "\__ \/ _|| '_|/ _` || '_ \)| '_ \)| || |(_-< ",
    Fore.CYAN    + "|___/\__||_|  \__,_|| .__/ | .__/  \_,_|/__/ ",
    Fore.CYAN + "                    |_|    |_|               ",
    Style.RESET_ALL  # Restart
]


functions = functions.Functions()

for line in ascii_art_colored:
    print(line)
    
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




    