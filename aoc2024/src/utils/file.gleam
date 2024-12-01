import simplifile as file

pub fn assert_unwrap(result: Result(t, _)) -> t {
  case result {
    Ok(value) -> value
    _ -> panic
  }
}

pub fn read_text(day) -> String {
  file.read("data/" <> day <> ".txt")
  |> assert_unwrap
}
