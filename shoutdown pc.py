import os
shutdown = input("Shoutdown your pc?(yes or no): ")
if shutdown == 'no':
    exit()
else:
    os.system("shutdown /s /t 1")

