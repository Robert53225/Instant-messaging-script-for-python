import socket as soc
import time 
import threading
s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
port = int(input("PORT:"))
nop = int(input("Number of People:"))
print("---------------")
print("Start server...")
s.bind(("0.0.0.0", port))
s.listen(nop)
while True:
	p, addr = s.accept()
	def acc():
			print(f"\n用户已加入[{addr}]")
			p.send("你已加入服务器, 现在可以开始聊天了\n".encode("utf-8"))
	def rec():
		try:
			while True:
				me = p.recv(1024).decode("utf-8")
				print(f"[{addr}]user:{me}")
				p.send(f"<用户{addr}>{me}".encode("utf-8"))
		except:
			print(f"客户端{addr}断开连接")
	def say():
		while True:
			sayy = input("")
			p.send(f"<管理员>{sayy}".encode("utf-8"))
	say_td = threading.Thread(target=say)
	say_td.start()
	acc_td = threading.Thread(target=acc)
	acc_td.start()
	rec_td = threading.Thread(target=rec)
	rec_td.start()