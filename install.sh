echo Установка...
echo -------------------------------------------------------------------
apt update && apt upgrade && apt install lolcat && pip3 install requests colorama
clear
echo '▄▄▄█████▓▓█████  ██▀███   ███▄ ▄███▓ █    ██ ▒██   ██▒
▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▓██▒▀█▀ ██▒ ██  ▓██▒▒▒ █ █ ▒░
▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒▓██    ▓██░▓██  ▒██░░░  █   ░
░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  ▒██    ▒██ ▓▓█  ░██░ ░ █ █ ▒
  ▒██▒ ░ ░▒████▒░██▓ ▒██▒▒██▒   ░██▒▒▒█████▓ ▒██▒ ▒██▒
  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░   ░  ░░▒▓▒ ▒ ▒ ▒▒ ░ ░▓ ░
    ░     ░ ░  ░  ░▒ ░ ▒░░  ░      ░░░▒░ ░ ░ ░░   ░▒ ░
  ░         ░     ░░   ░ ░      ░    ░░░ ░ ░  ░    ░
            ░  ░   ░            ░      ░      ░    ░

 ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███
▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒
▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄
░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒
░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
 ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░
 ░          ░ ░         ░    ░         ░  ░   ░
      ░                           ░' | lolcat
echo Добро пожаловать в KBomb!
echo В следущий раз для запуска KBomb пишите: python3 bomber.py. Нажмите Enter чтобы продолжить...
read k
chmod +x KBomb.py
python3 KBomb.py
rm install.sh
