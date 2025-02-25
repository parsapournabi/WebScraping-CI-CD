from datetime import datetime

with open("README.md", "w") as file:
    file.write(f"{datetime.now().strftime('%d %B, %Y, %H:%M')}")
    file.close()
