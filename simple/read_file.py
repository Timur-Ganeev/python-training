def read_file_by_line_while(path: str, breakLine: str = '', withStrip: bool = True):
    textByLine = []
    with open(path) as tf:
        for line in iter(tf.readline, breakLine):
            if withStrip:
                textByLine.append(line.strip())
            else:
                textByLine.append(line)

    return textByLine


def read_file_by_line_while_gen(path: str, breakLine: str = '', withStrip: bool = True):
    with open(path) as tf:
        for line in iter(tf.readline, breakLine):
            if withStrip:
                yield line.strip()
            else:
                yield line


def can_convert_to_float(strToConvert: str):
    try:
        return float(strToConvert)
    except ValueError:
        pass


if __name__ == '__main__':
    import os
    import pickle
    from pprint import pprint

    filePath = "automation/data/sensor.csv"
    dirPath = os.path.dirname(os.getcwd())
    dataPath = os.path.join(dirPath, filePath)

    # all file in memory ->
    # data = read_file_by_line_while(dataPath)
    # seq = [i.split(',') for i in data]
    #
    # plainSeq = [word for line in seq for word in line]

    # read in memory by line with generator function ->
    plainSeq = []
    for line in read_file_by_line_while_gen(dataPath):
        plainSeq.extend(line.split(','))

    # convert with expression
    data_result = []
    convertExp = (float(fword) for fword in plainSeq if can_convert_to_float(fword) is not None)
    for fnum in convertExp:
        data_result.append(fnum)

    # pprint(plainSeq)
    pprint(data_result)

    data_dict = {key: data_result[key] for key in range(len(data_result))}
    print(data_dict)

    with open(os.path.join(dirPath, "data.pickle"), "wb") as wf:
        # data_stings = [f'{json.dumps(pair)}\n' for pair in data_dict]
        pickle.dump(data_dict, wf)


