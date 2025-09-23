from datetime import datetime
import re
import os

def safe_filename(title: str) -> str:
    title = title.strip().lower()
    title = title.replace(" ", "_").replace("/", "-")
    title = re.sub(r'[^a-z0-9_\-]', '', title)
    return title

now = datetime.now()
date_str = now.strftime("%Y-%m-%d %H-%M")
year_str = now.strftime("%Y")
time_str = now.strftime("%H:%M")

entry_title = input("Entry title: ")
safe_title = safe_filename(entry_title)

if not os.path.exists(year_str):
    os.makedirs(year_str)

filename = f"{date_str}_{safe_title}.md" if safe_filename else f"{date_str}.md"
file_path = os.path.join(year_str, filename)

with open(file_path, 'w') as file:
    file.write(f"# {entry_title}\n\n")
    file.write(f"*Date:* {now.strftime('%Y-%m-%d')}\n\n")
    file.write(f"*Time:* {time_str}\n\n")
    file.write("---\n\n")
    file.write("Thoughts...\n")

print(f"Created journal entry: {file_path}")