#Task: Create a chatbot that will help new customers at a bank/credit institution-
#-troubleshoot/answer common questions for the user.

def zelle_faq(): #Answers the users questions regarding Zelle FAQ
    print ('\n\nYes you can send money with Zelle through the Bank mobiile app or via online banking.\nJust enroll with your email or U.S. Mobile number, and you are ready to send money to trusted recipents.\n')
    choice = input('1) Are there any fees for using Zelle with my bank account?\n2) Exit\n\nPlease select (1) or (2): ')
   if choice == '1':
        print ('\n\nThere are no fees associated with using Zelle with your Bank account.\n')
        exit()
    elif choice == '2':
        exit()
    else:
        exit()
        

def newCard_faq(): #Answers the users questions regarding activating a new card FAQ
    print ('\n\nTo activate your new Bank card, select "Activate New Card" through the Bank Mobile app and then complete the steps.\nYou can also use the same method through your Bank account online.\n')
    choice = input('1) If I activate my card online or through the app, how long will it take before I can use it?\n2) Exit\n\nPlease select (1) or (2): ')
    if choice == '1':
        print ("\n\nOnce you activate your card online or through the app, it's typically ready to use immediately.\n")
        exit()
    elif choice == '2':
        exit()
    else:
        exit()

def creditLimit_faq(): #Answers the users questions regarding increasing their credit limit FAQ
    print ('\n\nYou can request a credit limit increase anytime through your Bank account online or in the mobile app.\nEligibility depends on factors like account age, payment history, and income.\n')
    choice = input('1) How long does it take to process a credit limit increase request?\n2) Exit\n\nPlease select (1) or (2): ')
    if choice == '1':
        print ("\n\nProcessing times for credit limit increase requests can vary, but Bank typically reviews and provides a decision within a few days.\nPlease contact a Bank helper if you'd be interested in more details!\n")
        exit()
    elif choice == '2':
        exit()
    else:
        exit()

def cardFees_faq(): #Answers the users questions regarding card fees FAQ
    print ("\n\nFees vary by card. Common fees include annual fees, late payment fees, and cash advance fees.\nSome cards may not have annual fees or foreign transaction fees. Check your card's terms for specific details.\n")
    choice = input('1) Which specific fees are associated with my card type?\n2) Exit\n\nPlease select (1) or (2): ')
    if choice == '1':
        choosing = True
        while choosing:
            print ("\n\nWhich card would you like to know about?\n\n- Venture Card\n- VentureOne Card\n- Quicksilver Card\n- Savor Card\n- Platinum Card\n- VentureX Card")
            userCard = input ('\nPlease Select: ').lower()
            cardList = ['venture card', 'ventureone card', 'quicksilver card', 'savor card', 'platinum card', 'venturex card']
            if userCard in cardList:
                if userCard == 'venture card':
                    print("\nThe Venture Card has a $95 annual fee and no foreign transaction fees.\n")
                    exit()
                elif userCard == 'ventureone card':
                    print("\nThe VentureOne Card has no annual fee and no foreign transaction fees.\n")
                    exit()
                elif userCard == 'quicksilver card':
                    print("\nThe Quicksilver Card has no annual fee and no foreign transaction fees.\n")
                    exit()
                elif userCard == 'savor card':
                    print("\nThe Savor Card has no annual fee and no foreign transaction fees.\n")
                    exit()
                elif userCard == 'platinum card':
                    print("\nThe Platinum Card has a $695 annual fee and no foreign transaction fees.\n")
                    exit()
                elif userCard == 'venturex card':
                    print("\nThe VentureX Card has a $395 annual fee and no foreign transaction fees.\n")
                    exit()
            else:
                print ('\nI couldnt quite grasp that. Please enter a valid card type.')           
    elif choice == '2':
        exit()
    else:
        exit()


banking = True    

while banking:
    name = input('Enter user ID: ')
    passw = input('Enter your user password: ')

    print (f'\n\nWelcome {name}! How can I assist you today?')

    print ('\n1) Can I send money with Zelle?')
    print ('2) How do I activate my new card?')
    print ('3) When can I apply for a credit card with a higher limit?')
    print ('4) What fees are associated with my card?')
    print ('5) Exit')

    choice = input('\nPlease Select: ')

    if choice == '1':
        zelle_faq()
    elif choice == '2':
        newCard_faq()
    elif choice == '3':
        creditLimit_faq()
    elif choice == '4':
        cardFees_faq()
    elif choice == '5':
        print ('Thank you for using Bank!\nGoodbye!')
        exit()
    else:
        print ('\nInvalid Input. Please select one of given options (1-5)\n')
    




