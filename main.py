import os, platform, time

class Startup():
    def __init__(self=None) -> None:
        pass

    def clear_console(self=None):
        system = platform.system()
        if system == "Windows":
            os.system("cls")
        elif system == "Linux" or system == "Darwin":
            os.system("clear")
        else:
            print("Sorry, unable to clear console on this operating system.")

    def Start(self=None):
        try:
            os.system("pip install cx_freeze")
            Startup.clear_console()
            file_directory = input("Enter file directory, or file name > ")
            Startup.clear_console()
            onefile = input("MF Directory (Y/n) > ")
            Startup.clear_console()
            file_name = input("FAC Name? > ")

            if(onefile == "y" or onefile == "Y"):
                os.system(f'''cxfreeze {file_directory} --target-dir dist --target-name {file_name} --base console''')
            else:
                os.system(f'''cxfreeze {file_directory} --target-dir dist_man_dir --target-name {file_name} --include-modules os,platform,time --onefile''')
        except:
            print("Problem installing cx_freeze, try reinstalling and adding python to path!")
            time.sleep(3)
            quit(1)

if __name__ == '__main__':
    Startup.Start()