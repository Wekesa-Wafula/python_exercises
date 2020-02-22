while True:
    try:
        input_balance = input('Enter your balance: ')
        
        if input_balance == 'q':
            break

        balance = int(input_balance)
        print('Your balance is: ' , balance)
        ssid = input('Kindly enter SSID for credit purchase: ')
        if ssid == '144':
            credit = int(input('How much credit do you want to buy: '))
            balance -= credit
            if balance < 0:
                print('You do not have sufficient balance to purchase ' + str(credit) + ' Ksh worth of airtime.')
            else: 
                print('You have just bought ' + str(credit) + ' Ksh worth of airtime.')
                print('Your balance is now ' , balance)       
        else:
            print('Kindly enter the correct ssid for credit purchase')

        
    except ValueError:
        print('Kindly enter the amount you wish to buy correctly.')
   
print('The application will close now')