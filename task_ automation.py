import os
import shutil
from datetime import datetime

print("=" * 60)
print("      ADVANCED FILE ORGANIZER AUTOMATION SYSTEM")
print("=" * 60)

folder_path = input("Enter Folder Path: ")

if not os.path.exists(folder_path):
    print("❌ Folder does not exist!")
    exit()

total_files = 0
moved_files = 0

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Programs": [".py", ".java", ".cpp"]
}

report = []

for file in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):

        total_files += 1
        moved = False

        for category, extensions in file_types.items():

            if any(file.lower().endswith(ext) for ext in extensions):

                destination_folder = os.path.join(
                    folder_path, category
                )

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                shutil.move(
                    file_path,
                    os.path.join(destination_folder, file)
                )

                moved_files += 1
                moved = True

                report.append(
                    f"{file} ---> {category}"
                )

                break

        if not moved:

            others_folder = os.path.join(
                folder_path, "Others"
            )

            if not os.path.exists(others_folder):
                os.makedirs(others_folder)

            shutil.move(
                file_path,
                os.path.join(others_folder, file)
            )

            moved_files += 1

            report.append(
                f"{file} ---> Others"
            )

report_file = os.path.join(
    folder_path,
    "automation_report.txt"
)

with open(report_file, "w") as f:

    f.write("FILE ORGANIZER REPORT\n")
    f.write("=" * 40 + "\n")
    f.write(
        "Generated On: "
        + str(datetime.now())
        + "\n\n"
    )

    for item in report:
        f.write(item + "\n")

    f.write("\n")
    f.write(
        f"Total Files Processed: {total_files}\n"
    )
    f.write(
        f"Total Files Moved: {moved_files}\n"
    )

print("\n✅ Automation Completed Successfully!")
print("📁 Files Organized Into Categories")
print("📄 Report Generated: automation_report.txt")
print(f"📊 Total Files Processed: {total_files}")
print(f"📦 Total Files Moved: {moved_files}")

print("=" * 60)
print("Thank You For Using File Organizer")
print("=" * 60)