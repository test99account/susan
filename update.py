import os, shutil
wait = input("Press enter to confirm update")
changeLogTrue = True
changeLogWriteTrue = True
version = open("version", "a")
version.write("1")
version.close()
statinfo = os.stat("version")
print("NEW BUILD NUMBER", statinfo.st_size)
changeLogFile = open("changeLog", "a")
print("Type 'exit' once you have finished entering changes")
buildNumber = str(["Build: ", statinfo.st_size, ]).strip("[']")
changeLogFile.write(buildNumber + "\n")
while changeLogTrue == True:
    changeLog = input("Add: ")
    if changeLog == "exit":
        changeLogTrue = False
        changeLogWriteTrue = False
    if changeLogWriteTrue == True:
        changeLogFile.write(changeLog + "\n")
changeLogFile.close()
exit()
