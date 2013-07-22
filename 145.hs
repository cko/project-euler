

digs :: Integral x => x -> [x]
digs 0 = []
digs x = x `mod` 10 : digs (x `div` 10)

all_odd :: Int -> Bool
all_odd a = length (filter even (digs a)) == 0

all_even :: Int -> Bool
all_even a = length (filter odd (digs a)) == 0

fromDigits = foldl addDigit 0 where addDigit num d = 10*num + d

main = do
	print $ length[x |x <- [2,4..1000000000], x `mod` 10 > 0, all_odd((fromDigits $ digs x) + x) == True] * 2
