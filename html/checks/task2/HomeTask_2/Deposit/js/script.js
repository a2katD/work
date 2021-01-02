
var deposit = 0;
var percent = 0;
var period = 5;
var nextYearDepositSize = 0;

deposit = window.prompt("Input deposit amount: ","");
deposit = parseFloat(deposit);
deposit = deposit.toFixed(2);

percent = window.prompt("Which percent?","");
percent = parseFloat(percent)/100;

nextYearDepositSize = parseFloat(deposit) + parseFloat(deposit * percent);


// if entered numbers data
if(!isNaN(deposit) && !isNaN(percent)){

	document.write("Your deposit:<br>");
	
	for (var i = 0; i < period; i++){
		

		document.write("After " + (i + 1) + " year: " + 		parseFloat(nextYearDepositSize) + "<br>");

		nextYearDepositSize = parseFloat(nextYearDepositSize) + parseFloat(nextYearDepositSize * percent);
		nextYearDepositSize = nextYearDepositSize.toFixed(2);

	}

}else{

	document.write("<b style='color:red'>Your entered wrong data</b><br>");

}





