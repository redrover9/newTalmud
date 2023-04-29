from textgenrnn import textgenrnn

t = textgenrnn()

t.train_from_largetext_file("gemara.txt", num_epochs=5)