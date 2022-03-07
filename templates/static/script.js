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

backgroundStyle = ['linear-gradient(to right, #ffadf0, rgb(251, 251, 103))', 'linear-gradient(to right, #b9ffad, rgb(103, 113, 251))', 'linear-gradient(to right, #f19448, rgb(169, 251, 103))', 'background-image: linear-gradient(to right, #fc7e7e, rgb(133, 240, 133));'];



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
    event_div.setAttribute('value', index);
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
        loc_input.setAttribute('onclick', "showPrice()");
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

function showPrice() {
    let container = document.getElementById('event');
    let index = container.getAttribute('value');
    console.log(index);
    let choice = document.getElementsByTagName('input');
    for (let i = 0; i < choice.length; i++) {
        if (choice[i].checked) {
            var val = choice[i].value;
            var index2 = concertsData.locations[index].indexOf(val)
            console.log(index2)
        }
    }
    if (document.getElementById('price_container')) {
        let price_container = document.getElementById('price_container');
        price_container.remove();
    }

    let show_container = document.createElement('div');
    show_container.setAttribute('id', 'price_container');
    let price = document.createElement('p');
    price.innerHTML = 'PRICE: Q.' + concertsData.prices[index][index2];
    price.classList.add('price_event');
    show_container.appendChild(price);
    let div = document.createElement('div');
    div.classList.add('center');
    let btn = document.createElement('button');
    btn.classList.add('btn_concert');
    btn.innerHTML = 'Buy now';
    div.appendChild(btn);
    show_container.appendChild(div);
    container.appendChild(show_container);
}


function getNumberofInputsLineUp() {
    let numberPerformers = document.getElementById('Nperformers').value;
    let lineup_div = document.getElementById('lineup');
    let lineup_input = document.createElement('input');
    lineup_input.setAttribute('type', 'text');
    lineup_input.setAttribute('id', 'performer');
    let linup_label = document.createElement('label');
    linup_label.innerHTML = 'Performer ' + numberPerformers;
    linup_label.appendChild(lineup_input);
    lineup_div.appendChild(linup_label);
}

function getNumberofInputsLoc() {
    let numberLocation = document.getElementById('NLoc').value;
    let loc_div = document.getElementById('loc');
    let loc_input = document.createElement('input');
    let price_input = document.createElement('input');
    loc_input.setAttribute('type', 'text');
    price_input.setAttribute('type', 'text');
    loc_input.setAttribute('id', 'location');
    price_input.setAttribute('id', 'price');
    let loc_label = document.createElement('label');
    let price_label = document.createElement('label');
    loc_label.innerHTML = 'Location ' + numberLocation;
    price_label.innerHTML = 'Price ' + numberLocation;
    loc_label.appendChild(loc_input);
    price_label.appendChild(price_input);
    loc_div.appendChild(loc_label);
    loc_div.appendChild(price_label);
}

function setNewConcert() {
    let newLineup = [];
    let newLocs = [];
    let newPrices = [];
    let choice = document.getElementsByTagName('input');
    concertsData.names.push(choice[0].value);
    concertsData.dates.push(choice[1].value);
    concertsData.times.push(choice[2].value);
    for (let i = 0; i < choice.length; i++) {
        if (choice[i].id == 'performer') {
            newLineup.push(choice[i].value);
        };
        if (choice[i].id == 'location') {
            newLocs.push(choice[i].value);
        }
        if (choice[i].id == 'price') {
            newPrices.push(choice[i].value);
        }
    };
    concertsData.lineups.push(newLineup);
    concertsData.locations.push(newLocs);
    concertsData.prices.push(newPrices);
    console.log(concertsData);
}