from getpass import getpass
from instagram_bot import InstagramBot

print("-------------Instagram Bot-------------")
print("---------------------------------------")
print("Please enter your Instagram credentials")

username = input("Username (not email): ")
password = getpass()

print("\n---------------------------------------")
print("LOGGING IN TO YOUR ACCOUNT...")
print("---------------------------------------\n")

bot = InstagramBot(username, password)

while True:
    print("Select an option (type the number)")
    print("---------------------------------------")
    print("1. Check who's not following you back")
    print("2. Use different Instagram account")
    print("3. Quit")
    chosen_option = input(": ").rstrip()

    if chosen_option == "1":
        pass
    elif chosen_option == "2":
        # bot.driver.quit()
        pass
    elif chosen_option == "3":
        bot.driver.quit()
        quit()
    else:
        print("\nInvalid option\n")
        continue

    print("\n---------------------------------------")
    print("THE TASK WAS COMPLETED SUCCESSFULLY")
    print("---------------------------------------\n")
