

  // counter starts at 0
  //Session.setDefault("counter", 0);

  // Template.home.helpers({
  //   counter: function () {
  //     return Session.get("counter");
  //   }
  // });


  Template.graph.rendered = function(){
    var filepath = musicData.findOne({ticker: Session.get('ticker')}).file;
    audio = new Audio(filepath);
    audio.play();
    generateGraph();
    animateGraph();
  };

  Template.graph.events({
    'click button': function () {
      // increment the counter when button is clicked
     // Session.set("counter", Session.get("counter") + 1);
      Router.go('capitalgain');
    }
  });

Template.graph.helpers({
  musicData: function(){
    return musicData.findOne({ticker: Session.get('ticker')});
}});

function generateGraph(){
  datadoc = musicData.findOne({ticker: Session.get('ticker')});
  console.log(datadoc);
  data = datadoc.musicdata;
  console.log(data);
  min = 60;
  max = 70;
  happy = ['#081A45','#18409E', '#7C828F', '#3B3E45', '#382E5C', '#0E453F', '#0B3B0F',
            '#0B4480', '#5C0F28', '#2F2952', '#492969', '#70215B', '#338238', '#328A88',
            '#1C857A', '#157A99', '#6C3E96', '#10A6AD', '#AD104F', '#6155E6', '#1D8539',
            '#4BD1AB', '#E7ED3B', '#3BD0ED', '#9156D1', '#5ABF1F', '#61EDE6'];
  var datavis = document.getElementById("data-vis");
  var absheight = datavis.clientHeight;
  var pixratio = ((128/60)*(audio.duration));
  console.log(pixratio);
  for(var h = 0; h < data.length; h++){
    for(var i= 0; i < data[h].length; i++){
      for(var j = 0; j < data[h][i].length; j++){
        //create note div with id
        //makeNote(data, i, j);
        var note = document.createElement("div");
        note.setAttribute("class", "note chord"+i);
        
        var ypos = absheight - 18*(data[h][i][j]['pitch'] - min);
        note.style.top = ypos + 'px';
        note.style.width = 250*(data[h][i][j]['dur']) + 'px';
        
        var left = 250*(data[h][i][j]['time']);
        note.style.left = left+"px";
        if(h != 1){
          note.style.backgroundColor= happy[data[h][i][j]['+/-']];  
        }
        else{
          note.style.backgroundColor = "black";
        }
        datavis.appendChild(note);
      }
    }
  }
  

}
function animateGraph(){
  var scroll = document.getElementById("data-vis");
  console.log(audio.duration);
  // var chord = document.getElementByClassName("chord"+i);
  // var fin = 0-chord.offsetLeft;
  // if(scroll.offsetLeft < fin){
  //   i++;
  //   chord.className.replace( /(?:^|\s)active(?!\S)/g , '' );
  // }
  // else if (!(chord.className.match(/(?:^|\s)active(?!\S)/))){
  //   chord.className+= "active";
  // }
  
  var left = scroll.offsetLeft - (8);
  scroll.style.left = left + 'px';
  //console.log(scroll.style.left);
  setTimeout(animateGraph, 15);
}
function makeNote(data, row, col){
  var note = document.createElement("div");
  note.setAttribute("class", "note chord"+i);
  
  var ypos = absheight - 18*(data[row][col]['pitch'] - min);
  note.style.top = ypos + 'px';
  note.style.width = 10*(data[row][col]['dur']) + 'px';
  
  var left = 10*(data[row][col]['time']);
  note.style.left = left+"px";
  note.style.backgroundColor= happy[data[row][col]['+/-']];
  datavis.appendChild(note);
}

