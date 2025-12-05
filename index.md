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
<p align="center">
  <small><i><b>Table 1:</b> A Glimpse into the Data Broker Industry</i></small>
</p>

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
          <small><i><b>Table 2:</b> Sources of Data</i></small>
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
<p align="center">
  <img src="notebooks/imgs/Permitted Data Types Collected By Data Brokers.svg" alt="Permitted Data Types Collected By Data Brokers">
</p>
<p align="center">
  <small><i><b>Figure 1:</b> Permitted Data Types Collected, Per Data Broker Privacy Policies</i></small>
</p>

<p align="center">
  <img src="notebooks/imgs/Data Collection Practices by Category.svg" alt="Transparency Gaps in Data Types Collected by Data Brokers">
</p>
<p align="center">
  <small><i><b>Figure 2:</b> Transparency Gaps in Data Types Collected by Data Brokers</i></small>
</p>


Furthermore, in terms of what personal data collected by data brokers is allowed to be used for, our LLM-parsing analysis demonstrates that the majority of data brokers explicitly allow personal data to be used for marketing (95.5%) and personalized advertising (86%). Approximately 60 to 70 percent of data brokers do not mention data use in the contexts of employment, consumer finance, and law enforcement requests (without a subpoena). Among the privacy policies that do mention these use cases, 59% allow data to be used in employment decisions. Figure 3 shows these trends below.

<p align="center">
  <img src="notebooks/imgs/Permitted Data Use Cases in Privacy Policies of Data Brokers.svg" alt="Permitted Data Uses By Data Brokers">
</p>
<p align="center">
  <small><i><b>Figure 3:</b> Permitted Data Uses, Per Data Broker Privacy Policies</i></small>
</p>

Among the sample of 200 privacy policies we analyzed, almost all (99%) of the data brokers allow data sharing with corporations, as shown in Figure 4. The majority of data broker privacy policies do not explicitly report whether data sharing is or is not allowed with the government or educational/research institutions. Of those that do report this data, 96.6% allow data sharing with the government and 95.2% permit sharing with educational/research institutions.

<p align="center">
  <img src="notebooks/imgs/Permitted Entity Data Sharing in Privacy Policies of Data Brokers.svg" alt="Permitted Entities To Share Data With, Per Data Broker Privacy Policies">
</p>
<p align="center">
  <small><i><b>Figure 4:</b> Permitted Entities To Share Data With, Per Data Broker Privacy Policies</i></small>
</p>

The vast majority of data brokers explicitly guarantee the right to access, correct, and delete data, as well as opt out of collection or sharing, as displayed in Figure 5. Approximately 63.5% of data brokers include non-discrimination statements around data use in their privacy policies, and 96% include provisions that allow users to opt out of data sharing and collection.

<p align="center">
  <img src="notebooks/imgs/User Rights and Controls in Privacy Policies of Data Brokers.svg" alt="User Rights and Controls in Data Broker Privacy Policies">
</p>
<p align="center">
  <small><i><b>Figure 5:</b> User Rights and Controls in Data Broker Privacy Policies</i></small>
</p>


### What consumers want
We surveyed respondents about their familiarity and understanding of data broker practices, which is displayed in Figure 6. Among the 62 survey respondents, 69.4% indicated a low or nonexistent understanding of data brokers: either “I’ve never heard of data brokers” (the most common response) or “I’ve heard of them but don’t know what they do.” The majority of respondents believed that data brokers collect biometric (62.9%), commercial (91.9%), employment (83.9%), location (88.7%), network data (91.9%), and reproductive health data (54.8%). Only 37% of respondents believed that data brokers collect minors’ data and 40% believed they collect government ID data. 

<p align="center">
  <img src="notebooks/imgs/Data Types that Respondents Believe Data Brokers Collect.svg" alt="Data Types That Respondents Believe Data Brokers Collect">
</p>
<p align="center">
  <small><i><b>Figure 6:</b> Data Types That Respondents Believe Data Brokers Collect</i></small>
</p>

The results of Figures 6 and 7 demonstrate a clear mismatch between respondents’ perceptions of current practices and their preferences. While they greatly overestimated the frequency at which data brokers collect data across different data types, with the exception of accuracy for commercial and employment data, responses showed that they did not want data brokers to collect these forms of data. To survey respondents, the most “permissible” data type to collect was commercial transactions data (53.2%) and then employment data (35.5%). Less than a quarter of respondents felt comfortable with data brokers collecting their biometric, location, minors, reproductive health, and government identification data, at approximately 3.2% for minors and 1.6% for government identification data. 

<p align="center">
  <img src="notebooks/imgs/Data Types That Respondents Are Comfortable with Data Brokers Collecting.svg" alt="Data Types That Respondents Are Comfortable with Data Brokers Collecting">
</p>
<p align="center">
  <small><i><b>Figure 7:</b> Data Types That Respondents Are Comfortable with Data Brokers Collecting</i></small>
</p>

In terms of purposes their personal data is used for, the most “approved” category was personalized advertising (62.9%), and then marketing (43.6%) and employment (25.8%). Results indicated general disapproval around their personal data being used across purposes—24.2% responded that they were uncomfortable with all the options. These results are shown in Figure 8.

<p align="center">
  <img src="notebooks/imgs/Use Cases That Respondents Are Comfortable With.svg" alt="Use Cases that Respondents Are Comfortable With">
</p>
<p align="center">
  <small><i><b>Figure 8:</b> Use Cases that Respondents Are Comfortable With</i></small>
</p>

Respondents also indicated extreme disapproval with their data shared with corporations, which differed greatly from research and educational institutions: 85.5% of respondents felt comfortable with their data being shared to educational and research institutions, and then government agencies at 35.5%, and corporations last at 24.2%. Notably, 11.29% did not approve of sharing to any of these three entities. These results are shown in Figure 9.

<p align="center">
  <img src="notebooks/imgs/Entities That Respondents Are Comfortable With Their Data Shared To.svg" alt="Entities That Respondents Are Comfortable With Their Data Shared To">
</p>
<p align="center">
  <small><i><b>Figure 9:</b> Entities That Respondents Are Comfortable With Their Data Shared To</i></small>
</p>

Our survey also asked respondents about provisions and safeguards they would like to see in privacy policies and laws. The most frequently selected provision was the “Option to opt out of data collection or sharing” at 93.6%, and then protections against discrimination (83.9%) and the right to access personal data (77.4%). That said, all the listed provisions were selected at at least 69% frequency. This data is displayed in Figure 10.

<p align="center">
  <img src="notebooks/imgs/Provisions In Privacy Policies and Laws Respondents Desire.svg" alt="Provisions In Privacy Policies and Laws Respondents Desire">
</p>
<p align="center">
  <small><i><b>Figure 10:</b> Provisions In Privacy Policies and Laws Respondents Desire</i></small>
</p>

Lastly, we were curious about the attitudes of Californian residents toward the DELETE Act, one of the most forward-thinking privacy statutes governing the data broker industry. Of the 12 Californian respondents surveyed, a quarter were aware of the DELETE Act prior to the survey. After providing a description of the Act’s tools, a quarter stated they intend to use the DELETE Act’s mechanisms once they become active, and two-thirds indicated that they might use them.

### The (in)action of regulators
Several federal frameworks may also constrain the practices of data brokers, but only in specific domains. For example, the Fair Credit Reporting Act (FCRA) regulates consumer reporting agencies, the Health Insurance Portability and Accountability Act (HIPAA) covers patient privacy, and the Children’s Online Privacy Protection Act (COPPA) protects the privacy of those under 13. The Federal Trade Commission (FTC), an independent agency, has authority to restrain unfair and deceptive trade practices, and have brought actions against data brokers. That said, the FTC sometimes lacks authority over enforcing against actions that do not fall within its statutory mandate, and enforcement is reactive, not practice. Congress has passed regulation prohibiting the sale or sharing of personal information with foreign adversary countries or entities they control, but this law does not restrict transfers to domestic entities. Furthermore, there does not exist a comprehensive federal framework governing consumer privacy, much less data brokers.

Nineteen states lack comprehensive consumer privacy laws, but only five (California, Oregon, Texas, Vermont, and Nevada) explicitly regulate data brokers. A key distinction is that these states not only address data brokers directly in their privacy frameworks but also require them to register with the state on an annual basis. Some states merely require data brokers to register, while others provide consumers with some rights and controls over their personal data. With the exception of Vermont, whose statute focuses on credit reporting agencies, they mandate opt‑out provisions for third‑party data sharing and sales, and they grant consumers rights to access, correct, and delete personal data, while prohibiting discriminatory uses of such data. Enforcement generally falls under the jurisdiction of the state Attorney General, though California has delegated oversight to the California Privacy Protection Agency (CPPA), which is specifically empowered to monitor data broker practices. California’s DELETE Act, for example, requires the California Privacy Protection Agency (CPPA) to create an accessible universal deletion mechanism by January 1, 2026. Consumers will then be able to access the platform to submit requests, and then data brokers must comply with deletion requests starting later in the year. It also requires data brokers to submit to independent, third-party audits for compliance.

In most other states, data brokers are governed indirectly by broader consumer privacy statutes. These laws do not explicitly reference data brokers but instead define “controllers” and “processors,” categories that encompass data broker activities. A controller is typically defined as an entity that determines the purposes and means of processing personal data, while a processor handles personal data on behalf of a controller. Consumer privacy acts generally impose obligations such as maintaining reasonable security measures, prohibiting discrimination against consumers, and ensuring rights to know what data is collected, to access and delete that data, and to opt out of its sale or certain processing activities, such as targeted advertising. Enforcement in these states also resides with the Attorney General.

## Summary
<table>
  <thead>
    <tr style="text-align: center;">
      <th></th>
      <th>Data Brokers</th>
      <th>Consumer Preference</th>
      <th>State Legislators</th>

    </tr>
  </thead>
  <caption style="caption-side:bottom; text-align: center; padding-top: 10px;">
          <small><i><b>Table 3:</b> Summarized Table of Findings</i></small>
  </caption>
  <tbody style="font-size: 12px; line-height: 1.4;">
    <tr>
      <td style="text-align: center;"><b>Data Type</b></td>
      <td>A majority of data brokers collect commercial transactions data (91.7%), employment data (82.4%), address data (70.5%), and social network data (66.7%). Approximately 21.3% collect minors’ data. 6.5% collect government ID data and less than 5% collect biometric and reproductive health-care data.</td>
      <td>Commercial transactions data is the data type individuals are most comfortable with data brokers collecting (53.23%) and then employment (35.48%), although these percentages all tend to be low (the rest are &lt;25%). A significant portion were unsure about their preferences (27.42%).</td>
      <td>Most state laws narrowly define personal data as identifiers such as addresses, birth details, family information, biometrics, and government ID numbers, while excluding transaction and employment records from this category.</td>
    </tr>
    <tr>
      <td style="text-align: center;"><b>Data Use</b></td>
      <td>A majority of data brokers explicitly permit personal data to be used for marketing (95.5%) and personalized ads (86%). Other use cases (employment, consumer finance, law enforcement requests without subpoena) are frequently not reported.</td>
      <td>The most “approved” data use categories were personalized advertising (62.9%), marketing (43.55%), and employment decisions (25.81%). Results indicated a general distrust and disapproval toward their personal data being used for any of the options—about a quarter stated that they were uncomfortable with all listed options.</td>
      <td>None of the states prohibit the listed data broker use cases, though most provide residents with opt‑out rights. Currently only four states, namely California, Vermont, Oregon, and Texas, maintain formal data broker registries, which may complicate enforcement of these laws.</td>
    </tr>
    <tr>
      <td style="text-align: center;"><b>Entity Sharing</b></td>
      <td>Data sharing overwhelmingly allowed to corporations, and if reported, mostly allowed to the government and educational/research institutions.</td>
      <td>Respondents were comfortable with data shared to educational and research institutions (85.48%), but uncomfortable with data sharing with government agencies (35.48%) and corporations (24.19%). </td>
      <td>None of the states prohibits sharing data to corporations, the government, and educational/research institutions. </td>
    </tr>
    <tr>
      <td style="text-align: center;"><b>Consumer Rights</b></td>
      <td>The majority of data brokers explicitly guarantee the right to access (88%), correct (81%), and delete data (89%), as well as opt-out of data collection or sharing (96%) and offer protections against discrimination (63.5%). Under half (44%) provide some restrictions on targeted advertising.</td>
      <td>Participants were in favor of options to opt out of data collection or sharing, protections against discrimination, the right to delete data, the right to access data, restrictions on targeted advertising, and the right to correct personal data, in decreasing order. The most popular provision being options to opt out of data collection or sharing.</td>
      <td>Of the 19 states with comprehensive consumer privacy laws, all provide the right to access personal data, 94.44% provide the right to correct and delete, and 47.34% ban discrimination. Some allow opt-outs for targeted advertising for minors (MD, DE, CT).</td>
    </tr>
  </tbody>
</table>

We mapped our most notable findings in Table 3, stratifying by category (data type, data use, entity sharing, consumer rights) and actors (data brokers, consumer preferences, state legislators). Survey results indicate general distrust toward data brokers; they tend to overestimate the amount of sensitive data that brokers collect, while indicating significant disapproval of this collection. One key difference between data broker practices and consumer preferences is the decision to share personal data with corporations. Only 24.2% of respondents approved data sharing to corporations; 99% of data brokers we analyzed allow sharing to corporations.

The two data types that consumers find most permissible for data brokers to collect do in fact align with the two most common data types that data brokers actually collect (commercial transactions and employment data), but the gap between these two sets of percentages are 38.5% and 46.9%, respectively. A similar pattern is true for use cases of personal data: consumers are most likely to approve of personalized advertising and marketing, which are the two most common explicitly permitted use cases of data. For example, marketing was the most common explicitly permitted use case of data by data brokers, at 95.5%, and the second most “approved” use case by participants. However, less than half (43.5%) of that percentage of participants approved of the marketing use case. Figures 11 and 12 display these disparities.

GRAPHADSFHASPDFHAPS FHPASDHJFPASDFHAPSD


A significant portion of respondents expressed uncertainty about which data types they were comfortable with data brokers collecting, which reflects the opaque nature of the industry. Consumers cannot make informed choices without knowledge of the actual and intended use cases of their personal data, especially post-data collection. Our survey results indicate this knowledge gap—the vast majority of respondents had never heard of data brokers, or had limited understanding of their practices, prior to the survey. 

Despite many data brokers allegedly providing the provisions that consumers want (e.g., the right to access and delete personal data, as well as opt-out mechanisms), approximately 95% of surveyed individuals were either unaware of deletion and/or have never requested to delete their personal data. We tested these mechanisms ourselves, and found they were not consistently reliable. In practice, the deletion process often proved cumbersome and ineffective. Several companies required consumers to submit requests through online forms—yet even after providing an email address, we did not receive any follow‑up, and no alternative communication channels were made available. In one case, a listed phone number was connected to an automated voice that redirected callers back to the same unresponsive form. In another, the company denied being a data broker altogether, despite its own privacy policy explicitly acknowledging the sale of personal information. 

Furthermore, results from Californians asked about the DELETE Act reinforce that merely passing a statute is not enough to provide consumers with data protections. Education plays a crucial role in helping individuals understand and exercise their data rights. While only a quarter of surveyed Californians knew about the DELETE Act prior to taking the survey, over 90% expressed willingness to use the tools that the California Privacy Protection Agency will provide during DELETE Act implementation.

However, while education is important, an approach that solely relies on individuals to delete their own data is wholly insufficient for providing meaningful privacy. This deficiency is especially acute given the enormity of the data broker industry, whose business model depends on its secrecy. While data broker companies must comply with privacy statutes in jurisdictions in which they operate, they often turn a blind eye to consumers’ privacy beyond publishing lengthy, difficult-to-read privacy policies. These policies are extremely difficult to parse (even for those with a university-level education) and would take approximately 30 minutes to read each. 

## So what’s next? 
Our analysis shows that regulatory action, paired with data literacy, can help bridge the gap between consumer preferences and the actual practices of data brokers. Regulators should pass laws that provide consumers with more meaningful controls, while also bolstering enforcement of existing privacy laws. They can codify consumer preferences we uncovered, such as strict limits on data sharing with corporations, in law.

Data broker-specific statutes may even be necessary. Regular reporting requirements to enforcement bodies, such as California’s Privacy Protection Agency, are also good steps toward ensuring legal compliance while bringing transparency to an opaque industry. Independent, third-party audits of internal firm processes, as well as any external privacy guarantees (such as the right to delete your data), should be conducted on a regular basis. Furthermore, legal regimes can provide clearer guidance on the definition and responsibilities of data brokers. Currently, data brokers often claim ignorance to evade legal accountability.

Beyond encouraging legal compliance, our findings suggest that agencies can take steps to centralize data broker registration to allow consumers to easily exercise controls over their personal data with one click. While some states have established data broker registries, many stop at data broker registration and do not provide any controls to consumers. As states are laboratories of democracy, state-level action is both desirable and feasible for creating a blueprint for national efforts.

Our results reveal a significant disconnect between consumer preferences, data brokers, and laws. Data brokers cannot self-regulate. Regulators must intervene. Without meaningful action, data brokers will continue profiting from our most intimate data in the shadows—information that can be weaponized against us.

## Sources

* **Pew Research Center:** [Americans’ Attitudes and Experiences with Privacy Policies and Laws](https://www.pewresearch.org/internet/2019/11/15/americans-attitudes-and-experiences-with-privacy-policies-and-laws/) (Nov 2019)
* **The Atlantic:** [Reading the Privacy Policies You Encounter in a Year Would Take 76 Work Days](https://www.theatlantic.com/technology/archive/2012/03/reading-the-privacy-policies-you-encounter-in-a-year-would-take-76-work-days/253851/) (March 2012)
* **NordVPN:** [Privacy Policy Study: How much is your time worth?](https://nordvpn.com/blog/privacy-policy-study-us/)
* **The New York Times:** [Opinion: We Read 150 Privacy Policies. They Were an Incomprehensible Disaster.](https://www.nytimes.com/interactive/2019/06/12/opinion/facebook-google-privacy-policies.html) (June 2019)
* **Congress.gov:** [H.R.2612 - 119th Congress (2025-2026)](https://www.congress.gov/bill/119th-congress/house-bill/2612/all-info)
* **Electronic Frontier Foundation (EFF):** [Why Are Hundreds of Data Brokers Not Registering in States?](https://www.eff.org/deeplinks/2025/06/why-are-hundreds-data-brokers-not-registering-states) (June 2025)
* **EPIC & PIRG:** [The State of Privacy 2025](https://epic.org/wp-content/uploads/2025/04/EPIC-PIRG-State-of-Privacy-2025.pdf) (PDF, April 2025)
* **EPIC:** [Data Brokers Issue Page](https://epic.org/issues/consumer-privacy/data-brokers/)
* **Global Cyber Strategies:** [Data Brokers and Privacy and Security](https://globalcyberstrategies.substack.com/p/data-brokers-and-privacy-and-security)
* **Federal Trade Commission (FTC):** [FTC Takes Action Against Gravy Analytics and Venntel](https://www.ftc.gov/news-events/news/press-releases/2024/12/ftc-takes-action-against-gravy-analytics-venntel-unlawfully-selling-location-data-tracking-consumers) (Dec 2024)
* **Federal Trade Commission (FTC):** [FTC Takes Action Against Mobilewalla](https://www.ftc.gov/news-events/news/press-releases/2024/12/ftc-takes-action-against-mobilewalla-collecting-selling-sensitive-location-data) (Dec 2024)
* **Justin Sherman (Duke/Cyber Policy):** [Data Brokers and Sensitive Data on U.S. Individuals](https://therealistjuggernaut.com/wp-content/uploads/2025/10/1.-Data-Brokers-and-Sensitive-Data-on-US-Individuals-Sherman-2021.pdf) (2021)
* **Adelphi Law Journal:** [Legal Analysis of Data Privacy](https://heinonline.org/HOL/Page?handle=hein.journals/adelphlj22&div=5&g_sent=1&casa_token=) (Vol. 22)
* **Forbes:** [The Real Problem Wasn't Cambridge Analytica But The Data Brokers That Outlived It](https://www.forbes.com/sites/robpegoraro/2020/10/08/the-real-problem-wasnt-cambridge-analytica-but-the-data-brokers-that-outlived-it/) (Oct 2020)