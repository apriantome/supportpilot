# === Stage 44: Add backup creation for the data file ===
# Project: SupportPilot
def create_backup(data_path, backup_dir=".backups"):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    backup_file = f"{data_path}.bak_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(data_path, backup_file)
    print(f"Backup created: {backup_file}")
