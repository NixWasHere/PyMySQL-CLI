from colorama import Fore
import ipaddress
import pymysql

RED = Fore.RED
LIGHTRED = Fore.LIGHTRED_EX

def validate_ip_address(ip_string):
   try:
       ip_object = ipaddress.ip_address(ip_string)
       print(f"The IP address {ip_object} is valid.")
       return str(ip_object)
   except ValueError:
       print(f"The IP address {ip_string} is not valid")

def validate_port(port):
    if 0 < port <= 65535:
        print(f"The port {port} is valid.")
        return port
    else:
        print(f"The port {port} is not valid.")

def mysql_connection(host: str, port: int, user: str, password: str):
    try:
        con = pymysql.connect(host=host,
                              user=user,
                              port=port,
                              password=password,
                              database="")
        cur = con.cursor()
        cur.execute('SELECT VERSION()')
        version = cur.fetchone()
        print("Connected successfully!")
        print(f'Database version: {version[0]}')
        con.close()
        return
    except:
        print("Connection Failed!")
        return

def execute_command(host: str, port: int, user: str, password: str, cmd: str, db: str):
    try:
        con = pymysql.connect(host=host,
                              user=user,
                              port=port,
                              password=password,
                              database=db)
        cur = con.cursor()
        cur.execute(str(cmd))
        rows = cur.fetchall()

        for row in rows:
            print(row)
        con.close()
        return
    except:
        print("Command Error.")
        return

def show_tables(host: str, port: int, user: str, password: str, db: str):
    try:
        con = pymysql.connect(host=host,
                              user=user,
                              port=port,
                              password=password,
                              database=db)
        cur = con.cursor()
        cur.execute("SHOW TABLES")
        rows = cur.fetchall()

        for row in rows:
            print(row)
        con.close()
        return
    except:
        print("Command Error.")
        return

def show_databases(host: str, port: int, user: str, password: str):
    try:
        con = pymysql.connect(host=host,
                              user=user,
                              port=port,
                              password=password,
                              database="")
        cur = con.cursor()
        cur.execute("SHOW DATABASES")
        rows = cur.fetchall()

        for row in rows:
            print(row)
        con.close()
        return
    except:
        print("Command Error.")
        return