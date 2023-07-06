main :: IO ()
main = do
    let sum = sumMultiples 999
    putStrLn $ "The sum is: " ++ show sum

sumMultiples :: Int -> Int
sumMultiples n = sum [x | x <- [1..n], x `mod` 3 == 0 || x `mod` 5 == 0]