var question = parseFloat(window.prompt("Number that you can add to any summ and summ not change: ", ""));

if(question == 0.0){

	document.write("<strong style='color:green'>Your answer is right</strong><br>");
	document.write("Game over");
}else{
	document.write("<strong style='color:red'>Your answer is not right</strong>");

}
