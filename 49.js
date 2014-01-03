function findPrimes(){
    var primes = new Array();
    for (var i = 1001; i < 10000; i += 2){
        var isPrime = isPrimeNumber (i);
        if (isPrime){
            primes.push(i);
        }
    }
    return primes;
}


function isPrimeNumber (i){
    for (var k = 2; k <= Math.sqrt(i); k += 1){
         if (i % k == 0){
             return false;
         }
    }
    return true;
}


function calculatePermutations (numbers, perm, permutations){
    var newPermutations = permutations; 
    for (var i = 0; i < numbers.length; i++){
        var newNumbers = Array();
        permNumber = numbers [i];
        var newPerm = permNumber + '' + perm;
        for (var k = 0; k < numbers.length; k++){
            if (k != i){
                newNumbers.push(numbers[k]);
            }
        }
        if (numbers.length > 1){
           calculatePermutations(newNumbers, newPerm, newPermutations);
        } else {
            newPermutations[newPerm] = true;
        }
    }
    return newPermutations;
}


function getSelectedPrimes (){
    var primes = findPrimes();
    var originalPrimes = primes.slice();
    var selectedPrimes = Array();
    while (primes.length > 0){
        var primeStr = primes.pop() + '';
        var primeArray = Array();
        for (var k = 0; k < primeStr.length; k++){
            primeArray.push(primeStr[k]);
        }
	var existingPermutation = {};
        var permutations = calculatePermutations(primeArray, "", {});
        var selectedPermutations = Array();
        for (var permStr in permutations){
            var permutation = parseInt(permStr);
            var index = originalPrimes.indexOf(permutation);
            if (index > -1){
                selectedPermutations.push(permutation);
                primes.splice (index, 1);
            }
        }
        if (selectedPermutations.length > 2){
            selectedPrimes.push(selectedPermutations);
        }
    }
    return selectedPrimes;
}

function calculateDifferences (primeArray) {
    var values = {};
    for (var i = 0; i < primeArray.length; i++){
        for (var k = 0; k < i; k++){
            var diff = Math.abs(primeArray[k] - primeArray[i]);
            if (typeof values[diff] == 'undefined'){ 
               values[diff] = Array();
               values[diff].push(primeArray[i]);
               values[diff].push(primeArray[k]);
             }
        } 
        
        for (var diffvalue in values){
             var ivalue = true;
             for (var number in values[diffvalue]){
                 var difference = Math.abs(values[diffvalue][number] - primeArray[i]);
                if (difference != 0.5 * diffvalue && difference != 2 * diffvalue && difference !=  diffvalue){
                    ivalue = false;
                }
             }
             if (ivalue){
                values[diffvalue].push(primeArray[i]);
             }
        }
    }
    for (var diff in values){
        if (values[diff].length > 2){
            console.log('diff: ' + diff + '\t ' + values[diff]);
        }
    }
}


var selectedPrimes = getSelectedPrimes ();
for (var i = 0; i < selectedPrimes.length; i++){
    var currentPrimes = selectedPrimes[i];
    calculateDifferences(currentPrimes);
}
