from pandas import read_csv
import pyperf

runner = pyperf.Runner()

def save_rename_col(filename):
    df = read_csv(filename)
    col = 'Daily Max 8-hour CO Concentration'
    df = df.rename(columns={col: 'CO'})
    df.to_csv('data/dataset_renamed.csv')

runner.bench_func('save_rename_col', save_rename_col, 'data/dataset.csv')
