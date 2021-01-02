var numArray = [];

function createArray(number){
	numArray.push(number);
}

function arrMin(arr){
	var min = 0;
	min = arr[0];
	for(var i = 0; i < arr.length; i++){
	if(min > arr[i]){
		min = arr[i];
	}
}
	return min;
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

	document.write("<br>Минимальный элемент массива: ");

	document.write(arrMin(numArray));
}else{
	document.write("Введенные данные не подходят для создания числового массива");
}




