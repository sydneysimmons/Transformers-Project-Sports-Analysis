# Sports Analysis Transformer Project
### Sydney Simmons, Cameron Rondeau, Donald Kane
### Overview
**Context:** For people interested in sports, there are many sporting events and seasons happening at one time. We wanted to use Transformers to build models that would help people aggregate information quickly for any sport event.

**Approach:** We wanted to use Transformers to not only give users a summary of a sporting event that they are interested in, but also allow them to ask questions about an event and get quick statistics. Therefore, we researched the Transformer pipelines to see which would be applicable to our idea and applied 3 of the them: 
1. Summarization Pipeline
2. Question Answering
3. Table Question Answering

**Testing:** We tested our models to start on data and articles from the 2022 Superbowl. Initially, we thought that summarization and questions answering would be an effective model to derive a summarization and key statistics for a sporting event. However, we realized that table question answering was far more accurate than question answering from a news article. We tested questions between question answering and table question answer for the same sporting event and while we left both pipelines in our interactive space, we would focus on table question answering and summarization going forward. 

**Potential Use Cases:** Our models could be used for the average sport enthusiast up to a sports commentator that needs a quick summary or information that happened in a sporting event. It could even be used for someone who does not like sports and needs a quick talking point for a game they didnt watch! Instead of reading an entire article or researching statistics about a game in depth, a user can link an article or a table to our Transformer tools and quickly see what happened in a game. 

### Link to Hugging Spaces - Interactive Sites

### Critical Analysis
**Next Steps:**
With more time, we would love to test our model on many sporting events and see how it performs across sports and different types of articles. We could put together a more extensive dataset with articles and tables from many different events. We could also develop summaries and answers to questions that we could use to derive metrics for how accurate our model is (ex. ROUGE for summarization). While we have a good idea of what summary is better from reading articles and we know answers to the questions we are asking, a future goal would be to formalize the metrics for our model's performance. 

**Limitation/Revelations from the Project:**
With summarization and question answering, we ran into limitations on the number of inputs into the model. We could not use the entire news article and this particularly impacted question answering because not all of the stats or the answers to the questions that we wanted were in the first few paragraphs of the article. This limitation led us to ultimately using the table question answering pipeline instead of using news articles. 

We also realized that using multiple pipelines on similar data can overcome limitations by allowing us to get different outputs on the same event and understand what is working and what is not.

### Resource Links
While we did not use SportsBERT because it was not applicable to our pipeline tasks, it was helpful to see a trained model on sports data.
https://huggingface.co/microsoft/SportsBERT

In depth article on other machine learning research occurring in sports:<br />
Performance & Recruitment<br />
https://www.frontiersin.org/articles/10.3389/fspor.2021.682287/full

Athlete Injuries<br />
https://sportsmedicine-open.springeropen.com/articles/10.1186/s40798-022-00465-4

Pipeline & Model Documentation Used For Project<br />
Models sorted by specific tasks<br />
https://huggingface.co/models?sort=downloads 

https://huggingface.co/docs/transformers/main_classes/pipelines

