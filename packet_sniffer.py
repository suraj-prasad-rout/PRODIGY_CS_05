#!/usr/bin/env python
import argparse
import scapy.all as scapy
from scapy.layers import http

# Function to get the network interface


def get_interface():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", required=True,
                        help="Specify interface on which to sniff packets")
    args = parser.parse_args()
    return args.interface

# Function to sniff packets on a given interface


def sniff(interface, timeout=60):
    print(f"Sniffing packets on interface: {interface} for {timeout} seconds")
    scapy.sniff(iface=interface, store=False,
                prn=process_packet, timeout=timeout)

# Function to process each captured packet


def process_packet(packet):
    log_message = "[*] Packet captured\n"

    # Extract and log the Source MAC Address
    smac = packet.src
    log_message += f"[+] Source MAC Address: {smac}\n"

    if packet.haslayer(http.HTTPRequest):
        host = packet[http.HTTPRequest].Host.decode('utf-8') if isinstance(
            packet[http.HTTPRequest].Host, bytes) else packet[http.HTTPRequest].Host
        path = packet[http.HTTPRequest].Path.decode('utf-8') if isinstance(
            packet[http.HTTPRequest].Path, bytes) else packet[http.HTTPRequest].Path
        log_message += f"[+] HTTP Request >> {host}{path}\n"

        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load.decode(
                'utf-8') if isinstance(packet[scapy.Raw].load, bytes) else packet[scapy.Raw].load
            keys = ["username", "password", "pass", "email"]
            for key in keys:
                if key in load:
                    log_message += f"\n\n\n[+] Possible username/password >> {load}\n\n\n"
                    break
    else:
        log_message += f"{packet.summary()}\n"

    # Write the log message to the file
    write_log(log_message)

# Function to write logs to a file


def write_log(message):
    with open("packet_logs.txt", "a") as log_file:
        log_file.write(message)

# Main function to execute the packet sniffer


def main():
    interface = get_interface()
    sniff(interface)


if __name__ == "__main__":
    main()
