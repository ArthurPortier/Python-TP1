def mes_impots(revenu) : 
    impots = 0 
    if revenu < 10095 :
        impots = 0 
    elif revenu < 25710 and revenu > 10095 : 
        impots = (revenu - 10095) * 11/100 
    elif revenu < 73516 and revenu > 25710 : 
        impots = ((revenu - 25710) * 30/100) + ((25710 - 10095) * 11/100)
    elif revenu < 158122 and revenu > 73517 : 
        impots = ((revenu - 73517) * 41/100) + ((73516 - 25710) * 20/100) + ((25710 - 10095) * 11/100)
    elif revenu > 158123 : 
        impots = ((revenu - 158123) * 45/100) + ((158123 - 73517) * 41/100) + ((73516 - 25710) * 20/100) + ((25710 - 10095) * 11/100)
    return impots 
