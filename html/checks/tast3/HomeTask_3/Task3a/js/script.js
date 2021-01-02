
var answersArr = [['бегемот', 'Бегемот', 'БЕГЕМОТ'], ['груша', 'Груша', 'ГРУША'], ['соль', 'Соль', 'СОЛЬ']];
var questionArr = [ 'Отгадайте первую  загадку: У него огромный рот, Он зовется ...', 
					'Отгадайте вторую  загадку: Этот фрукт на вкус хорош. И на лампочку похож ...',
					'Отгадайте третью  загадку: В воде родится, воды боится ...'];
					
var offset = 0;

function rightAnswer(answersArr, userAnswer, offset){
	
	for (var i = 0; i < answersArr.length; i++){
		if(userAnswer == answersArr[offset][i]){
			alert("Вы угадали");
			return true;
		}
	}
	alert("Вы не угадали");
	return false;
}


function getAnswer(){
	for (var i = 0;  i < questionArr.length; i++){
		alert(questionArr[i]);
		userAnswer = prompt('Введите ваш ответ');
		rightAnswer(answersArr, userAnswer, offset);
		offset++;
	}
	
}


getAnswer();
document.write("Загадки закончились");