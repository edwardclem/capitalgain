Router.map( function () {
  this.route('capitalgain', {path: '/'});
});

Router.map(function(){
	this.route('about', {path:'/about'});
})

Router.map(function(){
	this.route('graph', {path: '/graph'}, {data: {test: 'test'}});
});
