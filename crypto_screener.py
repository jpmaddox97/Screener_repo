import get_crypto_data as gcld
# from crypt_login import User


class Screener():

    def __init__(self, crlist='', limit='', data='', running=''):
        self.crlist = crlist
        self.limit = limit
        self.data = data
        self.running = running

    def createlist(self):
        # A function to make a list to be entered into the crypto data program
        clist = []

        adding = True

        print("To add cryptos to your list input the symbol of the currency and press enter."
              " When you are finished adding to your list press 'f'.")

        while adding:
            cryp = input("Add Crypto Symbol: ")
            if cryp == 'f':
                adding = False
            if cryp != 'f':
                clist.append(cryp)

        self.crlist = []

        for c in clist:
            cu = c.upper()
            self.crlist.append(cu)
        # print(clist)
        # print(crlist)
        return self.crlist

    # Place in run method

    def _changelimit(self):
        # Change the limit range of the data
        self.ol = str(
            input('Please enter an integer value for the limit: '))
        # Could take hexadecimal
        if self.ol.isnumeric() == False:
            print("You must enter an integer!")
            self._changelimit()
        return self.ol

    def _show_list(self):
        # Prints the formatted list
        for c in self.crlist:
            print(c)

    def check_list(self):
        check = input(
            "Would you like to check your list before beginning the program? (y/n): ")
        self.ol = '200'

        if check == 'y':
            self._show_list()
            cont = input("Everything good? (y/n): ")
            if cont == 'y':
                self.data = gcld.GetCryptoListData(self.ol, self.crlist)
            elif cont == 'n':

                print("Limit is set to 200 by default. If after running program you receive an error check"
                      " the symbols in your list or else you may need to increase the size of the limit.")
                cl = input("Would you like to change the limit? (y/n): ")
                if cl == 'y':
                    self._changelimit()
                if cl == 'n':
                    self.createlist()
        elif check == 'n':
            self.data = gcld.GetCryptoListData(self.ol, self.crlist)
        return self.data

    def options(self):
        options = ['Get Price - 0',
                   'Get Daily Volume - 1',
                   'Percent Change Hourly - 2',
                   'Percent Change Daily - 3',
                   'Percent Change Weekly - 4',
                   ]

        print("What data would you like to see for your list?")

        for opts in options:
            print(opts)

        data_choice = input(
            "Select the corresponding number to see its data: ")
        answ = ['0', '1', '2', '3', '4']
        if data_choice not in answ:
            print("Enter the number corresponding with the data you want to see.")
            data_choice = input(
                "Select the corresponding number to see its data: ")

        if data_choice == '0':
            self.data.get_price()
        if data_choice == '1':
            self.data.get_volume_24()
        if data_choice == '2':
            self.data.perc_change_h()
        if data_choice == '3':
            self.data.perc_change_d()
        if data_choice == '4':
            self.data.perc_change_w()

    def _cont_running(self):
        pcont = ['x', 's']
        cont = input("Press 'x' to exit or 's' to continue: ")
        if cont.lower() == 'x':
            self.running = False
            return self.running
        elif cont.lower() not in pcont:
            print("You must enter 'x' or 's'.")
            self._cont_running()
        elif cont.lower() == 's':
            self.options()
            self._cont_running()

    def run(self):
        self.createlist()
        self.check_list()
        self.running = True
        while self.running:
            self.options()
            self._cont_running()
        print("Exiting Program...")


if __name__ == "__main__":
    sc = Screener()
    sc.run()
