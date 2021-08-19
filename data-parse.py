import pandas as pd

# Grab the column names from the data frame and return a list
def get_column_names(data):
    cols = []

    for col in data:
        cols.append(col)

    return cols


# Creates the initial dict with the x values 
def build_x_vals(data, cols, index):
    x = data[ cols[index] ]

    x_vals = {}

    for row in x:
        # print(row)
        try: 
            x_vals.index(str(row))
        except:
            x_vals[str(row)] = {}

    return x_vals



def build_y_vals(data, cols, index):
    y = data[ cols[index] ]

    y_vals = []

    for row in y:
        try:
            y_vals.index(str(row))
        except:
            y_vals.append(str(row))
    
    return y_vals


def init_table_dict(x_vals, y_vals):

    for val in x_vals:
        for entry in y_vals:
            x_vals[val][entry] = 0

    return x_vals


def parse_data(data, cols, i, j, x_vals):

    df = data[ [cols[i], cols[j] ]]

    for row in df.iterrows():
        f = str(row[1][0])
        s = str(row[1][1])
        
        x_vals[f][s] += 1

    return pd.DataFrame(x_vals)




# Controls the flow of the program
def main():
    data = pd.read_csv('mental-heath-in-tech-2016_20161114.csv')

    cols = get_column_names(data)

    count = 0
    page = 1

    for i in range(0, len(cols)):
        for j in range(i+1, len(cols)):
            count += 1
            if count > 20:
                count = 0
                page += 1
            print(page, count)

            path = './data_files/results-{}.md'.format(str(page))

            with open(path, 'a') as file:

                try:                    
                    x_vals = build_x_vals(data, cols, i)
                    y_vals = build_y_vals(data, cols, j)

                    table_dict = init_table_dict(x_vals, y_vals)

                    df = parse_data(data, cols, i, j, table_dict)

                    file.write(str(cols[i] + ' vs ' + cols[j]))
                    file.write('\n')
                    file.write(df.to_markdown())
                    file.write('\n\n')

                except:
                    pass




if __name__ == '__main__':
    main()