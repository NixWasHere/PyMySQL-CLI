from cmd import Cmd
from .libs import *

class PySQLPrompt(Cmd):
    dport = 3306
    host = "127.0.0.1"
    user = "root"
    password = ""
    database = ""
    cmd = ""
    prompt = f'{RED}pymsql > '
    intro = "Welcome! Type ? to list commands.\n"

    def do_EXIT(self, inp):
        print(f"Exiting..")
        return True

    def do_SETHOST(self, ip: str):
        if ip == "":
            print("Usage: SETHOST <HOST> ")
        else:
            print(f"{LIGHTRED}Checking host...")
            self.host = validate_ip_address(ip)

    def help_SETHOST(self):
        print(f"Sets host that will connect to.")

    def do_SETUSER(self, temp_user: str):
        if temp_user == "":
            print(f"{LIGHTRED}Usage: SETUSER <USER>")
        else:
            print(f"{LIGHTRED}Username saved.")
            self.user = temp_user

    def help_SETUSER(self):
        print(f"Sets username that will be used when connecting (default=root).")

    def do_SETPASS(self, temp_pass: str):
        if temp_pass == "":
            print(f"{LIGHTRED}Usage: SETPASS <PASS>")
        else:
            print(f"{LIGHTRED}Password saved.")
            self.password = temp_pass

    def help_SETPASS(self):
        print(f"Sets password that will be used when connecting.")

    def do_SETPORT(self, Dport: int):
        if Dport == "":
            print(f"{LIGHTRED}Usage: SETPORT <0-65535 DEFAULT: 3306>")
            return
        else:
            self.dport = validate_port(int(Dport))
            print(f"{LIGHTRED}Port set to {Dport}.")

    def do_SETCOMMAND(self, cmd: str):
        if cmd == "":
            print(f"{LIGHTRED}Usage: SETCOMMAND <Command>")
            return
        else:
            self.cmd = cmd

    def do_ABOUT(self, inp):
        print(f"{RED}Author: NixWasHere")

    def help_SETPORT(self):
        print(f"{LIGHTRED}Sets mysql port that will connect to (default=3306).")

    def do_SETDATABASE(self, datab: str):
        if datab == "":
            print(f"{LIGHTRED}Usage: SETDATABASE <DB>")
            return
        else:
            self.database = datab

    def do_INFO(self, inp):
        print(f"""
          {LIGHTRED}Host: {self.host}\n
          {RED}Port: {self.dport}\n
          {LIGHTRED}User: {self.user}\n
          {RED}Pass: {self.password}\n
          {LIGHTRED}Cmd : {self.cmd}\n
          {RED}DB  : {self.database}\n""")

    def do_CONNECT(self, inp):
        mysql_connection(self.host, self.dport, self.user, self.password)

    def help_CONNECT(self):
        print(f"Simply tests the connection to the target and prints out MariaDB version.")

    def help_EXECUTE(self):
        print(f"Executes custom payload.")

    def help_EXIT(self):
        print(f"Exits the program.")

    def help_SETCOMMAND(self):
        print(f"Sets the command thats going to be used in payload.")

    def do_SHOWTABLES(self, inp):
        show_tables(self.host, self.dport, self.user, self.password, self.database)

    def do_SHOWDATABASES(self, inp):
        show_databases(self.host, self.dport, self.user, self.password)

    def help_SHOWDATABASES(self):
        print(f"Prints out available Databases.")

    def help_SHOWTABLES(self):
        print(f"Prints out available Tables")

    def help_SETDATABASE(self):
        print(f"Sets the database.")

    def do_EXECUTE(self, inp):
        execute_command(self.host, self.dport, self.user, self.password, self.cmd, self.database)

    def do_Q(self, COMMAND: str):
        execute_command(self.host, self.dport, self.user, self.password, COMMAND, self.database)

    def help_Q(self, inp):
        print(f"Q stands for QUICK. This commands purpose is for quick execution of payload.")

    def help_INFO(self):
        print(f"Shows info of payload.")

    def default(self, inp):
        if inp == 'EXIT' or inp == 'QUIT':
            return self.do_EXIT(inp)

def start():
    print(LIGHTRED + open('libs/banner.txt', 'r').read())
    PySQLPrompt().cmdloop()
