$(document).ready(function() {

	
	$("#click").hide()
	$("#encapsule").mouseenter(function(){
		$(this).fadeTo("fast",0.50);
		$("#click").toggle("fast")
	});
	$("#encapsule").mouseleave(function(){
		$(this).fadeTo("fast",1);
		$("#click").hide();
	});
	

	$("#button").mouseenter(function(){
		$(this).fadeTo("fast",0.50);
	});

	$("#button").mouseleave(function() {
		$(this).fadeTo("fast",1);
	});

	

});

