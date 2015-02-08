data = [[{'pitch':44,'dur':0.5,'time':0,'vel':90},
              {'pitch':48,'dur':0.5,'time':0,'vel':90},
              {'pitch':51,'dur':0.5,'time':0,'vel':90}],
            [{'pitch':56,'dur':0.5,'time':0,'vel':90}],
            [{'pitch':51,'dur':0.5,'time':1,'vel':90},
              {'pitch':55,'dur':0.5,'time':1,'vel':90},
              {'pitch':58,'dur':0.5,'time':1,'vel':90}],
            [{'pitch':58,'dur':1,'time':1,'vel':90}]];
min = 40;
max = 70;
if (Meteor.isClient) {
  // counter starts at 0
  //Session.setDefault("counter", 0);

  // Template.home.helpers({
  //   counter: function () {
  //     return Session.get("counter");
  //   }
  // });

Template.graph.rendered = function(){
  //console.log("rendered!");
  //console.log(Session.get('ticker'));
}

  Template.graph.events({
    'click button': function () {
      // increment the counter when button is clicked
     // Session.set("counter", Session.get("counter") + 1);
      Router.go('capitalgain');
    }
  });
}

Template.graph.helpers({
  musicData: function(){
    return musicData.findOne({ticker: Session.get('ticker')});
  }
})

