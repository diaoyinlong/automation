import os
from com.android.monkeyrunner import MonkeyRunner

CMD_MAP = {
    'TOUCH': lambda dev, arg: dev.touch(**arg),
    'DRAG': lambda dev, arg: dev.drag(**arg),
    'PRESS': lambda dev, arg: dev.press(**arg),
    'TYPE': lambda dev, arg: dev.type(**arg),
    'WAIT': lambda dev, arg: MonkeyRunner.sleep(**arg)
}

root_path = 'D:/automation_test/'
file_parent_path = root_path + 'MobileTest/Action/'

file_list = os.listdir(file_parent_path)

package = 'com.kongfz.app'
startActivity = 'com.kongfz.app.view.SplashActivity'


def process_file(fp, device):
    for line in fp:
        (cmd, rest) = line.split('|')
        try:
            rest = eval(rest)
        except:
            print('unable to parse options')
            continue

        if cmd not in CMD_MAP:
            print('unknown command: ' + cmd)
            continue

        CMD_MAP[cmd](device, rest)


def main():
    device = MonkeyRunner.waitForConnection()

    for file in file_list:
        fp = open(file_parent_path + file, 'r')

        try:
            process_file(fp, device)

        finally:
            fp.close()
            result = device.takeSnapshot()
            result.writeToFile(root_path + '/Log/' + file.split('/')[4] + '.png', 'png')

            device.startActivity(component=package + '/' + startActivity)
            MonkeyRunner.sleep(5)


if __name__ == '__main__':
    main()
