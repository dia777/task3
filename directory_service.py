import os
import shutil

class directory_service:

    def __init__(self):
        pass

    def create_folder(self, parent_directory, folder_name):
        path = os.path.join(parent_directory, folder_name)
        os.mkdir(path)
     
    def read_csv (self, parent_directory, path_csv):
        counter = 0
        with open(path_csv, 'r') as f:
            for line in f:
                if counter==0:
                    counter = counter +1
                    continue
                line = line.rstrip()
                text =line.split(',')
                folder_name = text[0]
                self.create_folder(parent_directory, folder_name)
                counter = counter +1

    def recursive(self):
        path = "D:/task3/task3/data"
        dir_list = os.listdir(path)
        for dir in dir_list:
            full_path = os.path.join(path, dir)
            if full_path.endswith('.pdf'):
                target_path = os.path.join('D:/task3/task3/result/Tutorials', dir)
                self.copy_file(full_path, target_path)
       
            if full_path.lower().endswith('game'):
                if full_path.lower().endswith('.game'):
                    target_path = os.path.join('D:/task3/task3/result/Games', dir)
                    self.copy_file(full_path, target_path)
                else:
                    sub_directory = os.listdir(full_path)
                    target_path = os.path.join('D:/task3/task3/result/Games', dir)
                    os.mkdir(target_path)
                    for sub_dir in sub_directory:
                        sub_full_path = os.path.join(full_path, sub_dir)
                        sub_target_path = os.path.join(target_path, sub_dir)
                        self.copy_file(sub_full_path, sub_target_path)
                    #shutil.copytree(full_path, 'D:/task3/task3/result/Games' )
                    
                    
    def copy_file(self, origin, target_folder):
        shutil.copyfile(origin, target_folder)
        
        

               
        

    

    