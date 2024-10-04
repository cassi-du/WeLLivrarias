import os
from pathlib import Path

#limpar backups, mantém apenas os 5 mais recentes
def limpar_backups(backup_dir):
    backups = sorted(backup_dir.glob("backup_livraria_*.db"), key=os.path.getmtime)
    if len(backups) > 5:
        for backup in backups[:-5]:
            os.remove(backup)
