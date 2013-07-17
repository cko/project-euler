package main

import "fmt"
import "math"

func main() {
	set := make(map[int]bool)
	for n:=1; n< 40000; n++ {
		p_n := n*(3*n-1)/2
		for k, _ := range set {  
			diff := p_n - k 
			sum := p_n + k
			sum_is_pentagonal := is_pentagonal(sum)
			diff_is_pentagonal := set[diff]
			if sum_is_pentagonal && diff_is_pentagonal {
				fmt.Println("----------")
				fmt.Println(p_n)
				fmt.Println(k)
				fmt.Println(diff)
			}
		}
		set[p_n] = true
	}
}

func is_pentagonal (sum int) bool {
	var term float64 = float64(1 + 24 * sum)
	sum_sqrt := math.Sqrt(term)
	int_sqrt := int32(sum_sqrt)
	if float64(int_sqrt * int_sqrt) != term {
		return false
	}
	if (1 + int_sqrt) % 6 == 0 {
		return true
	}
	return false
}