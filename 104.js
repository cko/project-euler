var isDoublePandigital = function (f_n){
	if (f_n.length < 9){
		return false;
	}
	var subarray_start = f_n.slice(0,9); 
	if(!isPandigital(subarray_start)){
		return false;
	}
	var subarray_end = f_n.slice(f_n.length - 9);
	return isPandigital(subarray_end);
}

var isPandigital = function (number){
	for (var i = 1; i <= 9; i++)
	if (number.indexOf(i) == -1){
		return false;
	}
	return true;
}

var fibonacci = function (f_n_1, f_n_2, n) {
	var f_n = new Array();
	f_n_2 = f_n_2.reverse();
	f_n_1 = f_n_1.reverse();
	var start = Date.now();
	while (!isDoublePandigital(f_n)){
		f_n = new Array();
		var uebertrag = 0;
		for (var i = 0; i < f_n_1.length; i++){
			var new_number = f_n_1[i] + uebertrag;
			if (f_n_2.length > i){
				new_number = new_number + f_n_2[i];
			}
			uebertrag = Math.floor(new_number/10);
			f_n.push(new_number % 10);
		}
		if (uebertrag > 0) {
			f_n.push(uebertrag);
		}
		++n;
		f_n_2 = f_n_1;
		f_n_1 = f_n;
		if (n % 1000 == 0){
			console.log (n);
			console.log('Zeit: ' + (Date.now()-start)/1000);
		}
  	}
  	console.log(n);
}

fibonacci([1],[1],2);