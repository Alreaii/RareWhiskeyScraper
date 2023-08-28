import base64
import ast


whiskeyfile = open("C:\\Users\\Haven\\Downloads\\whiskeydata.js", "r") #input file
textfile = open("C:\\Users\\Haven\\Downloads\\whiskeydata.txt", "w") #output file

def atob(encoded_str):
    return base64.b64decode(encoded_str).decode('utf-8')

whiskey_names = ["Dalmore Index", "Karuizawa Index", "Rosebank OB Index"] #etc etc etc

for i in range(len(whiskey_names)):
    label = whiskey_names[i]
    for line in whiskeyfile:
        if label in line:
            label_line = next(whiskeyfile)
            label_line = label_line.replace("atob(", "")
            label_line = label_line.replace(")", "")
            label_line = label_line.replace(";", "")
            label_line = label_line.replace('data:', "")
            label_line = label_line[:-5]
            label_line = label_line + "]"
            break
    encoded_data = ast.literal_eval(label_line)

    decoded_data = [atob(encoded_str) for encoded_str in encoded_data]

    textfile.write(label + "\n")
    textfile.write(str(decoded_data))
    textfile.write("\n")
    textfile.write("\n")





