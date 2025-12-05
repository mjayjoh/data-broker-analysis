# Data about Data Brokers: Unveiling the Data Broker Industry

Imagine if your location data, tracked through your phone, was sold without your knowledge to random firms, political campaigns, and advertisers. What if you were visiting a pregnancy center? Or attending a protest? Or a place of worship? This scenario is not a dystopian thought experiment—it is our lived reality. Just last year, the Federal Trade Commission (FTC) alleged that Mobilewalla, a data broker, collected more than 500 million “unique consumer advertising identifiers” linked with precise location data at sensitive sites, which was not anonymized and sold to third-parties. The data was used to create audience segments, or labels, for various purposes (including, but not limiting advertising): segments included location data of women who visited pregnancy centers or demographic analysis of people who protested the death of George Floyd. This is not an isolated case—the company Kochava has sold tracking data of people visiting reproductive health clinics, data brokers powered Cambridge Analytica’s voter suppression efforts, and three data brokers recently sold lists of vulnerable Americans (including elderly folks and people with Alzheimer’s) to scammers.


## What are data brokers?
Data brokers collect, buy, and aggregate extensive personal data on individuals, selling this data (often without explicit consent) to companies that use individual profiles to micro-target subgroups for commercial and/or political gain. Table 1, “A Glimpse into the Data Broker Industry” displays some of the practices of major data broker agencies—companies that probably have your data, but you’ve never heard of.

In this business model, consumers are the product. Given the extensive adoption of digital technologies and smart wearables, these companies now know the following personal information (note that this list is not comprehensive): 
- Name
- Address
- Telephone number
- E-mail address
- Gender
- Age
- Marital status
- Children
- Education
- Profession
- Income
- Political preferences
- Real estate ownership
- Health information
- Sites we visit
- Products we buy
- Advertisements we click on

By now, you might feel uneasy, but perhaps you’re wondering: what is the real harm of this data collection? When these datasets are sold to advertisers and/or malicious actors, with few safeguards in place, our personal data can be used against us: to manipulate, defraud, or target politically. With the rising popularity of algorithms trained on data, discriminatory profiling is a real threat, especially when individuals are labeled based on protected characteristics, such as race, gender, or income. These decisions may influence our equal opportunity to education, healthcare, and financial services, as they can lead to unfair and opaque denial of benefits, inflation of insurance rates, or lowered credit scores. 

<table>
  <thead>
    <tr style="text-align: center;">
      <th>Agency</th>
      <th>Practices</th>
    </tr>
  </thead>
  <caption style="caption-side:bottom; text-align: right; padding-top: 5px;">
          <sub>*was implicated in the Cambridge Analytica scandal</sub>
  </caption>
  <tbody>
    <tr style="text-align: center;">
      <td><b>Acxiom*</b></td>
      <td>Collects and sells extensive data on over <mark>2.5 billion</mark> consumers worldwide, covering demographics, finances, interests, behaviors, purchases, and even geolocation.</td>
    </tr>
    <tr style="text-align: center;">
      <td><b>LexisNexis</b></td>
      <td>Links over <mark>283 million</mark> U.S. consumer profiles with billions of records on finances, property, vehicles, and phone numbers. Offers tools to track people’s locations, connections, and identities, search criminal and public records, and provide real-time updates, with data sourced from both U.S. and international databases.</td>
    </tr>
    <tr style="text-align: center;">
      <td><b>Nielsen</b></td>
      <td>Collects extensive audience and consumer data across more than <mark>60,000</mark> segments, tracking demographics, spending, media use, shopping habits, and credit card transactions.</td>
    </tr>
    <tr style="text-align: center;">
      <td><b>Experian*</b></td>
      <td>Handles over <mark>2 billion</mark> records each month, holds over 8 billion name and address combinations, and holds data on about 95% of the U.S. population, linking billions of transactions and personal identifiers into detailed consumer profiles.</td>
    </tr>
    <tr style="text-align: center;">
      <td><b>Equifax</b></td>
      <td>Collects data on <mark>45% of the nation’s assets</mark>, covering financial habits, spending, credit, and lifestyle behaviors across many categories, links customer data with third-party information for marketing insights, and buys payroll and employment data.</td>
    </tr>
  </tbody>
</table>
<div style="text-align:center">Table 1: A Glimpse into the Data Broker Industry</div>


## What we did
To shed light on the industry, we analyzed the three key players in the data broker ecosystem: data brokers, consumers, and legislatures. We created a standardized set of questions to compare the three entities across four major categories: data type collected, data use, data sharing, and user controls.

We used a data broker dataset compiled by Privacy Rights Clearinghouse, a nonprofit organization focusing on privacy, who compiled data broker information from state registries. We collected information about data type from this dataset. After cleaning the dataset of data brokers, we obtained a random sample of 200 data brokers, from the full set of approximately 600. From there, we downloaded data broker privacy policies of those 200 data brokers and used a Gemini 2.5 Pro model (“Reasoning, math & code”) to query each privacy policy about data use, data sharing, and user controls. We manually validated a sample of the data. We simultaneously conducted an online survey of university students, using the standardized set of questions. The survey included dropdown questions where participants could easily select which entries they approved of. For example, for a question about data use, participants selected whether they approved of each of the specific use cases of personal data that we listed (biometric, employment, address, geolocation, etc.). We also asked Californian residents two additional questions about the DELETE Act, the strongest state statute on data brokers. Lastly, we examined state laws covering both data brokers and consumer privacy. Table 2 summarizes our data sources for each form of analysis.

<table>
  <thead>
    <tr style="text-align: center;">
      <th>Entity</th>
      <th>Data Brokers</th>
      <th>Consumer Preferences</th>
      <th>State Laws</th>
    </tr>
  </thead>
  <caption style="caption-side:bottom; text-align: center; padding-top: 10px;">
          Table 2: Sources of Data
  </caption>
  <tbody>
    <tr style="text-align: center;">
      <td><b>Data Type</b></td>
      <td>Privacy Rights Clearinghouse Data</td>
      <td>Survey</td>
      <td>Independent Analysis</td>
    </tr>
    <tr style="text-align: center;">
      <td><b>Data Use</b></td>
      <td>LLM-parsed Privacy Policies</td>
      <td>Survey</td>
      <td>Independent Analysis</td>
    </tr>
    <tr style="text-align: center;">
      <td><b>Entity Sharing</b></td>
      <td>LLM-parsed Privacy Policies</td>
      <td>Survey</td>
      <td>Independent Analysis</td>
    </tr>
    <tr style="text-align: center;">
      <td><b>Consumer Rights</b></td>
      <td>LLM-parsed Privacy Policies</td>
      <td>Survey</td>
      <td>Independent Analysis</td>
    </tr>
  </tbody>
</table>

## What we found
### The Practices of Data Brokers
As shown in the figures below, the majority of data brokers that do report the type of data they collect gather address data, commercial transactions data, employment data, and social network data. Among the other data types, approximately 3.2% of our data brokers collect biometric data, 21.3% of data brokers collect minors’ data, 1.6% of data brokers collect reproductive health data, and 6.5% of data brokers collect government ID data, such as Social Security Numbers. However, with the exception of minors’ data, where approximately 45% of data brokers explicitly report whether they collect or do not collect minors’ data, data brokers overwhelmingly do not even disclose whether they collect the other forms of sensitive data, such as social network data, employment data, commercial transactions data, biometric data, government ID data, addresses, and reproductive health data. This transparency gap highlights the shadowy practices of data brokers: joint human (Privacy Rights Clearinghouse, Electronic Frontier Foundation, and the Harvard Law School Cyberlaw Clinic) and algorithmic analysis of data broker registrations across state registry databases were unable to determine whether data brokers collected some forms of sensitive data.
![Permitted Data Types Collected By Data Brokers](/notebooks/imgs/data_type_chart.svg)
*Figure 1: Permitted Data Types Collected, Per Data Broker Privacy Policies*

### What consumers want
We asked survey respondents about their knowledge and understanding of data broker practices. Among the 62 survey respondents, 69.35% indicated a low or nonexistent understanding of data brokers: either “I’ve never heard of data brokers” (the most common response) or “I’ve heard of them but don’t know what they do.” 3.23% of respondents indicated they either have a good understanding of data brokers. A majority of respondents believed that data brokers collect biometric (62.90%), commercial (91.94%), employment (83.87%), location (88.71%), network data (91.94%), and reproductive health data (54.84%). Only 37% of respondents believed that data brokers collect minors’ data and 40% believed they collect government ID data. 

When respondents were asked about their preferences, the data differed greatly from their answers around data broker collection practices. While respondents overestimated the types of data that data brokers collect, with the exception of accuracy for commercial (~90%) and employment (~80%) data, the responses indicate that individuals did not want data brokers to collect their personal data, across all data types. The most “permitted” data type to collect was commercial transactions data (at 53.23%) and then employment data (35.48%). Less than a quarter of respondents felt comfortable with data brokers collecting their biometric, location, minors, reproductive health, and government ID data, at approximately 3.23% for minors and 1.613% for government ID data. Notably, about a quarter of respondents were unsure about what data types they felt comfortable with data brokers collecting (note that respondents could select multiple options).

In terms of purposes their personal data is used for, the most “approved” category was personalized advertising (although only at 62.90%), and then marketing (43.55%), and employment decisions (25.81%). Results indicated a general distrust and disapproval toward their personal data being used for any of the options—24.19% responded that they were uncomfortable with all the options. 

The results in response to the question of which entities respondents felt comfortable with their data being shared to also depart drastically from the actual practices listed in privacy policies. 85.48% of respondents felt comfortable with data being shared to educational and research institutions, and then government agencies at 35.48%, and corporations last at 24.19%. 11.29% did not approve of sharing to any of these three entities.

Our survey also asked respondents about provisions and safeguards they would like to see in privacy policies and laws. The most frequently selected provision was the “Option to opt out of data collection or sharing” at 93.55%, and then protections against discrimination (83.87%), and the right to access personal data (77.42%). That said, all the listed provisions were selected at at least 69% frequency.  

We also decided to analyze the attitudes of Californian residents toward the DELETE Act. Of the 12 respondents surveyed, 25% were aware of the DELETE Act prior to the survey. After providing a description of the Act’s tools, 25% stated they would use the DELETE Act’s mechanisms once they became active and 66.66% indicated that they might use them.

### The (in)action of regulators
Discuss federal and state laws; The majority of states do not even have comprehensive consumer privacy laws and only five explicitly regulate data brokers (CA, OR, TX, VT, NV).
## Summary

| Category | Data Brokers | Consumer Preferences | State Laws |
|---|---|---|---|
| **Data Type** | A majority of data brokers collect commercial transactions data (91.7%), employment data (82.4%), address data (70.5%), and social network data (66.7%). Approximately one-fifth collect minors’ data. 6.5% collect government ID data and less than 5% collect biometric and reproductive health-care data. | Commercial transactions data is the data type individuals are most comfortable with data brokers collecting (53.23%) and then employment (35.48%), although these percentages all tend to be low (the rest are <25%). A significant portion were unsure about their preferences (27.42%). | Most state laws narrowly define personal data as identifiers such as addresses, birth details, family information, biometrics, and government ID numbers, while excluding transaction and employment records from this category. |
| **Data Use** | A majority of data brokers explicitly permit personal data to be used for marketing and personalized ads (XXX). Other use cases (employment, consumer finance, law enforcement requests without subpoena) are frequently not reported. | The most “approved” data use categories were personalized advertising (62.90%), marketing (43.55%), and employment decisions (25.81%). Results indicated a general distrust and disapproval toward their personal data being used for any of the options—about a quarter stated that they were uncomfortable with all listed options. | None of the states prohibit the listed data broker use cases, though most provide residents with opt‑out rights. Currently only four states, namely California, Vermont, Oregon, and Texas, maintain formal data broker registries, which may complicate enforcement of these laws. |
| **Entity Sharing** | Data sharing overwhelmingly allowed to corporations, and if reported, mostly allowed to the government and educational/research institutions. | Respondents were comfortable with data shared to educational and research institutions (85.48%), but uncomfortable with data sharing with government agencies (35.48%) and corporations (24.19%). | None of the states prohibits sharing data to corporations, the government, and educational/research institutions. |
| **Consumer Rights** | The majority of data brokers explicitly guarantee the right to access, correct, and delete data, and opt-out of collection or sharing, as well as protections against discrimination. XXX provide restrictions on targeted advertising. | Participants were in favor of options to opt out of data collection or sharing, protections against discrimination, the right to delete data, the right to access data, restrictions on targeted advertising, and the right to correct personal data, in decreasing order. The most popular provision being options to opt out of data collection or sharing. | Of the 19 states with comprehensive consumer privacy laws, all provide the right to access personal data, 94.44% provide the right to correct and delete, and 47.34% ban discrimination. Some allow opt-outs for targeted advertising for minors (MD, DE, CT). |

## So what’s next? 
Moving forward, [go into what should happen]

In terms of next steps for a similar project, [go into limitations]

## Sources of Data

Link and describe Github here

## Questions to ask Jotte
Is it ok that it’s a summary b/c hard to 1 to 1 analysis
Limitations? Should that be listed if it’s like “pop science”
How to straddle the boundary between pop science and reporting results
Length?
Citations?