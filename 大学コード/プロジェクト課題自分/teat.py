def extract_strings_T(input_data):
    # "T" から始まる文字列を抽出して配列に格納
    filtered_strings = [word for word in input_data if word.startswith("T")]
    return filtered_strings

input_data = ["Tiger", "Lion", "Turtle", "Elephant", "Tiger Shark", "Tiger Woods", "T-Rex", "Giraffe"]
result = extract_strings_T(input_data)

print(result)
