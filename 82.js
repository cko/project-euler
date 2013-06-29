var fs = require('fs');

size = 80;
var result_matrix = new Array(size);
var initial_matrix = new Array(size);
for (var row = 0; row < size; row++) {
	result_matrix[row] = new Array(size);
	initial_matrix[row] = new Array(size);
	for (var column = 0; column < size; column++) {
		result_matrix[row][column] = 0;
		initial_matrix[row][column] = 0;
	}
}

var row = 0;
fs.readFileSync('./matrix2.txt').toString().split('\n').forEach(function(line){
    if (line.length > 0){
	    var elements = line.toString().split(',');
	    for (var column in elements){
	    	initial_matrix[row][column] = parseInt(elements[column]);
	    }
	    row++;
	}
 });

for (var column = 0; column < size; column++){
	for (var row = 0; row < size; row++){
		if (column == 0){
			result_matrix[row][0] = initial_matrix[row][0];
		}
		else {
			prev_col = result_matrix[row][column - 1];
			min_prev = prev_col;
			if (row > 0){
				prev_row = result_matrix[row - 1][column];
				min_prev = Math.min(prev_row, prev_col);
			}
			result_matrix[row][column] = initial_matrix[row][column] + min_prev;
		}
	}
	for (var row = size-1; row > 0; row--){
		current_result_value = result_matrix[row-1][column] - initial_matrix[row-1][column];
		next_row_value = result_matrix[row][column] 
		min_value = Math.min(current_result_value, next_row_value)
		result_matrix[row-1][column] = initial_matrix[row-1][column] + min_value;	
	}
}

min_value = result_matrix[0][size-1]
for (var row = 0; row < size; row++){
	var current_value = result_matrix[row][size-1];
	if (current_value < min_value){
		min_value = current_value;
	}
}
console.log(min_value);
