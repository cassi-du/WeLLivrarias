import os
from pathlib import Path

def limpar_backups(backups_dir):
    backups = [f for f in os.listdir(backups_dir) if f.endswith('.db')]
    backups.sort(key=lambda x: os.path.getmtime(os.path.join(backups_dir, x)), reverse=True)

    if len(backups) > 5:
        for backup in backups[5:]:
            os.remove(os.path.join(backups_dir, backup))
            print(f"Backup removido: {backup}")
