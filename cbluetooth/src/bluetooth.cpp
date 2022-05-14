//
// Created by Wu Mianzhi on 5/14/22.
//
#include "../include/bluetooth.h"

void catch_error(GError** error)
{
    if(*error)
        std::cout<<(*error)->message<<std::endl;
    *error = nullptr;
}
void pair()
{
    GError* error = nullptr;
    GDBusProxy* agent = g_dbus_proxy_new_for_bus_sync(G_BUS_TYPE_SYSTEM,
                                                        G_DBUS_PROXY_FLAGS_NONE,
                                                        nullptr, /* GDBusInterfaceInfo */
                                                        "org.bluez",
                                                        "/org/bluez",
                                                        "org.bluez.AgentManager1",
                                                        nullptr, /* GCancellable */
                                                        &error);
    catch_error(&error);
    GDBusProxy* adapter = g_dbus_proxy_new_for_bus_sync(G_BUS_TYPE_SYSTEM,
                                                      G_DBUS_PROXY_FLAGS_NONE,
                                                      nullptr, /* GDBusInterfaceInfo */
                                                      "org.bluez",
                                                      "/org/bluez/hci0",
                                                      "org.freedesktop.DBus.Properties",
                                                      nullptr, /* GCancellable */
                                                      &error);
    catch_error(&error);
    g_dbus_proxy_call_sync(agent,
                           "RegisterAgent",
                           g_variant_new("(os)","/org/bluez/hci0", "NoInputNoOutput"),
                           G_DBUS_CALL_FLAGS_NONE,
                           -1,
                           nullptr,
                           &error);
    catch_error(&error);
    g_dbus_proxy_call_sync(adapter,
                           "Set",
                           g_variant_new("(ssv)","org.bluez.Adapter1", "Discoverable", g_variant_new("b", TRUE)),
                           G_DBUS_CALL_FLAGS_NONE,
                           -1,
                           nullptr,
                           &error);
    catch_error(&error);
    g_dbus_proxy_call_sync(adapter,
                           "Set",
                           g_variant_new("(ssv)","org.bluez.Adapter1", "Pairable", g_variant_new("b", TRUE)),
                           G_DBUS_CALL_FLAGS_NONE,
                           -1,
                           nullptr,
                           &error);
    catch_error(&error);
    auto discoverable = g_dbus_proxy_call_sync(adapter,
                                           "Get",
                                           g_variant_new("(ss)","org.bluez.Adapter1", "Pairable"),
                                           G_DBUS_CALL_FLAGS_NONE,
                                           -1,
                                           nullptr,
                                           &error);
    catch_error(&error);
    auto pairable = g_dbus_proxy_call_sync(adapter,
                                       "Get",
                                       g_variant_new("(ss)","org.bluez.Adapter1", "Pairable"),
                                       G_DBUS_CALL_FLAGS_NONE,
                                       -1,
                                       nullptr,
                                       &error);
    catch_error(&error);
    g_dbus_proxy_call_sync(agent,
                           "UnregisterAgent",
                           g_variant_new("(o)", "/org/bluez/hci0"),
                           G_DBUS_CALL_FLAGS_NONE,
                           -1,
                           nullptr,
                           &error);
//For test DO NOT USE
//    gsize r = 2;
//    GVariant* ress = nullptr;
//    g_variant_get(pairable, "(v)", &ress);
//    if(ress)
//    std::cout<<g_variant_get_boolean(ress);
}

void connect()
{
    GError* error = nullptr;
    GDBusProxy* agent = g_dbus_proxy_new_for_bus_sync(G_BUS_TYPE_SYSTEM,
                                                      G_DBUS_PROXY_FLAGS_NONE,
                                                      nullptr, /* GDBusInterfaceInfo */
                                                      "org.bluez",
                                                      "/org/bluez",
                                                      "org.bluez.AgentManager1",
                                                      nullptr, /* GCancellable */
                                                      &error);
    catch_error(&error);
    GDBusProxy* adapter = g_dbus_proxy_new_for_bus_sync(G_BUS_TYPE_SYSTEM,
                                                        G_DBUS_PROXY_FLAGS_NONE,
                                                        nullptr, /* GDBusInterfaceInfo */
                                                        "org.bluez",
                                                        "/org/bluez/hci0",
                                                        "org.freedesktop.DBus.Properties",
                                                        nullptr, /* GCancellable */
                                                        &error);
    catch_error(&error);
    g_dbus_proxy_call_sync(agent,
                           "RegisterAgent",
                           g_variant_new("(os)","/org/bluez/hci0", "NoInputNoOutput"),
                           G_DBUS_CALL_FLAGS_NONE,
                           -1,
                           nullptr,
                           &error);
    catch_error(&error);
    g_dbus_proxy_call_sync(adapter,
                           "Set",
                           g_variant_new("(ssv)","org.bluez.Adapter1", "Discoverable", g_variant_new("b", TRUE)),
                           G_DBUS_CALL_FLAGS_NONE,
                           -1,
                           nullptr,
                           &error);
    catch_error(&error);
    auto discoverable = g_dbus_proxy_call_sync(adapter,
                                               "Get",
                                               g_variant_new("(ss)","org.bluez.Adapter1", "Pairable"),
                                               G_DBUS_CALL_FLAGS_NONE,
                                               -1,
                                               nullptr,
                                               &error);
    catch_error(&error);
    g_dbus_proxy_call_sync(agent,
                           "UnregisterAgent",
                           g_variant_new("(o)", "/org/bluez/hci0"),
                           G_DBUS_CALL_FLAGS_NONE,
                           -1,
                           nullptr,
                           &error);
}