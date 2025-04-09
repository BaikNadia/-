#  Интерактивная игра "Камень, ножницы, бумага", где пользователь соревнуется с компьютером.

## Как это работает?
1. Выбор пользователя :
Игрок вводит свой выбор ("камень", "ножницы" или "бумага").
Если игрок введёт "выход", игра завершится.

2. Выбор компьютера :
Компьютер случайно выбирает один из трёх вариантов с помощью random.choice().

3. Определение победителя :
Если выборы совпадают, объявляется ничья.
Используются условия для проверки, кто победил, основываясь на правилах игры.

4.Подсчёт очков :
За каждую победу начисляются очки игроку или компьютеру.

## Как можно развивать этот код?
1. Добавить несколько раундов :
Реализовать ограниченное количество раундов (например, 5) и определить общего победителя.

2. Графический интерфейс :
Использовать библиотеку tkinter для создания оконного приложения.

3. Расширить правила :
Добавить новые элементы (например, ящерицу и спока из расширенной версии игры).

# Игра дополнена блоком visual_version:
Что нового?

Функция show_final_score :
Отображает итоговый счёт в диалоговом окне.
После показа результата закрывает окно игры (root.destroy()).
Кнопка "Завершить игру" :
Добавлена новая кнопка, которая вызывает функцию show_final_score.

Сохранение результатов :
Сохранять результаты игры в файл для последующего просмотра.

# Игра дополнена файлом visual.html для запуска игры в браузере

Как это работает?

1.HTML :
Создаёт основную структуру игры.
Кнопки ("Камень", "Ножницы", "Бумага") позволяют игроку сделать выбор.
Отображается текущий счёт (player-score и computer-score) и результат последнего раунда (result).

2.CSS :
Добавляет базовое оформление для кнопок, текста и контейнера игры.
Создаёт привлекательный внешний вид с использованием цветов, отступов и теней.

3.JavaScript :
Логика игры реализована в функции play().
Функция getComputerChoice() генерирует случайный выбор компьютера.
После каждого хода обновляется счёт с помощью updateScores().
Функция resetGame() показывает итоговый счёт в диалоговом окне (alert) и сбрасывает игру.

## Как запустить игру?

Сохраните код в файл с расширением .html (например, rock_paper_scissors.html).

Откройте этот файл в любом браузере (Google Chrome, Firefox, Edge и т.д.).
