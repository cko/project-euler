import scala.collection.mutable.ArrayBuffer

def isPrimeNumber (i: Int):Boolean = {
    for (k <- 2 to (math.sqrt(i)).toInt + 1){
         if (i % k == 0){
             return false
        }
    }
    return true;
}


def getPrimes () : ArrayBuffer[Int] = {
    var primes = ArrayBuffer.empty[Int]
    primes += 2
    for (i <- 3 to 7071 by 2){
        if (isPrimeNumber(i)){
            primes += i
        }
    }
    return primes
}

var primeNumbers = getPrimes()
var numbers = Set.empty[Int]
for (p1 <- primeNumbers; p2 <- primeNumbers; if p2 < 370 ){
    var p23 = math.pow(p2,3)
    var p12 = math.pow(p1,2)
    for (p3 <- primeNumbers; if p3 < 84){
        var sum = p12.toInt + p23.toInt +  math.pow(p3, 4).toInt
        if (sum < 50000000){
            numbers += sum
        }
    }
}
println (numbers.size)
