//
// Created by Wu Mianzhi on 5/14/22.
// The Header File is to fix the undefined reference error when invoke C function in CPP source code file

#ifndef MRSS_BLUETOOTH_CPP_SOCKET_SERVER_H
#define MRSS_BLUETOOTH_CPP_SOCKET_SERVER_H
extern "C"
{
#include "socket_server.h"
}
#endif //MRSS_BLUETOOTH_CPP_SOCKET_SERVER_H
