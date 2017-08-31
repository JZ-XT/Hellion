from cmd import Cmd

#Find this automaticaly in future
scanners = 0
exploits = 0
misc     = 0

class hfc(Cmd):
    def do_exit(self, args):
        """Exits hfc"""
        exit(0)

if __name__ == "__main__":
    print('''
        Hellion Framework Console
    [Scanners: '''+str(scanners)+''', Exploits: '''+str(exploits)+''', Misc: '''+str(misc)+''']\n\n\n
    ''')
    prompt = hfc()
    prompt.prompt = 'hfc> '
    prompt.cmdloop('Starting hfc...')
