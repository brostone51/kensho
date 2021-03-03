# kensho

As of my push at ~7:30, it parses through the pages super well and arrives at results pretty quickly, even in my VM where the process is a bit limited.
However, the results aren't matching what the wikipedia page says should happen. Something is likely to be wrong with my `get_first_anchor` function.

### update

Was able to make it better, but only somewhat. There seems to be something wrong with my link finding function, but I'm not sure what. According to the sample pages I am actually viewing, it should be accurately grabbing the first link from the page. But based on the ratio I'm seeing in outuput, either this article is no longer true or something is up.

At any rate, I am pretty much out of time here. I wish I could figure out why I'm getting the wrong link, but it still succesffuly parses the link chains and does some pruning when it knows it going to fail.

Here is a sample output:

```text

```
