from datetime import datetime
from colorama import Fore
import threading


lock = threading.Lock()
class Logger:
    def Success(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock.acquire()
        print(Fore.BLUE + "["+ Fore.WHITE + current_time + Fore.LIGHTCYAN_EX + "] [\] " + Fore.WHITE + text + Fore.RESET)
        lock.release()
    
    def Error(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock.acquire()
        print(Fore.RED + "["+ Fore.WHITE + current_time + Fore.LIGHTRED_EX + "] [-] " + Fore.WHITE + text + Fore.RESET)
        lock.release()

    def Info(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock.acquire()
        print(Fore.YELLOW + "["+ Fore.WHITE + current_time + Fore.LIGHTYELLOW_EX + "] [!] " + Fore.WHITE + text + Fore.RESET)
        lock.release()


# Logger.Success("Example Success")
# Logger.Error("Example Error")
# Logger.Info("Example Info")