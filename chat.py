import socket as soc
import threading
import time
#初始化基础变量、对象等
c = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
port = 14454
xzcd_cfg = {"专服1":"192.168.0.8", "专服2":"127.0.0.1"}
#绘制UI
print("即时通讯-PYTHON版\n-------------")
xzcd = ["专服1","专服2", "自定义", "软件信息"]
for xzcddd in xzcd:
	print(f"[{xzcddd}]")
aod = input("-------------\n连接服务器: ")
##开始掉头发
#判断用户写的是黄片网址还是正确内容
try:
	if aod in xzcd_cfg:
		ip = xzcd_cfg[aod]
	elif aod == "自定义":
		ip = input("You IP:")
		port = int(input("You PORT:"))
	else:
		print("-------------\n小可爱,你乱写的样子真的很可爱!(地球话:别瞎写!)")
		time.sleep(3)
		quit()
except Exception as e:
	print(f"报错内容:{e}")
c.connect((ip, port))
#定义俩Byd函数,一个发屎一个赤屎
def recv():
	try:
		while True:
			mess = c.recv(4096).decode("utf-8")
			print(mess)
	except Exception as e:
		print(f"无法连接到服务器\n--------------\n自己滚去重连!")
		time.sleep(2)
		print(f"程序赤屎失败:{e}")
		c.close()
def send():
	try:
		while True:
			cme = input("")
			c.send(cme.encode("utf-8"))
	except:
		print("无法连接到服务器")
		time.sleep(3)
		c.close()
#多线程！启动！
recv_td = threading.Thread(target=recv)
recv_td.start()
send_td = threading.Thread(target=send)
send_td.start()