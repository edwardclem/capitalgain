

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
  console.log(musicData.findOne({ticker: Session.get('ticker')}));
  data = [
          [{'pitch':44,'dur':2,'time':0,'vel':90, 'happy': 20},
            {'pitch':48,'dur':2,'time':0,'vel':90, 'happy': 25},
            {'pitch':51,'dur':2,'time':0,'vel':90, 'happy': 22}],
          [{'pitch':56,'dur':2,'time':0,'vel':90, 'happy': 18}],
          [{'pitch':51,'dur':2,'time':1,'vel':90, 'happy': 12},
            {'pitch':55,'dur':2,'time':1,'vel':90, 'happy': 8},
            {'pitch':58,'dur':2,'time':1,'vel':90, 'happy': 3}],
          [{'pitch':58,'dur':4,'time':1,'vel':90, 'happy': 14}]

          ];
  min = 40;
  max = 70;
  happy = ['#06144F','#4A4B4D', '#091E73', '#656B85', '#7480AD', '#3B4B8A', '#213FB8',
            '#2A806C', '#2ABD9A', '#1DB86A', '#1F9135', '#0AC42F', '#7ECF15', '#E8E520',
            '#B3154A', '#99264C', '#B3207D', '#E8159B', '#D052F2', '#C884DB', '#94D1F7',
            '#43B4FA', '#FA4383', '#89E34D', '#ED4037', '#BF54BC', '#A865BA'];
  var datavis = document.getElementById("data-vis");
  console.log(datavis);
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

