import markdown
import os

def main():
    path = "index.md"
    is_default_path: str = input("Default path .md file ("+path+") Y/N: ")
    if is_default_path.upper() == "N":
        while True:
            path = input("Path to .md file: ")
            if os.path.exists(path): break
            else: print("Uncorrect path")
    
    with open(path, "r") as file:
        lines = file.readlines()
        md = ''.join(lines)
        html = markdown.markdown(md)

    with open(path.split(".")[0]+".html", "w") as html_file:
        html_file.write(html)

if __name__  == "__main__":
    main()