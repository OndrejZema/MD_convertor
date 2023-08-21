import markdown
import os
import sys
def main(args):
    path = "index.md"
    if len(args) != 2:    
        is_default_path: str = input("Default path .md file ("+path+") Y/N: ")
        if is_default_path.upper() == "N":
            while True:
                path = input("Path to .md file: ")
                if os.path.exists(path): break
                else: print("Uncorrect path")
    else:
        path = args[1]
    with open(path, "r") as file:
        lines = file.readlines()
        md = ''.join(lines)
        html = markdown.markdown(md)

    with open(path.split(".")[0]+".html", "w") as html_file:
        html_file.write(html)

if __name__  == "__main__":
    main(sys.argv)