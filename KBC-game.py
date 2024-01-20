name = input("Enter your name sir/mam: ")
print("Kon Banega Crorepati me apka hardik swagat hai -", name, " ji")

que_1 = "Question-1! aapki computer screen pe ye rha-\n In which group of places the Kumbha Mela is held every twelve years?"
que_2 = "Question-2! aapki computer screen pe ye rha-\n Bahubali festival is related to"
que_3 = "Question-3! aapki computer screen pe ye rha-\n September 27 is celebrated every year as"
que_4 = "Question-4! aapki computer screen pe ye rha-\n Where is India Gate located?"
que_5 = "Question-5! aapki computer screen pe ye rha-\n Who had composed the original Ramayana?"

question = [que_1, que_2, que_3, que_4, que_5]
options = [
    " A. Ujjain, Puri, Prayagraj, Haridwar \n B. Prayagraj, Haridwar, Ujjain, Nasik \n C. Rameshwaram, Puri, Badrinath, Dwarika \n D. Chittrakoot, Ujjain, Prayagraj, Haridwar",
    " A. Islam \n B. Hinduism \n C. Buddhism \n D. Jainism",
    " A. Teachers' Day\n B. National Integration Day \n C. World Tourism Day \n D. International Literacy Day",
    " A. Agra \n B. Punjab \n C. Mumbai \n D. New Delhi",
    " A. Rishi Valmiki \n B. Tulsi Das \n C. Sant Ek Nath \n D. Anhinanda"
]

answers = ['B', 'D', 'C', 'D', 'A']


def kbc():
    total_prize = 0
    life_line = 1

    for i in range(5):
        print(question[i])
        print(options[i])
        print("Give the answer please within time.")
        user_input = input("Your answer (Enter A, B, C, D, or PASS): ")

        if user_input.upper() == answers[i]:
            total_prize += 1000

            if total_prize == 5000:

               print(f"\n--Jesa aapne kaha, iss prishn ka sahi uttar - {answers[i]} \n Badhai ho {name} jii!\n --ye bilkul sahi uttar h --\n -crorepati toh nhi lekin aap bante h {total_prize} ke malik!\n --Aapko milte h {total_prize} rupees {name} Jii --\n Aakhir kya krenge aap itne paise ka?? \n ### GAME SAMAPT ###")
            else:
                print(f"\n **Sahii Jawab, aap jitte hai {total_prize} rupees**")
                print(
                    f"--Jesa aapne kaha, iss prishn ka sahi uttar - {answers[i]} ye bilkul sahi h --\n -Toh chaliye badte h aagle prishn ki or-\n")

        elif user_input.upper() == "PASS" and life_line > 0:
            confirm = input("Kya aap apni ik matr lifeline ka ismaal krna chate h?\n (aapka jawab Yes or No): ").upper()
            if confirm == "YES":
                total_prize += 1000
                life_line -= 1
                print(f"*Aapne lifeline ka istemaal kiya!*\n **Ab aapke pass ik bhi lifeline sesh nhi hai* - {life_line} \n *Aapko milte hain agle sawaal ke saath {total_prize} rupees.*\n")
                continue
            else:
                print("Aapne lifeline ka istemaal nahi kiya! Try again.")
            continue


        else:
            print("\n***Uff Aapka jawab galat hai. Akhir kya soch ke apne ye jawaab diya!!***")
            print(f"--toh apke jankari ke liye hum bta de, sahi uttar hota - {answers[i]} hota--")
            print("**Kher koi baat nhi, Aap jeet ke le jare h - ", total_prize, "Rupees**")
            print("*Aapko Dher sari badhayiaan*")

            break

kbc()
