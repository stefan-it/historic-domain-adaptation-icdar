from flair.datasets import ColumnCorpus

column_format = {0: "token", 1: "ner"}

train_file = "train.txt"
dev_file = "dev.txt"
test_file = "test.txt"

gold_stats = {
    "fr": {
        "train": 7936,
        "dev": 992,
        "test": 992
    },
    "nl": {
        "train": 5777,
        "dev": 722,
        "test": 723
    }
}

def check_sentences(reference: int, actual: int, split_name: str):
    assert actual == reference, f"Mismatch in number of sentences for {split_name} split"

for language in ["fr", "nl"]:
    data_folder = f"./data/{language}"

    corpus = ColumnCorpus(data_folder=data_folder,
                          column_format=column_format,
                          train_file=train_file,
                          dev_file=dev_file,
                          test_file=test_file,
                          comment_symbol="# ",
                          column_delimiter="\t"
                        )
    print(f"Stats for language: {language}:")
    print(corpus)

    check_sentences(len(corpus.train), gold_stats[language]["train"], "train")
    check_sentences(len(corpus.dev), gold_stats[language]["dev"], "dev")
    check_sentences(len(corpus.test), gold_stats[language]["test"], "test")
