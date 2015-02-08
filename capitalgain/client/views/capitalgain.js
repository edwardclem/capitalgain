Template.capitalgain.events({
    'click button': function() {
        //gets the stock ticker
        var ticker = document.getElementById('search').value;
        console.log(ticker);

        //checking if ticker has been entered and is valid...
        if (ticker && musicData.findOne({ticker: ticker})){
          Session.set('ticker', ticker);
          Router.go('graph');
        }
    }
});
Template.capitalgain.rendered = function(){
  //console.log("resetting ticker");
  Session.set('ticker', null);
  audio.pause();
  audio = null;
}
