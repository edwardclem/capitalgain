Template.graph.rendered = function() {
    console.log("rendered");
    var filepath = musicData.findOne({
        ticker: Session.get('ticker')
    }).file;
    audio = new Audio(filepath);
    generateGraph();
    console.log(graphWidth());
    animateGraph(0);
};

Template.graph.events({
    'click #playbutton': function() {
        console.log('play');
        if (!Session.get('playing')) {
            audio.play();
            Session.set('playing', true);
            animateGraph();
        } else {
            Session.set('playing', false);
            audio.pause();
            clearInterval(interval);
        }
    }

});

Template.graph.helpers({
    musicData: function() {
        return musicData.findOne({
            ticker: Session.get('ticker')
        });
    }

});

function generateGraph() {
    console.log("generating graph");
    datadoc = musicData.findOne({
        ticker: Session.get('ticker')
    });
    data = datadoc.musicdata;
    console.log(data);
    min = 60;
    max = 70;
    maxlength = data.length[0];
    happy = ['#081A45', '#18409E', '#7C828F', '#3B3E45', '#382E5C', '#0E453F', '#0B3B0F',
        '#0B4480', '#5C0F28', '#2F2952', '#492969', '#70215B', '#338238', '#328A88',
        '#1C857A', '#157A99', '#6C3E96', '#10A6AD', '#AD104F', '#6155E6', '#1D8539',
        '#4BD1AB', '#E7ED3B', '#3BD0ED', '#9156D1', '#5ABF1F', '#61EDE6'
    ];
    var datavis = document.getElementById("data-vis");
    var absheight = datavis.clientHeight;
    for (var h = 0; h < data.length; h++) {
        for (var i = 0; i < data[h].length; i++) {
            for (var j = 0; j < data[h][i].length; j++) {
                //create note div with id
                //makeNote(data, i, j);
                var note = document.createElement("div");
                note.setAttribute("class", "note chord" + i);


                var ypos = absheight - 18 * (data[h][i][j]['pitch'] - min);
                note.style.top = ypos + 'px';
                note.style.width = 250 * (data[h][i][j]['dur']) + 'px';

                var left = 250 * (data[h][i][j]['time']);
                note.style.left = left + "px";
                if (h != 1) {
                    note.style.backgroundColor = happy[data[h][i][j]['+/-']];
                } else {
                    note.style.backgroundColor = "black";
                }
                datavis.appendChild(note);
            }
        }
    }

}

function movementRate() {

}

function animateGraph() {
    console.log(audio.duration);
    var duration = 15;
    interval = setInterval(moveGraph, duration);
}

//there's probably a more elegant way to do this.
function graphWidth() {
    datadoc = musicData.findOne({
        ticker: Session.get('ticker')
    });
    //console.log(datadoc);
    data = datadoc.musicdata;
    var lastpoint = data[1][data[1].length - 1][0];
    console.log(lastpoint);
    var lasttime = lastpoint['time'];
    var lastdur = lastpoint['dur']
    return (lasttime + lastdur) * 250
}

function moveGraph() {
    var scroll = document.getElementById("data-vis");
    console.log(audio.duration);
    console.log(scroll.style.width);
    // var chord = document.getElementByClassName("chord"+i);
    // var fin = 0-chord.offsetLeft;
    // if(scroll.offsetLeft < fin){
    //   i++;
    //   chord.className.replace( /(?:^|\s)active(?!\S)/g , '' );
    // }
    // else if (!(chord.className.match(/(?:^|\s)active(?!\S)/))){
    //   chord.className+= "active";
    // }

    var left = scroll.offsetLeft - (9.48);
    scroll.style.left = left + 'px';
    //console.log(scroll.style.left);
}

function animateGraph(i) {
    console.log(maxlength);
    if (i < maxlength) {
        var scroll = document.getElementById("data-vis");
        var chord = document.getElementsByClassName("chord" + i);
        console.log(chord.length);

        for (var j = 0; j < chord.length; j++) {
            // console.log(chord[j].className);
            var fin = 0 - chord[j].offsetLeft;
            if (scroll.offsetLeft < fin) {
                i++;
                chord[j].className.replace(/(?:^|\s)active(?!\S)/g, '');
            } else if (!(chord[j].className.match(/(?:^|\s)active(?!\S)/))) {
                chord[j].className += "active";
            }
        }

        var left = scroll.offsetLeft - (8);
        scroll.style.left = left + 'px';
        //console.log(scroll.style.left);
        setTimeout(animateGraph(i), 15);
    }