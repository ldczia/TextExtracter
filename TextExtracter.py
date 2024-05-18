with open("cookies.txt", "r") as f: #If you want extract different file, change the name of 'cookies.txt'
    lines = f.readlines()

#Example
file_lines = [line.strip() for line in lines if line.strip().startswith("instagram")] #its extracts all instagram lines

with open("output.txt", "w") as f: #saves in new text file
    f.write("\n".join(file_lines))
