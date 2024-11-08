with open("static/input.txt", "r") as f:
    phrase = f.readline()
    phrase = phrase[:len(phrase) - 1:]
    word = f.readline()

def build_freq_table(s):
    prob_table = {char: s.count(char) / len(s) for char in list(s)}
    sorted_prob_table = dict(sorted(prob_table.items(), key= lambda item: item[1], reverse=True))
    freq_table = dict()
    cumulative_prob = 0.0

    for symbol, probability in sorted_prob_table.items():
        # Интервал для символа начинается с cumulative_prob и заканчивается на cumulative_prob + probability
        freq_table[symbol] = ((cumulative_prob), (cumulative_prob + probability) )
        cumulative_prob += probability  # Обновляем кумулятивную вероятность для следующего символа

    return freq_table

def arithmetic(data):
    low, high = 0.0, 1.0 # Определяем начальные границы
    freq_table = build_freq_table(data)
    for symbol in data:
        range_width = high - low # Получаем интервал для текущего символа
        symbol_low, symbol_high = freq_table[symbol]
        # Обновляем границы интервала
        high = low + range_width * symbol_high
        low = low + range_width * symbol_low

    return sum((low, high))/2

def bwt(input_string):
    l, s = [], input_string
    for i in range(len(input_string)):
        l.append(s)
        s = s[1:] + s[0]

    return "".join(it[-1] for it in sorted(l))

def mtf(input_string):
    alphabet = sorted(set(input_string))  # Инициализируем алфавит
    result = ""
    for char in input_string:
        index = alphabet.index(char) # Находим индекс символа в алфавите
        result += str(index) # Добавляем индекс в результат

        # Перемещаем символ в начало алфавита
        alphabet.pop(index)
        alphabet.insert(0, char)
    return result

arf_res = arithmetic(phrase)
bwt_res = bwt(word)
mtf_res = mtf(bwt_res)

with open("static/output.txt", "w") as f:
    f.write(
f"""Фраза для арифметического кодирования:
{phrase}
результат арифметического кодирования: {arf_res}

Фраза для bwt и mtf кодирования: {word}
Результат bwt: {bwt_res}
Результат mtf: {mtf_res}++++""")