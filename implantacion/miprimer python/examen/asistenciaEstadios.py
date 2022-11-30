asistenciaSemanal = 0
publicoNeutralSuma = 0
asistenciaNeutralSemanal = 0

for i in range(7):
    print("dia",i+1)

    asistenciaTotalDiaria=0
    asistenciaNeutralDiaria=0

    for j in range(4):
        publicoLocal = int(input("Cuanto publico local habia en el partido"+str(j)+"? "))
        publicoVisitante = int(input("Cuanto publico visitante habia en el partido"+str(j)+"? "))
        publicoNeutral = int(input("Cuanto publico neutral habia en el partido"+str(j)+"? "))
        
        asistenciaTotalDiaria += publicoLocal + publicoVisitante + publicoNeutral
        asistenciaSemanal += asistenciaTotalDiaria
        asistenciaNeutralSemanal += publicoNeutral
        asistenciaNeutralDiaria += publicoNeutral

    print("La asistencia total diaria es: ",asistenciaTotalDiaria, "personas")
    print("La asistencia media neutral diaria es: ",asistenciaNeutralDiaria/4, "personas")
    
    publicoNeutralDia = (publicoNeutralSuma / 4) // 1
    print("La media es de:",publicoNeutralDia, "personas neutrales")



print("La asistencia total neutral es de: ",asistenciaNeutralSemanal, "personas y la asistencia total es de: ",asistenciaSemanal, "personas")