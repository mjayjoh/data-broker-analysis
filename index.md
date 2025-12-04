# Data about Data Brokers: Unveiling the Data Broker Industry

Imagine if your location data, tracked through your phone, was sold without your knowledge to random firms, political campaigns, and advertisers. What if you were visiting a pregnancy center? Or attending a protest? Or a place of worship? This scenario is not a dystopian thought experiment—it is our lived reality. Just last year, the Federal Trade Commission (FTC) alleged that Mobilewalla, a data broker, collected more than 500 million “unique consumer advertising identifiers” linked with precise location data at sensitive sites, which was not anonymized and sold to third-parties. The data was used to create audience segments, or labels, for various purposes (including, but not limiting advertising): segments included location data of women who visited pregnancy centers or demographic analysis of people who protested the death of George Floyd. This is not an isolated case—the company Kochava has sold tracking data of people visiting reproductive health clinics, data brokers powered Cambridge Analytica’s voter suppression efforts, and three data brokers recently sold lists of vulnerable Americans (including elderly folks and people with Alzheimer’s) to scammers.


## What are data brokers?
Data brokers collect, buy, and aggregate extensive personal data on individuals, selling this data (often without explicit consent) to companies that use individual profiles to micro-target subgroups for commercial and/or political gain. The table below, “A Glimpse into the Data Broker Industry” displays some of the practices of major data broker agencies—companies that probably have your data, but you’ve never heard of.

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
    <tr>
      <th>Agency</th>
      <th>Practices</th>
    </tr>
  </thead>
  <caption style="caption-side:bottom; text-align: center; padding-top: 10px;">
      <b>A Glimpse into the Data Broker Industry</b>
  </caption>
  <tbody>
    <tr>
      <td><b>Acxiom*</b></td>
      <td>collects and sells extensive data on over <mark>2.5 billion</mark> consumers worldwide, covering demographics, finances, interests, behaviors, purchases, and even geolocation</td>
    </tr>
    <tr>
      <td><b>LexisNexis</b></td>
      <td>links over <mark>283 million</mark> U.S. consumer profiles with billions of records on finances, property, vehicles, and phone numbers and offers tools to track people’s locations, connections, and identities, search criminal and public records, and provide real-time updates, with data sourced from both U.S. and international databases</td>
    </tr>
    <tr>
      <td><b>Nielsen</b></td>
      <td>collects extensive audience and consumer data across more than <mark>60,000 segments</mark>, tracking demographics, spending, media use, shopping habits, and credit card transactions</td>
    </tr>
    <tr>
      <td><b>Experian*</b></td>
      <td>handles over <mark>2 billion records</mark> each month and holds data on about 95% of the U.S. population, linking billions of transactions and personal identifiers into detailed consumer profiles</td>
    </tr>
    <tr>
      <td><b>Equifax</b></td>
      <td>collects data on <mark>45% of the nation’s assets</mark>, covering financial habits, spending, credit, and lifestyle behaviors across many categories, links customer data with third-party information for marketing insights, buys payroll and employment data</td>
    </tr>
  </tbody>
</table>
<div style="float: right; font-size: smaller;">
          <sub>*was implicated in the Cambridge Analytica scandal</sub>
      </div>

## What we did
We decided to analyze the interactions between several entities, conducting our analysis through three major entities in the data broker ecosystem: data broker companies, legislatures, and consumers themselves. We conducted an analysis of the three different entities who shape the ecosystem: data brokers, legislatures, and consumers.

Since we wanted to compare three perspectives on the issue (state legislators, actual practices of data broker companies, and consumer preferences), we came up with a standardized rubric for comparing the three entities across four major categories: data collected, data use, data sharing, and user controls.

To systematically analyze the purported practices of data broker companies themselves, we used Privacy Clearinghouse’s data, which compiles data broker information from state registries. After cleaning the dataset of data brokers, we obtained a random sample through simple random sampling of the dataframe, extracting 200 of the approximately 600 data brokers. Then, we downloaded data broker privacy policies. After that, for each privacy policy, we uploaded the privacy policy PDF through Gemini 2.5 Pro (“Reasoning, math & code”) and queried each privacy policy three times: about how entities use information, which third parties they share or sell data with, and consumer rights they provide consumers. We then validated a sample of the data extracted from the LLM and determined that the LLM responses were approximately 96.67% accurate.

We simultaneously conducted a survey of college students using the standardized set of questions. The survey was short and included dropdown questions where participants could easily select which entries they approved of. For example, for a question about data use, participants selected (any/all/none) of various common use cases we listed (biometric, employment, address, geolocation, etc.). We also asked two additional questions for Californian residents about the DELETE Act, arguably one of the strongest state statutes on data broker transparency. We disseminated the survey among college students online.

Lastly, we conducted a systematic analysis of state laws, reading statutes explicitly covering data brokers and evaluating consumer privacy laws, when relevant.

## What we found
### The Actual Practices of Data Brokers
A majority of data brokers collect address data, commercial transactions data, employment data, and social network data. Among the other data types, approximately 3.2% of our data brokers collect biometric data, 21.3% of data brokers collect minors’ data, 1.6% of data brokers collect reproductive health data, and 6.5% of data brokers collect government ID data, such as Social Security Numbers. That said, the analysis presented in Figure X represents the data collection practices, by data type, explicitly reported by data brokers, which only represent a small percentage of the total dataset of 941 data brokers. Figure Y represents the transparency gaps: with the exception of minors’ data, where approximately 45% of data brokers explicitly report whether they collect or do not collect minors’ data, data brokers overwhelmingly do not explicitly disclose whether they collect the other forms of sensitive data: social network data, employment data, commercial transactions data, biometric data, government ID data, addresses, and reproductive health data. This transparency gap highlights the lack of information disclosed by data brokers: even with a combination of human and algorithmic analysis of data broker registrations across state registry databases, Privacy Rights Clearinghouse, Electronic Frontier Foundation, and the Harvard Law School Cyberlaw Clinic were unable to determine whether data brokers collected those forms of sensitive data. 

Furthermore, in terms of what personal data collected by data brokers is allowed to be used for, our LLM-parsing analysis demonstrates that the majority of data brokers explicitly permit personal data to be used for marketing and personalized ads. Approximately XXX percent of data brokers do not mention data use in the contexts of employment, consumer finance, and law enforcement requests (without a subpoena). Among the privacy policies that do mention these use cases, XXX allow data to be used in employment decisions, while XXX do not. [Add same stats for consumer finance and law without subpoena].

In the sample of 200 privacy policies we analyzed, almost all of the data brokers allow data sharing with corporations. The majority of data broker privacy policies do not report whether data sharing is allowed with the government or educational/research institutions, although of those that do report this data, XXX percent allow data sharing with the government and XXX permit sharing with educational/research institutions.

The vast majority of data brokers explicitly guarantee the right to access, correct, and delete data, as well as opt out of collection or sharing. Approximately XXX percent of data brokers include non-discrimination statements around data use in their privacy policies, and XXX percent allow users to turn off targeted advertising.

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