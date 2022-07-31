# implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends,
# case-insensitively, in any of these suffixes:
#  .gif
#  .jpg
#  .jpeg
#  .png
#  .pdf
#  .txt
#  .zip

fname = input("whats the file name?   ").casefold().strip()

if fname.endswith("gif"):
    print("image/gif")
elif fname.endswith("jpg") or fname.endswith("jpeg"):
    print("image/jpeg")
elif fname.endswith("png"):
    print("image/png")
elif fname.endswith("pdf"):
    print("application/pdf")
elif fname.endswith("txt"):
    print("text/plain")
elif fname.endswith("zip"):
    print("application/zip")
else:
    print("application/octet-stream")
