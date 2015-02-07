Meteor.startup(function(){
	console.log("test");
	//accessing collections
	test = new Mongo.Collection("stuff");
	console.log(test.find().fetch());
});