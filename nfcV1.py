import os,time

started = time.time()

def reader():
	readnfc = os.popen("nfc-list").read()
	uidLoc = 'UID (NFCID1):'
	indexNFC = readnfc.find(uidLoc)
	badge=-1
	if indexNFC != -1:
		badge=readnfc[indexNFC+len(uidLoc):indexNFC+len(uidLoc)+15].strip(" ")
	print(badge)
	return badge


if __name__ == '__main__':
	badge = reader()
	while(badge == -1):
		badge = reader()
		time.sleep(1)
