var answer = parseInt(Math.random() * 100);
var user1Answer = 0;
var user2Answer = 0;

while(user1Answer != 111 && user2Answer != 111){

	user1Answer = prompt("Player 1 guess number from 0 to 100" + "\n Input 111 for exit");

	user2Answer = prompt("Player 2 guess number from 0 to 100" + "\n Input 111 for exit");

	user1Answer = parseInt(user1Answer);
	user2Answer = parseInt(user2Answer);

	if(user1Answer == 111 || user2Answer == 111)break;

	if(user1Answer > answer) {

		alert("Player 1 your number is too much.");

	} else if(user1Answer < answer) {

		alert("Player 1 your number is too small.");

	} else if(user1Answer == answer) {

		alert("Bingo! Player 1 win!");

		break;

	} else if(user1Answer == 111 || user2Answer == 111) {


		break;

	} else {

		alert("Player 1 your input is not number!");

	}

	if(user2Answer > answer) {

		alert("Player 2 your number is too much.");

	} else if(user2Answer < answer) {

		alert("Player 2 your number is too small.");

	} else if(user2Answer == answer) {

		alert("Bingo! Player 2 win!");

		break;

	} else {

		alert("Player 2 your input is not number!");

	}


}







