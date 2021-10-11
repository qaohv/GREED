# ST-GREED: Space-Time Generalized Entropic Differences for Frame Rate Dependent Video Quality

### Background:

Set necessary libraries using following command:

```
pip3 install -r requirements.txt
```

### Score prediction

To predict scores for LIVE VQA dataset run following command:

```
make -f live-vqa-bench.make run
```

To predict scores for CSIQ dataset run following command:

```
make -f csiq-bench.make run
```

### SROCC calculation

To calculate SROCC score run following command:
```
python3 calculate_metrics.py --gt-csv <path-to-csv-with-gt> --predicted-scores-path <path-to-predicted scores>
```

For example:

```
python3 calculate_metrics.py --gt-csv csv/csiq-dmos.csv --predicted-scores-path csiq.log
```