from pycricbuzz import Cricbuzz
def cricCommentry():
        c = Cricbuzz()
        matches = c.matches()
        # for match in matches:
        match=matches[0]
        # print( match)
        if(match['mchstate'] != 'nextlive'):
                print (c.livescore(match['id']))
                print( c.commentary(match['id']))
                print( c.scorecard(match['id']))
        print('sun',c.commentary(match['id'])['commentary'][0]['comm'])
        a,b=c.commentary(match['id'])['commentary'][0]['comm'],''
        while(1):
                if(a!=b):
                        # speak(a)
                        d=c.scorecard(match['id'])['scorecard']
                        print(a)
                        print(d[0]['batteam'],'score is ',d[0]['runs'],'for',d[0]['wickets'],'wickets')
                        b=a
                else:
                        a=c.commentary(match['id'])['commentary'][0]['comm']
cricCommentry()