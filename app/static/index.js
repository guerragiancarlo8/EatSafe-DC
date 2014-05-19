$(document).ready(function() {

	$("#container").fadeTo("fast",0);
	$("#click").hide()
	$("#encapsule").mouseenter(function(){
		$(this).fadeTo("fast",0.50);
		$("#click").toggle("fast")
	});
	$("#encapsule").mouseleave(function(){
		$(this).fadeTo("fast",1);
		$("#click").hide();
	});
	$("#encapsule").click(function() {
		$("#container").fadeTo("fast",0.90);


	});

	$("#button").mouseenter(function(){
		$(this).fadeTo("fast",0.50);
	});

	$("#button").mouseleave(function() {
		$(this).fadeTo("fast",1);
	});

	

});

