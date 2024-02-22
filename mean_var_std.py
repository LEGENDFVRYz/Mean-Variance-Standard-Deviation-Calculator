import numpy as np

def calculate(list):
    # INPUT VALIDATION TO PROCEED (list should only have 9 elements, else we raise an error)
    if len(list) == 9:
        
        # MAKE THE GIVEN LIST TO A NUMPY MATRIX (conv_matrix short for "converted_matrix")
        conv_list = np.array(list)  # Could be used as a flatten computations
        conv_matrix = conv_list.reshape(3, 3)
        
        # PROCEED TO CALCULATIONS
        calculations = {}

        # print(np.mean(conv_matrix, axis=0))       # Experimentation Purposes Only
        # print(np.mean(conv_matrix, axis=1))       # Experimentation Purposes Only
        # print(np.mean(conv_list))                 # Experimentation Purposes Only

        calculations['mean'] = [np.mean(conv_matrix, axis=0).tolist(),
                                np.mean(conv_matrix, axis=1).tolist(),
                                np.mean(conv_list)] # Conv_list is already flattened

        calculations['variance'] = [np.var(conv_matrix, axis=0).tolist(),
                                    np.var(conv_matrix, axis=1).tolist(),
                                    np.var(conv_list)] # Conv_list is already flattened

        calculations['standard deviation'] =   [np.std(conv_matrix, axis=0).tolist(),
                                                np.std(conv_matrix, axis=1).tolist(),
                                                np.std(conv_list)] # Conv_list is already flattened

        calculations['max'] =  [np.max(conv_matrix, axis=0).tolist(),
                                np.max(conv_matrix, axis=1).tolist(),
                                np.max(conv_list)] # Conv_list is already flattened

        calculations['min'] =  [np.min(conv_matrix, axis=0).tolist(),
                                np.min(conv_matrix, axis=1).tolist(),
                                np.min(conv_list)] # Conv_list is already flattened

        calculations['sum'] =  [np.sum(conv_matrix, axis=0).tolist(),
                                np.sum(conv_matrix, axis=1).tolist(),
                                np.sum(conv_list)] # Conv_list is already flattened

        return calculations

    else:
        # Raise Error if n(list) < 9
        raise ValueError('List must contain nine numbers.') 