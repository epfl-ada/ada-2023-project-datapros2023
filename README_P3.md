# Box Office Breakdown: Unraveling the Secrets of Cinema's Financial Success
## Datastory

Join our [meeting](https://rpythoud.github.io/datapros2023/) today at BlockBuster Inc. as we unveil our plan to stack the odds in our favor and head to the direction of the most profitable movie of all time !  
## Motivation

Unlike the other arts, cinema stands at a peculiar position between art and industry. Ever since the studio system had been set up and the Golden Age of Hollywood begun, moviemaking inadvertedly shifted towards money-making [1]. Today, it is a multi-billion dollar business.

_It is a very complex question with a lot of variables_, says Alyosha, our friend who is a film director based in Berlin. _Really, predicting a move's box office success seems like an impossible task._

But let us now attempt the impossible and try to figure out how to make money in Hollywood.

## Abstract

The purpose of this project is to investigate and uncover hidden factors contributing to a movie's financial success. To do so, We will approach this question from different angles. Firstly, we will examine direct movie attributes such as genre, runtime, release date, country of origin, and language. Secondly, through textual analysis of movie summaries, we aim to identify key themes, emotions, and narrative elements that may influence box office performance. Thirdly, we will analyze the impact of actors on individual movie successes by modeling their fame and prominence. Fourthly, we will investigate hypotheses regarding the influence of cast diversity and the role of gender on box office returns. Finally, we will try to detect and interpret trend shifts in the industry by looking at the overall picture.

## Research questions

1. **Does the gender of the character has, or have had, a signifiacante impact on the performance of a movie, either in rating or box office ?** Look at the character and gender, relate it to the rating or the box office to look at the evolution of gender diversity in the most succesfull movies and try to gauge correlations.

2. **How does the fame of actors relate to the movie’s box office success?** Try to model actor's fame as a new feature and use this metric to predict box office success.

3. **Is there a way to relate movies' motives and topics to their box office revenue?** By employing LDA topic modelling on film summaries, coherent clusters of common plot ideas can be extracted. These ideas do not correspond one-to-one to the film genre, though some correlation is to be expected.

4. **Are there discernible trend shifts in factors influencing box office success, and can they be explained?** 

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

**2. Investigation of actors specific informations and prominence**

- **A.** Process and analyze each actor’s data to calculate a 'Fame Score' for each actor, according to their career span, mean revenue, weighted mean rating and number of movies they starred in. This did not end in a single feature, but lead to investigation of relation in revenue and actor informations.

- **B.** Construct different regression between actor feature and the revenue and rating of movies.

- **C.** Explore actor gender representation and it's relation with the box office and the rating of a movie.

**3. How do movies' motives relate to the revenue?**

- **A.** Extract words by their POS. Only nouns, verbs, adjectives and adverbs carry useful information.

- **B.** Model topics by LDA algorithm. Fine-tune the parameters to get the most informative classification and interpret it.

- **C.** Explore the properties of the topics and establish their influence on the revenue.

## Executed timeline

24/11 :
- Investigated potential implementation of the fame score. Dropped features.
- Planning ahead.

01/12 :
- Brainstorming on the data story setup and idea.
- Start of the analysis and plotting related to genre, gender and actor factors.
- Working on LDA algorithm.

08/12 :
- Creation of the website.
- Creating of website ready plot and story coherent developpement.
- First results with the LDA algorithm.
- Adding regression to plot for a better presentation on the website.

15/12 :
- Introduction of the story on the website and general developpement.
- Creation of animated graphs designed for website.
- Answering some more hypothesis related to actor experience.
- Investigation and analysis with the new results from LDA.

22/12:
- Finalising story.
- Cleaning and clearing code.
- Fusing personal notebook into the final notebook.
- Updating the previous READ.ME

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
    <td>1. Analyzed the box office depending on genres, movie languages, country of initial release, runtime and release date.<br>
    2. Analyzed the correlation of movies financial successes and their ratings<br> 
    3. Generated interactive plots with buttons using Plotly when relevant to split depending on genre.
    </td>
  </tr>
  <tr>
    <td style="text-align: center;">Dusan</td>
    <td>1. Processed the movie summaries using NLP<br>
    2. Extracted topic, motives and main emotions from the summaries processing<br>
    3. Inspected possible influences of story features to the movie box office<br>
    4. Contacted friends in the film industry (directors/DPs/procucers) for further insights.
    </td>
  </tr>
  <tr>
    <td style="text-align: center;">Gilles</td>
    <td>1. Studied the overall impact of gender, cast diversity on the box office<br>
    2. Considered and assessed ethical questions regarding cast diversity and box office revenues<br>
    3. Analyse the tendencies throught time and the recent evolution of gender representation.<br>
    4. Assisted with the story concept and the website.<br>
    5. Assisted other group memmber in plotting and story developpement.
    </td>
  </tr>
  <tr>
    <td style="text-align: center;">Marko</td>
    <td>1. Generated a new feature called "actor prominence", derived from indirect measurables such as the actor's industry longevity, filmography volumes, and prior box office performances. This is a scrapped feature. <br>
    2. Analyzed the shifts in roles of main actors over their carreer span.<br>
    3. Studied the influence of main actors prominence and box office success.
</td>
  </tr>
  <tr>
    <td style="text-align: center;">Romain</td>
    <td>1. Supplemented the main dataset with movie ratings.<br>
    2. Adjusted box office revenues for inflation<br>
    3. Studied the trend of the box office over the years. <br>
    4. Created the Website and major part in the story writing<br>
    5. Assisted other member in the realisation of intereactive plots and regressions.
    </td>
  </tr>
</tbody>
</table>


## References
[1] David A. Cook, _A History of Narrative Film_, 5th edition, W. W. Norton & Company, 2016. [link](https://ia601805.us.archive.org/15/items/a-history-of-narrative-film-by-david-a.-cook/A%20History%20of%20Narrative%20Film%20by%20David%20A.%20Cook.pdf)
