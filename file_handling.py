with open('ruchipic.jpg','rb') as file1:
    data=file1.read()
    print("image copied")
with open('copied_ruchipic.jpg','wb') as file1:
    file1.write(data)
    print("copy created")
