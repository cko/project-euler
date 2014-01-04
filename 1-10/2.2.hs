main = do
	let fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
	let l = takeWhile (<4000000) fibs
	let l2 = filter even l
	print $ sum l2
