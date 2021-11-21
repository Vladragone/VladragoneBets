import sqlite3
import random
db = sqlite3.connect('baze.db')
cur = db.cursor()
commands = ['G2','Natus','Sportsly','Faze','EG','OG','PSG.LGD','Gambit','Spirit','Vitality','Fnatic','NiP','Astralis','Team Secret','Team Aster']
import string
def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return (rand_string)


def Bets_sums(team,versusteam):
    ssss = 0
    cur = db.cursor()
    cur.execute("SELECT Bet FROM Guy WHERE (team='" + team + "') AND (versusteam='" + versusteam + "')")
    su = 0
    
    for row in cur.fetchall():
        row = list(row)
        
        su += int(row[0])
    
    flag = False
    cur = db.cursor()
    cur.execute("SELECT id FROM Match WHERE (Team1='" + team + "') AND (Team2='" + versusteam + "')")
    sa = cur.fetchall()
    if sa == []:
        cur = db.cursor()
        flag = True
        team,versusteam=versusteam,team
        cur.execute("SELECT id FROM Match WHERE (Team1='" + team + "') AND (Team2='" + versusteam + "')")
        sa = cur.fetchall()
    for i in sa:
        

        ssss = list(i)[0]
    idd = ssss
    if not flag:
        bet = 'Bet1'
    else:
        bet = 'Bet2'
    cur = db.cursor()
    cur.execute('UPDATE Match set '+ str(bet)+' = ? WHERE id = ?',(su,idd))
    db.commit()

for i in range(len(commands)):
    for j in range(i+1,len(commands)):
        Bets_sums(str(commands[i]),str(commands[j]))
