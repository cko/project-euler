import Data.List (nub)

main = do
	let fives = [5,10..995]
	let threes = [3,6..999]

	let reduced_list = nub (fives ++ threes)
	print $ sum reduced_list
