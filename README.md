# Sports Analysis Transformer Project
### Sydney Simmons, Cameron Rondeau, Donald Kane
### Overview
**Context:** For people interested in sports, there are many sporting events and seasons happening at one time. We wanted to use Transformers to build models that would help people aggregate information quickly for any sport event.

**Approach:** We wanted to use Transformers to not only give users a summary of a sporting event that they are interested in, but also allow them to ask questions about an event and get quick statistics. Therefore, we researched the Transformer pipelines to see which would be applicable to our idea and applied 3 of the them: 
1. Summarization Pipeline
2. Question Answering Pipeline
3. Table Question Answering Pipeline

**Testing:** We tested our models to start on data and articles from the 2022 Superbowl. Initially, we thought that summarization and question answering would be effective pipelines to derive a summarization and answer questions on key statistics for a sporting event. However, we realized that table question answering was far more accurate than question answering from a news article. We tested questions between question answering and table question answering for the same sporting event and while we left both pipelines in our interactive space, we would focus on table question answering and summarization going forward. 

**Potential Use Cases:** Our models could be used for the average sport enthusiast up to a sports commentator that needs a quick summary or information that happened in a sporting event. It could even be used for someone who does not like sports and needs a quick talking point for a game they didnt watch! Instead of reading an entire article or researching statistics about a game in depth, a user can link an article or a table to our Transformer tools and quickly see what happened in a game. 

### [Link to Hugging Spaces - Interactive Sites](https://huggingface.co/spaces/camerondeau/Sports_Transformers_Analysis)

### Question Answering
#### Comparing the same questions across multiple articles.

| Question                                   | Correct Answer             | Article 1                                 | Article 2        | Article 3           |
|--------------------------------------------|----------------------------|-------------------------------------------|------------------|---------------------|
| Where was the 2022 Super Bowl?             | Los Angeles / SoFi Stadium | Los Angeles                               | SoFi Stadium     | SoFi Stadium        |
| What team won the 2022 Super Bowl?         | Los Angeles Rams           | Rams                                      | Los Angeles Rams | The Rams            |
| What was the score of the 2022 Super Bowl? | 23-20                      | 23-20                                     | 38               | 23-20               |
| Who scored the first touchdown?            | Odell Beckham Jr.          | Ernest Jones                              | Ja'Marr Chase    | Odell Beckham Jr.   |
| How many yards did Cooper Kupp have?       | 92                         | 39                                        | 92               | 92                  |
| How many passes did Burrow complete?       | 22 of 33                   | seven                                     | 46               | 22 of 33            |
| How many yards did Burrow have?            | Cooper Kupp                | Kupp                                      | Cooper Kupp      | Donald              |
| Why did the Rams win?                      |                            | Their defense laying siege to the Bengals | their families   | That defensive line |


#### Comparing different wording of questions for one article.

| Question                                | Answer           |
|-----------------------------------------|------------------|
| What team won?                          | Los Angeles Rams |
| What team won the Super Bowl?           | Tennessee Titans |
| What team won the 2022 Super Bowl?      | The Rams         |
| What team lost?                         | Los Angeles Rams |
| What team lost the 2022 Super Bowl?     | Bengals          |
| How many completions did Stafford have? | two decades      |
| How many passes did Stafford complete?  | 26 of 40         |

### TaPaS


### Critical Analysis
**Next Steps:**
With more time, we would love to test our model on many sporting events and see how it performs across sports and different types of articles. We could put together a more extensive dataset with articles and tables from many different events. We could also develop summaries and answers to questions that we could use to derive metrics for how accurate our model is (ex. ROUGE for summarization). While we have a good idea of what summary is better from reading articles and we know answers to the questions we are asking, a future goal would be to formalize the metrics for our model's performance. 

**Limitation/Revelations from the Project:**
With summarization and question answering, we ran into limitations on the number of inputs into the model. We could not use the entire news article and this particularly impacted question answering because not all of the stats or the answers to the questions that we wanted were in the first few paragraphs of the article. This limitation led us to ultimately using the table question answering pipeline instead of using news articles. 

We also realized that using multiple pipelines on similar data can overcome limitations by allowing us to get different outputs on the same event and understand what is working and what is not.

### Result Screenshots 
**US World Cup Game**
<img width="1545" alt="Screen Shot 2022-12-06 at 5 54 38 PM" src="https://user-images.githubusercontent.com/89158606/206051222-7da3b2c8-5728-45db-976c-512c4f816db3.png">

**2022 Superbowl**
<img width="1548" alt="Screen Shot 2022-12-06 at 5 56 14 PM" src="https://user-images.githubusercontent.com/89158606/206051392-cd8469a1-d8b5-424b-a3ea-1112f0eb051b.png">

### Resource Links
While we did not use SportsBERT because it was not applicable to our pipeline tasks, it was helpful to see a trained model on sports data.
https://huggingface.co/microsoft/SportsBERT

In depth article on other machine learning research occurring in sports:<br />
Performance & Recruitment<br />
https://www.frontiersin.org/art![Uploading Screen Shot 2022-12-06 at 5.52.59 PM.png…]()
icles/10.3389/fspor.2021.682287/full

Athlete Injuries<br />
https://sportsmedicine-open.springeropen.com/articles/10.1186/s40798-022-00465-4

Pipeline & Model Documentation Used For Project<br />
Models sorted by specific tasks<br />
https://huggingface.co/models?sort=downloads 

Descriptions of pipelines that we used<br />
https://huggingface.co/docs/transformers/main_classes/pipelines

TaPas: Weakly Supervised Table Parsing via Pre-training (Herzig et al., ACL 2020) />
https://aclanthology.org/2020.acl-main.398.pdf
