def convert_string_to_lists(input_string):
    result_lists = [[] for _ in range(4)]  # 4つの空リストを用意

    current_list = None
    for char in input_string:
        if char.isdigit():
            if current_list is not None:
                current_list.append(int(char))
        elif char.isalpha():
            if char == "m":
                current_list = result_lists[0]
            elif char == "p":
                current_list = result_lists[1]
            elif char == "s":
                current_list = result_lists[2]
            elif char == "z":
                current_list = result_lists[3]
            else:
                current_list = None

    return result_lists

# テスト用の文字列
input_string = "99m14789p12s555z"

# 関数の呼び出し
result = convert_string_to_lists(input_string)

# 結果の表示
print(result)
