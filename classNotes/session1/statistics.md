<p align="left">
  <a href="./readme.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./data.md"><b>Next →</b></a>
  </span>
</p>

---

# Statistics

Is a tool that will be used to perform computation on dataset inorder to get meaningful insights.

could be classified into two categories

| Descriptive statistics                    | Inferential statistics                        |
| :---------------------------------------- | :-------------------------------------------- |
| used to understand data                   | helps in making decisions                     |
| Refers to what is already happened        | Refers to what might/about to happen          |
| is more concerned with data summarization | talk about population parameter from a sample |

## Terminologies used in statistics

Before we go deep, lets imagine from a data perspective:
Lets call the data we have now as `dataNow`, can have any kind of data that has been already collected.
Now you want to apply some conclusion of this past data for my future events.
Note, the data that you have is only partly related with the future i.e. `futureData`

In machine learning, we deal with such things and this partly related data is called as `test data`

**Test Dataset** help us evaluate how well a model generalizes to new to unseen data, ensuring its effectiveness in the real world applications.

Yes future data is different from the data we have, but both are coming from same place.
Yeah you guessed right, this place is called the population.

1. **Population**: 
   - Is the universe of all possible data for a specified object i.e. sum of past, present, future data.<br>NOTE: Theoretically, it's possible to observe a full population at once, but not practically. <br>But due to the advancements in tech, we are now able to do deliberately observe population, e.g. census
   - Example: People who have visited or will visit my website

2. **Parameter**:
   - Is a numerical value that is associated with the population
   - What are we interested in the population
   - Example: The average amount of time people spend on my website.
   - Is this observed? No in the same way of population

3. **Sample**: 
   - Is a part(selected observations) of population
   - Example: People who visit a website on a specific day/date.
   - Yes this is observed. This is data, as you can do calculation on it.
   - But its doest not represents the whole population, its not we are interested into as it will not happen again.
**Estimates**: is a process of using sampling data to infer the unknown population parameters

4. **Statistic**
   - is a numerical value associated with an observed sample.
   - i.e. when you perform calculation on a sample, then such a sample is called statistic (without `s`)
   - Example: the average amount of time people spent on a website on a specific day.

So the statistical problem is to go from the observed to the non-observed, i.e. to go from the sample to the population, coz the object we are interested in is not the statistic but the parameter, as the universe we are interested in is the population.


This notion of a sample drawn from a population has defined the subject of statistics for many years. And this is being challenged even today, as we see something called big-data that appears to be a population, but not a sample, thus the idea of sampling may not make any sense in physical way.
But also keep in mind, even though you can see all your customer in big data that you have today, your results will still have to infer what this customer will be in future.

so even if you can see the entire population, that extraction of that will be to the elements that are still not in the population.

Thus if you are thinking you are working with the sample, betta think twice, as actual population might have changed while you end up cleaning/processing your data. Thus its considered good to think you dataset as a sample rather than a population.

---

## Need for statistics?

Statistics was invented to solve numerical problems like
- if i put this amount of fertilizer, what amount of yield, will i get.
- if the medicine improved the curing?

**Statistical Methods**:
Statistical Methods have been used to simply describe what we just saw.
These methods are now adapted to certain standards which are defined by events
Events, that has to do with technology development:
- social networks
- collection of automated data
- how computers do calculation
- storage of data
- processing of data

The **Design phase** in a project/experiment is most crucial for statistical planning.


## Big Data:

A set of data that cannot be managed, processed, or analyzed with traditional software/algorithm within a reasonable amount of time.

It revolves around:
- Volume
- Velocity
- Variety
- Value
- Veracity

e.g.: Walmart handles over 1 million purchase transaction per hour

---

<p align="left">
  <a href="./readme.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./data.md"><b>Next →</b></a>
  </span>
</p>
