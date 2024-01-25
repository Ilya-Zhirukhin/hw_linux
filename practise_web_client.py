#!/usr/bin/env python3

import socket

# Запрашиваем у пользователя IP адрес сервера
server_ip = input('Введите IP адрес сервера: ')

# Создаем сокет с параметрами AF_INET (сетевой сокет) и SOCK_STREAM (TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Подключаемся к серверу по адресу и порту 1303
client_socket.connect((server_ip, 1303))

# Получаем данные от сервера
data = client_socket.recv(1024)
# Декодируем данные из байтов в строку
data = data.decode()
# Выводим данные на экран
print('Получено от сервера:', data)

# Закрываем сокет
client_socket.close()
