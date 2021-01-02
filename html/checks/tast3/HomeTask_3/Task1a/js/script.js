function createArray(counter){
	var array = [];
	for(var i = 0; i < counter; i++){
		array.push(i+1);
	}
	return array;
}

var arrCounter = window.prompt("Введите число элементов массива: ","");
arrCounter = parseInt(arrCounter);

var numbersArr = createArray(arrCounter);

document.write("Создан массив: ");
for(var i = 0; i < numbersArr.length; i++){
	document.write(numbersArr[i] + ", ");
}



