var bigInt = require("big-integer");

calculateSequence = function (){
	var seq = []
	for (var i = 1; i <= 100; i++){
		if (i % 3 == 0){ seq[i-1] = (i/3) * 2 } 
		else if (i == 1){ seq [i-1] = 2;} 
		else { seq[i-1] = 1;}
	}
	return seq;
}

calculateNumberString = function (){
	seq = calculateSequence();
	zaehler = bigInt(1);
	nenner = bigInt(seq[99]);
	for (var i = 98; i >= 0; i--){
		zaehler_n = zaehler.add(nenner.multiply(seq[i]));
		nenner_n = nenner;
		zaehler = nenner_n;
		nenner = zaehler_n;
	}
	return nenner.toString();
}

numberString = calculateNumberString();
sum = 0;
for (var i = 0; i < numberString.length; i++){
	number = parseInt (numberString[i-1,i])
	sum += number;
}
console.log(sum);
