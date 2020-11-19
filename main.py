from getpass import getpass
from instagram_bot import InstagramBot


def print_with_lines(message):
    print("\n---------------------------------------")
    print(message)
    print("---------------------------------------\n")


print("-------------Instagram Bot-------------")
print("---------------------------------------")

while True:
    print("Please enter your Instagram credentials")

    username = input("Username (not email): ")
    password = getpass()

    print_with_lines("LOGGING IN TO YOUR ACCOUNT...")

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
            print_with_lines("LOGGING OUT OF YOUR ACCOUNT...")

            bot.driver.quit()
            break
        elif chosen_option == "3":
            print_with_lines("QUITTING...")

            bot.driver.quit()
            quit()

        try:
            if chosen_option == "1":
                print_with_lines("COMPLETING THE TASK...")

                bot.get_not_following_back()

                with open("not_following_back", "w") as f:
                    f.writelines(
                        [f"{name}\n" for name in bot.not_following_back])
            else:
                print("\nInvalid option\n")
                continue
        except:
            print(
                "The bot couldn't complete the task, check your internet connection and try again\n")
        else:
            # What happens when code executes without an exception
            print_with_lines("THE TASK WAS COMPLETED SUCCESSFULLY")

    continue
