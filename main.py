import random

def rock_paper_scissors():
    """
    Игра 'Камень, ножницы, бумага'. Пользователь соревнуется с компьютером.
    """
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    print("Введите ваш выбор: камень, ножницы или бумага (или 'выход' для завершения игры).\n")

    # Варианты ходов
    choices = ["камень", "ножницы", "бумага"]
    computer_score = 0
    player_score = 0

    while True:
        # Ход пользователя
        player_choice = input("Ваш выбор: ").lower()

        # Проверка выхода из игры
        if player_choice == "выход":
            print(f"\nИгра завершена.\nСчёт:\nВы: {player_score}\nКомпьютер: {computer_score}")
            break

        # Проверка корректности ввода
        if player_choice not in choices:
            print("Некорректный выбор. Попробуйте снова.\n")
            continue

        # Ход компьютера
        computer_choice = random.choice(choices)
        print(f"Компьютер выбрал: {computer_choice}")

        # Определение победителя
        if player_choice == computer_choice:
            print("Ничья!\n")
        elif (player_choice == "камень" and computer_choice == "ножницы") or \
             (player_choice == "ножницы" and computer_choice == "бумага") or \
             (player_choice == "бумага" and computer_choice == "камень"):
            print("Вы выиграли!\n")
            player_score += 1
        else:
            print("Компьютер выиграл!\n")
            computer_score += 1

# Запускаем игру
if __name__ == "__main__":
    rock_paper_scissors()
