import random
from tkinter import Tk, Button, Label, messagebox, StringVar

def play(player_choice):
    """
    Обработка хода игрока.
    """
    global player_score, computer_score

    # Выбор компьютера
    choices = ["камень", "ножницы", "бумага"]
    computer_choice = random.choice(choices)

    # Определение победителя
    if player_choice == computer_choice:
        result = "Ничья!"
    elif (player_choice == "камень" and computer_choice == "ножницы") or \
         (player_choice == "ножницы" and computer_choice == "бумага") or \
         (player_choice == "бумага" and computer_choice == "камень"):
        result = "Вы выиграли!"
        player_score += 1
    else:
        result = "Компьютер выиграл!"
        computer_score += 1

    # Обновление результатов
    update_scores()
    messagebox.showinfo("Результат", f"Вы выбрали: {player_choice}\n"
                                   f"Компьютер выбрал: {computer_choice}\n"
                                   f"{result}")

def update_scores():
    """
    Обновление счёта на экране.
    """
    score_label.set(f"Вы: {player_score} | Компьютер: {computer_score}")

def show_final_score():
    """
    Показывает итоговый счёт и завершает игру.
    """
    messagebox.showinfo("Итоговый счёт", 
                       f"Игра завершена!\n"
                       f"Общий счёт:\nВы: {player_score}\nКомпьютер: {computer_score}")
    root.destroy()  # Закрываем окно

# Создание окна
root = Tk()
root.title("Камень, Ножницы, Бумага")
root.geometry("350x250")

# Счёт
player_score = 0
computer_score = 0
score_label = StringVar()
score_label.set("Вы: 0 | Компьютер: 0")

# Метка для отображения счёта
Label(root, textvariable=score_label, font=("Arial", 14)).pack(pady=10)

# Кнопки для выбора
Button(root, text="Камень", command=lambda: play("камень"), font=("Arial", 12), width=10).pack(pady=5)
Button(root, text="Ножницы", command=lambda: play("ножницы"), font=("Arial", 12), width=10).pack(pady=5)
Button(root, text="Бумага", command=lambda: play("бумага"), font=("Arial", 12), width=10).pack(pady=5)

# Кнопка для завершения игры
Button(root, text="Завершить игру", command=show_final_score, font=("Arial", 12), width=15, bg="red", fg="white").pack(pady=20)

# Запуск приложения
root.mainloop()
