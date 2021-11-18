def bissextile (annee) : 
    if (annee % 100 != 0 and annee % 4 == 0) or annee % 400 == 0 : 
        return True 
    else : 
        return False 

def nbr_jours (mois,annee) : 
    if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois ==12 : 
       return 31 
    elif mois == 4 or mois == 6 or mois == 9 or mois == 11 : 
        return 30 
    elif mois == 2 and bissextile(annee) : 
        return 29 
    elif mois == 2 and not bissextile(annee) : 
        return 28 
    
def date_validity (jours,mois,annee) : 
    j = 0 
    m = 0 
    if jours > 0 and jours <= nbr_jours(mois,annee) :
       j = 1 
    if mois > 0 and mois <= 12 : 
      m = 1 
    if j == 1 and m ==1  :
        return True 
    else :
        return False 

def test_date () : 
    print ('Jour : ') 
    j = input()
    jour = int(j)
    print ('Mois : ')
    m = input()
    mois = int(m) 
    print ('Annee : ')
    an = input()  
    annee = int(an)
    a = date_validity (jour,mois,annee) 
    if a : 
        print ('date valide') 
    else : 
        print ('date non valide')
