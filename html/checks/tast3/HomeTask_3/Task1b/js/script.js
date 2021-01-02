var numArray = [];

function createArray(number){
	numArray.push(number);
}

function arrSumm(arr){
	var summ = 0;
	for(var i = 0; i < arr.length; i++){
	summ += arr[i];
}
	return summ;
}
var number = 0;

do{
	
	number = window.prompt("Введите элемент массива: " + "\nДля окончания ввода оставьте строку пустой или введите не число","");
	
	number = parseInt(number);
	
	if(number){
		
		createArray(number);
		
		console.log(numArray);
		
	}else{
	}
	
}
while(number)

if(numArray.length > 0){
	
	document.write("Создан массив: ");
for(var i = 0; i < numArray.length; i++){
	document.write(numArray[i] + ", ");
}

	document.write("<br>Сумма элементов массива: ");

	document.write(arrSumm(numArray));
}else{
	document.write("Введенные данные не подходят для создания числового массива");
}




