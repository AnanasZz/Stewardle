import pyxel as py, random

py.init(128,128,"STEWARDLE")
py.load("assets/f1.pyxres",True,True,False,False)
py.cls(0)
pilots,pilot,col,guess,guesses,gagne={"Leclerc":['LEC','3',['FE'],'16','25','17','5']},'',[[1 for i in range(7)] for j in range(5)],-1,[],False
mystery=random.choice(list(pilots.keys()))

def draw():
    py.text(48,2,"STEWARDLE",7)
    py.text(5,18,"DRI FLAG TEAM NUM AGE YEAR WINS",7)
    for i in range(7):
        for j in range(5):
            py.rect(i*17+6,j*17+25,15,15,col[j][i])
    for i in range(7):
        for j in range(5):
            py.rect(i*17+7,j*17+26,13,13,5)
    if pilot!='':
        for i in range(len(guesses)):
            py.text(7,26+17*i,f"{pilots[guesses[i]][0]}",7)
            py.blt(24,26+17*i,0,int(pilots[guesses[i]][1])*13+1,0,13,13)
            py.text(41,26+17*i,f"{pilots[guesses[i]][2][0]}   {pilots[guesses[i]][3]}  {pilots[guesses[i]][4]}  {pilots[guesses[i]][5]}  {pilots[guesses[i]][6]}",7)
        py.text(7,26+17*guess,f"{pilots[pilot][0]}",7)
        py.blt(24,26+17*guess,0,int(pilots[pilot][1])*13+1,0,13,13)
        py.text(41,26+17*guess,f"{pilots[pilot][2][0]}   {int(pilots[pilot][3])}  {int(pilots[pilot][4])}  {int(pilots[pilot][5])}  {int(pilots[pilot][6])}",7)
    if gagne==True:
        py.cls(0)
        for i in range(7):
            for j in range(1):
                py.rect(i*17+6,j*17+25,15,15,col[j][i])
        for i in range(7):
            for j in range(1):
                py.rect(i*17+7,j*17+26,13,13,5)
        py.text(7,26+17*guess,f"{pilots[pilot][0]}",7)
        py.blt(24,26+17*guess,0,int(pilots[pilot][1])*13+1,0,13,13)
        py.text(41,26+17*guess,f"{pilots[pilot][2][0]}   {int(pilots[pilot][3])}  {int(pilots[pilot][4])}  {int(pilots[pilot][5])}  {int(pilots[pilot][6])}",7)
        py.text(55,60,"GAGNE",7)

def update():
    global pilots,pilot,col,mystery,guess,guesses,gagne
    if py.btnr(py.KEY_L):
        pilot='Leclerc'
        guesses.append(pilot)
        guess+=1
    if pilot!='':
        for i in range(len(pilots[pilot])):
            if pilots[pilot][i]==pilots[mystery][i] and i==0:
                col[guess]=[11 for j in range(7)]
            elif pilots[pilot][i]<pilots[mystery][i] and i!=0 and i!=2:
                col[guess][i]=10
            elif pilots[pilot][i]>pilots[mystery][i] and i!=0 and i!=2:
                col[guess][i]=14
            elif pilots[pilot][i]==pilots[mystery][i] and i!=0 and i!=2:
                col[guess][i]=11
            elif pilots[pilot][i][0]==pilots[mystery][i][0]:
                col[guess][i]=11
            else:
                col[guess][i]=8
    if found(col):
        gagne=True

def found(col):
    for i in col[guess]:
        if i!=11:
            return False
    return True

py.run(update,draw)
