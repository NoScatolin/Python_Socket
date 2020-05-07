#!/usr/bin/python
import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
codigo = cliente.connect_ex((ip, porta))