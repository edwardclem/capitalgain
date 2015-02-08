

  // counter starts at 0
  //Session.setDefault("counter", 0);

  // Template.home.helpers({
  //   counter: function () {
  //     return Session.get("counter");
  //   }
  // });


  Template.graph.rendered = function(){
    generateGraph();
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
function generateGraph(data){
  datadoc = musicData.findOne({ticker: Session.get('ticker')});
  data = datadoc.musicdata;
  console.log(data);
  min = 40;
  max = 70;
  happy = ['#081A45','#18409E', '#7C828F', '#3B3E45', '#382E5C', '#0E453F', '#0B3B0F',
            '#0B4480', '#5C0F28', '#2F2952', '#492969', '#70215B', '#338238', '#328A88',
            '#1C857A', '#157A99', '#6C3E96', '#10A6AD', '#AD104F', '#6155E6', '#1D8539',
            '#4BD1AB', '#E7ED3B', '#3BD0ED', '#9156D1', '#5ABF1F', '#61EDE6'];
  var datavis = document.getElementById("data-vis");
  
  var absheight = datavis.clientHeight;
  for(var i= 0; i < data.length; i++){
    for(var j = 0; j < data[i].length; j++){
      //create note div with id
      var note = document.createElement("div");
      note.setAttribute("class", "note chord"+i);
      
      var ypos = absheight - 15*(data[i][j]['pitch'] - min);
      note.style.top = ypos + 'px';
      note.style.width = data[i][j]['dur']*30 + 'px';

      var left = 40*data[i][j]['time'];
      note.style.left = left+"px";
      note.style.backgroundColor= happy[data[i][j]['happy']];
      datavis.appendChild(note);
    }
  }
}

