import time
import socket
import struct


class S7:
	def __init__(self, ip_addr):
		self.ip = ip_addr
		self.SocketFlag = False
		self.S7Socket = None
		self._Connect()

	def AccessS7(self, db_no, db_offset, db_len=0, db_data=None):
		if not self.SocketFlag:
			if not self._Connect():
				return False
		try:
			cmd = self._CreateBuf(db_no, db_offset, db_len, db_data)
			self.S7Socket.CoreSocket.sendall(cmd)
			res,msg= self.S7Socket.ReceiveMessage()
			if res:
				return True,self._AnalysisResult(msg, db_len)
			else:
				self.SocketFlag=False
				return False,msg
		except Exception as e:
			self.SocketFlag = False
			return False,str(e)

	def _Connect(self):
		try :
			self.S7Socket = _NetworkBase()
			res,msg=self.S7Socket.CreateSocketAndConnect(self.ip, 102)
			if res:
				self.S7Socket.CoreSocket.sendall(self.S7Socket.plcHead1)
				res, msg = self.S7Socket.ReceiveMessage()
				if res:
					self.S7Socket.CoreSocket.sendall(self.S7Socket.plcHead2)
					res, msg = self.S7Socket.ReceiveMessage()
					if res:
						self.SocketFlag = True
						return True
			return False,msg
		except Exception as e:
			return False,str(e)

	def _CreateBuf(self, db_no, db_offset, db_len=0, data=None):
		#   read S7
		if data is None:
			Command = bytearray(31)
			Command[0] = 0x03
			Command[1] = 0x00
			Command[2] = len(Command) // 256  # 长度
			Command[3] = len(Command) % 256
			Command[4] = 0x02  # 固定
			Command[5] = 0xF0
			Command[6] = 0x80
			Command[7] = 0x32  # 协议标识
			Command[8] = 0x01  # 命令：发
			Command[9] = 0x00  # redundancy identification
			# (reserved): 0x0000;
			Command[10] = 0x00  # protocol data unit reference;
			# it’s increased by request
			# event;
			Command[11] = 0x00
			Command[12] = 0x01  # 参数命令数据总长度
			Command[13] = (len(Command) - 17) // 256
			Command[14] = (len(Command) - 17) % 256
			Command[15] = 0x00  # 读取内部数据时为00，读取CPU型号为Data数据长度
			Command[16] = 0x00
			# =====================================================================================
			Command[17] = 0x04  # 读写指令，04读，05写
			Command[18] = 1  # 读取数据块个数
			Command[19] = 0x12			# 指定有效值类型
			Command[20] = 0x0A			# 接下来本次地址访问长度
			Command[21] = 0x10			# 语法标记，ANY
			Command[22] = 0x02			# 按字为单位
			Command[23] = db_len // 256			# 访问数据的个数
			Command[24] = db_len % 256
			Command[25] = db_no // 256			# DB块编号，如果访问的是DB块的话
			Command[26] = db_no % 256
			Command[27] = 0x84			# 访问数据类型
			Command[28] = db_offset * 8 // 256 // 256 % 256			# 偏移位置
			Command[29] = db_offset * 8 // 256 % 256
			Command[30] = db_offset * 8 % 256

		#   write S7
		else:
			Command = bytearray(35+len(data))
			Command[0] = 0x03
			Command[1] = 0x00
			Command[2] = (35 + len(data)) // 256			# 长度
			Command[3] = (35 + len(data)) % 256
			Command[4] = 0x02			# 固定
			Command[5] = 0xF0
			Command[6] = 0x80
			Command[7] = 0x32
			Command[8] = 0x01			# 命令 发
			Command[9] = 0x00			# 标识序列号
			Command[10] = 0x00
			Command[11] = 0x00
			Command[12] = 0x01
			Command[13] = 0x00			        # 固定
			Command[14] = 0x0E
			Command[15] = (4 + len(data)) // 256			# 写入长度+4
			Command[16] = (4 + len(data)) % 256
			Command[17] = 0x05		        	# 读写指令
			Command[18] = 0x01		        	# 写入数据块个数
			Command[19] = 0x12			        # 固定，返回数据长度
			Command[20] = 0x0A
			Command[21] = 0x10
			Command[22] = 0x02			        # 写入方式，1是按位，2是按字
			Command[23] = len(data) // 256		# 写入数据的个数
			Command[24] = len(data) % 256
			Command[25] = db_no // 256			# DB块编号，如果访问的是DB块的话
			Command[26] = db_no % 256
			Command[27] = 0x84			        # 写入数据的类型
			Command[28] = db_offset*8 // 256 // 256 % 256			# 偏移位置
			Command[29] = db_offset*8 // 256 % 256
			Command[30] = db_offset*8 % 256
			Command[31] = 0x00		        	# 按字写入
			Command[32] = 0x04
			Command[33] = len(data) * 8 // 256	# 按位计算的长度
			Command[34] = len(data) * 8 % 256
			Command[35:] = data

		return Command

	def _AnalysisResult(self, result, length):
		len = result.__len__()
		buffer = bytearray(length)
		if len - length == 25 and result[21] == 0xFF and result[22] == 0x04:
			buffer[:length] = result[25:25 + length]
			return buffer
		return "写入数据成功"

#   used internal

class _NetworkBase:
	plcHead1 = bytearray(
		[0x03, 0x00, 0x00, 0x16, 0x11, 0xE0, 0x00, 0x00, 0x00, 0x01, 0x00, 0xC0, 0x01, 0x0A, 0xC1, 0x02, 0x01, 0x02,
		 0xC2, 0x02, 0x01, 0x00])
	plcHead2 = bytearray(
		[0x03, 0x00, 0x00, 0x19, 0x02, 0xF0, 0x80, 0x32, 0x01, 0x00, 0x00, 0x04, 0x00, 0x00, 0x08, 0x00, 0x00, 0xF0,
		 0x00, 0x00, 0x01, 0x00, 0x01, 0x01, 0xE0])
	CoreSocket = None

	def Receive(self, length):
		totle = 0
		data = bytearray()
		try:
			while totle < length:
				data.extend(self.CoreSocket.recv(length - totle))
				totle = len(data)
			return True, data
		except Exception as e:
			return False, str(e)

	def CreateSocketAndConnect(self, ipAddress, port, timeout=1):
		try:
			self.CoreSocket = socket.socket()
			self.CoreSocket.settimeout(timeout)
			self.CoreSocket.connect((ipAddress, port))
			return True,"socket连接成功"
		except Exception as e:
			return False,str(e)

	def ReceiveMessage(self):
		try:
			headResult, headData = self.Receive(4)
			if headResult == False:
				return headResult, headData
			contentLength = headData[2] * 256 + headData[3] - 4
			if contentLength == 0:
				return False, 0
			else:
				contentResult, contentData = self.Receive(contentLength)
				return contentResult, headData + contentData
		except Exception as e:
			return False,str(e)


if __name__ == "__main__":
	x = S7("10.168.1.21")
	while True:
		res,rd = x.AccessS7(db_no=1, db_offset=42, db_len=4)
		if res:
			res = struct.unpack('>f', rd)[0]
			print(res)
			res,wd=x.AccessS7(db_no=1, db_offset=2, db_data=struct.pack('>f',res+50))
			print(wd)
		# y = x.WriteS7(db_no=1, db_offset=58, db_len=1)
		time.sleep(0.08)
