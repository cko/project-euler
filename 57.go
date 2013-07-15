package main

import "fmt"
import "math/big"

func main() {
	var zaehler = big.NewInt(1);
	var nenner = big.NewInt(2);
	var zaehler_neu = big.NewInt(1);
	var nenner_neu = big.NewInt(1);
	count := 0;
	for i:= 0; i < 1000; i++ {
		var doubleNenner = big.NewInt(1);
		doubleNenner.Mul(big.NewInt(2), nenner);
		zaehler_neu = zaehler_neu.Add(zaehler, doubleNenner);
		nenner_neu.Set(nenner);

		zaehler.Set(nenner_neu);
		nenner.Set(zaehler_neu);

		var finalzaehler = big.NewInt(1);
		finalzaehler = finalzaehler.Add(zaehler_neu, nenner_neu)
		if len(finalzaehler.String()) > len(nenner.String()) {
			count += 1;
		}
	}
	fmt.Println(count);	
}
