fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = do
	fib (n - 2) + fib (n - 1) 

main = do
	let xxs = [fib(x) | x <- [1..36], fib(x) < 4000000]	
	print $ sum [ x | x <- xxs, even x ]
