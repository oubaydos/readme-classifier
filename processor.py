import csv
import os
import random


def count(path="res"):
    counter = 0
    for i in os.listdir(path):
        # print(i)
        if os.path.isdir(os.path.join(path, i)):
            counter += count(os.path.join(path, i))
        else:
            counter += 1
    return counter


def rename_to_md(path="res"):
    for i in os.listdir(path):
        # print(i)
        if os.path.isdir(os.path.join(path, i)):
            os.rename(os.path.join(path, i))
        else:
            os.rename(os.path.join(path, i), os.path.join(path, i.split(".")[0] + ".md"))
        print(i)


def move(path="res", destination_subfolder="good"):
    destinations = [os.path.join("train", destination_subfolder), os.path.join("test", destination_subfolder)]
    counter = 1
    for j in os.listdir(path):
        exact_path = os.path.join(path, j)
        if os.path.isdir(exact_path):
            for i in os.listdir(exact_path):
                os.rename(os.path.join(exact_path, i), os.path.join(random.choice(destinations), str(counter) + ".md"))
                counter += 1
        print(exact_path)


def convert_to_csv(test=False, good=False):
    path = None
    output = None
    if test and good:
        path = "test\\good"
        output = "test\\good.csv"
    elif test:
        path = "test\\bad"
        output = "test\\bad.csv"
    elif good:
        path = "train\\good"
        output = "train\\good.csv"
    else:
        path = "train\\bad"
        output = "train\\bad.csv"

    readmes = [["id", "readme", "is_good"]]
    counter = 1
    for i in os.listdir(path):
        with open(os.path.join(path, i)) as txt_file:
            txt = txt_file.read()
            # remove b' prefix and ' suffix
            if txt[:2] == "b'":
                txt = txt[2:-2]
            readmes.append([counter, txt, good])
        counter += 1
    with open(output, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(readmes)
    print(readmes)


convert_to_csv(False, False)
convert_to_csv(True, False)
convert_to_csv(False, True)
convert_to_csv(True, True)
