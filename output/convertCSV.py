import glob, os, csv, json

for file in glob.glob("*.txt.*"):
    print(file)
    with open(file,'r') as input:
        mergedlsit = []
        for i in input.readlines():
            json_acceptable_string = i.replace("'", "\"")
            l = json.loads(json_acceptable_string)
            mergedlsit = mergedlsit + l
        keys = mergedlsit[0].keys()
        print(keys)
        with open(file+'.csv','w') as outputFile:
            dict_writer = csv.DictWriter(outputFile, keys)
            dict_writer.writeheader()
            dict_writer.writerows(mergedlsit)