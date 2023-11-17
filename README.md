# Box Office Breakdown: Unraveling the Secrets of Cinema's Financial Success

## Motivation

Unlike the other arts, cinema stands at a peculiar position between art and industry. Ever since the studio system had been set up and the Golden Age of Hollywood begun, moviemaking inadvertedly shifted towards money-making [1]. Today, it is a multi-billion dollar business.

_It is a very complex question with a lot of variables_, says Alyosha, our friend who is a film director based in Berlin. _Really, predicting a move's box office success seems like an impossible task._

But let us now attempt the impossible and try to figure out how to make money in Hollywood.

## Abstract

The purpose of this project is to investigate and uncover hidden factors contributing to a movie's financial success. To do so, We will approach this question from different angles. Firstly, we will examine direct movie attributes such as genre, runtime, release date, country of origin, and language. Secondly, through textual analysis of movie summaries, we aim to identify key themes, emotions, and narrative elements that may influence box office performance. Thirdly, we will analyze the impact of actors on individual movie successes by modeling their fame and prominence. Fourthly, we will investigate hypotheses regarding the influence of cast diversity and the role of gender on box office returns. Finally, we will try to detect and interpret trend shifts in the industry by looking at the overall picture.

## Research questions

2. **Does the gender of the character has, or have had, a signifiacante impact on the performance of a movie, either in rating or box office ?** Look at the character and gender, relate it to the rating or the box office to look at the evolution of gender diversity in the most succesfull movies and try to gauge correlations.

3. **How does the fame of actors relate to the movie’s box office success?** Try to model actor's fame as a new feature and use this metric to predict box office success.

4. **Is there a way to relate movies' motives and topics to their box office revenue?** By employing LDA topic modelling on film summaries, coherent clusters of common plot ideas can be extracted. These ideas do not correspond one-to-one to the film genre, though some correlation is to be expected.



## Additional datasets
- **IMDb Datasets**: 
This external dataset is used to supplement the CMU Movie Corpus Dataset with ratings. Only subsets of the IMDb Movie Dataset are used, namely the title.akas.tsv, title.basics.tsv and title.ratings.tsv datasets.

- **CPI Inflation data**:
The python module cpi is used to adjust box office revenues for inflation with the CPI historical data. The origin of the data comes from the US Bureau of Labor Statistics (BLS).

## Methods

**1. Data loading and pre-processing**
- **A.** Load and merge the data into two main pandas dataframes: movies and characters_movies. 

- **B.** Supplement the data with the ratings from the IMDb dataset and merge with the main dataframes. Adjust the box office revenues for inflation with the CPI historical data.

- **C.** Make sure each column of the dataframe has a uniform data type.

**2. Modeling actors fame and prominence**

- **A.** Process and analyze each actor’s data to calculate a 'Fame Score' for each actor, according to their career span, mean revenue, weighted mean rating and number of movies they starred in.

- **B.** Construct a regression model to find optimal weights for determining the ‘Fame score’ .

- **C.** Explore the relation between the fame score of the cast and movie box office success.

**3. How do movies' motives relate to the revenue?**

- **A.** Extract words by their POS. Only nouns, verbs, adjectives and adverbs carry useful information.

- **B.** Model topics by LDA algorithm. Fine-tune the parameters to get the most informative classification and interpret it.

- **C.** Explore the properties of the topics and establish their influence on the revenue.

## Proposed timeline

24/11 :
- Actor fame score done.
- LDA algorithm in progress.
- Overview plot ready.

01/12 :
- Progress/done the LDA.
- Analysis of actor prominence. 
- Setup for hypothesis testing.

08/12 :
- LDA algorithm done.
- Finishing hypothesis testing.
- Starting website.

15/12 :
- Hypothesis analysis regarding gender and diversity.
- Hard progress on the website.
- Starting the final README.md.

22/12:
- Website done, story done.
- README.md done.
- Clearing up the Notebook.
- Getting in the Christmas mood. (Very important)

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
    3. Generate interactive plots with buttons using Plotly when relevant
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
    <td>1. Study the overall impact of gender, cast diversity on the box office<br>
    2. Consider and assess ethical questions regarding cast diversity and box office revenues<br>
    3. Analyse whether certain genres are more sensible to gender representation and has a bigger impact in box office.<br>
    4. Build html backend and web interface for the Data story
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

## References
[1] David A. Cook, _A History of Narrative Film_, 5th edition, W. W. Norton & Company, 2016. [link](https://ia601805.us.archive.org/15/items/a-history-of-narrative-film-by-david-a.-cook/A%20History%20of%20Narrative%20Film%20by%20David%20A.%20Cook.pdf)