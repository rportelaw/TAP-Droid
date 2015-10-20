with open('myinput.sh') as f:
    final_hex = (line.rsplit(None, 1)[-1] for line in f)
    for hexa, hexb in zip(final_hex, final_hex):
        hexc = int(hexa, 16)
        hexd = int(hexb, 16)
        print('adb shell input tap', hexc, hexd)
