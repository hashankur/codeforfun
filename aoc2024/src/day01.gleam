import gleam/int
import gleam/io
import gleam/list
import gleam/result
import gleam/string
import utils/file

pub fn main() {
  let input = file.read_text("day01")

  let part_1_answer = part1(input)
  io.println("Part 1 answer: " <> int.to_string(part_1_answer))

  let part_2_answer = part2(input)
  io.println("Part 2 answer: " <> int.to_string(part_2_answer))
}

pub fn part1(input: String) -> Int {
  let assert Ok(#(list_1, list_2)) = parse(input)
  total_distance_lists(list_1, list_2)
}

pub fn part2(input: String) -> Int {
  let assert Ok(#(list_1, list_2)) = parse(input)
  similarity_score(list_1, list_2)
}

fn parse(input: String) -> Result(#(List(Int), List(Int)), Nil) {
  string.split(input, "\n")
  |> list.filter(fn(line) { line != "" })
  |> list.map(parse_line)
  |> result.all()
  |> result.map(list.unzip)
}

fn parse_line(input: String) -> Result(#(Int, Int), Nil) {
  let assert [a, b] = string.split(input, "   ")

  case int.parse(a), int.parse(b) {
    Ok(a), Ok(b) -> Ok(#(a, b))
    _, _ -> Error(Nil)
  }
}

fn total_distance_lists(list_1, list_2) -> Int {
  let sorted_1 = list_1 |> list.sort(int.compare)
  let sorted_2 = list_2 |> list.sort(int.compare)

  list.map2(sorted_1, sorted_2, fn(x, y) { int.absolute_value(x - y) })
  |> int.sum
}

fn similarity_score(list_1, list_2) -> Int {
  list_1
  |> list.map(fn(x) { x * list.count(list_2, fn(y) { x == y }) })
  |> int.sum
}
