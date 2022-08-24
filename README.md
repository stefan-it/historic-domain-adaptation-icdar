# Data Centric Domain Adaptation for Historical Text with OCR Errors

This repository contains code and datasets that are used in our paper
["Data Centric Domain Adaptation for Historical Text with OCR Errors"](https://link.springer.com/chapter/10.1007/978-3-030-86331-9_48)
by Luisa März, Stefan Schweter, Nina Poerner, Benjamin Roth and Hinrich Schütze. The publicly accessible preprint can be found
[here](https://arxiv.org/abs/2107.00927).

# Changelog

* 24.08.2022: Add license and instructions to use the datasets in Flair.
* 14.08.2022: Mention corpus stats for French and Dutch. Add BibTeX entry.
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

# Usage in Flair

With latest Flair master branch, native support for our released datasets [was added](https://github.com/flairNLP/flair/pull/2911).
It is possible to load our datasets with the following lines of code:

```python
from flair.datasets import NER_ICDAR_EUROPEANA

french_corpus = NER_ICDAR_EUROPEANA(language="fr")
dutch_corpus  = NER_ICDAR_EUROPEANA(language="nl")
```

# License

We release the data under CC0 1.0 Universal (CC0 1.0) license (Same license as used for [Europeana NER Corpora](https://github.com/EuropeanaNewspapers/ner-corpora)).

# Citation

You can use the following BibTeX entry for citing our paper/data:

```bibtex
@InProceedings{10.1007/978-3-030-86331-9_48,
    author="M{\"a}rz, Luisa
    and Schweter, Stefan
    and Poerner, Nina
    and Roth, Benjamin
    and Sch{\"u}tze, Hinrich",
    editor="Llad{\'o}s, Josep
    and Lopresti, Daniel
    and Uchida, Seiichi",
    title="Data Centric Domain Adaptation for Historical Text with OCR Errors",
    booktitle="Document Analysis and Recognition -- ICDAR 2021",
    year="2021",
    publisher="Springer International Publishing",
    address="Cham",
    pages="748--761",
    abstract="We propose new methods for in-domain and cross-domain Named Entity Recognition (NER) on historical data for Dutch and French. For the cross-domain case, we address domain shift by integrating unsupervised in-domain data via contextualized string embeddings; and OCR errors by injecting synthetic OCR errors into the source domain and address data centric domain adaptation. We propose a general approach to imitate OCR errors in arbitrary input data. Our cross-domain as well as our in-domain results outperform several strong baselines and establish state-of-the-art results. We publish preprocessed versions of the French and Dutch Europeana NER corpora.",
    isbn="978-3-030-86331-9"
}
```