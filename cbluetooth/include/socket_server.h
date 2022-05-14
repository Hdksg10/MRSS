//
// Created by Wu Mianzhi on 4/16/22.
// Code here is designed to create a socket server to receive message from apps.
//

#ifndef MRSS_bluetooth_SOCKET_SERVER_H
#define MRSS_bluetooth_SOCKET_SERVER_H
#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <bluetooth/bluetooth.h>
#include <bluetooth/rfcomm.h>

/**
 * @effect Create a socket server for bluetooth connection
 * @note Max buffer size : 1024
 */
void socket_server();

#endif //MRSS_bluetooth_SOCKET_SERVER_H
