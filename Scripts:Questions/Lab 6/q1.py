user = input("What is your name: ")
amount = float(input("How much would you like to send: "))
recipient = input("Who is your recipient: ")
sec_question = input("What is your security question: ")
sec_answer1 = input("What is your security answer: ")

answer = input(f"{recipient} you recieved {amount} from {user} do you accept?: ")
if answer.lower() == "n":
    print(user,"your e-transfer is declined by,",recipient)
if answer.lower() == "y":
    sec_answer2 = input(f"Security Question: {sec_question}: ")
    if sec_answer1.lower() == sec_answer2.lower():
        print("The security question's answer is correct, the money is deposit in your account.")
    else:
        print("Sorry, the security questions answer is wrong, the money is returned to",user)