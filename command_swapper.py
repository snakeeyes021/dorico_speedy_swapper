import os
import shutil

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Read configuration
config_path = os.path.join(current_dir, "config.txt")
config = {}
with open(config_path, 'r') as config_file:
    for line in config_file:
        name, value = line.strip().split('=')
        config[name] = value

# Construct paths based on configuration
user_folder = config['user_folder']
dorico_version = config['dorico_version']
keycommands_file1 = rf"C:\Users\{user_folder}\AppData\Roaming\Steinberg\Dorico {dorico_version}\keycommands_en.json"
keycommands_file2 = rf"C:\Users\{user_folder}\AppData\Roaming\Steinberg\Dorico {dorico_version}\keycommands_en.json.bak"
preferences_file1 = rf"C:\Users\{user_folder}\AppData\Roaming\Steinberg\Dorico {dorico_version}\preferences.xml"
preferences_file2 = rf"C:\Users\{user_folder}\AppData\Roaming\Steinberg\Dorico {dorico_version}\preferences.xml.bak"

# Define backup paths in the script directory
backup_keycommands_primary = os.path.join(current_dir, "keycommands_en.json")
backup_preferences_primary = os.path.join(current_dir, "preferences.xml")
backup_keycommands_secondary = os.path.join(current_dir, "keycommands_en.json.bak")
backup_preferences_secondary = os.path.join(current_dir, "preferences.xml.bak")

# Check if the swapper files already exist; if not, it's first run, so create them AND create an additional long-term backup in the script directory
if not os.path.exists(keycommands_file2):
    shutil.copy(keycommands_file1, keycommands_file2)
    shutil.copy(keycommands_file1, backup_keycommands_primary)

if not os.path.exists(preferences_file2):
    shutil.copy(preferences_file1, preferences_file2)
    shutil.copy(preferences_file1, backup_preferences_primary)

# Check for secondary backup files if primary backups exist
if os.path.exists(backup_keycommands_primary) and not os.path.exists(backup_keycommands_secondary):
    shutil.copy(keycommands_file2, backup_keycommands_secondary)

if os.path.exists(backup_preferences_primary) and not os.path.exists(backup_preferences_secondary):
    shutil.copy(preferences_file2, backup_preferences_secondary)

# Swap keycommands files
temp_file = keycommands_file1 + ".tmp"
os.rename(keycommands_file1, temp_file)
os.rename(keycommands_file2, keycommands_file1)
os.rename(temp_file, keycommands_file2)

# Swap preferences files
temp_file = preferences_file1 + ".tmp"
os.rename(preferences_file1, temp_file)
os.rename(preferences_file2, preferences_file1)
os.rename(temp_file, preferences_file2)

print("Files swapped successfully and backups created in the script directory.")
