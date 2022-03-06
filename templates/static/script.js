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
        a.href = './' + i;
        let btn = document.createElement('button');
        btn.classList.add('btn_concert');
        btn.innerHTML = 'Get tickets now'
        a.appendChild(btn);
        btn_container.appendChild(a);
        concert_card.appendChild(btn_container);
        concerts_container.appendChild(concert_card);
    };
}

function getSelectedConcertData(index) {
    const locations = concertsData.locations[index];
    const lineup = concertsData.lineups[index];
    let event_div = document.getElementById('event');
    event_div.style.backgroundImage = backgroundStyle[index];
    let event_h = document.createElement('h1');
    event_h.classList.add('h_event');
    event_h.innerHTML = concertsData.names[index];
    event_div.appendChild(event_h);
    let date_div = document.createElement('div');
    date_div.classList.add('date_event');
    let date = document.createElement('p');
    date.innerHTML = "This " + concertsData.dates[index] + ", don't miss the chance to see";
    date_div.appendChild(date);
    event_div.appendChild(date_div);
    let lineup_div = document.createElement('div');
    lineup_div.classList.add('lineup_event');
    for (let i = 0; i < lineup.length; i++) {
        let li = document.createElement('li');
        li.innerHTML = lineup[i];
        lineup_div.appendChild(li);
    }
    event_div.appendChild(lineup_div);
    let location_div = document.createElement('div');
    location_div.classList.add('date_event');
    let location = document.createElement('p');
    location.innerHTML = "in " + concertsData.places[index];
    location_div.appendChild(location);
    event_div.appendChild(location_div);
    let division = document.createElement('div');
    division.classList.add('division');
    event_div.appendChild(division);
    let div_p = document.createElement('div');
    let p_content = document.createElement('p');
    p_content.classList.add('p_event');
    p_content.innerHTML = "Choose your spot";
    div_p.appendChild(p_content);
    event_div.appendChild(div_p);
    let div_forms = document.createElement('div');
    div_forms.classList.add('wrap');
    let forms = document.createElement('form');
    forms.setAttribute('action', '');
    forms.classList.add('formulario');
    let div_locations = document.createElement('div');
    div_locations.classList.add('radio');
    for (let j = 0; j < locations.length; j++) {
        let loc_input = document.createElement('input');
        loc_input.setAttribute('type', 'radio');
        loc_input.setAttribute('name', 'locations');
        loc_input.setAttribute('value', locations[j]);
        loc_input.setAttribute('id', locations[j]);
        loc_input.setAttribute('onclick', "showPrice(index)");
        div_locations.appendChild(loc_input);
        let loc_label = document.createElement('label');
        loc_label.setAttribute('for', locations[j]);
        loc_label.innerHTML = locations[j];
        div_locations.appendChild(loc_label);
    }
    forms.appendChild(div_locations);
    div_forms.appendChild(forms);
    event_div.appendChild(div_forms);
}
