def allmycode():
    print("This is the place where you access all my code: ")
    print("a = link to github b = repositories c = quit")
    code = input("What would you like to see: ")
    if code == "a":
        print("https://github.com/AzielSolomon")

    elif code == "b":
        x = input("g = Guessing-Games or  a = calculators")
        if x == "g":
            import random

            number = random.randint(1, 10)
            tries = 1

            name = input("Hello, What is your name?")

            print("Hello", name + ".", )

            question = input("Would you like to play a game? [Y/N] ")
            if question == "n":
                print("oh..okay your loss")

            if question == "y":
                print("I'm thinking of a number between 1 & 10")
            guess = int(input("Have a guess: "))
            if guess > number:
                print("Guess lower...")
            if guess < number:
                print("Guess higher..")
            while guess != number:
                tries += 1
                guess = int(input("Try again: "))
                if guess < number:
                    print("Guess Higher...")
                if guess > number:
                    print("Guess Lower...")
            if guess == number:
                print("Congratulations you win!!! The number was {0} and it only took you {1} tries".format(number, tries))

        else:
            p = input("e = Bmi Calculator h = Normal Calculator")
            if p == "e":
                height = float(input("Enter height in meters : "))
                weight = float(input("Enter weight in kg: "))
                bmi = weight / (height ** 2)
                print("Your BMI is: {0} and you are: ".format(bmi), end='')
                if (bmi < 16):
                    print("severely underweight")
                elif (bmi >= 16 and bmi < 18.5):
                    print("underweight")
                elif (bmi >= 18.5 and bmi < 25):
                    print("healthy")
                elif (bmi >= 25 and bmi < 30):
                    print("overweight")
                elif (bmi >= 30):
                    print("severely overweight")

            else:
                Intro = "This is a calculator that calculates Addition Mutlplication and Subtration and Divivsion"
            Example = "For the first question you could put 1, so that means you are doing addition and for the second question put 6 for the third question put 10 and you will get an output of 16"
            print(Intro)
            print(Example)


            def add(x, y):
                return x + y


            def subtract(x, y):
                return x - y


            def multiply(x, y):
                return x * y


            def divide(x, y):
                return x / y


            print("Chose the operation you want to do")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")

            while True:
                choice = input("Enter choice(1/2/3/4): ")

                if choice in ('1', '2', '3', '4'):
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice == '1':
                        print(num1, "+", num2, "=", add(num1, num2))

                    elif choice == '2':
                        print(num1, "-", num2, "=", subtract(num1, num2))

                    elif choice == '3':
                        print(num1, "*", num2, "=", multiply(num1, num2))

                    elif choice == '4':
                        print(num1, "/", num2, "=", divide(num1, num2))
                    break
                else:
                    print("Enter a valid number or READ example AND intro")

    elif code == "c":
        quit()


allmycode()