var fileload = require('./fileload.js');
var cluster = require('cluster')

processRomanNumber = function (number){
	var total = 0;
	if (number.indexOf('VIIII') != -1 ){
		total += 3;
	} else if (number.indexOf('VIV') != -1){
		total += 1;
	} else if (number.indexOf('IIII') != -1 ){
		total += 2;
	} 
	if (number.indexOf('LXXXX') != -1 ){
		total += 3;
	} else if (number.indexOf('XXXX') != -1 ){
		total += 2;
	} 
	if (number.indexOf('DCCCC') != -1 ){
		total += 3;
	} else if (number.indexOf('CCCC') != -1 ){
		total += 2;
	} 
	return total;
}

work = function (start, end){
	var sum = 0;
	for (var i = start; i < end; i++){
		line = lines[i];
		result = processRomanNumber(line);
		sum += result;
	}
	return sum;
}

var lines = fileload.readFileLines('roman.txt');

if (cluster.isMaster) {
	var total = 0;
    for (var i = 0; i < 4; i++) { 
        worker = cluster.fork();
        worker.on('message', function(msg) {
        	this.disconnect();
            console.log('Worker[%d] has finished: ',msg.from,msg.msg);
            total += msg.msg;
        });
        worker.send({ msg: i });
    }
    cluster.on('exit', function(worker, code, signal) {
  		if (Object.keys(cluster.workers).length == 0){
  			console.log("no active workers remaining");
  			console.log(total);
  		}
	});
} else {
    process.on('message', function(msg) {
    	var no = parseInt(msg.msg);
        sum =work(250 * no, 250* (no +1));
        process.send({ msg: sum , from: cluster.worker.id });
    });
}
