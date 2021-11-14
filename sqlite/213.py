import sqlite3
db = sqlite3.connect('baze.db')


def Bets_sums(team):
    
    cur = db.cursor()
    cur.execute("SELECT Bet FROM Guy WHERE team='" + team + "'")
    su = 0
    idd = 1
    for row in cur.fetchall():
        row = list(row)
        
        su += int(row[0])
    if team == 'Natus':
        bet = 'Bet2'
    else:
        bet = 'Bet1'
    cur.execute('UPDATE Match set '+ str(bet)+' = ? WHERE id = ?',(su,idd))
    db.commit()

Bets_sums('Sportsly')
