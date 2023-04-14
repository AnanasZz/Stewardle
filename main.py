import pyxel as py, random
from database import pilots

py.init(128,128,"STEWARDLE")
py.load("assets/f1.pyxres",True,True,False,False)
py.cls(0)
pilot,col,guess,guesses,gagne='',[[1 for i in range(7)] for j in range(5)],-1,[],False
mystery=random.choice(list(pilots.keys()))
print('''Yellow -> Mystery pilot's corresponding number is strictly higher.
Salmon -> Mystery pilot's corresponding number is strictly lower.
Green -> The mystery pilot has the same thing.
Red -> The mystery pilot does not have the same thing.''')

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
            py.blt(24,26+17*i,0,int(pilots[guesses[i]][1])*13,0,13,13)
            py.text(41,26+17*i,f"{pilots[guesses[i]][2][0]}   {pilots[guesses[i]][3]}  {pilots[guesses[i]][4]}  {pilots[guesses[i]][5]}  {pilots[guesses[i]][6]}",7)
        py.text(7,26+17*guess,f"{pilots[pilot][0]}",7)
        py.blt(24,26+17*guess,0,int(pilots[pilot][1])*13,0,13,13)
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
        py.blt(24,26+17*guess,0,int(pilots[pilot][1])*13,0,13,13)
        py.text(41,26+17*guess,f"{pilots[pilot][2][0]}   {int(pilots[pilot][3])}  {int(pilots[pilot][4])} {int(pilots[pilot][5])}  {int(pilots[pilot][6])}",7)
        py.text(50,60,"WINNER !",7)
    if gagne=='LOST':
        py.cls(0)
        py.text(40,60,f"LOSER !\nIt was {mystery} !",7)

def update():
    global pilots,pilot,col,mystery,guess,guesses,gagne
    if py.btnr(py.KEY_L) and py.btn(py.KEY_E) and py.btn(py.KEY_C):
        pilot='Leclerc'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_V) and py.btn(py.KEY_E) and py.btn(py.KEY_R):
        pilot='Verstappen'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_P) and py.btn(py.KEY_E) and py.btn(py.KEY_R):
        pilot='Perez'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_A) and py.btn(py.KEY_L) and py.btn(py.KEY_O):
        pilot='Alonso'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_H) and py.btn(py.KEY_A) and py.btn(py.KEY_M):
        pilot='Hamilton'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_S) and py.btn(py.KEY_A) and py.btn(py.KEY_I):
        pilot='Sainz'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_S) and py.btn(py.KEY_T) and py.btn(py.KEY_R):
        pilot='Stroll'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_R) and py.btn(py.KEY_U) and py.btn(py.KEY_S):
        pilot='Russell'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_N) and py.btn(py.KEY_O) and py.btn(py.KEY_R):
        pilot='Norris'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_H) and py.btn(py.KEY_U) and py.btn(py.KEY_L):
        pilot='Hulkenberg'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_B) and py.btn(py.KEY_O) and py.btn(py.KEY_T):
        pilot='Bottas'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_O) and py.btn(py.KEY_C) and py.btn(py.KEY_N):
        pilot='Ocon'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_P) and py.btn(py.KEY_I) and py.btn(py.KEY_A):
        pilot='Piastri'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_G) and py.btn(py.KEY_A) and py.btn(py.KEY_S):
        pilot='Gasly'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_Z) and py.btn(py.KEY_H) and py.btn(py.KEY_O):
        pilot='Zhou'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_T) and py.btn(py.KEY_S) and py.btn(py.KEY_U):
        pilot='Tsunoda'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_M) and py.btn(py.KEY_A) and py.btn(py.KEY_G):
        pilot='Magnussen'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_A) and py.btn(py.KEY_L) and py.btn(py.KEY_B):
        pilot='Albon'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_S) and py.btn(py.KEY_A) and py.btn(py.KEY_R):
        pilot='Sargeant'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_D) and py.btn(py.KEY_E) and py.btn(py.KEY_V):
        pilot='De Vries'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_V) and py.btn(py.KEY_E) and py.btn(py.KEY_T):
        pilot='Vettel'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_R) and py.btn(py.KEY_I) and py.btn(py.KEY_C):
        pilot='Ricciardo'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_S) and py.btn(py.KEY_C) and py.btn(py.KEY_H):
        pilot='Schumacher'
        guesses.append(pilot)
        guess+=1
    if py.btnr(py.KEY_L) and py.btn(py.KEY_A) and py.btn(py.KEY_T):
        pilot='Latifi'
        guesses.append(pilot)
        guess+=1
    if pilot!='':
        col[guess][0]=8
        if pilots[pilot][0]==pilots[mystery][0]:
            col[guess]=[11 for j in range(7)]
        for i in range(1,len(pilots[pilot])):
            if pilots[pilot][i]<pilots[mystery][i] and i>2:
                col[guess][i]=10
            elif pilots[pilot][i]>pilots[mystery][i] and i>2:
                col[guess][i]=14
            elif pilots[pilot][i]==pilots[mystery][i] and i>2:
                col[guess][i]=11
            elif pilots[pilot][i][0]==pilots[mystery][i][0] and i!=1:
                col[guess][i]=11
            elif pilots[pilot][i]==pilots[mystery][i] and i==1:
                col[guess][i]=11
            else:
                col[guess][i]=8
    if found(col):
        gagne=True
        guess=0
    if len(guesses)==5 and gagne==False:
        gagne='LOST'
        guess=0

def found(col):
    for i in col[guess]:
        if i!=11:
            return False
    return True

py.run(update,draw)