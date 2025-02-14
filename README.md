# File Management Utilities

## Overview
This repository contains two Python scripts designed to automate file management tasks:

1. **PDFDecrypter.py** – A script to decrypt password-protected PDF files.
2. **filesorter.py** – A script to automatically organize files into categorized folders based on their extensions.

---

## 1️⃣ PDF Decrypter

### Description
This script decrypts a password-protected PDF file and saves an unprotected version while removing the original encrypted file.

### Dependencies
- `PyPDF2`
- `os`

### Usage
1. Modify the `pdf_name` variable in `PDFDecrypter.py` to point to your encrypted PDF file.
2. Set the correct password in `reader.decrypt("password")`.
3. Run the script.

### Code Flow
- The script checks if the PDF file exists.
- It decrypts the file using `PyPDF2`.
- A new unprotected PDF is created and saved.
- The original encrypted file is deleted.

---

## 2️⃣ File Sorter

### Description
This script organizes files into predefined categories based on their extensions. It helps keep your directories clean and well-structured.

### Dependencies
- `os`
- `shutil`

### Usage
1. Modify the `directory` path in `organize_files(r"C:\Users\YourUsername\Downloads")` to the folder you want to organize.
2. Run the script.

### Code Flow
- The script checks if the directory exists.
- It creates categorized folders (e.g., Images, Documents, Videos, etc.).
- It moves files to their respective categories based on their extensions.
- Unrecognized file types are moved to an "Others" folder.
- A confirmation message is printed after completion.

---

## 💡 Notes
- Ensure the required dependencies are installed using:
  ```sh
  pip install PyPDF2
  ```
- Run these scripts carefully, as they modify files and directories.
- For custom extensions, modify the `FILE_CATEGORIES` dictionary in `filesorter.py`.

---

## 📜 License
This project is open-source. Feel free to modify and use it as needed!

---

## 📧 Contact
For questions or improvements, feel free to contribute or reach out!

---
