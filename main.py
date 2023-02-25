from colorama import Fore, Back
from time import sleep
import os
import sys
import subprocess

os.system("mode 360")

startText1 = f"{Fore.GREEN }Server Connection..."

for char in startText1:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(0.1)

sleep(2)

os.system("mode 360")
os.system("clear")


menu = f"""
           _              _____           _       _   
     /\   | |            / ____|         (_)     | |  
    /  \  | | _____  __ | (___   ___ _ __ _ _ __ | |_ 
   / /\ \ | |/ _ \ \/ /  \___ \ / __| '__| | '_ \| __|
  / ____ \| |  __/>  <   ____) | (__| |  | | |_) | |_ 
 /_/    \_\_|\___/_/\_\ |_____/ \___|_|  |_| .__/ \__|
                                           | |        
                                           |_|        

                                                {Fore.RED + "Made By @DevElectus"}
                                                {Fore.YELLOW + "Version 1.0.2"}
"""

hackList = f"""
{Fore.YELLOW}[{Fore.WHITE}1{Fore.YELLOW}] {Fore.RED} Kayıtlı Wifi Şifresi Bulma
{Fore.YELLOW}[{Fore.WHITE}2{Fore.YELLOW}] {Fore.RED} İnstagram Kullanıcı İnfo Alma {Fore.YELLOW}[Devre Dışı]
"""

print(Fore.GREEN + menu)

alexText = f"{Fore.WHITE}[ {Fore.GREEN}Alex {Fore.WHITE}]"

password = input(alexText + " Key: ")

sleep(2)

if password == "a74s7b7nx8xz3":
    print(alexText + Fore.GREEN + " Key Başarılı")
    os.system("mode 360") or os.system("clear")

    print(menu)
    sleep(1.5)
    for char in hackList:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.1)

    secenek = input(alexText + "Hangi İşlem Yapılsın: ")

    if secenek == "1":
        while True:

            print(alexText + "Sistem analiz ediliyor")
            import time

            time.sleep(1)

            print(alexText + "Bulunan Wifiler: ")

            veri = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
            sistemler = [i.split(":")[1][1:-1] for i in veri if "All User Profile" in i]
            for i in sistemler:
                sonuç = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split(
            '\n')
                sonuç = [b.split(":")[1][1:-1] for b in sonuç if "Key Content" in b]
                try:
                    print(Fore.RED + " \\{:<30}| Şifre:  {:<}".format(i, sonuç[0]))
                except IndexError:
                    print(Fore.RED + " \\{:<30}| Şifre:  {:<}".format(i, ""))

            exe = int(input("\n \n \n1'e basarak yeniden sistemi analiz edebilirsiniz \n2'ye basarak çıkış yapabilirsiniz "))
            if (exe == 1):
                print("")
                import time

                time.sleep(1)


            elif (exe == 2):
                print("")
                import time

                time.sleep(1)
                break
                quit()

            else:
                print("Bir hata yaptınız lütfen tekrar deneyin")

        else:
            print(alexText + Fore.RED + " Key Yanlış")