import os
import json
 
JSON_FILE_PATH = '.'
COMPILE_FOLDER_PATH = 'combined/'
COMPILE_FILE_PATH = COMPILE_FOLDER_PATH+'combined.json'

if not os.path.exists(COMPILE_FOLDER_PATH):
   os.makedirs(COMPILE_FOLDER_PATH)

with open(COMPILE_FILE_PATH, 'w', encoding='utf-8') as output:
    output.write("[")

for input in os.listdir(JSON_FILE_PATH):
    f = os.path.join(JSON_FILE_PATH, input)
    if os.path.isfile(f):
        with open(f) as data:
            try: 
                data = json.load(data)
                with open(COMPILE_FILE_PATH, 'a', encoding='utf-8') as output:
                    json.dump(data, output, ensure_ascii=False, indent=4)
                    output.write(",")
                    print("Written " + str(input))
            except Exception:
                None

with open(COMPILE_FILE_PATH, 'rb+') as output:
    output.seek(-1, os.SEEK_END)
    output.truncate()
with open(COMPILE_FILE_PATH, 'a', encoding='utf-8') as output:
    output.write("]")
    
print("Finished writing")
 