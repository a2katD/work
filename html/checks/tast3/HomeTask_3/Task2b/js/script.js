var lettersFirstLevel = ["ы", "в"];
var lettersSecondLevel = ["о", "ж"];

function generateText(letters, length){
	
	var text = "";
	
	for (var i = 0; i < length; i++){
		var n = getRandomNumber(letters.length - 1);
		text = text + letters[n];
	}
	
	return text;
}

function getRandomNumber(max){
	return Math.round(Math.random() * max);
}


alert("Вас приветствует программа по обучению слепой печати");


while(true){
	
	alert(	
			"Поставьте мизинец левой руки на букву Ф, \nбезымянный палец — на Ы, \nсредний — на В, \nуказательный — на А. " + 
			"\nМизинец правой руки на букву Ж, \nбезымянный палец — на Д, \nсредний — на Л, \nуказательный — на О. " + 
			"\nЗапомните расположение пальцев. \nПовторяйте за мной. \nПостарайтесь не смотреть на клавиатуру."
	);
	
	var text = generateText(lettersFirstLevel, 10);
	
	var userText = prompt(text);
	
	if(userText == text){
		alert("Все верно. Теперь следующий уровень.");
		break;
	}else{
		alert("Неправильно введены буквы");
	}
	
}

while(true){
	
	alert(	
			"Поставьте мизинец левой руки на букву Ф, \nбезымянный палец — на Ы, \nсредний — на В, \nуказательный — на А. " + 
			"\nМизинец правой руки на букву Ж, \nбезымянный палец — на Д, \nсредний — на Л, \nуказательный — на О. " + 
			"\nЗапомните расположение пальцев. \nПовторяйте за мной. \nПостарайтесь не смотреть на клавиатуру."
	);
	
	var text = generateText(lettersSecondLevel, 10);
	
	var userText = prompt(text);
	
	if(userText == text){
		alert("Все верно");
		break;
	}else{
		alert("Неправильно введены буквы");
	}
	
}

document.write("Все упражнения закончены");