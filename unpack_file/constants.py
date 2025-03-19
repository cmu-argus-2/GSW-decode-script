DATA_FORMAT = {
    "adcs" : "LB" + 6 * "f" + "B" + 3 * "f" + 9 * "H" + 6 * "B" + 4 * "f",
    "cdh" : "LbLbbbbb",
    "cmd_logs" : "LBB", 
    "comms" : "f",
    "eps" : "Lbhhhhb" + "h" * 4 + "L" * 2 + "h" * 30,
    "gps" : "fBBBHLllllHHHHHllllll",
}

FIELDS = {
    "adcs" : ["MODE", 
              "GYRO_X", 
              "GYRO_Y", 
              "GYRO_Z", 
              "MAG_X",
              "MAG_Y",
              "MAG_Z",
              "SUN_STATUS", 
              "SUN_VEC_X",
              "SUN_VEC_Y",
              "SUN_VEC_Z",
              "LIGHT_SENSOR_XM",
              "LIGHT_SENSOR_XP",
              "LIGHT_SENSOR_YM",
              "LIGHT_SENSOR_YP",
              "LIGHT_SENSOR_ZM",
              "XP_COIL_STATUS",
              "XM_COIL_STATUS",
              "YP_COIL_STATUS",
              "YM_COIL_STATUS",
              "ZP_COIL_STATUS",
              "ZM_COIL_STATUS",
              "ATTITUDE_QW",
              "ATTITUDE_QX",
              "ATTITUDE_QY",
              "ATTITUDE_QZ"],
    "cmd_logs" : ["TIME", 
                  "CMD_ID", 
                  "STATUS"],
    "cdh" : ["TIME", 
             "SC_STATE", 
             "SD_USAGE", 
             "CURRENT_RAM_USAGE",
             "REBOOT_COUNT",
             "WATCHDOG_TIMER",
             "HAL_BITFLAGS"],
    "comms" : ["RSSI"],
    "eps" : ["TIME",
        "EPS_POWER_FLAG",
        "MAINBOARD_TEMPERATURE",
        "MAINBOARD_VOLTAGE",
        "MAINBOARD_CURRENT",
        "BATTERY_PACK_TEMPERATURE",
        "BATTERY_PACK_REPORTED_SOC",
        "BATTERY_PACK_REPORTED_CAPACITY",
        "BATTERY_PACK_CURRENT",
        "BATTERY_PACK_VOLTAGE",
        "BATTERY_PACK_MIDPOINT_VOLTAGE",
        "BATTERY_PACK_TTE",
        "BATTERY_PACK_TTF",
        "XP_COIL_VOLTAGE",
        "XP_COIL_CURRENT",
        "XM_COIL_VOLTAGE",
        "XM_COIL_CURRENT",
        "YP_COIL_VOLTAGE",
        "YP_COIL_CURRENT",
        "YM_COIL_VOLTAGE",
        "YM_COIL_CURRENT",
        "ZP_COIL_VOLTAGE",
        "ZP_COIL_CURRENT",
        "ZM_COIL_VOLTAGE",
        "ZM_COIL_CURRENT",
        "JETSON_INPUT_VOLTAGE",
        "JETSON_INPUT_CURRENT",
        "RF_LDO_OUTPUT_VOLTAGE",
        "RF_LDO_OUTPUT_CURRENT",
        "GPS_VOLTAGE",
        "GPS_CURRENT",
        "XP_SOLAR_CHARGE_VOLTAGE",
        "XP_SOLAR_CHARGE_CURRENT",
        "XM_SOLAR_CHARGE_VOLTAGE",
        "XM_SOLAR_CHARGE_CURRENT",
        "YP_SOLAR_CHARGE_VOLTAGE",
        "YP_SOLAR_CHARGE_CURRENT",
        "YM_SOLAR_CHARGE_VOLTAGE",
        "YM_SOLAR_CHARGE_CURRENT",
        "ZP_SOLAR_CHARGE_VOLTAGE",
        "ZP_SOLAR_CHARGE_CURRENT",
        "ZM_SOLAR_CHARGE_VOLTAGE",
        "ZM_SOLAR_CHARGE_CURRENT",],
    "gps" : ["TIME",
            "GPS_MESSAGE_ID",
            "GPS_FIX_MODE",
            "GPS_NUMBER_OF_SV",
            "GPS_GNSS_WEEK",
            "GPS_GNSS_TOW",
            "GPS_LATITUDE",
            "GPS_LONGITUDE",
            "GPS_ELLIPSOID_ALT",
            "GPS_MEAN_SEA_LVL_ALT",
            "GPS_GDOP",
            "GPS_PDOP",
            "GPS_HDOP",
            "GPS_VDOP",
            "GPS_TDOP",
            "GPS_ECEF_X",
            "GPS_ECEF_Y",
            "GPS_ECEF_Z",
            "GPS_ECEF_VX",
            "GPS_ECEF_VY",
            "GPS_ECEF_VZ"] 
}
