# Frequent Pattern Mining

<p>
    <a href="https://www.python.org/downloads/release/python-3106/">
        <img src="https://img.shields.io/static/v1?label=python&style=flat-square&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48IS0tIFVwbG9hZGVkIHRvOiBTVkcgUmVwbywgd3d3LnN2Z3JlcG8uY29tLCBHZW5lcmF0b3I6IFNWRyBSZXBvIE1peGVyIFRvb2xzIC0tPgo8c3ZnIHdpZHRoPSI4MDBweCIgaGVpZ2h0PSI4MDBweCIgdmlld0JveD0iMCAwIDMyIDMyIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPg0KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xMy4wMTY0IDJDMTAuODE5MyAyIDkuMDM4MjUgMy43MjQ1MyA5LjAzODI1IDUuODUxODVWOC41MTg1MkgxNS45MjM1VjkuMjU5MjZINS45NzgxNEMzLjc4MTA3IDkuMjU5MjYgMiAxMC45ODM4IDIgMTMuMTExMUwyIDE4Ljg4ODlDMiAyMS4wMTYyIDMuNzgxMDcgMjIuNzQwNyA1Ljk3ODE0IDIyLjc0MDdIOC4yNzMyMlYxOS40ODE1QzguMjczMjIgMTcuMzU0MiAxMC4wNTQzIDE1LjYyOTYgMTIuMjUxNCAxNS42Mjk2SDE5LjU5NTZDMjEuNDU0NyAxNS42Mjk2IDIyLjk2MTcgMTQuMTcwNCAyMi45NjE3IDEyLjM3MDRWNS44NTE4NUMyMi45NjE3IDMuNzI0NTMgMjEuMTgwNyAyIDE4Ljk4MzYgMkgxMy4wMTY0Wk0xMi4wOTg0IDYuNzQwNzRDMTIuODU4OSA2Ljc0MDc0IDEzLjQ3NTQgNi4xNDM3OCAxMy40NzU0IDUuNDA3NDFDMTMuNDc1NCA0LjY3MTAzIDEyLjg1ODkgNC4wNzQwNyAxMi4wOTg0IDQuMDc0MDdDMTEuMzM3OCA0LjA3NDA3IDEwLjcyMTMgNC42NzEwMyAxMC43MjEzIDUuNDA3NDFDMTAuNzIxMyA2LjE0Mzc4IDExLjMzNzggNi43NDA3NCAxMi4wOTg0IDYuNzQwNzRaIiBmaWxsPSJ1cmwoI3BhaW50MF9saW5lYXJfODdfODIwNCkiLz4NCjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMTguOTgzNCAzMEMyMS4xODA1IDMwIDIyLjk2MTYgMjguMjc1NSAyMi45NjE2IDI2LjE0ODJWMjMuNDgxNUwxNi4wNzYzIDIzLjQ4MTVMMTYuMDc2MyAyMi43NDA4TDI2LjAyMTcgMjIuNzQwOEMyOC4yMTg4IDIyLjc0MDggMjkuOTk5OCAyMS4wMTYyIDI5Ljk5OTggMTguODg4OVYxMy4xMTExQzI5Ljk5OTggMTAuOTgzOCAyOC4yMTg4IDkuMjU5MjggMjYuMDIxNyA5LjI1OTI4TDIzLjcyNjYgOS4yNTkyOFYxMi41MTg1QzIzLjcyNjYgMTQuNjQ1OSAyMS45NDU1IDE2LjM3MDQgMTkuNzQ4NSAxNi4zNzA0TDEyLjQwNDIgMTYuMzcwNEMxMC41NDUxIDE2LjM3MDQgOS4wMzgwOSAxNy44Mjk2IDkuMDM4MDkgMTkuNjI5Nkw5LjAzODA5IDI2LjE0ODJDOS4wMzgwOSAyOC4yNzU1IDEwLjgxOTIgMzAgMTMuMDE2MiAzMEgxOC45ODM0Wk0xOS45MDE1IDI1LjI1OTNDMTkuMTQwOSAyNS4yNTkzIDE4LjUyNDQgMjUuODU2MiAxOC41MjQ0IDI2LjU5MjZDMTguNTI0NCAyNy4zMjkgMTkuMTQwOSAyNy45MjU5IDE5LjkwMTUgMjcuOTI1OUMyMC42NjIgMjcuOTI1OSAyMS4yNzg1IDI3LjMyOSAyMS4yNzg1IDI2LjU5MjZDMjEuMjc4NSAyNS44NTYyIDIwLjY2MiAyNS4yNTkzIDE5LjkwMTUgMjUuMjU5M1oiIGZpbGw9InVybCgjcGFpbnQxX2xpbmVhcl84N184MjA0KSIvPg0KPGRlZnM+DQo8bGluZWFyR3JhZGllbnQgaWQ9InBhaW50MF9saW5lYXJfODdfODIwNCIgeDE9IjEyLjQ4MDkiIHkxPSIyIiB4Mj0iMTIuNDgwOSIgeTI9IjIyLjc0MDciIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj4NCjxzdG9wIHN0b3AtY29sb3I9IiMzMjdFQkQiLz4NCjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzE1NjVBNyIvPg0KPC9saW5lYXJHcmFkaWVudD4NCjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQxX2xpbmVhcl84N184MjA0IiB4MT0iMTkuNTE5IiB5MT0iOS4yNTkyOCIgeDI9IjE5LjUxOSIgeTI9IjMwIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+DQo8c3RvcCBzdG9wLWNvbG9yPSIjRkZEQTRCIi8+DQo8c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNGOUM2MDAiLz4NCjwvbGluZWFyR3JhZGllbnQ+DQo8L2RlZnM+DQo8L3N2Zz4=&message=3.10.6&color=3776AB" />
    </a>
    <a>
        <img src="https://img.shields.io/static/v1?label=ubuntu&style=flat-square&logo=ubuntu&message=22.04.2&color=E95420" />
    </a>
</p>

## 1 The Data

The data consists of paper titles from conferences in computer science of 5 domains: ***Data Mining (DM)***, ***Machine
Learning (ML)***, ***Database (DB)***, ***Information Retrieval (IR)*** and ***Theory (TH)***. The raw data is available in
[paper_raw.txt](./paper_raw.txt). Each line contains two columns, `PaperID` and `Title` of a paper, separated by
`Tab(‘\t’)`. The `PaperID` is unique in the whole data set. However, since this data is a subset of all the paper titles
from a large corpus, `PaperID`s are not starting from 0 and not consecutive. The raw data looks like this:

| `PaperID` | `Title`                                           |
|:----------|:--------------------------------------------------|
| 7600      | The Automatic Acquisition of Proof Methods        |
| 85825     | Frequent pattern discovery with memory constraint | 

The raw data has been pre-processed by removing stop words, converting the words to lower cases and lemmatization. The
processed data is available in [paper.txt](./paper.txt). In this file, each line is a `PaperID` followed by a list of
terms. The format is `PaperID Tab(‘\t’) term1 Space(‘ ’) term2 Space(‘ ’) ...`. paper.txt looks like this:

| `PaperID` | `[term1] [term2] [term3] [term4] ... [termN]` |
|:----------|:----------------------------------------------|
| 7600      | automatic acquisition proof method            |
| 85825     | frequent pattern discovery memory constraint  |

We will be working on the pre-processed data in [paper.txt](./paper.txt).

## 2 Further Preprocessing

This step prepares input for LDA (Latent Dirichlet Allocation). Two files will be generated based on
[paper.txt](./paper.txt).

### 2.1 Generate Dictionary

First, generate a vocabulary from [paper.txt](./paper.txt). The vocabulary file will be names as ***vocab.txt***. Each
line in this file is a unique term extracted from [paper.txt](./paper.txt); each term should appear exactly once. Here
is an example of the first five lines in vocab.txt. Note that the sequence of terms may be different.

```text
automatic
acquisition
proof
method
philosophical
...
```

A sample can be found in [vocab.txt](./vocab.txt).

### 2.2 Tokenize Plain Text by Dictionary

In this step, each title is represented as a sparse vector of word counts. Each title is transformed (i.e., each line in
[paper.txt](./paper.txt)) into the following format (`[M] (space) [t1]:[c1] (space) [t2]:[c2] (space) ...`):
```text
[M] [term 1]:[count] [term 2]:[count] ... [term N]:[count]
```

where `[M]` is the number of unique terms in the title, and the `[count]` associated with each term is how many times
that term appeared in the title. For example, in [paper.txt](./paper.txt), suppose we have a title `“automatic
acquisition proof method”`. The corresponding line in the output file should be `“4 0:1 1:1 2:1 3:1”`. Note that
`[term_i]` is an integer which indexed a term in vocab.txt; it starts from `0`. The output file is named as
***title.txt***.

A sample available in [title.txt](./title.txt).

_Note: if you use any other lda package rather than the one mentioned in next step, please make sure the format in
title.txt match what your lda package requires._

## 3 Partitioning

Recall that paper titles were collected from conferences of 5 domains in computer science. If we run frequent pattern
mining algorithms directly on paper titles, the patterns would be independent of topics. Thus, if we want to mine
frequent patterns in each domain, titles and terms should be partitioned into 5 domains. Note that the domain knowledge
is not known to you. Instead, we apply topic modeling to uncover the hidden topics behind titles and terms
automatically. Specifically, we apply LDA to assign a topic to each term.

### 3.1 Assign a Topic to Each Term

1. Download the LDA package [here](http://www.cs.columbia.edu/~blei/lda-c/lda-c-dist.tgz). Unzip it, and you can see a
list of source code.
2. Open a terminal and go to the directory of the source code. Type `make`. An executable lda will be is generated.
3. In `lda-c-dist` directory, there is a `settings.txt` file. You could use the settings provided there, but feel free
to tune the parameters if you know how inference works for LDA.
    ```text
    var max iter 20
    var convergence 1e-6
    em max iter 100
    em convergence 1e-4
    alpha estimate
    ```
4. Run LDA with the following command:
    ```
    <dir>/lda-c-dist/lda est 0.001 5 <dir>/lda-c-dist/settings.txt <dir>/title.txt random <dir>/result
    ```
   where `<dir>` is your own working directory, and `0.001` is the prior for topic proportion (it is just a parameter,
   and you don’t have to change it if you don’t know how) given to LDA. `5` represents 5 topics. `title.txt` is the file
   you generate at [Step 2](#2-further-preprocessing). The output will be put into `result` directory (a sample can be
   found in [result/](./result)).
5. Check your output.

   In the `result` directory, open file `word-assignments.dat`. Each line is of the form (`[M] (space) [t1]:[k1] (space)
   [t2]:[k2] (space) ...`):
    ```
    [M] [term 1]:[topic] [term 2]:[topic] ... [term N]:[topic]
    ```
   where `[M]` is the number of unique terms in the title, and `[topic]` associated with each term is the topic assigned
   to it. Topic number starts from `0`. One line could be: `004 0000:02 0003:02 0001:02 0002:02`; which means that all
   terms in this title are assigned to the 3rd topic (topic 02). Note that you are not confined to use this package.
   Here is another option: [Topic Modeling | Mallet](http://mallet.cs.umass.edu/topics.php).

   A sample is available in [result/word-assignments.dat](./result/word-assignments.dat).

### 3.2 Re-organize the Terms by Topic

You are asked to re-organize the terms by 5 topics. For the i-th topic, you should create a file named ***topic-i.txt***.
Separate each line in `word-assignment.dat` by topics assigned to them. For example, the lines in `word-assignment.dat`
can be considered as the following form (Note that here we replace the integers with the real terms for better
illustration):
```text
004 automatic:02 acquisition:02 proof:02 method:02
005 classification:03 noun:02 phrase:03 concept:01 individual:03
```
Then your output files would be:

_topic-0.txt_
```text
...
```

_topic-1.txt_
```text
concept
...
```

_topic-2.txt_
```text
automatic acquisition proof method
noun
...
```

_topic-3.txt_
```text
classification phrase individual
...
```

In the real files, each term should be represented as the id corresponding to the dictionary generated from Step 2
(e.g., `0001`, `0056`). ***topic-i.txt*** looks like this:
```text
[term1] [term2] ... [termN]
[term1] [term2] ... [termN]
...
```

See samples: [topic-0.txt](./topic-0.txt), [topic-1.txt](./topic-1.txt), [topic-2.txt](./topic-2.txt),
[topic-3.txt](./topic-3.txt), [topic-4.txt](./topic-4.txt).

## 4 Mining Frequent Patterns for Each Topic

In this step, the frequent pattern mining algorithm, _Apriori Algorithm_ is implemented. The algorithm will be run on 5
files corresponding to 5 topics. The output is of the form (`[s] (space) [t1 (space) t2 (space) t3 (space) ...]`), where
each term should be represented as the term id:
```text
#Support [frequent pattern]
#Support [frequent pattern]
...
```
The frequent patterns are sorted from high to low by `#Support`. The output files is to be put into a directory named as
`patterns`. The i-th file is named as `pattern-i.txt`.

The `min_sup` for a frequent pattern was chosen to be `1%` (or `0.01`) as it was the largest value which gave a decent
amount of patterns per topic (∼ 70 patterns on average), and patterns with at least 3 items were present (you may choose
your own).

Samples present in [patterns/](./patterns).

## 5 Mining Maximal / Closed Patterns

In this step, you need to implement an algorithm to mine maximal patterns and closed patterns. You could write the code
based on the output of Step 4, or implement a specific algorithm to mine maximal/closed patterns, such as `CLOSET`,
`MaxMiner`, etc.

The output should be of the same form as the output of [Step 4](#4-mining-frequent-patterns-for-each-topic). Max
patterns are put into ***max*** directory. The i-th file is named as ***max-i.txt***. Closed patterns are put into
***closed*** directory. The i-th file is named as ***closed-i.txt***.

View samples for max patterns and closed patterns in [max/](./max) and [closed/](./closed) respectively.

## 6 Re-rank by Purity of Patterns

In this implementation _Purity_ is introduced as one of the ranking measures for phrases. A phrase is _pure_ in topic
_t if it is only frequent in documents (here documents refer to titles) about topic _t_ and not frequent in documents
about other topics. For example, ‘`query processing`’ is a more _pure_ phrase than ‘`query`’ in the `Database` topic.
We measure the purity of a pattern by comparing the probability of seeing a phrase in the topic-$t$ collection $D(t)$
and the probability of seeing it in any other topic-$t′$ collection ($t′ = 1, ..., k, t′ \neq t$). In our case, $k = 4$.
Purity essentially measures the distinctness of a pattern in one topic compared to that in any other topic. The
definition is as follows:

```math
purity(p, t) = \log_2[f(t, p) / |D(t)|] − \log_2(max[(f(t, p) + f (t′, p)) / |D(t, t′)|])
```

Here $f(t, p)$ is the frequency of pattern $p$ appearing in topic $t$ (i.e., support of $p$ in topic-t.txt). We define
$D(t)$ to be the collection of documents where there is at least one word being assigned the topic $t$. $D(t)$ =
{ $d$ |topic $t$ is assigned to at least one word in $d$ }. $D(t, t′)$ is the union of $D(t)$ and $D(t′)$.
$| ∗ |$ measures the size of a set. Actually $|D(t)|$ is exactly the number of lines in topic-i.txt. But note that
$|D(t, t′)| \neq |D(t)| + |D(t′)|$
.
Re-rank the patterns obtained from [Step 4](#4-mining-frequent-patterns-for-each-topic). The output should be of the
form:
```text
Purity [frequent pattern]
Purity [frequent pattern]
...
```
and frequent patterns are sorted from high to low by a measure which combines Support and Purity (you will need to come
up with how to combine them). Your output files should be put into one directory named as ***purity***. The i-th file is
named as ***purity-i.txt***.

For this implementation, the patterns were re-ranked based on the score generated as follows:
```math
score(support, purity) = support * \sigma(purity)
```
where $\sigma(x)$ is the sigmoid function, defined as
```math
\sigma(x) = \frac{1}{1 + e^{-x}}
```
This was done so that the purity values were squashed to a value in the range $(0, 1)$ and were scaled based on the
support of the pattern.

You can see the samples in [purity/](./purity).

## 7 Mapping Term ID Numbers to Terms from the Vocabulary

This mapping step helps you to examine the quality of the mined patterns and see if they make sense in terms of forming
phrases.

For every file in ***patterns*** / ***max*** / ***closed*** / ***purity***, map the id numbers to terms based on your
dictionary. Use the same format with the only difference that each integer is replaced by a term, name each new file as
***originalFileName.phrase*** and put it in the same directory as the original file. For example, ***pattern-0.txt***
will be mapped to ***pattern-0.txt.phrase*** and it will be put in the directory ***patterns***.
