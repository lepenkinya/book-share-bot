def get_ISBN(lines):
    for line in lines:
        if "ISBN" in line:
            return extract_ISBN_number(line)
    return ''


def extract_ISBN_number(line):
    start_index = 0
    end_index = 0

    for i in range(len(line)):
        if line[i].isdigit():
            start_index = i
            break

    for i in range(len(line) - 1, 0, -1):
        if line[i].isdigit():
            end_index = i
            break

    return line[start_index:end_index + 1]
