import os

print("🔄 Scanning all folders and child directories...")

# os.walk automatically goes inside every subfolder
for root, dirs, files in os.walk('.'):
    for filename in files:
        # 1. Skip this script itself
        if filename == 'rename_all.py':
            continue
            
        # 2. Check if the file name starts with a number and ends in .py
        # Using filename[0].isdigit() catches names like "1.py" and "1_1_intro.py"
        if filename.endswith('.py') and filename[0].isdigit():
            
            # Create the full file paths so Python knows exactly where they are
            old_filepath = os.path.join(root, filename)
            new_filepath = os.path.join(root, f"ch_{filename}")
            
            # Rename the file right where it sits inside its subfolder
            os.rename(old_filepath, new_filepath)
            print(f"✅ Renamed in {root}: {filename} ➔ ch_{filename}")

print("🎉 Finished renaming all files across all child directories!")
