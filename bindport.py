import subprocess

portl = input("Введите порт: ")
ipl = input("Введите ip на который переадресовывать: ")

subprocess.run(["iptables", "-t", "nat", "-A", "PREROUTING", "-p", "udp", "-m", "udp", "--dport", portl, "-j", "DNAT", "--to-destination", ipl + str(":") + portl])
subprocess.run("/sbin/iptables-save")

print("Порты добавлены")
