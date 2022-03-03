from numpy import append
from Concert import Concert


lineUp1 = ['Bad Bunny', 'Rauw Alejandro', 'Jhay Cortez', 'Jay Wheeler']
lineUp2 = ['C. Tangana', 'Rels B', 'Rosalia', 'Humbe', 'Sebastian Cortes']
lineUp3 = ['Dua Lipa', 'Doja Cat', 'Harry Styles',
           'Bruno Mars', 'Lady Gaga', 'The Weeknd']

capacity = ['50000', '30550', '90800']

price = [['1000', '1500', '2000', '2500'], ['850', '1300',
                                            '1700', '2300'], ['1250', '1750', '2100', '3400']]

location = [['PLATONICOS', 'TIMELEZZ', 'VICE VERSA', 'YHLQMDLG'],
            ['SAOKO', 'ENTROPIA', 'LA ISLA', 'EL MADRILEÑO'], ['PLANET HER', 'THE FAME', 'DAWN FM', 'FINE LINE']]

dates = ['April 16 2022', 'July 1 2022', 'October 29 2022']
time = ['12:00AM', '3:00PM', '11:30AM']

place = ['Puerto San Jose', 'Finca Gutierres', 'Finca Jocotillo']

concert1 = Concert(
    lineUp1, 50000, price[0], location[0], 'April 16 2022', '12:00AM', 'Puerto San Jose')
concert2 = Concert(
    lineUp2, 30550, price[1], location[1], 'July 1 2022', '3:00PM', 'Finca Gutierres')
concert3 = Concert(
    lineUp3, 90800, price[2], location[2], 'October 29 2022', '11:30AM', 'Finca Jocotillo')


def getConcerts():
    concerts = []
    concerts.append(concert1)
    concerts.append(concert2)
    concerts.append(concert3)
    return concerts
