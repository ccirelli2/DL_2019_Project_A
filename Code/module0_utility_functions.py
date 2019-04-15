import os
import pandas as pd



def write_to_excel(dataframe, filename, target_dir):
    '''Inputs:  dataframe, filename, target_dir'''
    os.chdir(target_dir)    
    writer = pd.ExcelWriter(filename+'.xlsx')
    dataframe.to_excel(writer, 'Data')
    print('Dataframe {} has been written to {}'.format(filename, target_dir))
    writer.save()



def write_predictions_to_file(dataframe, model, result, target, variant, target_dir):
    os.chdir(target_dir)
    filename = str(model) + str(result) + str(target) + str(variant)
    writer = pd.ExcelWriter(filename+'.xlsx')
    dataframe.to_excel(writer, 'results')
    print('Dataframe {} has been written to {}'.format(filename, target_dir))
    writer.save()

