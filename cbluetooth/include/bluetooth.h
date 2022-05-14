//
// Created by Wu Mianzhi on 5/14/22.
// Code here is designed to control BlueZ through DBus implemented by GIO to set the bluetooth state.
//

#ifndef MRSS_BLUETOOTH_BLUETOOTH_H
#define MRSS_BLUETOOTH_BLUETOOTH_H
#include <string>
#include <gio/gio.h>
#include <iostream>
/**
 * @effect Catch the error and output to std::cout (if error is existed)
 * @param pointer of a pointer pointed GError
 */
void catch_error(GError** error);

/**
 * @effect Set the device can be discovered, paired, and connected
 * @implements Use DBus implemented by GIO to control BlueZ\n
 * Method invoked : RegisterAgent(NoInputNoOutput), Set(Discoverable), Set(Pairable)
 */
void pair();

/**
 * @effect Set the device can be discovered and connected
 * @implements Use DBus implemented by GIO to control BlueZ\n
 * Method invoked:RegisterAgent(NoInputNoOutput), Set(Discoverable)
 */
void connect();


#endif //MRSS_BLUETOOTH_BLUETOOTH_H
