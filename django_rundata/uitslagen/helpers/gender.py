import pandas as pd

def selectWomen(df):
    """ given a dataFrame included 'cat' it will return a dataframe
    with return a dataFrame only with women and a gender column"""
    # labels starting with "V" is always womem
    dfV = df[df['cat'].str[0:1] == "V"]
    df = df[df['cat'].str[0:1] != "V"]
    womenKeyWords = ['DSEN', 'VR', 'DAM',  'D35', 'D45', 'D50', 'VSEN', 'V35',
                     '10D', 'V45', 'V50', 'V55']
    result = pd.DataFrame()
    for filter in womenKeyWords:
        temp = df[df['cat'].str.contains(filter)]
        result = pd.concat([temp, result])
        temp = []
    result = pd.concat([result, dfV])
    result['gender'] = 0
    return result

def selectMen(df):
    """ given a dataFrame included 'cat' it will return a dataframe
    with return a dataFrame only with women and a gender column"""
    # labels starting with "V" is always womem
    dfH = df[df['cat'].str[0:1] == "H"]
    dfM = df[df['cat'].str[0:1] == "M"]

    df = df[df['cat'].str[0:1] != "H"]
    df = df[df['cat'].str[0:1] != "M"]
    menKeyWords = ['HS', 'HEREN',"H30", 'H35','H40', 'H45','H50','H55','H60', 'H65', '10M', '10H'
                   'H65', 'MAN', 'MSEN', 'MSEN', 'M30',  'M35', 'M40', 'M55', 'M60', 'M65' ]
    result = pd.DataFrame()
    for filter in menKeyWords:
        temp = df[df['cat'].str.contains(filter)]
        result = pd.concat([temp, result])
        temp = []
    result = pd.concat([result, dfH, dfM])
    result['gender'] = 1
    return result