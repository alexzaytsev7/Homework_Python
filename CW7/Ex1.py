values = [1, 23, 5, 'asdfg']
transformed_values = list(map(lambda x: x, values))
if values == transformed_values:
    print('ok')
else:
    print ('fail')