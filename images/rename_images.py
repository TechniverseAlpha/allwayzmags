import os
import re

# Path to your images folder
base_dir = r"C:\Clients\MagsNCo\ETL\images"

# Regex pattern to capture the design name
pattern = re.compile(r"Page\d+__([A-Za-z0-9_]+)__Page\d+\.jpg", re.IGNORECASE)

count = 0
for filename in os.listdir(base_dir):
    if not filename.lower().endswith(".jpg"):
        continue

    match = pattern.match(filename)
    if match:
        design_name = match.group(1).upper()  # e.g., BULL_ELK_2
        new_name = f"{design_name}.jpg"
        old_path = os.path.join(base_dir, filename)
        new_path = os.path.join(base_dir, new_name)

        # Handle duplicates
        if os.path.exists(new_path):
            print(f"⚠️ Skipping (already exists): {new_name}")
            continue

        os.rename(old_path, new_path)
        print(f"✅ Renamed: {filename} → {new_name}")
        count += 1
    else:
        print(f"❌ No match: {filename}")

print(f"\nDone. {count} files renamed successfully.")
