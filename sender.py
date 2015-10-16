import serial

def setup():
    global device
    device = serial.Serial(
                port='/dev/tty.usbserial-AD026AOK',
                baudrate='9600',
            )
    if not device.isOpen():
        device.open()
    loop()

def loop():
    uuids_for_game = []
    while len(uuids_for_game) < 4:
        uuid = device.readline().rstrip()

        if uuid in uuids_for_game:
            print 'That player is already in the game!'
        else:
            uuids_for_game.append(uuid)
    send_uuids(uuids_for_game)

def send_uuids(uuids_for_game):
    pass

if __name__ == '__main__':
    setup()
