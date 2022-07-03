const sessionList = document.getElementById('card-parent');
var searchText = document.getElementById('searchText');
var results = document.getElementById('results');
var keySessions = [];
var durationJS = 100;
var pressedJS = false;

const loadSessions = async () => {
    try {
        const res = await fetch('https://iristeam.wixsite.com/osiris/_functions/sessions');
        keySessions = await res.json();
        const resEq = await fetch('https://iristeam.wixsite.com/osiris/_functions/keyEq');
        keyEq = await resEq.json();
        displaySessions(filterByKeyword(keySessions, keyEq));
    } catch (err) {
        console.error(err);
    }
};

const displaySessions = (mySessions) => {
    const htmlString = mySessions
        .map((session) => {
            var str = session.image == undefined ? "" : 'https://static.wixstatic.com/media/' + session.image.split('/')[3];
            return `
            <a href=showSession?sessionId=${session._id} class="card">
            <div class="card__head">
                <div class="card__image" style="background-image: url('${str}');"></div>
                <div class="card__author">
                    <div class="author">
                        <div class="author__content">
                    <p class="author__header">${session.title}</p>
                    <p class="author__subheader">${session.categorie}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="card__body">
                <h2 class="card__headline"></h2>
            </div>
            <div class="card__foot">
                <span class="card__link">Explore</span>
            </div>
            <div class="card__border"></div>
        </a>
        `;
        })
        .join('');
        sessionList.innerHTML = htmlString;
        empty = searchText.value == '' || searchText.value == undefined;
        if(!empty || pressedJS){
            results.innerHTML = "Found " + mySessions.length + " results!";
        } else if(empty){
            results.innerHTML = "";
        }
};

function filterByKeyword(keySessions, keyEq){
    empty = searchText.value == '' || searchText.value == undefined;
    let sessions = [];
    let keyEqMap = [];
    let filteredSessions = [];
    var searchValueList = empty ? "" : searchText.value.split(",").filter(r => r !== "").map(function(item) {
        return item.toLowerCase().trim();
      });
    //const checker = value => !searchValueList.some(element => value.includes(element));

    for (var data in keyEq){
        for (var entry in keyEq[data]){
            //if(keyEq[data][entry].eq.toLowerCase().filter(checker).size()>0){
            if(!empty && searchValueList.some(value => keyEq[data][entry].eq.toLowerCase().includes(value.toLowerCase()))) {
                keyEqMap.push(keyEq[data][entry].title)
            }
        }
    }
    
    for (var data in keySessions){
        for (var entry in keySessions[data]){
            if(empty){
                sessions.push(keySessions[data][entry]);
            }
            else if(keyEqMap.length != 0 && keyEqMap.every(value => keySessions[data][entry].keyword.toLowerCase().includes(value.toLowerCase()))){
                sessions.push(keySessions[data][entry]);
            }
        }
    }

    if(pressedJS){
        for(var data in sessions){
            duree = parseInt(sessions[data].duree.split("'")[0]) // duration[0] = 5'12 = 53.
            if(duree >= durationJS - 5 && duree < durationJS){
                filteredSessions.push(sessions[data])
            }
        }
    } else filteredSessions = sessions

    return filteredSessions;
}

function search(duration, pressed){
    if(duration != null && pressed != null){
        durationJS = duration
        pressedJS = pressed
    }
    loadSessions();
}