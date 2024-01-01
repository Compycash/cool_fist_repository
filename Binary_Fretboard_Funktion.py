testton = "Ges"
testskala = "moll"
'''
def tonvorrat_values (tonart, skala):   #gibt die liste der erlaubten tönen in chromatischen Zahlenwerten relativ zum "C" aus
     
    #Funtkion nimmt eine Tonart und eine Skala auf und gibt relativ zum "C" in halbtönen die positiven zahlenwerte der erlaubten töne aus.
    
    tonarten_namensliste = ("C", "CIS", "D", "DIS", "E", "F", "FIS", "G", "GIS", "A", "AIS", "H") # die positionen der tonarten in dieser liste sollten den referirenden Werten entsprechen
    if skala.upper() == "DUR": #der gewählten Skala werden die erlaubten Tonwerte zugewiesen.
        general_skala_values = [0, 2, 4, 5, 7, 9, 11]
    elif skala.upper() == "MOLL":
        general_skala_values = [0, 2, 3, 5, 7, 8, 10]
    else:
        print("Skala existiert nicht!")
    
    tonarten_shift = tonarten_namensliste.index(tonart.upper())#suche nach dem Tonforrat in der gewählten tonart, sprich der shift im vergleich zu "C". ausgegeben wird die abgeänderte Liste skala_values
    
    actual_skala_values = [] #wertepool für die tatsächche tonart generiert mit den general_skala_values, die über die skala bstimmen.
    for _ in general_skala_values:
        new_ = _+tonarten_shift
        if new_ > 11:  #verhindert, dass im Wertevorrat werte größer als 11 vorkommen, da diese mittels Index nicht mehr aus der tonarten_namensliste herauslesbar wären. 
            new_ = new_ -12
        actual_skala_values.append(new_) 
    print(actual_skala_values)
    for _ in actual_skala_values:
        print(tonarten_namensliste[_]) #TEST!

'''
def tonvorrat_values (tonart, skala):   #gibt die liste der erlaubten tönen in chromatischen Zahlenwerten relativ zum "C" aus
    ''' 
    Funtkion nimmt eine Tonart und eine Skala auf und gibt relativ zum "C" in halbtönen die positiven zahlenwerte der erlaubten töne aus.
    '''

    tonarten_namensliste = ("C", "CIS", "D", "ES", "E", "F", "FIS/GES", "G", "AS", "A", "B", "H")  # die positionen der tonarten in dieser liste sollten den referirenden Werten entsprechen
    
    if skala.upper() == "DUR": #der gewählten Skala werden die erlaubten Tonwerte zugewiesen.
        general_skala_values = [0, 2, 4, 5, 7, 9, 11]
    elif skala.upper() == "MOLL":
        general_skala_values = [0, 2, 3, 5, 7, 8, 10]
    else:
        print("Skala existiert nicht!")

    if tonart.upper() == "FIS" or "GES":    #die bezeichnung Fis und Ges sind beide legitim.
        tonart = "FIS/GES"

    tonarten_shift = tonarten_namensliste.index(tonart.upper())#suche nach dem Tonforrat in der gewählten tonart, sprich der shift im vergleich zu "C". ausgegeben wird die abgeänderte Liste skala_values
    
    actual_skala_values = [] #wertepool für die tatsächche tonart generiert mit den general_skala_values, die über die skala bstimmen.
    for _ in general_skala_values:
        new_ = _+tonarten_shift
        if new_ > 11:  #verhindert, dass im Wertevorrat werte größer als 11 vorkommen, da diese mittels Index nicht mehr aus der tonarten_namensliste herauslesbar wären. 
            new_ = new_ - 12
        actual_skala_values.append(new_) 
    
    return actual_skala_values
    #for _ in actual_skala_values: #TEST
    #    print(tonarten_namensliste[_]) #TEST!

tonvorrat_values (testton, testskala)

test_saiten = [4, 9, 2, 7, 11, 4]
def fretboard_list (scale_values, saiten):

    fretboard_all_values = []  #liste die einfach nur die chromatischen werte jedes tons ralativ zum "C".
    fretboard_laenge = 12
    for _ in saiten:
        string = []
        for _2 in range(fretboard_laenge):
            string.append(_2+_)
        fretboard_all_values.append(string)
    print(fretboard_all_values)       



    
