"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_number = 1
    max_number = 100
    predict_number = np.random.randint(1, 101) #предполагаемое число
    while True:
        # воспользуемся алгоритмом бинарного поиска
        count += 1
        if number < predict_number:
            max_number = predict_number - 1
            predict_number = (max_number+min_number)//2
        elif number > predict_number:
            min_number = predict_number + 1
            predict_number = (max_number+min_number)//2
        else:
            break  # выход из цикла если угадали
    return count
print(f'Количество попыток: {random_predict()}')


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
