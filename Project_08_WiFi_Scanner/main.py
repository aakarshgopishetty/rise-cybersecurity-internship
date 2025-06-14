import time
import pywifi
from pywifi import const

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(2)
    results = iface.scan_results()

    print("\nNearby Wi-Fi Networks:\n")
    print(f"{'SSID':30} {'Signal (dBm)':15} {'Security'}")
    print("-" * 60)
    
    seen = set()
    for network in results:
        if network.ssid not in seen:
            seen.add(network.ssid)
            ssid = network.ssid
            signal = network.signal
            security = get_security_type(network)
            print(f"{ssid:30} {signal:<15} {security}")

def get_security_type(network):
    if network.akm:
        if const.AKM_TYPE_WPA2PSK in network.akm:
            return "WPA2-PSK"
        elif const.AKM_TYPE_WPAPSK in network.akm:
            return "WPA-PSK"
        elif const.AKM_TYPE_NONE in network.akm:
            return "Open"
    return "Unknown"

if __name__ == "__main__":
    scan_wifi()
