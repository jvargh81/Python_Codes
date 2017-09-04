import os


def change_name() :
    file_list = os.listdir("/home/jerrin/Downloads/prank")
    #print(file_list)
    save_path = os.getcwd()
    os.chdir("/home/jerrin/Downloads/prank")
    for file_name in file_list :
        os.rename(file_name,file_name.strip("0123456789"))

#file_list = os.listdir("/home/jerrin/Downloads/prank")
#print(file_list)
    os.chdir(save_path)
change_name()







































