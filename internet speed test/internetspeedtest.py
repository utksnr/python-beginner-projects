import speedtest

stest=speedtest.Speedtest()

def convert(bytes):
    KB = 1024
    MB = KB*1024
    return int(bytes/MB)

downloadspeed= convert(stest.download())
print(f"Downdload speed: {downloadspeed}")
uploadspeed = convert(stest.upload())
print(f"Upload speed: {uploadspeed}")
