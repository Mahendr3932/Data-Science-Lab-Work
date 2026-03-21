import random
import time

# Slow text effect
def slow_print(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# ASCII Title
def show_title():
    print("""
  ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
  ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
  ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
  ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
  ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
  ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
        🎯 NUMBER GUESSING GAME 🎯
    """)

def play_game():
    number = random.randint(1, 100)
    attempts = 7
    score = 100

    slow_print("\n🤖 I have selected a number between 1 and 100.")
    slow_print("🔥 You have 7 attempts to guess it!\n")

    while attempts > 0:
        try:
            guess = int(input("👉 Enter your guess: "))
        except:
            print("⚠️ Invalid input! Enter a number.")
            continue

        print("⏳ Checking...")
        time.sleep(0.5)

        if guess == number:
            print("""
🎉🎉🎉 YOU WIN! 🎉🎉🎉
██████╗  ██████╗ ██████╗ 
██╔══██╗██╔═══██╗██╔══██╗
██████╔╝██║   ██║██████╔╝
██╔═══╝ ██║   ██║██╔══██╗
██║     ╚██████╔╝██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝
""")
            slow_print(f"🏆 Final Score: {score}")
            break

        elif guess > number:
            print("📉 Too high!")
        else:
            print("📈 Too low!")

        # Hint system
        diff = abs(guess - number)
        if diff <= 5:
            print("🔥 VERY CLOSE!")
        elif diff <= 10:
            print("😎 Close!")
        else:
            print("❄️ Far away!")

        attempts -= 1
        score -= 10

        print(f"❤️ Attempts left: {attempts}")
        print(f"⭐ Score: {score}")
        print("-" * 40)

    if attempts == 0:
        print("""
💀 GAME OVER 💀
  ________                       
 /  _____/_____    _____   ____  
/   \  ___\__  \  /     \_/ __ \ 
\    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  (____  /__|_|  /\___  >
        \/     \/      \/     \/ 
""")
        slow_print(f"The correct number was: {number}")

def main():
    show_title()
    slow_print("🎮 Welcome Player!")
    time.sleep(1)

    while True:
        play_game()
        choice = input("\n🔁 Play again? (yes/no): ").lower()
        if choice != "yes":
            slow_print("\n👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()