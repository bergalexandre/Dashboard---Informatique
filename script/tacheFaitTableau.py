import shutil

shutil.copyfile("template/tableauDeTaches.tex", "tableauDeTaches.tex")

outputFile = []

with open('tableauDeTaches.tex', 'r', encoding='utf8') as tableauFile:
    Lines = tableauFile.readlines()

    # Strips the newline character
    for line in Lines:
        line = line.replace("tache1", "allo")
        line = line.replace("res1", "allo")
        line = line.replace("etat1", "allo")
        outputFile.append(line)
        print(outputFile[-1])

with open('tableauDeTaches.tex', 'w', encoding='utf8') as tableauFile:
    tableauFile.writelines(outputFile)