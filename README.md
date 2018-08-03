# DataAnalyticsPipeline
Dev days lab for data analytics via Topic Modelling and Sentiment Analysis

## Introduction:
In this lab ,we are focussed on data analysis using a Data Pipeline .  

For building an effective data analytics pipeline , it is important to focus on the following :
1. Help ingest data easily from multiple sources.
2. Analyze it for completeness and accuracy.
3. Use it for metrics computations.
4. Store the data assets and scale as they grow rapidly without causing disruptions.
5. Adapt to changes as they happen.
6. Have a relatively short development cycle that is repeatable and easy to implement.


From an architecture standpoint ,usually the first step would be to ingest the data in a data lake.
A data lake is a repository that holds a large amount of raw data in its native (structured or unstructured) format until the data is needed. Storing data in its native format enables you to accommodate any future schema requirements or design changes.

This lab walks the audience through two processes:
1. Process of topic modeling using Amazon Comprehend using a combination of AWS Console and “Cloud9”. While the recommendation   is to use at least 1,000 documents for a topic modeling job, for the purposes of this lab we will use a sample set of five documents.  The sample documents consist of a subset of research and education material available from ResMed website (www.resmed.com).
2. Serverless Process of sentiment analysis using Amazon Comprehend ,S3 and Quicksight


This lab will use AWS S3 as the data lake solution to post a list of documents for part 1 and reviews for part 2 . 

## Implementation

### Part 1:

For this part , AWS Service Comprehend is used to do the Topic Modelling from S3 and further uses Quicksight to review the results .

Amazon Comprehend examines a corpus of documents to find the common themes contained within the corpus. Amazon Comprehend’s topic modeling capability examines the documents in the corpus and then returns the most prominent topics and the documents that are associated with each topic. Topic modeling is an asynchronous process, where you submit a set of documents for processing and then later get the results when processing is complete. 

This lab involves completing these high-level steps:
1.	Prerequisite : Install and configure ‘awscli’. This should have been completed already as a part of pre-setup .
2.	Or Install and Setup Cloud9 environment.

These steps involve the developers to learn and experiment.
3.	Download the sample corpus of documents.
4.	Create an S3 bucket to be used by the topic modeling job.
5.	Create a topic modeling job from Amazon Comprehend console.
6.	Analyze topic modeling job results.
7.	Cleanup lab resources

Let’s dive into each of these steps in detail.


Step 1 has already been done . So , you need to login to Cloud9 environment 

Inline-style: 
![alt text](https://github.com/aashmeet/images/1.png "AWS Cloud9 Environment")




