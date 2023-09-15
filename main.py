import requests
import random
import pandas as pd
import string
import hashlib
from cryptography.fernet import Fernet


def sum(num1, num2):
    result = num1 + num2
    print(result)
    return sum

def mul(num1, num2):
    result = num1 * num2
    print(result)
    return mul

def div(num1, num2):
    result = num1 / num2
    print(result)
    return div

def min(num1, num2):
    result = num1 - num2
    print(result)
    return min

def get_random_quote():
    api_url = "https://zenquotes.io/api/random"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            if len(data) > 0:
                return data[0]['q']
            else:
                return "No quotes found."
        else:
            return "Error: Failed to fetch quotes."

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"



def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")


def todo_list():
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Higher! Try again.")
            elif guess > secret_number:
                print("Lower! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")



def analyze_data():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 28, 22],
        'Salary': [50000, 60000, 75000, 52000, 48000]
    }

    df = pd.DataFrame(data)

    print("Data Analysis:")
    print("Sample Data:")
    print(df)

    print("\nSummary Statistics:")
    print(df.describe())


    tasks = []
    while True:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        print("Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Back to Main Menu")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            task = input("Enter a task: ")
            tasks.append(task)
        elif choice == '2':
            if tasks:
                task_index = int(input("Enter the task number to remove: ")) - 1
                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    print(f"Removed: {removed_task}")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks to remove.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def check_weather():
    api_key = "YOUR_API_KEY"  # guys go to this website and add your api key 
    city = input("Enter a city: ")
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            weather_data = response.json()
            if 'main' in weather_data and 'temp' in weather_data['main']:
                temperature_kelvin = weather_data['main']['temp']
                temperature_celsius = temperature_kelvin - 273.15
                print(f"Temperature in {city}: {temperature_celsius:.2f}°C")
            else:
                print("Weather data not available.")
        else:
            print("Error: Failed to fetch weather data.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def get_random_joke():
    api_url = "https://official-joke-api.appspot.com/random_joke"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            joke_data = response.json()
            if 'setup' in joke_data and 'punchline' in joke_data:
                print("Joke:")
                print(joke_data['setup'])
                print(joke_data['punchline'])
            else:
                print("Joke data not available.")
        else:
            print("Error: Failed to fetch a joke.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")



def generate_password():
    length = int(input("Enter the length of the password: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Password:")
    print(password)


def encrypt_text():
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    plaintext = input("Enter the text to encrypt: ").encode()
    encrypted_text = cipher_suite.encrypt(plaintext)
    print("Encrypted Text:")
    print(encrypted_text.decode())

def decrypt_text():
    key = input("Enter the encryption key: ").encode()
    cipher_suite = Fernet(key)

    encrypted_text = input("Enter the encrypted text: ").encode()
    try:
        decrypted_text = cipher_suite.decrypt(encrypted_text)
        print("Decrypted Text:")
        print(decrypted_text.decode())
    except Exception as e:
        print("Decryption failed. Check the key and input text.")

def main():
    while True:
        print("\nWelcome to the Multifunctional Python Program!")
        print("1. Calculator")
        print("2. Random Quote Generator")
        print("3. Guess the Number Game")
        print("4. Data Analysis")
        print("5. To-Do List")
        print("6. Check Weather")
        print("7. Random Joke Generator")
        print("8. Password Generator")
        print("9. Text Encryption/Decryption")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            num1 = int(input("Enter your number: "))
            num2 = int(input("Enter your number: "))
            total = input("+ ,- ,*, /, ")
            if total =='+':
                sum(num1,num2)
            elif total =='-':
                min(num1,num2)
            elif total =='*':
                mul(num1,num2)
            elif total =='/':
                div(num1,num2)
        elif choice == '2':
            print("Random Quote:")
            print(get_random_quote())
        elif choice == '3':
            guess_the_number()
        elif choice == '4':
            analyze_data()
        elif choice == '5':
            todo_list()
        elif choice == '6':
            check_weather()
        elif choice == '7':
            get_random_joke()
        elif choice == '8':
            generate_password()
        elif choice == '9':
            encrypt_text()
        elif choice == '10':
            decrypt_text()
        elif choice == '11':
            
            pass
        elif choice == '12':
            
            pass
        elif choice == '13':
            
            pass
        elif choice == '14':
            
            pass
        elif choice == '15':
            
            pass
        elif choice == '16':
            
            pass
        elif choice == '17':
            
            pass
        elif choice == '18':
            
            pass
        elif choice == '19':
            
            pass
        elif choice == '20':
            
            pass
        elif choice == 'exit':
            print("program break (ft gajhalaxmi)")
            break
        else:
            print("lol all invalid")

if __name__ == "__main__":
    main()