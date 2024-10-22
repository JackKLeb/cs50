def main():
    file = input("File name: ").lower().strip().split(".")

    application = ["pdf", "zip"]
    image = ["png", "gif"]

    if file[-1] == "txt":
        print("text/plain")
    elif file[-1] in application:
        print(f"application/{file[-1]}")
    elif file[-1] in image:
        print(f"image/{file[-1]}")
    elif file[-1] == "jpeg" or file[-1] == "jpg":
        print("image/jpeg")
    else:
        print("application/octet-stream")







main()
