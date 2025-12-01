---
layout: post
title: "Data about Data Brokers: Unveiling the Data Broker Industry"
---

Imagine if your location data, tracked through your phone, was sold without your knowledge to random companies, advertisers, and firms. What if you were visiting a pregnancy center? Or attending a protest? Or a place of worship? This scenario is not a dystopian thought experiment, but our lived reality. The Federal Trade Commission alleged that Mobilewalla, a data broker, collected more than 500 million “unique consumer advertising identifiers” linked with precise location data at sensitive sites, which was not anonymized and sold to third-parties. The data was used to create audience segments for advertising purposes, among others: segments included location data from women who visited pregnancy centers or demographic analysis of people who protested the death of George Floyd. And this is not an isolated case—the FTC has also brought action against Kochava for selling tracking data of people visiting reproductive health clinics and the Department of Justice previously charged three data brokers with conspiracy to commit fraud for selling lists of vulnerable Americans (including elderly folks and people with Alzheimer’s) to scammers.

What are data brokers?
According to the Electronic Privacy Information Center (EPIC), data brokers collect, buy, and aggregate extensive personal data on individuals, selling this data (often without explicit consent) to companies that use individual profiles to micro-target subgroups for commercial and/or political gain. In this business model, consumers are the product. Given the extensive adoption of digital technologies and smart wearables, these companies now know (this list is not comprehensive): 
Name
Address
Telephone number
E-mail address
Gender
Age
Marital status
Children
Education
Profession
Income
Political preferences
Real estate ownership
Health information
Sites we visit
Products we buy
Advertisements we click on

By now, you might be feeling uneasy, but perhaps you’re wondering: what is the real harm of this data collection? When these datasets are sold to advertisers and/or bad actors (with few safeguards), malicious entities can buy personal data to manipulate, defraud, or politically target individuals. With the rising popularity of algorithms trained on data, discriminatory profiling may occur, when individuals are categorized based on protected characteristics, such as race, gender, or income, which influences equal opportunity to education, healthcare, and financial services. These practices lead to unfair decisions that impact individuals without their knowledge, such as denied benefits, inflated insurance rates, or lowered credit scores.
 
The lack of transparency and knowledge around the data broker industry is astounding. Only 37% of adults in a 2024 study stated they knew what a data broker was, and only 6% of American adults have used data removal options. 

The current state of play
Some states have passed data privacy acts, with different levels of success and effectiveness. However, few have laws governing the data broker industry specifically. Some states, such as Vermont, California, Texas, and Oregon, have established data broker registries. Some merely require data brokers to register, while others provide consumers with some rights and controls over their rights. The most intensive approach is that advanced by California’s DELETE Act, which requires the California Privacy Protection Agency (CPPA) to create an accessible universal deletion mechanism by January 1, 2026. Consumers will then be able to access the platform to submit requests and then data brokers must comply with deletion requests starting later in the year.

There are also several compliance loopholes with the data broker registration approach that state consumer protection agencies are taking, due to ambiguity or willful blindness around the covered definition of “data brokers.” There have been some bills proposed in Congress, such as the “DELETE Act,” but they have not advanced.

Several additional federal frameworks also govern the data broker industry, but often in domain-specific ways. For example, the Fair Credit Reporting Act (FCRA) regulates consumer reporting agencies that provide information used for credit, employment, or insurance decisions. But, many data brokers evade these rules by avoiding classification as reporting agencies, allowing them to influence such decisions without adhering to accuracy or fairness standards. Other rules include the Gramm-Leach-Bliley Act (GLBA) that governs the way financial institutions share customer information, as well as HIPAA (Health Insurance Portability and Accountability Act) and COPPA (Children’s Online Privacy Protection Act). The Federal Trade Commission also has authority to restrain unfair and deceptive trade practices, but there does not exist a comprehensive federal framework governing data brokers (nor a comprehensive federal consumer privacy act). 

Currently, data broker companies must comply with privacy statutes in jurisdictions where they operate. A problem not unique to the data broker industry, companies often turn a blind eye to consumers’ privacy beyond publishing length, difficult-to-read privacy policies laying out the supposed rights and obligations of companies toward users’ data. As scholars and investigative reporters have noted, the privacy policy regime is insufficient when providing users with meaningful control over their data. In fact, privacy policies were extremely difficult to parse (even for those with a university-level education) and would take approximately 30 minutes to read each, which would amount to hundreds of dollars of work-time lost, per month. These barriers limit the effectiveness of privacy policies: just 9% of U.S. adults say they always read privacy policies before consenting.

What we did
We decided to analyze the interactions between several entities, conducting our analysis through three major entities in the data broker ecosystem: data broker companies, legislatures, and consumers themselves. We conducted an analysis of the three different entities who shape the ecosystem:

[Add a diagram highlighting the views of each of these entities]

Since we wanted to compare three perspectives on the issue (state legislators, actual practices of data broker companies, and consumer preferences), we came up with a standardized rubric for comparing the three entities across four major categories: data collected, data use, data sharing, and user controls.

To systematically analyze the purported practices of data broker companies themselves, we used Privacy Clearinghouse’s data, which compiles data broker information from state registries. After cleaning the dataset of data brokers, we obtained a random sample through simple random sampling of the dataframe, extracting 200 of the approximately 600 data brokers. Then, we downloaded data broker privacy policies. After that, for each privacy policy, we uploaded the privacy policy PDF through Gemini 2.5 Pro (“Reasoning, math & code”) and queried each privacy policy three times: about how entities use information, which third parties they share or sell data with, and consumer rights they provide consumers. We then validated a sample of the data extracted from the LLM and determined that the LLM responses were approximately 96.67% accurate. 

Simultaneously, we conducted a survey of college students using the standardized set of questions. The survey was short and included dropdown questions where participants could easily select which entries they approved of. For example, for a question about data use, participants selected (any/all/none) of various common use cases we listed (biometric, employment, address, geolocation, etc.). We also asked two additional questions for Californian residents about the DELETE Act, arguably one of the strongest state statutes on data broker transparency. We disseminated the survey among college students online.

Lastly, we conducted an analysis of state laws. XXX

What we found
<div id="familiarity-chart"></div>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
  const familiarityData = [
    { answer: "I’ve heard of them but don’t know what they do", count: 21 },
    { answer: "I’ve never heard of data brokers", count: 20 },
    { answer: "I have a basic understanding of their role and practices", count: 17 },
    { answer: "I have a good understanding of their role and practices", count: 1 },
    { answer: "I’m very familiar with how data brokers operate", count: 1 }
  ];

  const margin = {top: 20, right: 30, bottom: 100, left: 40},
      width = 600 - margin.left - margin.right,
      height = 400 - margin.top - margin.bottom;

  const svg = d3.select("#familiarity-chart")
    .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

  const x = d3.scaleBand()
    .range([ 0, width ])
    .domain(familiarityData.map(d => d.answer))
    .padding(0.2);

  svg.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(d3.axisBottom(x))
    .selectAll("text")
      .attr("transform", "translate(-10,0)rotate(-45)")
      .style("text-anchor", "end");

  const y = d3.scaleLinear()
    .domain([0, d3.max(familiarityData, d => d.count)])
    .range([ height, 0]);

  svg.append("g")
    .call(d3.axisLeft(y));

  svg.selectAll("mybar")
    .data(familiarityData)
    .enter()
    .append("rect")
      .attr("x", d => x(d.answer))
      .attr("y", d => y(d.count))
      .attr("width", x.bandwidth())
      .attr("height", d => height - y(d.count))
      .attr("fill", "#69b3a2");

</script>
→ interpretation; similarities and differences
→ briefly, limitations of findings and the nuances of interpretation

[Anecdotes]
From calling or other things

[Discuss recommendations]
[go into limitations and theories of privacy]

Sources
