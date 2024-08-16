import polars as pl
import pyperf


runner = pyperf.Runner()

def save_rename_col(filename):
    df = pl.read_csv(filename)
    col = 'Daily Max 8-hour CO Concentration'
    df = df.with_columns(pl.col(col).alias('CO'))
    df.write_csv('data/dataset_renamed_polars.csv')

runner.bench_func('save_rename_col', save_rename_col, 'data/dataset.csv')
