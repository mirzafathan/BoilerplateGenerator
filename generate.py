import zipfile
import sys
import os
import shutil 

def extract_zip(zip_file, source_directory):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    with zipfile.ZipFile(os.path.join(source_directory, zip_file), 'r') as zip_ref:
        zip_ref.extractall(script_directory)

def edit_main_activity(project_name, default_model, new_model):
    lower_case = project_name.lower()
    main_activity_dir = f'./{project_name}/app/src/main/java/org/pytorch/demo/{lower_case}/MainActivity.java'
    if(not os.path.exists(main_activity_dir)):
        main_activity_dir = main_activity_dir[:-4] + "kt"
    with open(main_activity_dir, 'r') as file:
        main_activity = file.read()

    modified_main_activity = main_activity.replace(default_model, f'{new_model}')

    with open(main_activity_dir, 'w') as file:
        file.write(modified_main_activity)

if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[1] == '-h':
        print("Usage: python generate.py [boilerplate project] [pytorch model directory]")
        print("Available options:")
        folder_path = "./BoilerplateCompressed"  
        zip_files = [f for f in os.listdir(folder_path) if f.endswith('.zip')]
        for zip_file in zip_files:
            print("- " + zip_file[:-4])
    else:
        compressed_files_directory = "./BoilerplateCompressed" 
        zip_file = sys.argv[1] + ".zip"
        extract_zip(zip_file, compressed_files_directory)
        print(f"Boilerplate for {sys.argv[1]} has been generated!")
        model_file_name = os.path.basename(sys.argv[2])
        shutil.copy(sys.argv[2], f"./{sys.argv[1]}/app/src/main/assets")
        edit_main_activity(sys.argv[1], 'model_name', model_file_name)