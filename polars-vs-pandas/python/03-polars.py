import polars as pl
import pyperf


runner = pyperf.Runner()

def rename_col(filename):
    df = pl.read_csv(filename)
    col = 'Daily Max 8-hour CO Concentration'
    df = df.with_columns(pl.col(col).alias('CO'))
    return df

runner.bench_func('rename_col', rename_col, 'data/dataset.csv')
