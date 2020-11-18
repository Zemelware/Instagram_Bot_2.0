from getpass import getpass
from instagram_bot import InstagramBot

print("-------------Instagram Bot-------------")
print("---------------------------------------")

while True:
    print("Please enter your Instagram credentials")

    username = input("Username (not email): ")
    password = getpass()

    print("\n---------------------------------------")
    print("LOGGING IN TO YOUR ACCOUNT...")
    print("---------------------------------------\n")

    try:
        bot = InstagramBot(username, password)
    except:
        # The page didn't load either because the user's internet connection is bad/they don't have internet, or they entered the wrong credentials
        print("The bot wasn't able to log in to your Instagram account because of one of two reasons:\n1. You entered the wrong credentials\n2. You have a slow internet connection or you aren't connected to the internet\n")
        continue

    while True:
        print("Select an option (type the number)")
        print("---------------------------------------")
        print("1. Check who's not following you back")
        print("2. Use different Instagram account")
        print("3. Quit")
        chosen_option = input(": ")

        if chosen_option == "2":
            print("\n---------------------------------------")
            print("LOGGING OUT OF YOUR ACCOUNT...")
            print("---------------------------------------\n")

            bot.driver.quit()
            break
        elif chosen_option == "3":
            print("\n---------------------------------------")
            print("QUITTING...")
            print("---------------------------------------\n")

            bot.driver.quit()
            quit()

        try:
            if chosen_option == "1":
                print("\n---------------------------------------")
                print("COMPLETING THE TASK...")
                print("---------------------------------------\n")

                bot.get_not_following_back()
            else:
                print("\nInvalid option\n")
                continue
        except:
            print(
                "The bot couldn't complete the task, check your internet connection and try again\n")
        else:
            # What happens when code executes without an exception
            print("\n---------------------------------------")
            print("THE TASK WAS COMPLETED SUCCESSFULLY")
            print("---------------------------------------\n")

    continue
