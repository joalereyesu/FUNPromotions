concertsData = {
    'names': ['HOLY SUMMER', 'LA ISLA', 'SPOOKY MONSTER FESTIVAL'],
    'lineups': [
        ['Bad Bunny', 'Rauw Alejandro', 'Jhay Cortez', 'Jay Wheeler'],
        ['C. Tangana', 'Rels B', 'Rosalia', 'Humbe', 'Sebastian Cortes'],
        ['Dua Lipa', 'Doja Cat', 'Harry Styles', 'Bruno Mars', 'Lady Gaga', 'The Weeknd']],
    'capacity': ['50000', '30550', '90800'],
    'prices': [['1000', '1500', '2000', '2500'],
    ['850', '1300', '1700', '2300'],
    ['1250', '1750', '2100', '3400']],
    'locations': [['PLATONICOS', 'TIMELEZZ', 'VICE VERSA', 'YHLQMDLG'],
    ['SAOKO', 'ENTROPIA', 'LA ISLA', 'EL MADRILEÑO'],
    ['PLANET HER', 'THE FAME', 'DAWN FM', 'FINE LINE']],
    'dates': ['April 16 2022', 'July 1 2022', 'October 29 2022'],
    'times': ['12:00AM', '3:00PM', '11:30AM'],
    'places': ['Puerto San Jose', 'Finca Gutierres', 'Finca Jocotillo']
};

backgroundStyle = ['linear-gradient(to right, #ffadf0, rgb(251, 251, 103))', 'linear-gradient(to right, #b9ffad, rgb(103, 113, 251))', 'linear-gradient(to right, #f19448, rgb(169, 251, 103))'];



function getConcertsMainData() {
    let concertNames = concertsData.names;
    let concerts_container = document.getElementById('concerts');
    for (let i = 0; i < concertNames.length; i++) {
        let concert_card = document.createElement('div');
        concert_card.classList.add('div_concerts_card');
        concert_card.style.backgroundImage = backgroundStyle[i];
        let h2 = document.createElement('h2');
        h2.innerHTML = concertsData.names[i];
        concert_card.appendChild(h2);
        let h3 = document.createElement('h3');
        h3.innerHTML = 'LINEUP';
        concert_card.appendChild(h3);
        let lineup_container = document.createElement('div');
        lineup_container.classList.add('lineup_container');
        concertsData.lineups[i].forEach(singer => {
            let li = document.createElement('li');
            li.innerHTML = singer;
            lineup_container.appendChild(li);
        });
        concert_card.appendChild(lineup_container);
        let date = document.createElement('div');
        date.classList.add('date_container');
        let p = document.createElement('p');
        p.innerHTML = concertsData.dates[i] + ' at ' + concertsData.times[i];
        date.appendChild(p);
        concert_card.appendChild(date);
        let btn_container = document.createElement('div');
        btn_container.classList.add('center');
        let a = document.createElement('a');
        let btn = document.createElement('button');
        btn.classList.add('btn_concert');
        btn.innerHTML = 'Get tickets now'
        a.appendChild(btn);
        btn_container.appendChild(a);
        concert_card.appendChild(btn_container);


        // let date_container = document.createElement('div');
        // date_container.classList.add('date_container');
        // let p = document.createElement('p');
        // p.innerHTML = concertsData.dates[i] + " at " + concertsData.times[i];
        // date_container.appendChild(p);
        // let btn_container = document.createElement('div');
        // btn_container.classList.add('center');
        // let a = document.createElement('a');
        // let btn = document.createElement('button');
        // btn.classList.add('btn_concert');
        // a.appendChild(btn);
        // btn_container.appendChild(a);
        // btn_container.appendChild(concert_card);
        concerts_container.appendChild(concert_card);
    };
}