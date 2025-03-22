class Functions:
    def validate_option(self, option):
        if (type(option) != int):
            return "Not valid option"

        if (option == 1):
            print('hereee', option)
            self.scrapping_host()
        
        
    def scrapping_host():
        print('scraaaaaping....')    
    