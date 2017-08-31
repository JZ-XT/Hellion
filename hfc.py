import os
from cmd import Cmd
from importlib import import_module

scanners = sum([len(files) for r, d, files in os.walk('modules/scanners')])
exploits = sum([len(files) for r, d, files in os.walk('modules/exploits')])
misc     = sum([len(files) for r ,d, files in os.walk('modules/misc')]) - 1

current = None

class hfc(Cmd):
    def do_show(self, args):
        """Shows Module Options"""
        raise NotImplementedError()

    def do_use(self, module):
        """Sets Current Module, ex: misc.ssh.bannergrab"""
        current = import_module('modules.'+module)
        self.prompt = 'hfc ' + module + '> '
    
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
