import Data.List (foldl')

diffs :: [Int] -> [Int]
diffs num = zipWith (-) num (tail num)

increment :: [Int] -> Int
increment = foldl' (\acc x -> if x < 0 then acc + 1 else acc) 0

main :: IO ()
main = do
  text <- readFile "input.txt"
  let num = map read (lines text)
  print $ increment $ diffs num
