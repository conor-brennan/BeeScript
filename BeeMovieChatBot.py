import keyboard

words = []
WORD_DELAY = 0.5
START = 'ctrl'
STOP = 'shift'

welcome_text = "Path to file: "
error_text = "File not found. Make sure to input the correct path to file"
instructions_query = "Would you like to read the instructions before continuing? Y/N "
continue_text = "Press enter to continue\n"

instructions_text1 = "\nOnce you have finished reading the instructions, the script will be active\n"
instructions_text2 = "To start the chat bot, you will only have to press " + START + "\n"
instructions_text3 = "If you have started the chat bot and wish to terminate it early, hold " + STOP + \
                     " until the program terminates\n"
instructions_text4 = "Each word will take approx. " + str(WORD_DELAY * 2) + "s to be output. This can be changed " \
                     "by changing the WORD_DELAY variable\n"
instructions_text5 = "Would you like to read the instructions again? Y/N "

starting_text = "\nThe chat bot is live. Press " + START + " when you are ready to begin\n"


def locate_text_file():
    in_path = ""
    while in_path == "":
        try:
            in_path = input(welcome_text)
            in_file = open(in_path, "r")
            parse_text_file(in_file)
            in_file.close()

            instructions = input(instructions_query).lower()
            print(starting_text)

            if instructions == "y":
                display_instructions()
        except FileNotFoundError:
            print("\n" + error_text + "\n")
            in_path = ""


def parse_text_file(text):
    for line in text.readlines():
        parse_words(line)


def parse_words(txt):
    start = 0
    index = 0
    length = len(txt)
    for char in txt:
        if char == " ":
            if start == index:
                start += 1
            else:
                words.append(txt[start:index])
                start = index + 1
        if char == "\n":
            if start == index:
                start += 2
            else:
                words.append(txt[start:index])
                start = index + 2
        index += 1
        if length == index and start != index:
            words.append(txt[start:index])


def display_instructions():
    print(instructions_text1)
    input(continue_text)
    print(instructions_text2)
    input(continue_text)
    print(instructions_text3)
    input(continue_text)
    print(instructions_text4)
    input(continue_text)

    repeat = input(instructions_text5).lower()
    if repeat == "y":
        display_instructions()

def chat_bot():
    keyboard.wait(START)
    keyboard.release(START)
    for word in words:
        if keyboard.is_pressed(STOP):
            break
        keyboard.write(word)
        keyboard.send("enter")
        keyboard.write("  ", delay=WORD_DELAY)
        keyboard.send('backspace')
        keyboard.send('backspace')


# parse_words("I am now trying to optimize timing to not glitch while also spamming")
# parse_words("This is support for a second sentence")
# parse_words("and maybe even a third!")

locate_text_file()
chat_bot()
