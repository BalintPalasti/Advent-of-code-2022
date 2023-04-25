def decide_what_to_do(information):
    global current_folder
    global folder_dictionary
    if information[0] == "$":                   
        if information[1] == "cd":              #change directory command
            if information [2] == "..":         #cd one level up
                current_folder = go_up_in_folder_tree(current_folder)
            else:                               #cd "this"
                if information[2] !='/':                #this if is necessary beacause of the 1st line of the .txt
                    current_folder = current_folder + information [2] + '/'
    else:
        if information[0] == "dir":
            folder_dictionary[current_folder + information[1] + '/'] = 0
        else:
            add_file_size_to_folders(int(information[0]))

def go_up_in_folder_tree(folder_path):
    folder_path = folder_path[:-1]      #removes the last "/"
    for i in reversed(folder_path):
        if i == '/':
            break
        folder_path = folder_path[:-1]
    return folder_path

def add_file_size_to_folders(file_size):
    current_folder_temp = current_folder
    folder_dictionary[current_folder_temp] += file_size     #add size to current path
    while current_folder_temp != '/':
        current_folder_temp = go_up_in_folder_tree(current_folder_temp)
        folder_dictionary[current_folder_temp] += file_size

folder_dictionary = {"/": 0}
current_folder = "/"

with open("07.txt") as f:
    for line in f:
        line_element = line.split()
        decide_what_to_do(line_element)

sum_size = 0

for i in folder_dictionary:
    if folder_dictionary[i] <= 100000:
        sum_size += folder_dictionary[i]

print("Overall:", sum_size)