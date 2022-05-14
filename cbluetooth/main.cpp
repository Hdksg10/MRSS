
#include <gio/gio.h>
#include <iostream>
#include <string>
#include <thread>

#include "./include/bluetooth.h"
#include "./include/cpp_socket_server.h"

//For test bluetooth module
using std::thread;
int main (int argc, char *argv[])
{
    pair();
    connect();
    thread socket(socket_server);
    socket.join();
    return 0;
}