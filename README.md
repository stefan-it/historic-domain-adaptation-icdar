# Data Centric Domain Adaptation for Historical Text with OCR Errors

This repository contains code and datasets that are used in our paper
["Data Centric Domain Adaptation for Historical Text with OCR Errors"](https://arxiv.org/abs/2107.00927) (Preprint)
by Luisa März, Stefan Schweter, Nina Poerner, Benjamin Roth and Hinrich Schütze.

# Changelog

* 07.12.2021: Release of French and Dutch data used for our experiments.

* 16.07.2021: Initial version of this repo.

# Datasets

The data used for our experiments can be found in the `data` folder of this repository.

# Stats

The following table shows an overview of the corpus stats for each language:

| Language | Training Sentences | Development Sentences | Test Sentences
| -------- | -----------------: | --------------------: | -------------:
| French   | 7,936              | 992                   | 992
| Dutch    | 5,777              | 722                   | 723

These stats can be calculated with the `flair_stats.py` script using Flair (commit: `7578403`).

# Code

Code for training our models will be released in near future.
