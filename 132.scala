def isPrimeNumber (i: Int):Boolean = {
    for (k <- 2 to (math.sqrt(i)).toInt + 1){
         if (i % k == 0){
             return false
        }
    }
    return true;
}


var sum = BigInt(0)
var count = 0
var exp = BigInt(10).pow(9)
var i = 3

while (count < 40){
    if (isPrimeNumber(i)){
        if (BigInt(10).modPow(exp, 9*i) == 1 ){
            sum += i
            count += 1
        }
    }
    i += 2
}
println (sum)
