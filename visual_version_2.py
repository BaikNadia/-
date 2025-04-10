import random
from tkinter import Tk, Button, Label, messagebox, Frame
from PIL import Image, ImageTk  # Для работы с PNG и изменения размера
import os

# Правила игры
win_rules = {
    "rock": ["scissors", "lizard"],  # Камень побеждает ножницы и ящерицу
    "scissors": ["paper", "lizard"],  # Ножницы побеждают бумагу и ящерицу
    "paper": ["rock", "spock"],       # Бумага побеждает камень и спока
    "lizard": ["spock", "paper"],     # Ящерица побеждает спока и бумагу
    "spock": ["scissors", "rock"]     # Спок побеждает ножницы и камень
}

# Создание окна
root = Tk()
root.title("Камень, Ножницы, Бумага, Ящерица, Спок")
root.geometry("400x400")

# Функция для загрузки и изменения размера изображений
def load_images(directory, size=(50, 50)):  # Укажите желаемый размер (например, 50x50 пикселей)
    """
    Загружает изображения из указанной директории и изменяет их размер.
    """
    images_dict = {}
    for file_name in os.listdir(directory):
        if file_name.endswith(".png"):
            name = file_name.split(".")[0]  # Убираем расширение .png
            if name in win_rules:  # Проверяем, что имя файла есть в словаре win_rules
                img = Image.open(os.path.join(directory, file_name))
                img = img.resize(size)  # Изменяем размер изображения
                images_dict[name] = ImageTk.PhotoImage(img)
    return images_dict

# Путь к папке с изображениями
images_directory = "images"
if not os.path.exists(images_directory):
    raise FileNotFoundError(f"Папка {images_directory} не найдена!")

# Загрузка изображений с изменением размера
images = load_images(images_directory, size=(50, 50))  # Размер иконок 50x50 пикселей

# Инициализация счёта
player_score = 0
computer_score = 0

# Функция для обработки хода игрока
def play(player_choice):
    global player_score, computer_score

    # Выбор компьютера
    computer_choice = random.choice(list(win_rules.keys()))

    # Определение победителя
    if player_choice == computer_choice:
        result = f"Ничья! Компьютер тоже выбрал {computer_choice.capitalize()}."
    elif computer_choice in win_rules[player_choice]:
        player_score += 1
        result = f"Вы выиграли! Компьютер выбрал {computer_choice.capitalize()}."
    else:
        computer_score += 1
        result = f"Вы проиграли! Компьютер выбрал {computer_choice.capitalize()}."

    # Обновление результатов
    update_scores()
    messagebox.showinfo("Результат", result)

# Функция для обновления счёта на экране
def update_scores():
    score_label.config(text=f"Вы: {player_score} | Компьютер: {computer_score}")

# Функция для завершения игры и показа итогового счёта
def reset_game():
    global player_score, computer_score
    final_result = f"Игра завершена!\nОбщий счёт:\nВы: {player_score}\nКомпьютер: {computer_score}"
    if player_score > computer_score:
        final_result += "\nВы победили в целом!"
    elif player_score < computer_score:
        final_result += "\nКомпьютер победил в целом!"
    else:
        final_result += "\nОбщий результат — ничья!"

    messagebox.showinfo("Итоговый счёт", final_result)

    # Сброс счёта
    player_score = 0
    computer_score = 0
    update_scores()

# Метка для отображения счёта
score_label = Label(root, text="Вы: 0 | Компьютер: 0", font=("Arial", 14))
score_label.pack(pady=10)

# Создание фрейма для кнопок
buttons_frame = Frame(root)
buttons_frame.pack(pady=10)

# Кнопки с изображениями, равномерно распределённые по фрейму
for choice, image in images.items():
    Button(
        buttons_frame,
        image=image,
        command=lambda c=choice: play(c)
    ).pack(side="left", expand=True, fill="both", padx=5)

# Кнопка для завершения игры
Button(
    root,
    text="Завершить игру",
    command=reset_game,
    font=("Arial", 12),
    bg="red",
    fg="white"
).pack(pady=20)

# Запуск приложения
root.mainloop()
