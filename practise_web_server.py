#!/usr/bin/env python3


import socket
# Импортируем модуль datetime для работы с датой и временем
import datetime
# Импортируем модуль signal для обработки сигналов
import signal
# Импортируем модуль sys для выхода из программы
import sys

# Создаем сокет с параметрами AF_INET (сетевой сокет) и SOCK_STREAM (TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Привязываем сокет к адресу 0.0.0.0 (все интерфейсы) и порту 1303
server_socket.bind(('0.0.0.0', 1303))
# Начинаем прослушивать сокет с максимальным количеством подключений 1
server_socket.listen(1)

# Определяем функцию для обработки сигнала прерывания Ctrl+C
def signal_handler(signal, frame):
    # Закрываем сокет
    server_socket.close()
    # Выводим сообщение о завершении работы
    print('Сервер остановлен')
    # Выходим из программы
    sys.exit(0)

# Регистрируем функцию для обработки сигнала SIGINT
signal.signal(signal.SIGINT, signal_handler)

# Выводим сообщение о запуске сервера
print('Сервер запущен')

# Входим в бесконечный цикл
while True:
    # Принимаем новое подключение от клиента
    client_socket, client_address = server_socket.accept()
    # Выводим сообщение о подключении клиента
    print('Подключен клиент с адресом', client_address)
    # Получаем текущую дату и время в формате 23.09.2023 13:10
    date_time = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
    # Отправляем клиенту строку с датой и временем
    client_socket.send(date_time.encode())
    # Закрываем соединение с клиентом
    client_socket.close()
    # Выводим сообщение о закрытии соединения
    print('Соединение с клиентом закрыто')
