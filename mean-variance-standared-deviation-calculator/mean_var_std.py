import numpy as np

def calculate(input_list):
    calculations = {}
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    
    data_array = np.array([input_list[0:3], input_list[3:6], input_list[6:9]])

    # cal mean
    calculations['mean'] = [np.mean(data_array, axis=0).tolist(), np.mean(data_array, axis=1).tolist(), np.mean(data_array)]
    
    #cal variance
    calculations['variance'] = [np.var(data_array, axis=0).tolist(), np.var(data_array, axis=1).tolist(), np.var(data_array)]

    #cal std
    calculations['standard deviation'] = [np.std(data_array, axis=0).tolist(), np.std(data_array, axis=1).tolist(), np.std(data_array)]

    #cal max
    calculations['max'] = [np.max(data_array, axis=0).tolist(), np.max(data_array, axis=1).tolist(), np.max(data_array)]

    #cal min
    calculations['min'] = [np.min(data_array, axis=0).tolist(), np.min(data_array, axis=1).tolist(), np.min(data_array)]

    #cal sum
    calculations['sum'] = [np.sum(data_array, axis=0).tolist(), np.sum(data_array, axis=1).tolist(), np.sum(data_array)]

    
    return calculations
