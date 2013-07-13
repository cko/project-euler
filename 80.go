package main

// https://gist.github.com/james4k/3730918
// The SSE instruction RSQRTSS might serve your purpose.
// 64-Bit: 0x5fe6eb50c7b537a9
import "fmt"
import "math/big"
import "strconv"

func main() {
	var total int64 = 0
	for i := 2; i <= 99; i++ {
		var a = big.NewRat(int64(i),1)
		var x = big.NewRat(int64(i-1),1)
    	var sqrt = big.NewRat(1,1)
    	sqrt = Newt_Sqrt(a,x)
		dec_string := sqrt.FloatString(102)
		var partial_sum = Calc_Sum(dec_string)
		total += partial_sum
	}
	fmt.Println(total)
}

func Newt_Sqrt(a *big.Rat, x *big.Rat) *big.Rat {
	for i := 0; i < 12; i++ {
		var quot1 = big.NewRat(1,1)
		quot1 = quot1.Quo(x, big.NewRat(2,1))
		var mul = big.NewRat(1,1)
		mul = mul.Mul(big.NewRat(2,1),x)
		var quot2 = big.NewRat(1,1)
		quot2 = quot2.Quo(a, mul)
		x = x.Add(quot1, quot2)		
	}
	return x
}

func Calc_Sum(x string) int64 {
	fmt.Println(x)
	var sum int64 = 0
	for i := 0; i < 99; i++ {
		s := x[2+i:3+i]
		number,_ := strconv.ParseInt(s, 10, 8)
		sum += number
	}
	
	if sum != 0 {
		number,_ := strconv.ParseInt(x[0:1], 10, 8)
		sum += number
	}
	return sum
}
