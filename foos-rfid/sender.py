import serial

def setup():
    global device_a
    global device_b
    device_a = serial.Serial(
                port='/dev/tty.usbserial-AD026AOK',
                baudrate='9600',
            )

    device_b = serial.Serial(
                port='/dev/tty.usbserial-AD026AOK',
                baudrate='9600',
            )
    if not device_a.isOpen():
        device_a.open()
    if not device_b.isOpen():
        device_b.open()
    loop()

def loop():
    uuids_for_game = { 'team_a': [], 'team_b': [] }
    while len() < 4:
        uuid = device.readline().rstrip()

        if uuid in uuids_for_game:
            print 'That player is already in the game!'
        else:
            uuids_for_game.append(uuid)
    send_uuids(uuids_for_game)

def is_game_full(uuids_for_game):
    pass

def send_uuids(uuids_for_game):
    pass

if __name__ == '__main__':
    setup()
