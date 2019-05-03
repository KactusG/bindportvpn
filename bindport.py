import subprocess

portl = input("Введите порт: ")
ipl = input("Введите ip на который переадресовывать: ")
subprocess.run(["bash", "getip.sh"])
print(subprocess.run(["cat", "ip.txt"]))
ipv = input("Введите ip который сейчас высветился: ")

subprocess.run(["iptables", "-t", "nat", "-A", "PREROUTING", "-p", "udp", "--dst", "0.0.0.0/0", "--dport", portl, "-j", "DNAT", "--to-destination", ipl + str(":") + portl])
subprocess.run(["iptables", "-t", "nat", "-A", "PREROUTING", "-p", "tcp", "--dst", "0.0.0.0/0", "--dport", portl, "-j", "DNAT", "--to-destination", ipl + str(":") + portl])
subprocess.run(["iptables", "-t", "nat", "-A", "POSTROUTING", "-p", "udp", "--dst", ipl, "--dport", portl, "-j", "SNAT", "--to-source", ipv])
subprocess.run(["iptables", "-t", "nat", "-A", "POSTROUTING", "-p", "tcp", "--dst", ipl, "--dport", portl, "-j", "SNAT", "--to-source", ipv])
subprocess.run("/sbin/iptables-save")
subprocess.run(["rm", "ip.txt"])
print("Порты добавлены")
