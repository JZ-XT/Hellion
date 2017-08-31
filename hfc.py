import os
from cmd import Cmd
from importlib import import_module
from termcolor import colored

scanners = sum([len(files) for r, d, files in os.walk('modules/scanners')])
exploits = sum([len(files) for r, d, files in os.walk('modules/exploits')])
misc     = sum([len(files) for r ,d, files in os.walk('modules/misc')]) - 1

current = None

class hfc(Cmd):
    def do_set(self, args):
        """Sets options, ex: set rhost '8.8.8.8'"""
        global current
        opt = args.split()
        exec('current.' + opt[0] + ' = ' + opt[1])
        current.reloadSettings()

    def do_exploit(self, args):
        """Runs the current module"""
        global current
        try:
            current.exploit()
        except Exception as e:
            print(str(e))

    def do_show(self, args):
        """Shows Module Options"""
        global current
        if (current == None):
            print('Module not set')
            return
        print('\nSetting : Description : Value')
        print('===============================\n')
        for setting, desc in current.settings.items():
            print(setting + ' : ' + desc['Desc'] + ' : ' + str(desc['Value']))
        print('\n')

    def do_use(self, module):
        """Sets Current Module, ex: misc.ssh.bannergrab"""
        global current
        current = import_module('modules.'+module)
        self.prompt = 'hfc ' + colored(module, 'red') + '> '
    
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
