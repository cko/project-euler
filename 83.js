var fs = require('fs');

calculateRow = function (column, row, result_matrix, initial_matrix){
	if (column == 0 && row == 0){
		result_matrix[0][0] = initial_matrix[0][0];
	}
	else if (column == 0) {
		prev_row = result_matrix[row - 1][column];
		result_matrix[row][column] = initial_matrix[row][column] + prev_row;
	} else {
		prev_col = result_matrix[row][column - 1];
		min_prev = prev_col;
		if (row > 0){
			prev_row = result_matrix[row - 1][column];
			min_prev = Math.min(prev_row, prev_col);
		} 
		result_matrix[row][column] = initial_matrix[row][column] + min_prev;
  	}
}

calculateMatrix = function (column_par, row_par, result_matrix, initial_matrix){
  for (var column = column_par; column < size; column++){
	for (var row = row_par; row < size; row++){
		calculateRow(column, row, result_matrix, initial_matrix);
		if (column < size && column > 1){
			prev_col = result_matrix[row][column-2];
			next_col = result_matrix[row][column];
			min_value = Math.min(prev_col, next_col);
			current_value = result_matrix[row][column-1];
			if (min_value + initial_matrix[row][column-1] < current_value ){
				result_matrix[row][column-1] = min_value + initial_matrix[row][column-1];
				for (var i = row + 1; i < size; i++){
					calculateRow(column-1, i, result_matrix, initial_matrix);
				}
			}
		}
	}
	for (var row = size-1; row > 0; row--){
		current_result_value = result_matrix[row-1][column] - initial_matrix[row-1][column];
		next_row_value = result_matrix[row][column] 
		min_value = Math.min(current_result_value, next_row_value)
		if (column < size - 1){
			next_column_value = result_matrix[row][column + 1]
		}
		result_matrix[row-1][column] = initial_matrix[row-1][column] + min_value;	
	}
  }
}


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
fs.readFileSync('./matrix3.txt').toString().split('\n').forEach(function(line){
    if (line.length > 0){
	    var elements = line.toString().split(',');
	    for (var column in elements){
	    	initial_matrix[row][column] = parseInt(elements[column]);
	    }
	    row++;
	}
 });

calculateMatrix(0, 0, result_matrix, initial_matrix);
console.log(result_matrix);
