import os
import shutil

# File categories based on extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".sh", ".bat", ".apk"],
    "Others": []  # Unrecognized files go here
}

def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory does not exist!")
        return

    # Create category folders if they don't exist
    for category in FILE_CATEGORIES.keys():
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

    # Iterate through files in the directory
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Identify file extension
        _, file_ext = os.path.splitext(file)

        # Find category
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_ext.lower() in extensions:
                shutil.move(file_path, os.path.join(directory, category, file))
                moved = True
                break

        # If no category found, move to "Others"
        if not moved:
            shutil.move(file_path, os.path.join(directory, "Others", file))

    print("✅ File organization complete!")


organize_files(r"C:\Users\YourUsername\Downloads")