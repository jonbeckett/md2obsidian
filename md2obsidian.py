import os
import sys
import os.path

if (len(sys.argv)!=3):
    print("\nmd2obsidian.py - Exports markdown files in wp2md format into an Obsidian file structure and format.\n\nExample : python wp2obsidian.py c:\\my\\md2wp\\files ../../obsidianvault/Areas/Writing/Blog\n\n")
    sys.exit(0)

input_path = sys.argv[1]
output_path = sys.argv[2]

print("Input Path : " + input_path)
print("Output Path : " + output_path)

if not os.path.isdir(input_path):
    print("The input path (" + input_path +") does not exist")
    sys.exit(0)

if not os.path.isdir(output_path):
    print("The output path (" + output_path +") does not exist")
    sys.exit(0)

for subdir, dirs, files in os.walk(input_path):
    for file in files:
        if '.md' in file and 'README.md' not in file:
        
            print("Processing " + file)

            # does a year subfolder exist? Create it if not
            year_folder = file[0:4]
            if not os.path.isdir(os.path.join(output_path,year_folder)):
                os.mkdir(os.path.join(output_path,year_folder))

            # does a month subfolder exist? Create it if not
            month_folder = file[0:7]
            if not os.path.isdir(os.path.join(output_path,year_folder,month_folder)):
                os.mkdir(os.path.join(output_path,year_folder,month_folder))
            
            # read the input file
            input_file_path = os.path.join(subdir, file)
            input_file = open(input_file_path,'r',encoding="latin-1")
            input_text = input_file.readlines()
            input_file.close()

            # get the body trim the first 4 lines (contain the title)
            output_text = "".join(input_text[4:])
            
            output_file_path = os.path.join(output_path,year_folder,month_folder,file)
            output_file = open(output_file_path, 'wb')
            output_file.write(bytes(output_text,'utf-8'))
            output_file.close()
