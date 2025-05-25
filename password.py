def password():
    while True:
        word = input("Enter a password: ")

        if len(word) < 8:
            print("Password must be at least 8 characters long.")
            continue

        if ' ' in word:
            print("Password should not contain spaces.")
            continue

        if not any(c.isupper() for c in word):
            print("Password must include at least one uppercase letter.")
            continue

        if not any(c.islower() for c in word):
            print("Password must include at least one lowercase letter.")
            continue

        if not any(c.isdigit() for c in word):
            print("Password must include at least one digit.")
            continue

        if not any(not c.isalnum() for c in word):
            print("Password must include at least one special character.")
            continue

        print("You have given a strong password! :)")
        break

password()
