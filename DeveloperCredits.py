#FUNCION IMPRIMIR CREDITOS AL PROGRAMADOR
def printCodeMaster():

    #PROJECT-DATA
    proyectName = "WORD-DATA-ENTRY-FORM"
    developer = "MAURO PEPA"
    proyectVersion = "0.5"

    developerCretis = "\n"+proyectName+ " - BY "+developer+" - V"+proyectVersion
    print(developerCretis)

    LongNumberStick = "-"*len(developerCretis)
    print(LongNumberStick)

if __name__ == '__main__':
    printCodeMaster()