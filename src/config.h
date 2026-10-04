#ifndef CONFIG_H
#define CONFIG_H

#define FW_VERSION "V1.0.2"

 // default 80 for http
#define SERVER_PORT 80

#define SCAN_SSIDS_NUM 10     //  The max number of SSIDs that we will scan for.

#define HOSTNAME "KNOMI"
#define AP_SSID "BTT-KNOMI" // Create a SSID for BTT KNOMI Access Point
#define AP_PWD "" // Default no password
#define AP_LOCAL_IP IPAddress(192, 168, 20, 1) // access point IP
#define AP_GATEWAY  IPAddress(192, 168, 20, 1) // gateway IP
#define AP_SUBNET   IPAddress(255, 255, 255, 0) // subnet mask

#define WIFI_STA_TIMEOUT 15000  // 15s
#define WIFI_DISABLE_SLEEP 1
#define WIFI_RECONNECT_INTERVAL_MS 5000UL

#define MOONRAKER_POLL_INTERVAL_MS 1000UL
#define MOONRAKER_GET_TIMEOUT_MS 5000UL
#define MOONRAKER_POST_TIMEOUT_MS 60000UL
#define MOONRAKER_STATUS_QUERY \
    "/printer/objects/query?webhooks&gcode_macro%20_KNOMI_STATUS&virtual_sdcard&display_status&idle_timeout"

// BTT red color for UI (RGB888)
#define LV_32BIT_BTT_RED    0xC02F30
#define LV_32BIT_BTT_BLUE   0x209ADE
#define LV_32BIT_BTT_PURPLE 0xA91DDA
#define LV_32BIT_BTT_GREEN  0x5DA910
#define LV_DEFAULT_COLOR    LV_32BIT_BTT_RED

#endif
