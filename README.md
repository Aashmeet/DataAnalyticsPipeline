# Lab: Data Pipeline for Topic Modeling and Sentiment Analysis Using Amazon S3 ,Amazon Comprehend ,Amazon Athena and Amazon Quicksight

## Introduction:

In this lab ,we are focussed on data analysis using a Data Pipeline .  

For building an effective data analytics pipeline , it is important to focus on the following :

1. Help ingest data easily from multiple sources.

2. Analyze it for completeness and accuracy.

3.  Use it for metrics computations.

4. Store the data assets and scale as they grow rapidly without causing disruptions.

5. Adapt to changes as they happen.

6. Have a relatively short development cycle that is repeatable and easy to implement.

From an architecture standpoint ,usually the first step would be to ingest the data in a data lake.
A data lake is a repository that holds a large amount of raw data in its native (structured or unstructured) format until the data is needed. Storing data in its native format enables you to accommodate any future schema requirements or design changes.

This lab walks the audience through two processes:

1. Process of topic modeling using Amazon Comprehend using a combination of AWS Console and "Cloud9". While the recommendation is to use at least 1,000 documents for a topic modeling job, for the purposes of this lab we will use a sample set of five documents. The sample documents consist of a subset of research and education material available from ResMed website ([www.resmed.com](http://www.resmed.com)).

2. Serverless Process of sentiment analysis using Amazon Comprehend ,S3 and Quicksight[[MOU1]](#_msocom_1) 

This lab will use AWS S3 as the data lake solution to post a list of documents for part 1 and reviews for part 2 .

### Part 1:

For this part , AWS Service Comprehend is used to do the Topic Modelling from S3 and further uses Quicksight to review the results .

Amazon Comprehend examines a corpus of documents to find the common themes contained within the corpus. Amazon Comprehend's topic modeling capability examines the documents in the corpus and then returns the most prominent topics and the documents that are associated with each topic. Topic modeling is an asynchronous process, where you submit a set of documents for processing and then later get the results when processing is complete.

This lab involves completing these high-level steps:

1. Prerequisite : Install and configure 'awscli'. This should have been completed already as a part of pre-setup .

2. Or Install and Setup Cloud9 environment.

These steps involve the developers to learn and experiment.

3. Download the sample corpus of documents.

4. Create an S3 bucket to be used by the topic modeling job.

5. Create a topic modeling job from Amazon Comprehend console.

6. Analyze topic modeling job results.

7. Cleanup lab resources

Let's dive into each of these steps in detail.

Step 1 has already been done . So , you need to login to Cloud9 environment

![](/media/Picture1.png)
**Step 2 -- ****Download the sample corpus of documents**

**For the purpose of the lab ,the data set is being downloaded to S3 . We can also use Ingestion process to upload these documents to S3(data lake) .**

1. Go to AWS Management Console and type Cloud9 in the Services .

2. In the terminal below , execute the commands as mentioned in Step 3

3. Use these commands to download the sample documents onto your local environment. 

*aws s3 cp s3://comprehend-topic-modeling-workshop/sample-document-corpus/AutoSetTechnology .*

*aws s3 cp s3://comprehend-topic-modeling-workshop/sample-document-corpus/DiabeticsSleepApnea .*

*aws s3 cp s3://comprehend-topic-modeling-workshop/sample-document-corpus/HotHMV .*

*aws s3 cp s3://comprehend-topic-modeling-workshop/sample-document-corpus/ObesitySleepApnea .*

*aws s3 cp s3://comprehend-topic-modeling-workshop/sample-document-corpus/SleepTherapyCompliance .*

*aws s3 cp s3://comprehend-topic-modeling-workshop/sample-document-corpus/TrafficAccidents .*

 ![](/media/Picture2.png)

4. These files downloaded should be available in your project .

 ![](/media/Picture3.png)

5. Examine the content in these documents to understand the content used for topic modeling.

**Step 3 -- ****Create an S3 bucket to be used by Amazon Comprehend topic modeling job .This S3 bucket is the placeholder for the structured/raw data to be consumed by other AWS services.**

1. Use these commands in the Cloud9 Terminal to create an S3 bucket and upload the sample documents into 'articles' folder

2. Set the environment variables (Use appropriate values below)

**(Note : These commands are assume unix, please use 'setenv' on windows)**

*TOPIC_MODELING_DEMO_BUCKET=topic-modeling-demo-<<username>>-date*

*AWS_REGION=us-west-2*

*ARTICLES_FOLDER=articles*

*OUTPUT_FOLDER=output*

3. Create the  bucket

*aws s3 mb s3://$TOPIC_MODELING_DEMO_BUCKET *

4. Upload the sample documents to this bucket into 'articles' folder

*aws s3  cp AutoSetTechnology            s3://$TOPIC_MODELING_DEMO_BUCKET/$ARTICLES_FOLDER/*

*aws s3 cp *DiabeticsSleepApnea *s3://$TOPIC_MODELING_DEMO_BUCKET/$ARTICLES_FOLDER/*

*aws s3 cp *HotHMV *s3://$TOPIC_MODELING_DEMO_BUCKET/$ARTICLES_FOLDER/*

*aws s3 cp *ObesitySleepApnea *s3://$TOPIC_MODELING_DEMO_BUCKET/$ARTICLES_FOLDER/*

*aws s3 cp *SleepTherapyCompliance * s3://$TOPIC_MODELING_DEMO_BUCKET/$ARTICLES_FOLDER/*

*aws s3 cp *TrafficAccidents *s3://$TOPIC_MODELING_DEMO_BUCKET/$ARTICLES_FOLDER/*

*5. *Validate that these files appear in S3 bucket using the console.

6. Additionally, create "output" folder in S3 bucket at the same level as "articles" folder.

 ![](/media/Picture4.png)

**Step 4 -- **Create a topic modeling job from Amazon Comprehend Console.

In order to do this ,go to the Organisation tab ,click on "Create"

 ![](/media/Picture5.png)
 
1. Click Create; Enter the following values.

S3 Data Location : <<BUCKET_NAME>>/input folder

No of topics : 10

**Input format : One document per file ( Make sure this is selected as this will impact the output)**

IAM Role : Create an IAM role to give permission to the user to access the input and output buckets

S3 Data Location

 ![](/media/Picture6.png)
 
 ![](/media/Picture7.png)
 
 ![](/media/Picture8.png)


As soon as you click on Start ,it starts running an asynchronous topic modelling job.

2. Comprehend dashboard should show the job created and In Progress status.

3. Topic Modeling job takes about 4 --5 minutes to complete.

 ![](/media/Picture9.png)

![Text Box: Once the job is complete, output is available in the S3 bucket.]

 ![](/media/Picture6.png)
  ![](/media/Picture7.png)

**Step 5 -- **Analyze topic modeling job results

1. Download results of topic modeling job from S3.

 ![](/media/Picture8.png)

a. Click on the Output data location link in the job info as shown in Step 5, to view the output.tar.gz in the S3 bucket.

b. Download to your laptop/desktop.

c. Extract output.tar.gz file

d. Verify that you can access the extracted files : "doc-topics.csv"  and "topics-term.csv"

2. Analyze results in Excel.

a. Open "topics-terms.csv" to see the different words (terms) grouped into 10 topics.

b. Open  "doc-topics.csv" to see the topics and their weights identified in the different documents.

c. Few observations :

The document "DiabeticsSleepApnea" has two different topics 1 and 9, just about 50% each. Now notice terms in topic 1 (collision, sufferer, risk, drive, dangerous, accident, relate, significantly sleepy, billion) and topic 9 (diabetes, apnea, sleep, patient, insulin, gluclose). Topic 1 also part of in "TrafficAccidents "(.87)

Similarly, the document "ObesitySleepApnea" has a single topic 3, which contains the terms : bariatric, surgery, weight, increase, patient, loss, consider, gain, operative, obese

Notice how the topics (grouped terms) make up the documents.

3. Visualize topic modeling job results in Amazon QuickSight.

a. Open Amazon QuickSight from AWS Console

b. Create Analysis for "doc-topics.csv"

 i. Click "New Analysis"

 ii. Click "New Data Set"

 iii. Click "Upload a file". Browse to and choose "doc-topics.csv"

 iv. On "Confirm file upload settings", Click "Next"

 v. After the data source is loaded, Click "Visualize"

 vi. In the Visualize view, select

a) Fields list : docname

b) Visual types : piechart

c) In Field wells section, Value : topic (Count) and Group/Color : docname.

d) Visualization should be similar to the screenshot below

 ![](/media/Picture9.png)

c. Create Analysis for "topic-terms.csv"

 i. Click "New Analysis"

 ii. Click "New Data Set"

 iii. Click "Upload a file". Browse to and choose "topic-terms.csv"

 iv. On "Confirm file upload settings", Click "Next"

 v. After the data source is loaded, Click "Visualize"

 vi. In the Visualize view, select

a) Fields list : #topic

b) Visual types : piechart

c) In Field wells section :   Value : topic (Count) and Group/Color : topic.

d) Visualization should be similar to screenshot below

 ![](/media/Picture10.png)

e) Right click on the "9" pie and select "Focus on 9", to drill down into topic 9.

f) In Field wells section, Value : term (Count) and Group/Color : term.

g) This will show the terms in Topic 9

 ![](/media/Picture11.png)

**Step 7 -- ****Clean up lab resources**

1.  Go back to Cloud9 and empty and delete the S3 bucket.

(Note : This is a force delete. Make sure to use correct bucket name. Alternatively, you can delete the bucket from console.)

*$TOPIC_MODELING_DEMO_BUCKET =="nameofbucket"*

* aws s3 rb s3://$TOPIC_MODELING_DEMO_BUCKET --force*

2. Delete Analysis and DataSet from QuickSight console.

Conclusion: From this lab , the process was to extract articles and publish them in S3 ,then use Topic-modelling to analyse the articles and work through visualization tools to analyse the data.

**Part 2:**

This part of the lab is a serverless data pipeline implementation to do sentiment analysis based on input entered by the user . This process is also leveraging S3 as a data lake . Please note that for the purpose of the lab we are uploading the reviews but this architecture can be extended to do real time sentiment analysis by getting real-time reviews from customer using Kinesis firehose and implementing an event -driven trigger to upload the data to S3 and conduct sentiment analysis .

![](/media/Architecture.png)
Step 1 : Select the region US-East and deploy the Cloudformation template .

 We will start off by deploying an [AWS CloudFormation](https://aws.amazon.com/cloudformation/) template to provision the necessary AWS Identity and Access Management (IAM) role and Lambda function needed in order to interact with the Amazon S3, AWS Lambda, and Amazon Comprehend APIs.

In the CloudFormation console, choose the **Launch Stack** button (above). If interested, you can view the YAML template [here](https://s3.amazonaws.com/aws-ml-blog/artifacts/Detect-sentiment-from-customer-reviews/setup.yaml). A YAML Template is provided ,so upload the template .

- Choose **Next** on the Select Template page.

![](/media/PictureCF1.png)


- Choose **Next** on the Specify Details page.

- On the Options page, leave all the defaults and Choose **Next**.

- On the Review page, check the boxes to acknowledge that CloudFormation will create IAM resources and IAM resources with customer names.

- Choose **Create Change Set**.

![](/media/PictureCF2.png)

 Finally, choose Execute and then let the CloudFormation launch resources in the background. You don't need to wait for it to finish before proceeding to the next step.
![](/media/PictureCFlast.png)


Make sure all the resources are created .

Step 2 : Amazon Simple Storage Service (S3) bucket event trigger:

Now that you have your IAM role, Lambda function, and S3 bucket deployed, let's make sure that we create an S3 event trigger for your Comprehend Sentiment Analysis function.

- Open the [Amazon S3 console](https://console.aws.amazon.com/s3/home?region=us-east-1) and select new S3 bucket that begins with 'review-sentiment.'

![](/media/PictureS3console.png)

- Create a folder in the bucket and call it "articles" .

-  

- Choose the **Properties** Under the Advanced Settings section, choose the **Events** box.

- Choose **+ Add notification** and configure the following:

Name: **SentimentAnalysis**

Events: **ObjectCreate (All)**

Prefix **: articles/**

Send to: **Lambda Function**

Lambda: **review-sentiment-ComprehendSentimentAnalysis-XYZ**

Choose **Save**.
![](/media/PictureS3Mgmt.png)
![](/media/PictureS3events.png)

Add your own review as a text file and upload to S3 in the folder 'articles':

For eg *:* *"So it ís been an interesting first few weeks with the Echo and am happy to say Echo 2nd Gen has finally delivered on its promise of improved sound quality over 1st Gen Echo, with the 3rd firmware since launch. If you are confused about a lot of the negative reviews, old firmware is the likely cause of most of them regarding poor sound quality.*

*Want to keep this short and spare all the gory details, but there was a bug in the launch version of the firmware, which was fixed after a few days, but the first fix, while satisfying some, was not, in my opinion a full fix and left the mid-range frequencies muted and tinny. Today I noticed that Alexaís voice in this unit sounded much more like Alexaís voice on Gen 1 Echoís I own and, after playing some music, suspected they had upgraded the firmware again, and indeed they have. The current firmware is 592452720 and itís a massive improvement over both the original and updated version 592452420.*

*So I decided to do some more side-by-side comparisons with the Gen 1 Echo and can honestly say in many areas the sound quality is now actually better than Gen 1 Echo. This is how the product should have sounded at launch! If I have any complaints at this point itís that the low-frequencies loudness could stand to be bumped up just a tad. (Better yet, PLEASE add an EQ feature to the Alexa app so users can adjust EQ for the room and music type they prefer). I did my comparisons at volume level 8. Anything above that and Gen 1 Echo dynamic range starts to break down, while Gen 2 maintains quality but doesnít get quite as loud and Gen 1. Itís the right trade off, I would rather it sound good than be louder and sound harsh. At that volume level I went thru a range of music, streamed over Bluetooth, switching between Gen 1 and Gen 2 devices, and found Gen 2 to be an improvement over Gen 1 for the vast majority of the music I tried. Iím impressed with the quality of the audio coming out of this form factor, and impressed how quickly Amazon has responded to feedback on the problems. Kudos, this Echo is a keeper."*

- Choose your S3 bucket from the console and then choose Add each one of the review text files and choose Upload.

- Refresh the bucket and then verify the following output in your bucket:

**Note: **This is an event-driven serverless architecture we created. The uploaded review to our S3 bucket was considered an event that triggered our **Comprehend-SentimentAnalysis** function, which then in return outputs the sentiment and sentiment confidence scores into a CSV within the sentiment folder of your S3 bucket.

![](/media/PictureS31.png)
![](/media/PictureS32.png)

 Select a review and then choose **Download**:

Choose the **sentiment** folder and **open the CSV file** to view its contents.
![](/media/PictureOutput.png)
![](/media/PictureSpreadsheet.png)

The Sentiment information describes the overall sentiment of the text and also sentiment scores of each label: Positive, Negative, Neutral, and Mixed. All of these sentiment scores are returned from an MXNet deep learning model and are depicted as a float between 0 and 1, where 1 is full confidence of the sentiment label. For example, this CSV shows that the Amazon Echo Dot review has a POSITIVE overall sentiment with an 82% positive sentiment score (confidence).

** Step 3 - Interactive querying with Amazon Athena**

We take this a step further by having our SQL statement order all of the reviews with the strongest negative sentiment in descending order. With this query, the business knows exactly where to start from and spend their cycles wisely.

In the [Athena](https://console.aws.amazon.com/athena/home?region=us-east-1) console, run the following commands to create the Athena table in the default database. Important: Replace **<bucket_name>** with the S3 bucket created earlier.

*"CREATE EXTERNAL TABLE IF NOT EXISTS default.ReviewSentimentAnalysis'<<firstnamealias>>' (*

* `ImageLocation` string,*

* `Timestamp` string,  *

* `Sentiment` string,*

* `Positive` string,*

* `Negative` string,*

* `Neutral` string,*

* `Mixed` string*

* )*

*ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'*

*WITH SERDEPROPERTIES (*

* 'serialization.format' = ',',*

* 'field.delim' = ','*

*) LOCATION 's3://<bucket_name>/sentiment/' "*

![](/media/PictureAthena1)

After you notice that your table has been successfully created, copy the following SQL statement and paste it into the editor.  Choose Run Query.

SELECT * FROM default.ReviewSentimentAnalysis WHERE sentiment='POSITIVE'

ORDER BY positive DESC

![](/media/PictureAthena)

**Step 4 : Cleanup Lab resources by  emptying the S3 bucket and then deleting the cloudformation stack .**

* * * * *

