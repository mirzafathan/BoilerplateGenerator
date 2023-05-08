import zipfile
import sys
import os

def extract_zip(zip_file, source_directory):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    with zipfile.ZipFile(os.path.join(source_directory, zip_file), 'r') as zip_ref:
        zip_ref.extractall(script_directory)

if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] == '-h':
        print("Usage: python extract_zip.py [zip_file1.zip] [zip_file2.zip] ...")
        print("Available options:")
        folder_path = "./BoilerplateCompressed"  # Replace with the folder path where your zip files are located
        zip_files = [f for f in os.listdir(folder_path) if f.endswith('.zip')]
        for zip_file in zip_files:
            print("- " + zip_file)
    else:
        compressed_files_directory = "./BoilerplateCompressed"  # Replace with the directory where the compressed files are located
        for zip_file in sys.argv[1:]:
            extract_zip(zip_file, compressed_files_directory)
            print(f"Extraction of {zip_file} complete!")

