# Variables

## Basic types

### Numbers
number1 = 10
number2 = 7

#### Operations on numbers
# + - / * % ** //
# print(number1 + number2)
# print(number1 - number2)
# print(number1 * number2)
# print(number1 / number2)
# print(number1 % number2)
# print(number1 ** number2)
# print(number1 // number2)

### Strings
string1 = "hello"
string2 = "python is a great programming language"

#### Operations on strings
# print(string1 + " guys")
# print(len(string1))
# print(string2.capitalize())
# print(string2.find("python"))
# print(string2.isalnum())
# print(string2.isdecimal())
# print(string2.replace("great", "fantastic"))
# print(string2.split(" "))

## Multivalue types

### Dictionaries
cousinsDct = {0:"Vatsu", 1:"Neelu", 2:"Balaji", 3:"Joema"}

#### Operations on dictionaries
# print("cousinsDct:", cousinsDct)
# print("cousinsDct[2]:", cousinsDct[2])
# cousinsDct[2] = "BBI"
# cousinsDct[4] = "Suman"
# print("adjusted cousinsDct:", cousinsDct)
# print("adjusted cousinsDct.keys:", cousinsDct.keys())
# print("adjusted cousinsDct.values:", cousinsDct.values())
cousinsDct.update({5: 'Kala'}); pp.pprint(cousinsDct)

### Lists
groceryList = ["eggs", "milk", "flour", "butter"]
clothesList = ["t shirt", "shorts", "sunglasses"]
shoppingList = [groceryList, clothesList]
masterList = groceryList + clothesList

#### Operations on lists
# print("groceryList:", groceryList)
# print("element 2 of groceryList:", groceryList[2])
# print("element :2 of groceryList:", groceryList[:2])
# print("element 2: of groceryList:", groceryList[2:])
# print("element 1:3 of groceryList:", groceryList[1:3])
# print("length of groceryList:", len(groceryList))
# print("max of groceryList:", max(groceryList))
# print("min of groceryList:", min(groceryList))
# groModList = groceryList
# groModList[2] = "baking soda"
# groModList.append("flour")
# groModList.insert(3, "sugar")
# groModList.remove("butter")
# del groModList[0]
# print("groModList:", groModList)
#
# print(" ")
# print("shoppingList:", shoppingList)
# print("Row 1 Column 0 element of shoppingList:", shoppingList[1][0])
# print("masterList:", masterList)

# List.sort() occurs in-place & returns None; use sorted() for a return value

# Find element in list
print(masterList.index("shorts"))
print(masterList.index("not present"))
print(masterList.index(["shorts", 'milk']))
print([masterList.index(elm) for elm in ["shorts", 'milk']])

### NpArrays
import numpy as np; print(np.__version__)
# np1Arr = np.array([1, 2, 3, 4, 5])
np1Arr = np.array([0, 2, 3, 4, 0])
np3x2Arr = np.array(
    [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
)

#### Operations on nparrays
print(np1Arr.reshape(1, 5).shape)

print(np.log(np1Arr))
print(np.log([1e-99 if x < 1e-99 else x for x in np1Arr]))
print(np.unique(np1Arr))
print(np.unique(np1Arr, return_counts = True))

print(np3x2Arr.ndim)
print(np3x2Arr.shape)
print(np3x2Arr[0, :].shape)
print(np3x2Arr.sum())
print(np3x2Arr.sum(axis = 0))
print(np3x2Arr.sum(axis = 1))

print(np.repeat(np.array([1, 2]), 3, axis = 0))
print(np.tile(np.array([1,2,3]), (4, 1)))


### pd DataFrames
import numpy as np; print(np.__version__)
import pandas as pd; print(pd.__version__)

df1 = pd.DataFrame({'val1': np.random.randint(0, 100, 20),
                    'val2': np.random.randint(0, 100, 20)})
labels = [ "{0} - {1}".format(i, i + 9) for i in range(0, 100, 10) ]
df1['group'] = pd.cut(df1.val1, range(0, 105, 10), right=False, labels=labels)
df1.index = ['row' + str(rIx) for rIx in list(df1.index)]
# df1.iloc[-1]['val2'] = 73 # this does not work; gives a warning
# df1.loc[-1, 'val2'] = 73 # this does not work; adds a row instead of updating in-place
df1.loc[df1.index[-1], 'val2'] = 73

df2 = pd.DataFrame({'val1': np.random.randint(0, 100, 20),
                    'val2': np.random.randint(0, 100, 20)})
labels = [ "{0} - {1}".format(i, i + 9) for i in range(0, 100, 10) ]
df2['group'] = pd.cut(df2.val1, range(0, 105, 10), right=False, labels=labels)
df2.index = ['row' + str(rIx) for rIx in list(df2.index)]

df = pd.concat([df1, df2])

#### Operations
print(df1['group'].unique())
rspSrs = pd.val1_counts(df1['group'], dropna = False)
clmLst = list(set(df1.columns).difference(set(['group'])))
print(sorted(list(df1['group'].unique())))
# print((df1['group']
#        .unique()
#        list()
#        sorted()))
print(df1.sort_values(['group', 'val1', 'val2'], ascending = [False, True, True]))

# iloc is integer based
print("df1.iloc[0:5, 0:2]:"%()); print(df1.iloc[0:5, 0:2])
print("df1.iloc[0:5][['val2', 'val1']]:"%()); print(df1.iloc[0:5][['val2', 'val1']])

# loc is label based
print("df1.loc[['row' + str(rIx) for rIx in range(5)], ['val2', 'val1']]:"%())
print(df1.loc[['row' + str(rIx) for rIx in range(5)], ['val2', 'val1']])

print("df1.loc[['row' + str(rIx) for rIx in range(5)]].iloc[:, 0:2]:"%())
print(df1.loc[['row' + str(rIx) for rIx in range(5)]].iloc[:, 0:2])

print("df1['val2'].max(): %f" % (df1['val2'].max()))

df1['valSum'] = df1.apply(lambda row: row['val1'] + row['val2'], axis = 1)
df1.loc[df1.index[-1], 'valSum'] = None
df1.loc[df1.index[np.isnan(df1['valSum'])], 'valSum'] = 200

# Note: The ix indexer has been deprecated in recent versions of Pandas, starting with version 0.20.1.

# filters
msk = (df1['val1'] >= 50) & (df1['val2'] >= 50)
print(df1[msk])

### Sets
number1Set = set([1, 2, 3, 4, 5])
number2Set = set([6, 7, 8, 9, 5])

#### Operations on sets
# print('number1Set.difference(number2Set): %s' % (number1Set.difference(number2Set)))

### Tuples
numberTuple = (1, 2, 3, 4, 5)
stringTuple = ("newspaper", "book", "magazine")
itemTuple = ("fruit", 2, 5.5)

#### Operations on tuples
# print("length of numberTuple:", len(numberTuple))
# print("max of stringTuple:", max(stringTuple))
# print("min of numberTuple:", min(numberTuple))
# print("index of element 2 in itemTuple:", itemTuple.index(2))


