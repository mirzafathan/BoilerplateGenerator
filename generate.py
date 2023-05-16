import zipfile
import sys
import os
import shutil 

def extract_zip(zip_file, source_directory):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    with zipfile.ZipFile(os.path.join(source_directory, zip_file), 'r') as zip_ref:
        zip_ref.extractall(script_directory)

def edit_pytorch_model_image_segmentation(model_name):
    with open('./ImageSegmentation/app/src/main/java/org/pytorch/imagesegmentation/MainActivity.java', 'r') as file:
        java_code = file.read()

    new_line = f'LiteModuleLoader.load(MainActivity.assetFilePath(getApplicationContext(), "{model_name}"));'

    modified_java_code = java_code.replace('LiteModuleLoader.load(MainActivity.assetFilePath(getApplicationContext(), "deeplabv3_scripted_optimized.ptl"));', new_line)

    with open('./ImageSegmentation/app/src/main/java/org/pytorch/imagesegmentation/MainActivity.java', 'w') as file:
        file.write(modified_java_code)


def edit_pytorch_model_speech_recognition(model_name):
    with open('./SpeechRecognition/app/src/main/java/org/pytorch/demo/speechrecognition/MainActivity.java', 'r') as file:
        java_code = file.read()

    new_line = f'LiteModuleLoader.load(assetFilePath(getApplicationContext(), "{model_name}"));'

    modified_java_code = java_code.replace('LiteModuleLoader.load(assetFilePath(getApplicationContext(), "wav2vec2.ptl"));', new_line)

    with open('./SpeechRecognition/app/src/main/java/org/pytorch/demo/speechrecognition/MainActivity.java', 'w') as file:
        file.write(modified_java_code)


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

        if(sys.argv[1]=="image_segmentation"):
            shutil.copy(sys.argv[2], "./ImageSegmentation/app/src/main/assets")
            model_file_name = os.path.basename(sys.argv[2])
            edit_pytorch_model_image_segmentation(model_file_name)
            print(f"Pytorch model for ImageSegmentation has been inserted to the project asset")
        
        elif(sys.argv[1]=="speech_recognition"):
            shutil.copy(sys.argv[2], "./SpeechRecognition/app/src/main/assets")
            model_file_name = os.path.basename(sys.argv[2])
            edit_pytorch_model_speech_recognition(model_file_name)
            print(f"Pytorch model for SpeechRecognition has been inserted to the project asset")


