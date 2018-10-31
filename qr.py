import qrcode

def crear_qr(st):
	img = qrcode.make(st)
	f = open("qr.jpg", "wb")
	img.save(f)
	f.close()
