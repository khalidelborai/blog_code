from pandas import read_csv
import pyperf

runner = pyperf.Runner()

def rename_col(filename):
    df = read_csv(filename)
    col = 'Daily Max 8-hour CO Concentration'
    df = df.rename(columns={col: 'CO'})
    return df

runner.bench_func('rename_col', rename_col, 'data/dataset.csv')
