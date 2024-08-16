import polars as pl
import pyperf

runner = pyperf.Runner()

def filter_dataset(filename):
    df = pl.read_csv(filename)
    df = df.filter(pl.col('Daily Max 8-hour CO Concentration') > 0.5)
    return df

runner.bench_func('filter_dataset', filter_dataset, 'data/dataset.csv')
