
def model(input_shape, output_shape):

    layer1 = {  'layer': 'input',
                'input_shape': input_shape # 1000
             }
    layer2 = {  'layer': 'conv1d',
                'num_filters': 24,
                'filter_size': 19,
                'padding': 'SAME',
                'norm': 'batch',
                'activation': 'relu',
                'max_pool': 50, # 4
                'max_pool_strides': 2,  # 100
                'dropout': 0.1,
                }
    layer3 = {  'layer': 'conv1d',
               'num_filters': 64,
               'filter_size': 5,
               'padding': 'SAME',
               'norm': 'batch',
               'activation': 'relu',
               'dropout': 0.1,
               'max_pool': 50, # 4
               }
    layer4 = {  'layer': 'dense',
               'num_units': 96,
               'norm': 'batch',
               'activation': 'relu',
               'dropout': 0.5,
               }
    layer5 = {  'layer': 'dense',
                'num_units': output_shape[1],
                'activation': 'sigmoid',
                }

    model_layers = [layer1, layer2, layer3, layer4, layer5]

    # optimization parameters
    optimization = {"objective": "binary",
                  "optimizer": "adam",
                  "learning_rate": 0.0003,
                  "l2": 1e-6,
                  }

    return model_layers, optimization