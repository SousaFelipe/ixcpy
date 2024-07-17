import os


def terminal(prompt: str) -> str:
    print(prompt, end=' ')
    output = str(input())
    return output


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')