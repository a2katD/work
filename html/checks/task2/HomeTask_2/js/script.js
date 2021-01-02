
var number;
var letter;
var rightAnswersCounter = 0;


number = window.prompt("3 + 3 = ?","");
number = parseInt(number);

if(number == 6){

	rightAnswersCounter++;

}


number = window.prompt("0 * (234,4345 * 567,6767 + 435,234 * 456,23 ) = ?","");
number = parseInt(number);

if(number == 0){

	rightAnswersCounter++;

}


letter = window.prompt("First letter in alphabet: ",""); 


// 4 letters, becouse 2 letters latin and 2 letters russian

if(letter == 'a' || letter == 'A' || letter == 'À' || letter == 'à'){

	rightAnswersCounter++;

}


if (rightAnswersCounter > 0){

	document.write("<strong style='color:green'>Right answers count = " + 	rightAnswersCounter + "</strong>");

}else{

	document.write("<strong style='color:red'>Right answers count = 0</strong>");

}


