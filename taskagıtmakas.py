import random

print(("-" * 30) + "\nTaş, Kağıt, Makas\n" + ("-" * 30))

user_score, computer_score = 0, 0

while True:
    print("\n1 - Taş\n2 - Kağıt\n3 - Makas")
    user_choice = input("Senin seçimin: ")
    computer_choice = random.choice(["1", "2", "3"])

    if user_choice == "1":
        if computer_choice == "1":
            print("Bilgisayarın Seçimi: Taş\nTaş taşa eşit. Berabere!")

        elif computer_choice == "2":
            print("Bilgisayarın Seçimi: Kağıt\nKağıt taşı sarar. Kaybettin!")
            computer_score += 100

        elif computer_choice == "3":
            print("Bilgisayarın Seçimi: Makas\nTaş makası kırar. Kazandın!")
            user_score += 100

    elif user_choice == "2":
        if computer_choice == "1":
            print("Bilgisayarın Seçimi: Kağıt\nKağıt taşı sarar. Kazandın!")
            user_score += 100

        elif computer_choice == "2":
            print("Bilgisayarın Seçimi: Kağıt\nKağıt kağıda eşit. Berabere!")

        elif computer_choice == "3":
            print("Bilgisayarın Seçimi: Makas\nMakas kağıdı keser. Kaybettin!")
            computer_score += 100

    elif user_choice == "3":
        if computer_choice == "1":
            print("Bilgisayarın Seçimi: Taş\nTaş makası kırar. Kaybettin!")
            computer_score += 100

        elif computer_choice == "2":
            print("Bilgisayarın Seçimi: Kağıt\nMakas kağıdı keser. Kazandın!")
            user_score += 100

        elif computer_choice == "3":
            print("Bilgisayarın Seçimi: Makas\nMakas makasa eşittir. Berabere!")

    else:
        break

print("\nSenin skorun: {}\nBilgisayarın skoru: {}".format(user_score, computer_score))