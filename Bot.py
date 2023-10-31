import urllib.request
import json
import colorama
colorama.init()
import os

print(colorama.Fore.YELLOW + '''
██╗░░██╗░█████╗░██╗░░██╗░█████╗░░█████╗░████████╗░░░░░░██████╗░░█████╗░████████╗
██║░██╔╝██╔══██╗██║░░██║██╔══██╗██╔══██╗╚══██╔══╝░░░░░░██╔══██╗██╔══██╗╚══██╔══╝
█████═╝░███████║███████║██║░░██║██║░░██║░░░██║░░░█████╗██████╦╝██║░░██║░░░██║░░░
██╔═██╗░██╔══██║██╔══██║██║░░██║██║░░██║░░░██║░░░╚════╝██╔══██╗██║░░██║░░░██║░░░
██║░╚██╗██║░░██║██║░░██║╚█████╔╝╚█████╔╝░░░██║░░░░░░░░░██████╦╝╚█████╔╝░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚════╝░░░░╚═╝░░░░░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░
Remake by Silal

- Help:
    - QuizID: https://play.kahoot.it/v2/lobby?quizId=eab4ca4e-e3a7-4672-8cfc-62bd0b93f661
                                                     ^            copy this!            ^
Socials:
    - Twitch: https://twitch.tv/ytsilal
    - Discord: silal
''')

def kahoot_answers():
    id = input(colorama.Fore.RED + "[Enter gameid/quizid!]> ")
    url = f"https://play.kahoot.it/rest/kahoots/{id}"
    color_list = [colorama.Fore.RED + "red", colorama.Fore.BLUE + "blue", colorama.Fore.YELLOW + "yellow", colorama.Fore.GREEN + "green"]
    corect_colors = []

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
        questions = json.loads(data)["questions"]

        print(corect_colors)

        for index, slide in enumerate(questions):
            for i, choice in enumerate(slide.get("choices", [])):
                if choice.get("correct", False):
                    print(f"{color_list[i]}-{index+1}: {choice.get('answer')}")

    except urllib.error.HTTPError:
        print("That Kahoot doesn`t exist or is Private!")


while True:
    kahoot_answers()
    print()