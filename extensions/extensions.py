file = input("File name: ")
if "." not in file:
    print("application/octet-stream")
else:
    file_split = file.split(".")
    file = file_split[-1]
    extension = file.strip().lower()
    if extension == "jpeg" or extension == "jpg":
        print(f"image/jpeg")
    elif extension == "gif" or extension == "png":
        print(f"image/{extension}")
    elif extension == "pdf" or extension == "zip":
        print(f"application/{extension}")
    elif extension == "txt":
        print("text/plain")
    elif extension == "txt":
        print("text/plain")
    else:
        print("application/octet-stream")
