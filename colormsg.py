from colorama import Fore, Back , Style


def ErrorMsg(msg):
    temp = '['+ Back.RED + Fore.WHITE + 'ERROR' + Fore.RESET + Back.RESET +']\t    ' + msg
    return temp

def SuccessMsg(masg):
    temp = '['+ Back.GREEN + Fore.BLACK + 'SUCCESS' + Fore.RESET + Back.RESET +']   ' + msg
    return temp

def InfoMsg(msg):
    temp = '[' + Back.BLUE + Fore.WHITE + 'INFO' + Fore.RESET + Back.RESET +']\t    ' + msg
    return temp

def WarnningMsg(msg):
    temp = '['+ Back.YELLOW + Fore.BLACK + 'WARRNING!' + Fore.RESET + Back.RESET +'] ' + msg
    return temp

def UniqueMsg(msg):
    temp = '[' + Back.CYAN + Fore.WHITE + '???????' + Fore.RESET + Back.RESET +']   ' + msg
    return temp

msg = "test message to check output"

