import zipfile
import sys
import os
import shutil 

def extract_zip(zip_file, source_directory):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    with zipfile.ZipFile(os.path.join(source_directory, zip_file), 'r') as zip_ref:
        zip_ref.extractall(script_directory)

def edit_main_activity(dir_main_activity, default_model, new_model):
    with open(dir_main_activity, 'r') as file:
        main_activity = file.read()

    modified_main_activity = main_activity.replace(default_model, f'{new_model}')

    with open(dir_main_activity, 'w') as file:
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

        if(sys.argv[1]=="image_segmentation"):
            shutil.copy(sys.argv[2], "./ImageSegmentation/app/src/main/assets")
            model_file_name = os.path.basename(sys.argv[2])
            edit_main_activity('./ImageSegmentation/app/src/main/java/org/pytorch/imagesegmentation/MainActivity.java',
                   'deeplabv3_scripted_optimized.ptl', model_file_name)
        
        elif(sys.argv[1]=="speech_recognition"):
            shutil.copy(sys.argv[2], "./SpeechRecognition/app/src/main/assets")
            model_file_name = os.path.basename(sys.argv[2])
            edit_main_activity('./SpeechRecognition/app/src/main/java/org/pytorch/demo/speechrecognition/MainActivity.java',
                               'wav2vec2.ptl', model_file_name)
            
        elif(sys.argv[1]=="object_detection"):
            shutil.copy(sys.argv[2], "./ObjectDetection/app/src/main/assets")
            model_file_name = os.path.basename(sys.argv[2])
            edit_main_activity('./ObjectDetection/app/src/main/java/org/pytorch/demo/objectdetection/MainActivity.java',
                               'yolov5s.torchscript.ptl', model_file_name)

        elif(sys.argv[1]=="question_answering"):
            shutil.copy(sys.argv[2], "./QuestionAnswering/app/src/main/assets")
            model_file_name = os.path.basename(sys.argv[2])
            edit_main_activity('./QuestionAnswering/app/src/main/java/org/pytorch/demo/questionanswering/MainActivity.kt',
                               'qa360_quantized.ptl', model_file_name)
            
        else:
            print(f'No boilerplate available for project ${sys.argv[1]}')
