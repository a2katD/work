var numArray = [];
var evenArray = [];

function createArray(number){
	numArray.push(number);
}

function arrEven(arr){
	var even = 0;
	even = arr[0];
	for(var i = 0; i < arr.length; i++){
	if((arr[i] % 2 ) == 0){
		evenArray.push(arr[i]);
	}
}
	return evenArray;
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


evenArray = arrEven(numArray);

	document.write("<br>Четные элементы массива: ");
for(var i = 0; i < evenArray.length; i++){
	document.write(evenArray[i] + ", ");
}
}else{
	document.write("Введенные данные не подходят для создания числового массива");
}




