# We're gonna be rich (motherfuckers)!

## Motivation

Unlike the other arts, cinema stands at a peculiar position between art and industry. Ever since the studio system had been set up and the Golden Age of Hollywood begun, moviemaking inadvertedly shifted towards money-making [1]. Today, it is a multi-billion dollar business.

_It is a very complex question with a lot of variables_, says Alyosha, our friend who is a film director based in Berlin. _Really, predicting a move's box office success seems like an impossible task._

But let us now attempt the impossible and try to figure out how to make money in Hollywood.

## Abstract

In this project, a relation of various film characteristics to its

## Research questions

3. **Is there a way to relate movies' motives and topics to their box office revenue?** By employing LDA topic modelling on film summaries, coherent clusters of common plot ideas can be extracted. These extracted topics do not correspond one-to-one to the film genre, though some correlation is to be expected.


## Additional datasets
- **IMDb Datasets**: 
In order to perform a deeper analysis of the Box Office, we will require more features than the financial revenues of a film. In particular, we would like to supplement the CMU Movie Corpus Dataset with the given ratings for each movie. This will gives us an additional feature related to the public perception of a film's success. The additional dataset should be sufficiently exhaustive as to include as much corresponding ratings to each film of the main dataset. With this in mind, we decided to use a subset of the IMDb Movie Dataset, namely the title.akas.tsv, title.basics.tsv and title.ratings.tsv datasets.

The merging of the 

- **Inflation data**:

## Methods


**3. How do movies' motives relate to the revenue?**

- **A.** Extract words by their POS. Not everything is useful - only nouns, verbs, adjectives and adverbs should carry the most information.

- **B.** Model topics by LDA algorithm. Fine-tune the parameters to get the most informative classification. The interpretation of the topics is a qualitative and subjective task, and must be done in multiple iterations.

- **C.** Explore the properties of the topics and establish their influence on the revenue.

## Proposed timeline


## Organization within team

<table style="table-layout: fixed; width: 600px">
<colgroup>
<col style="width: 40px">
<col style="width: 200px">
</colgroup>
<thead>
  <tr>
    <th style="text-align: center;">Teammate</th>
    <th style="text-align: center;">Tasks</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td style="text-align: center;">Adam</td>
    <td>1. Analyze the box office depending on genres, movie languages, country of initial release, runtime and release date.<br>
    2. Analyze the correlation of movies financial successes and their ratings<br>
    3. (Fake) Generate interactive plots with buttons using Plotly when relevant
    </td>
  </tr>
  <tr>
    <td style="text-align: center;">Dusan</td>
    <td>1. Process the movie summaries using NLP<br>
    2. Extract topic, motives and main emotions from the summaries processing<br>
    3. Inspect possible influences of story features to the movie box office<br>
    4. Contact friends in the film industry (directors/DPs/procucers) for further insights
    </td>
  </tr>
  <tr>
    <td style="text-align: center;">Gilles</td>
    <td>1. Study the impact of gender, cast diversity on the box office<br>
    2. Expose and assess ethical questions regarding cast diversity and box office revenues<br>
    3. (Fake) Build html backend and web interface for the Data story
    </td>
  </tr>
  <tr>
    <td style="text-align: center;">Marko</td>
    <td>1. Generate a new feature called "actor prominence", derived from indirect measurables such as the actor's industry longevity, filmography volumes, and prior box office performances. <br>
    2. Analyze the shifts in roles of main actors over their carreer span.<br>
    3. Study the influence of main actors prominence and box office success
</td>
  </tr>
  <tr>
    <td style="text-align: center;">Romain</td>
    <td>1. Supplement the main dataset with movie ratings.<br>
    2. Adjust box office revenues for inflation<br>
    3. Study the trend of the box office over the years. <br>
    4. Detect cycles and sudden changes in trend shifts for the box office, cast diversity and movie genres over the years.<br>
    5. Find plausible explanations for trend shifts such as financial crisis, wars or technological disruptions.
    </td>
  </tr>
</tbody>
</table>

[1] David A. Cook, _A History of Narrative Film_, 5th edition, W. W. Norton & Company, 2016. [link](https://ia601805.us.archive.org/15/items/a-history-of-narrative-film-by-david-a.-cook/A%20History%20of%20Narrative%20Film%20by%20David%20A.%20Cook.pdf)