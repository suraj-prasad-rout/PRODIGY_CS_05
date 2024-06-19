import sys
from scapy.all import *

# Function to handle each packet


def handle_packet(packet, log):
    # Print a summary of the packet
    print(packet.summary())

    # Check if the packet contains IP layer
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # Check if the packet contains TCP layer
        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            # Write TCP connection information to log file
            log.write(
                f"TCP Connection: {src_ip}:{src_port} -> {dst_ip}:{dst_port}\n")

    else:
        # Print message if packet does not contain IP layer
        print("Packet does not contain IP layer")

    # Handle other protocols or scenarios if needed

# Main function to start packet sniffing


def main(interface, verbose=False):
    # Create log file name based on interface
    logfile_name = f"sniffer_{interface}_log.txt"

    # Open log file for writing
    with open(logfile_name, 'w') as logfile:
        try:
            # Start packet sniffing on specified interface with verbose output
            sniff(iface=interface, prn=lambda pkt: handle_packet(
                pkt, logfile), store=0)

        except KeyboardInterrupt:
            sys.exit(0)


# Check if the script is being run directly
if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python sniffer.py <interface> [verbose]")
        sys.exit(1)

    # Determine if verbose mode is enabled
    verbose = False
    if len(sys.argv) == 3 and sys.argv[2].lower() == "verbose":
        verbose = True

    # Call the main function with the specified interface and verbose option
    main(sys.argv[1], verbose)