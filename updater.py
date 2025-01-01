"""
Traverse the csv file, using the first line as a list of fields
make a list of dicts
make each line it's own dict, containing the header as the key, and the episode data as the value
"""

def read_file(file_name):
    data = []
    with open (file_name) as file:
        fields = file.readline().strip().split(',')
        for line in file:
            episode = {}
            spaces = line.strip(" ").split(',')
            for i, header in enumerate (fields):
                episode [header] = spaces[i]
                data.append(episode)
        return (data)



            



def main():
    data = read_file("iasip.csv")
    for line in data:
        print (line)qqq
        for ep in line:
            print (line[ep])

if __name__ == "__main__":
    main()