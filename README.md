# Pykov
A markov chain implemntation for text generation made in python 3

## Use
Enter your source text in the "text" variable. If you wish, you can easily read in text through a file instead.

You will get more "coherent" text the higher you make the number associated with the "order" variable. I find that 5 is a good balance for medium sized texts. For larger texts (like books for example), you may have better results with order 10 n-grams.

As well you can edit the constant integer in line 7. That number is the amount of characters the markov() function will output.

Happy chaining!
