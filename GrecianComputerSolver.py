plate1 = [
    [2,3,8,14]
    ,[5,3,9,11]
    ,[10,14,10,14]
    ,[7,14,11,14]
    ,[16,21,12,11]
    ,[8,21,13,14]
    ,[7,9,14,11]
    ,[8,9,15,14]
    ,[8,4,4,11]
    ,[3,4,5,11]
    ,[4,6,6,14]
    ,[12,6,7,11]
]

plate2 = [
    [1,3,9,7]
    ,["h",26,20,"h"]
    ,[9,6,12,9]
    ,["h","h",3,"h"]
    ,[12,2,6,7]
    ,["h",13,"h",14]
    ,[6,9,14,11]
    ,["h","h",12,"h"]
    ,[10,17,3,8]
    ,["h",19,8,"h"]
    ,[10,3,9,16]
    ,["h",12,"h",2]
]

plate3 = [
    ["h",5,21,9]
    ,["h","h",6,13]
    ,["h",10,15,9]
    ,["h","h",4,7]
    ,["h",8,9,13]
    ,["h","h",18,21]
    ,["h",22,11,17]
    ,["h","h",26,4]
    ,["h",16,14,5]
    ,["h","h",1,"h"]
    ,["h",9,12,7]
    ,["h","h","h",8]
]

plate4 = [
    ["h","h",4,7]
    ,["h","h","h",3]
    ,["h","h",7,"h"]
    ,["h","h",15,6]
    ,["h","h","h","h"]
    ,["h","h","h",11]
    ,["h","h",14,11]
    ,["h","h","h",6]
    ,["h","h",9,11]
    ,["h","h","h","h"]
    ,["h","h",12,6]
    ,["h","h","h",17]
]

plate5 = [
    ["h","h","h",3]
    ,["h","h","h","h"]
    ,["h","h","h",6]
    ,["h","h","h","h"]
    ,["h","h","h",10]
    ,["h","h","h","h"]
    ,["h","h","h",7]
    ,["h","h","h","h"]
    ,["h","h","h",15]
    ,["h","h","h","h"]
    ,["h","h","h",8]
    ,["h","h","h","h"]
]

plates = [
    plate1
    ,plate2
    ,plate3
    ,plate4
    ,plate5
]

def stack_columns(columns):
    """
    Returns a list representing the result when a
    single column from every plate is stacked to
    remove holes (h).

    columns: list with one column from each plate in the order
    plate1 to plate5. [p1_column, p2_column, ..., p5_column]
    """
    stacked_column = [0,0,0,0]

    for idx in range(4,0,-1):
        first_nonzero = None
        found = False
        idx_tmp = idx + 1
        while not found:
            idx_tmp = idx_tmp - 1
            if columns[idx_tmp][idx-1]  != "h":
                found = True
                first_nonzero = idx_tmp
        
        stacked_column[idx-1] = columns[idx_tmp][idx-1]
    return stacked_column

def assemble_plates(indices):
    """
    Returns a list of lists representing the
    aligned plates on the puzzle

    indices: list with column indices of plates
    2 through 4 in that order
    """
    stacked_columns = []
    for incr in range(0,12):
        indices_incr = [(idx + incr) %12 for idx in indices]
        # print(f"incr {incr}: {indices_incr}")
        columns = [
            plate1[incr]
            ,plate2[indices_incr[0]]
            ,plate3[indices_incr[1]]
            ,plate4[indices_incr[2]]
            ,plate5[indices_incr[3]]
        ]
        # print(columns)
        stacked_columns.append(stack_columns(columns=columns))
    return stacked_columns

for index_p2 in range(0,12):
    for index_p3 in range(0,12):
        for index_p4 in range(0,12):
            for index_p5 in range(0,12):
                indices = [
                    index_p2
                    ,index_p3
                    ,index_p4
                    ,index_p5
                ]
                # print(f"indices: {indices}")
                assembled_plates = assemble_plates(indices=indices)
                # print(assembled_plates)
                column_sums = [sum(column) for column in assembled_plates]
                # print(f"{indices}: {column_sums}")
                if column_sums == [42] * 12:
                    print(indices)
                    print(assembled_plates)