Article

# An Ontology Development Methodology Based on Ontology-Driven Conceptual Modeling and Natural Language Processing: Tourism Case Study

Shaimaa Haridy *Rasha M. Ismail, Nagwa Badr and Mohamed Hashem

Department of Information Systems, Faculty of Computer and Information Sciences, Ain Shams University, Cairo 11566, Egypt

* Correspondence: shaimaaharidy@cis.asu.edu.eg

Abstract: Ontologies provide a powerful method for representing, reusing, and sharing domain knowledge. They are extensively used in a wide range of disciplines, including artificial intelligence, knowledge engineering, biomedical informatics, and many more. For several reasons, developing domain ontologies is a challenging task. One of these reasons is that it is a complicated and time-consuming process. Multiple ontology development methodologies have already been proposed.

However, there is room for improvement in terms of covering more activities during development (such as enrichment) and enhancing others (such as conceptualization). In this research, an enhanced ontology development methodology (ON-ODM) is proposed. Ontology-driven conceptual modeling (ODCM) and natural language processing (NLP) serve as the foundation of the proposed methodology. ODCM is defined as the utilization of ontological ideas from various areas to build engineering artifacts that improve conceptual modeling.

NLP refers to the scientific discipline that employs computer techniques to analyze human language. The proposed ON-ODM is applied to build a tourism ontology that will be beneficial for a variety of applications, including e-tourism. The produced ontology is evaluated based on competency questions (CQs) and quality metrics. It is verified that the ontology answers SPARQL queries covering all CQ groups specified by domain experts. Quality metrics are used to compare the produced ontology with four existing tourism ontologies.

For instance, according to the metrics related to conciseness, the produced ontology received a first place ranking when compared to the others, whereas it received a second place ranking regarding understandability. These results show that utilizing ODCM and NLP could facilitate and improve the development process, respectively.

Keywords: artificial intelligence; natural language processing; ontology-driven conceptual modeling; ontology engineering; OntoUML; OWL; semantic web

![](dt=2026-06-05/ht=05/eee24e16b875474621a6bb3fed6dfd2f774fba618916c23d408361f6e7713017.jpg)

Citation: Haridy, S.; Ismail, R.M.; Badr, N.; Hashem, M. An Ontology Development Methodology Based on Ontology-Driven Conceptual Modeling and Natural Language Processing: Tourism Case Study. Big Data Cogn. Comput. 2023, 7, 101. https://doi.org/10.3390/bdcc7020101

Academic Editors: Manolis Wallace,  
Vassilis Poulopoulos,  
Angeliki Antoniou and  
Martín López-Nores

Received: 21 April 2023

Revised: 15 May 2023

Accepted: 18 May 2023

Published: 21 May 2023

![](dt=2026-06-05/ht=05/a07a118005611e7822825d3e4bf3377c8f410328ab80b73ef093169b884c98d1.jpg)

Copyright: © 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).

# 1. Introduction

In recent years, semantic technologies have advanced rapidly. The semantic web is one of such technologies concerned with transforming the Web from a repository of human-readable content to a format that can be easily understood by machines [1,2]. The popularity of semantic data models such as ontologies and knowledge graphs has grown significantly in recent years [3]. Ontologies are considered to be the backbone of the semantic web [4]. Ontology is defined as an "explicit specification of a conceptualization" [5].

Given that ontologies provide context and meaning to data, they are essential for efficient knowledge extraction and reuse. Additionally, they offer a remedy for syntactic and semantic interoperability problems, which hinder efficient information exchange and collaboration among heterogenous systems [6]. Thus, ontologies have been employed in a wide range of applications across different domains [2].

Including, but not limited to, climate policy development [7], robot inspection systems [8], study of terrorism [9], knowledge about digital extortion attacks [10], drones' semantic trajectories [11], and sentiment analysis [12].

#

big data and cognitive computing

MDPI

Big Data Cogn. Comput. 2023, 7, 101. https://doi.org/10.3390/bdcc7020101

https://www.mdpi.com/journal/bdcc

In this context, ontology engineering has lately garnered great attention [13]. It is defined as "the set of activities that concern the ontology development process, the ontology life cycle, and the methodologies, tools and languages for building ontologies" [14]. One of the objectives of this branch of engineering is to offer a method to develop ontologies. For several reasons, developing domain ontologies is a challenging task. One of these reasons is that it is a complicated and time-consuming process [15]. Further challenges and possible future directions have been proposed in [16].

Ontology development methodology provides guidelines about the organization of activities and tasks, the definition of transitions between them, the selection of methods applied in each task, recommendation of the most suitable tools, and so on. Despite the fact that a variety of methodologies have been proposed [4,15,17], there are still many open issues about ontology development that have yet to be answered [13]. New methodologies continue to be introduced as they propose ontology development from different perspectives and focus on different aspects [15]. In brief, there is no common consensus on an ideal methodology; however, the purpose of developing the ontology may aid in the selection of the most suitable methodology.

One of the most essential activities in the process of ontology engineering is conceptualization. It is concerned with recognizing concepts in the real world in order to construct a model of the relevant domain [18]. Enhancing the activity of conceptualization has a significant impact on the final ontology's quality. The reason for this is that the quality of any model-based artifact is highly constrained by the quality of the model itself [19].

The researchers presented a novel method called ontology-driven conceptual modeling (ODCM) [20], which is defined as the utilization of ontological ideas to construct engineering objects that enhance theory and practice of conceptual modeling. OntoUML is one of the most popular languages in ODCM, which is "a language whose meta-model has been designed to comply with the ontological distinctions and axiomatization of a theoretically well-grounded foundational ontology named UFO (Unified Foundational Ontology)" [21].

UFO is "an axiomatic formal theory based on contributions from Formal Ontology in Philosophy, Philosophical Logics, Cognitive Psychology, and Linguistics" [22].

Natural Language Processing (NLP) is one of the most significant sciences utilized in the semantic web. NLP analyses human natural language in text format using computer techniques to obtain meaningful semantic information [23]. Several NLP methods have been utilized in conjunction with ontologies in many studies, for instance, [24-26].

The goal of this research is to propose an enhanced ontology development methodology (ON-ODM). Ontology-driven conceptual modeling (ODCM) and natural language processing (NLP) serve as the foundation of the proposed methodology. The proposed ON-ODM methodology is applied to build a tourism ontology, which will be useful for many applications such as e-tourism. The remaining sections of the paper are organized as follows. The paper begins with a review of the literature. The proposed methodology is then described in detail, followed by the results and discussion. Finally, the paper ends with conclusions and recommendations for further research.

# 2. Literature Review

Several ontology development methodologies have been defined in the literature. This is because there is no single correct methodology for constructing ontologies, where target application and necessary features aid in the selection of the most appropriate methodology. Therefore, authors competed to suggest methodologies that consider the development process from different perspectives and focus on various aspects. This section summarizes some such methodologies that have been proposed in the past five years. Table 1 compares 20 methodologies to the proposed ON-ODM. The comparison is based on 20 different criteria that cover all stages of the development process.

Big Data Cogn. Comput. 2023, 7, 101

2 of 23

Table 1. Comparison of ontology development methodologies (ODM) from 2018 to 2023.

![](dt=2026-06-05/ht=05/851d19bdb1f73c9857998d211402ed8e3c05b48abb47b52979612cbdb979141b.jpg)

<table><tr><td>ODM</td><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td><td>C6</td><td>C7</td><td>C8</td><td>C9</td><td>C10</td><td>C11</td><td>C12</td><td>C13</td><td>C14</td><td>C15</td><td>C16</td><td>C17</td><td>C18</td><td>C19</td><td>C20</td></tr><tr><td>[15], 2023</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✓</td><td>F</td></tr><tr><td>[17], 2023</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✘</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>S</td></tr><tr><td>[13], 2022</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✓</td><td>✓</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>S</td></tr><tr><td>[27], 2022</td><td>✓</td><td>✘</td><td>✓</td><td>✓</td><td>✘</td><td>✓</td><td>✘</td><td>✘</td><td>✓</td><td>✘</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>S</td></tr><tr><td>[28], 2022</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✓</td><td>✘</td><td>✓</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✘</td><td>S</td></tr><tr><td>[29], 2021</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>S</td></tr><tr><td>[30], 2021</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>S</td></tr><tr><td>[31], 2021</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>S</td></tr><tr><td>[32], 2020</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✘</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>F</td></tr><tr><td>[33], 2020</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>S</td></tr><tr><td>[34], 2020</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>S</td></tr><tr><td>[35], 2020</td><td>✓</td><td>✘</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✓</td><td>✘</td><td>✓</td><td>✘</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>S</td></tr><tr><td>[36], 2020</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>S</td></tr><tr><td>[37], 2020</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>S</td></tr><tr><td>[38], 2019</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✓</td><td>✘</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>S</td></tr><tr><td>[39], 2019</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>S</td></tr><tr><td>[40], 2019</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✓</td><td>✘</td><td>✓</td><td>✘</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>S</td></tr><tr><td>[41], 2019</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>S</td></tr><tr><td>[42], 2018</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>S</td></tr><tr><td>[43], 2018</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✘</td><td>✘</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✘</td><td>✓</td><td>✓</td><td>✓</td><td>S</td></tr><tr><td>ON-ODM</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>S</td></tr></table>

Some criteria have been collected from [13,15,29,31,35,36,44], in addition to another set suggested in the current study. An outline of these criteria is given below.

As noticed from Table 1:

Big Data Cogn. Comput. 2023, 7, 101

3 of 23

Thus, the aim of this research is to propose the ON-ODM semi-automatic methodology that supports all the criteria discussed in Table 1.

The proposed methodology has been applied to the tourism domain. In this sector, a wide variety of ontologies have been introduced. The following are some that are accessible for download and will be used later on during the evaluation process:

# 3. Proposed Methodology

The study proposes an enhanced ontology development methodology (ON-ODM) that offers detailed guidelines for all crucial activities, from requirements specification to ontology assessment. ON-ODM is domain-independent and can be applied to any domain. In this paper, ON-ODM is applied to the context of tourism, because of its significance and impact on promoting the economy of any nation. Egyptian tourism is suggested as a case study due to its richness of tourist cities and monuments, which leads to an abundance of data to be used in the application. Figure 1 depicts the proposed methodology, which is made up of seven major modules. The following subsections provide a detailed explanation of these modules.

![](dt=2026-06-05/ht=05/16a597a134dfddb65ec8563ed427be668dc5fbbf3b3318dfbb33b1f7c5870f78.jpg)

Big Data Cogn. Comput. 2023, 7, 101

4 of 23

# 3.1. Requirements Acquisition Module

The aim of this module is to acquire the list of requirements that the output ontology should fulfill. In ON-ODM, the acquisition of requirements begins with the identification of the domain's main information and user needs. It is followed by an analysis of these needs, and the final list of ontology requirements is specified after that. This module's input consists of the available domain documentation in a variety of forms, in addition to related online resources and knowledge about the domain from experts. The output of this module is the list of ontology requirements in three different forms, which will be covered in further detail in the next subsections.

# 3.1.1. Identification

In this step, at first, the ontology engineer should list all of the resources that are accessible so that they can be used to obtain the necessary information and requirements. These resources include the following:

Then, all the above resources are utilized to extract the main information about the domain and the user needs that should be addressed later by the ontology. Natural language statements are used to outline this description in a document. A document called the Domain Description Document (DDD) is proposed. This document's significance lies in several points:

This is a sample of how the DDD can be used to describe the domain and express the user requirements that reflect their final expectations.

# 3.1.2. Analysis

Currently, the DDD has a wide range of user requirements that have been listed as points. Now, it is time to analyze these needs and turn them from their present form into a set of distinct and well-defined functions that are devoid of repetitions and impractical requirements. The use case diagram can be helpful for this target. It is one of the UML diagrams that focuses on the system requirements as seen from the user's perspective and expresses them as system functionalities. Additionally, it shows the interaction between users (actors) and functions (use cases).

The use case's most significant advantage is that it offers a technique to represent the domain in a diagram that is easy for different roles to comprehend, review, and evaluate. Any of the UML design tools can be utilized in this activity, in the tourism case study, the Rational Rose tool [48] is used.

A portion of the citizen actor use case diagram is illustrated in Figure 2. It includes 15 of the total number of functions that a citizen is capable of performing. For instance: "Obtain photographic permit", "Organize activities and events", "Browse directory", and so on. The figure illustrates that twelve use cases are initiated directly by the citizen, while three are extended from other use cases. Table 2 shows the suggested DDD template applied to the tourism domain

Big Data Cogn. Comput. 2023, 7, 101

5 of 23

Table 2. The suggested DDD applied to the tourism domain.

![](dt=2026-06-05/ht=05/5a4966a126a0928efcf1c17cd8b0796e088b2bedb5a8a3d53e25934580b74227.jpg)

<table><tr><td>Domain:
Tourism
Description:
A sector of economy that deals with all aspects of travel, including activities, services, products, and more ....
Goals:
· Visitor satisfaction.
· Community development.
· Resource protection.
· Economic development.
......</td></tr><tr><td>Scope:
Egyptian tourism
User Requirements:
Requirement 1: Buy museum ticket
Roles: Citizen, Tourism company
Description: The user shall be able to purchase and print a museum ticket online.
Requirement 2: Browse directory
Roles: Citizen
Description: The user shall be able to browse the directory of (tourism companies, hotels, museums, and so on), in order to know their contact information.
......</td></tr><tr><td>Resources:
......</td></tr></table>

![](dt=2026-06-05/ht=05/2e80162ffacd838db8c1e78f0c02a12f9004e4bd4abf583edb82251c8c43940f.jpg)

Big Data Cogn. Comput. 2023, 7, 101

6 of 23

# 3.1.3. Specification

In this activity, the previous list of refined requirements will be transformed into a final set of competency questions (CQs). This approach, which was first described in [49], is one of the widely used methods for specifying ontology functional requirements. These questions are crucial for guiding the ontology development process, since the ontology in its complete version must be capable of answering them. Furthermore, they can be combined with expected results to be employed later in the ontology's evaluation. Table 3 displays sample of the proposed CQs for the Egyptian tourism case study. They are categorized into the following five main categories:

Table 3. Proposed competency questions (CQs) for the Egyptian tourism case study.

![](dt=2026-06-05/ht=05/7bca24b03d920d6b2523b8135c2bc2c7bf667288d90e1c55ff6edfcac1e439fc.jpg)

<table><tr><td>CQ1-1: What is the available information about &quot;Tutankhamun&quot;?</td></tr><tr><td>CQ1-2: How many antiquities were recovered back to Egypt?</td></tr><tr><td>CQ1-3: Where are the &quot;Pyramids&quot; located?</td></tr><tr><td>... ... ...</td></tr><tr><td>CQ2-1: What and where are the historical museums?</td></tr><tr><td>CQ2-2: Where is the &quot;Grand Egyptian Museum&quot; located?</td></tr><tr><td>CQ2-3: What are the different categories of museums available in Egypt?</td></tr><tr><td>... ... ...</td></tr><tr><td>CQ3-1: What are the available tourism companies and their addresses?</td></tr><tr><td>CQ3-2: What is the contact information of &quot;Miracle&quot; company?</td></tr><tr><td>CQ3-3: What are the full details about trips visiting &quot;Marsa Alam&quot;?</td></tr><tr><td>... ... ...</td></tr><tr><td>CQ4-1: What are the available hotels in &quot;Luxor&quot;?</td></tr><tr><td>CQ4-2: What are the rates per night in &quot;Sheraton&quot; hotel?</td></tr><tr><td>CQ4-3: Which hotels have diving centers?</td></tr><tr><td>... ... ...</td></tr><tr><td>CQ5-1: What are the full details about &quot;The Pharaohs Golden Parade&quot; event?</td></tr><tr><td>CQ5-2: What are the events that will occur in year 2023?</td></tr><tr><td>CQ5-3: What are the festivals that take place in Egypt?</td></tr><tr><td>... ... ...</td></tr></table>

At this point, the requirements acquisition module is complete, and three alternative versions of the requirements (DDD, use case diagram, and CQs) are available.

# 3.2. Ontology Development Module

In this module, the ontology is constructed on the basis of previously collected requirements. ON-ODM's development module adheres to the fundamental structure proposed in METHONTOLOGY [50], as this research places the same emphasis on the conceptualization activity. The module consists of four main activities: Specification, Conceptualization, Formalization, and Implementation. They are explained in further detail though the next subsections. This module's result is the initial version of the ontology.

# 3.2.1. Specification

The initial stage entails describing the ontology data in a textual document using natural language. The ontology metadata vocabulary (OMV) [51] is a typical suggestion for the ontologies' description. It enables ontologies to be easily accessed, exchanged over the Internet, and integrated across different domains. The Egyptian tourism ontology's OMV is listed in Table 4.

Big Data Cogn. Comput. 2023, 7, 101

7 of 23

Table 4. The proposed tourism domain ontology 's OMV.

![](dt=2026-06-05/ht=05/c19a193cbd61e9999dc98cb4bff1346ce86404f695098b6b29f2bb21e8d5b7a0.jpg)

<table><tr><td colspan="2">Egyptian Tourism Ontology Metadata Vocabulary OMV</td></tr><tr><td>Ontology Name:</td><td>Egyptian Tourism Ontology (EGYTOUR)</td></tr><tr><td>Location:</td><td>Ain Shams University, Cairo, Egypt</td></tr><tr><td>Party (Organization):</td><td>Faculty of Computer and Information Sciences</td></tr><tr><td>License Model:</td><td>Academic research</td></tr><tr><td>Ontology Type:</td><td>Domain Ontology</td></tr><tr><td>Ontology Domain:</td><td>Tourism</td></tr><tr><td>Ontology Engineering Tool:</td><td>OntoUML Lightweight Editor (OLED)</td></tr><tr><td>Ontology Language:</td><td>OWL</td></tr><tr><td>Ontology Syntax:</td><td>rdfs xml Syntax</td></tr><tr><td></td><td>Describes data and services provided by Egyptian tourism. EGYTOUR represents a semantic description of domain aspects such as concepts, regulations, services, and organizational chart.</td></tr><tr><td>Ontology Task:</td><td></td></tr><tr><td>Ontology Engineering Methodology:</td><td>ON-ODM methodology for building domain ontologies.</td></tr><tr><td></td><td>Non ontological resources: (domain documentation, online resources such as</td></tr><tr><td>Source of Knowledge:</td><td>“Egyptian tourism portal”, knowledge from domain experts, and corpora).</td></tr><tr><td></td><td>Ontological resources: (existing ontologies)</td></tr></table>

# 3.2.2. Conceptualization

This activity is one of the strengths of the proposed methodology, because of its reliance on ODCM, which applies the ontological theories to enhance conceptual modeling [20]. The activity involves designing the model of the target domain, using one of the ODCM languages. The conceptual model of the proposed case study is designed using OntoUML language [21], whose class and relationship stereotypes are elaborated upon in [52]. OntoUML reliance on UFO foundational ontology aids in the application of a common structure that guarantees easy reusability, integration, and interoperability. The OLED [53] tool is utilized, which is a model-based environment for formalizing, developing, and testing OntoUML models.

Due to its quite large size, just two portions of the Egyptian tourism conceptual model are depicted in Figures 3 and 4. Figure 3 shows a sample of the various relations that the citizen ROLE is capable of performing. For instance, the Citizen can:

In Figure 4, the Consumer ROLEMIXIN can make two different CATEGORIES of Reservations to:

SUBKINDs of Place including (Hotel, Resort, Restaurant, Cafe, and Cruise). Some Reservations have a Type like (Full, Half, Breakfast, and All inclusive). Hotels are composite of Floors, which are made up of Rooms. The Room may be (Single, Double, Triple, or Suite).

SUBKINDs of Transportation such as (Airplane, Ship, Bus, and Car). And the Airplane is composed of many Flights.

For both Reservations, a Bill is issued. This Bill is associated with a Payment.

Big Data Cogn. Comput. 2023, 7, 101

8 of 23

![](dt=2026-06-05/ht=05/866562943667b7b9e307fe6e1ce684d402b13a0c18386c4682b0289190d6203d.jpg)

# 3.2.3. Formalization

The prior activity's model is expressed in a modeling language that is only comprehensible by humans. The purpose of this activity is to transform this form into a new one that is interpreted by computer programs. This can be easily performed using the OLED code generation feature. The outcome is an ontology represented by Web Ontology Language (OWL), which is one of the most well-known ontology representation languages. Currently, there is an ontology called EGYTOUR that comprises 228 classes.

# 3.2.4. Implementation

In this activity, the ontology engineer populates the ontology by manually adding new data properties and individuals. Then, they are assigned to the appropriate ontology classes. This can be accomplished with the help of any ontology editor. In the proposed case study, the protégé tool [54] was used. It offers many useful features, the most essential of which is that it supports collaborative construction. The resources defined in Section 3.1.1 assist the ontology engineer in obtaining the necessary information. Due to the case study's excessive amount of data, only a portion of it is used in this activity. This portion consists of 246 data properties and 1602 individuals. Figures 5 and 6 depict a sample of EGYTOUR data properties and individuals, respectively.

Big Data Cogn. Comput. 2023, 7, 101

9 of 23

![](dt=2026-06-05/ht=05/471de3b53bdecddd95395a694c4a2d1a95084432000c632487c602cf461249f7.jpg)

![](dt=2026-06-05/ht=05/38b14755ccc3d3a5b10ca2fe6c63c6f82c5a280f72c6e354ae1d919c7419c8ce.jpg)

Big Data Cogn. Comput. 2023, 7, 101

10 of 23

![](dt=2026-06-05/ht=05/d1f153d227e7afd5c89a60b59356db04ac6a13b253280de86d0f41cf6da062be.jpg)

# 3.3. Ontology Enrichment Module

Unlike many previous methodologies, ON-ODM considers the enrichment module as an essential step in developing ontologies. This is because it assists the ontology engineer with suggestions for classes and relationships that were missing in the initial version of the ontology. There are multiple approaches to enrich ontologies; ON-ODM suggests one that makes use of NLP techniques. Another method that depends on ontology matching was proposed in an earlier work [55]. The scope of this study is to enrich the ontology with relationships extracted from corpus.

The module consists of three main activities: Preprocessing, Relations Extraction, and Enrichment. The module's input is the initial version of the ontology in addition to the corpus documents. An enriched version of the ontology is the output. The module is thoroughly explained in the following sections.

# 3.3.1. Preprocessing

The names of the ontology classes should undergo some preparation before extracting the new relations from corpus. The preprocessing step is essential, because only the words that are determined at this stage will go through the subsequent activities. In ON-ODM, the preprocessing activity consists of four steps:

In EGYTOUR ontology, the preprocessing is fulfilled via the SpaCy library [56], which is a Python open-source library for advanced NLP techniques. It assists in developing applications that comprehend large volumes of text. SpaCy can be used in text preprocessing, natural language understanding, and information extraction. Table 5 lists some examples of the results of this activity.

Big Data Cogn. Comput. 2023, 7, 101

11 of 23

Table 5. Examples of the EGYTOUR ontology's preprocessing results.

![](dt=2026-06-05/ht=05/0682133b150d9827af779ec72d2677052c57b28e36460df42efc19c5d97b5124.jpg)

<table><tr><td>Class Name</td><td>Output</td></tr><tr><td>Museum-Ticket</td><td>Museum Ticket</td></tr><tr><td>Activities-and-Events</td><td>Activity Event</td></tr><tr><td>Indoor-Offices</td><td>Indoor Office</td></tr><tr><td>Fees</td><td>Fee</td></tr><tr><td>Tourist-Relations</td><td>Tourist Relation</td></tr><tr><td>Directors-Affairs</td><td>Director Affair</td></tr></table>

# 3.3.2. Relations Extraction

In this activity, a text corpus is used to extract new candidates for relationships between classes. Any of the numerous NLP-based techniques for information extraction from text may be employed in this activity. Considering that the NLP is not the main focus of this study, a simple and straightforward method is suggested in the tourism case study. The SpaCy library [56] is used for:

The results of this activity are a list of candidates for each class. In addition to the creation of a recommended list of verbs that can be used for identifying relationships. The Open American National Corpus (OANC) [57] is used to identify those new candidates for the EGYTOUR ontology. OANC is an entirely open repository of American English electronic texts. It has 8832 files with a total of approximately 15 million words. As is well known, dealing with such large corpus is not an easy task. It is one of the significant challenges confronting NLP models. For that reason, only a sample of the EGYTOUR ontology is used to apply the extraction approach. This sample consists of 15 classes, yielding 1661 extracted candidates. Table 6 displays two candidates returned from the extraction step.

Table 6. Examples of the EGYTOUR ontology's relations extraction results.

![](dt=2026-06-05/ht=05/c73b109aef500f73e8a44acf4f99b92a4e3e4ebd5bc0de7a996d4878d9dd669b.jpg)

<table><tr><td>Class Name</td><td>Candidate</td><td>Verbs</td></tr><tr><td>Museum-Ticket</td><td>A combined ticket covers all the sights in the palaces, gardens, and museums</td><td>cover</td></tr><tr><td>Museum-Ticket</td><td>Some tickets to The Phantom Menace will, indeed, be sold in advance and no doubt be snapped up by scalpers</td><td>sellsnap</td></tr><tr><td>Car</td><td>The man would get the cars</td><td>get</td></tr></table>

The preprocessing and relations extraction activities are both outlined in Algorithms 1 and 2.

Big Data Cogn. Comput. 2023, 7, 101

12 of 23

Algorithm 1. Relations Extraction from Corpus—Main Algorithm

![](dt=2026-06-05/ht=05/51935ca92fefecb65a4866d73a1b09c9aa49eccdcca1368c050f1e63816e0ddc.jpg)

<table><tr><td colspan="2">INPUT: Proposed ontology (proposedonto)</td></tr><tr><td colspan="2">INPUT: Corpus documents</td></tr><tr><td colspan="2">OUTPUT: List of occurrences for ontology classes (occlist)</td></tr><tr><td colspan="2">BEGIN</td></tr><tr><td>1</td><td>classeslist ← proposedonto.GETCLASSES()</td></tr><tr><td>2</td><td>LOAD corpus documents INTO documentslist</td></tr><tr><td>3</td><td>FOR EACH c IN classeslist DO</td></tr><tr><td>4</td><td>name ← c.GETCLASSNAME() / /Preprosessing</td></tr><tr><td>5</td><td>name.REMOVESTOPWORDS()</td></tr><tr><td>6</td><td>name.REMOVENONALPHABETIC()</td></tr><tr><td>7</td><td>lemma ← name.GETLEMMA()</td></tr><tr><td>8</td><td>FOR EACH doc IN documentslist DO //Call Algorithm 2 to get class occurrences in corpus document</td></tr><tr><td>9</td><td>occlist ← GETOCCURRENCES(lemma,doc)</td></tr><tr><td>10</td><td>END FOR</td></tr><tr><td>11</td><td>END FOR</td></tr><tr><td>12</td><td>RETURN (c,occlist)</td></tr><tr><td colspan="2">END</td></tr></table>

Algorithm 2. Class Occurrences Extraction from Document

![](dt=2026-06-05/ht=05/d5166dcb5f1fec5eb9d5bb8805bd80fefdce62e0712cb49a5b0c474638b83038.jpg)

<table><tr><td colspan="2">INPUT: Lemma of the ontology class (lemma)</td></tr><tr><td colspan="2">INPUT: Corpus document (doc)</td></tr><tr><td colspan="2">OUTPUT: List of document statements in which the class occurred</td></tr><tr><td colspan="2">BEGIN</td></tr><tr><td></td><td>//Sentence Segmentation</td></tr><tr><td>1</td><td>senlist ← doc.GETSENTENCES()</td></tr><tr><td>2</td><td>FOR EACH s IN senlist DO</td></tr><tr><td>3</td><td>IF exists(lema,s) THEN</td></tr><tr><td></td><td>//POS tagging</td></tr><tr><td>4</td><td>POSTAG(s)</td></tr><tr><td>5</td><td>verbs ← s.EXTRACTVERBS()</td></tr><tr><td>6</td><td>outputlist.add (lemma, doc, s, verbs)</td></tr><tr><td>7</td><td>END IF</td></tr><tr><td>8</td><td>END FOR</td></tr><tr><td>9</td><td>RETURN (outputlist)</td></tr><tr><td colspan="2">END</td></tr></table>

# 3.3.3.Enrichment

In this activity, the ontology engineer decides the appropriate action towards each candidate. It is also possible to consult domain experts to benefit from their guidance about the correct decision. Thus, the intervention of a human in this step is crucial in order to avoid ambiguity and redundancy. The engineer approves the candidate if: (1) new, (2) meaningful, and (3) both classes exist in the ontology. While they reject the candidate if: (1) the relation already exists in the ontology, (2) has no meaning, or (3) one of the classes is not defined in the ontology. The approved candidates are added to the ontology as object properties between the participating classes. For instance, Table 7 shows the actions performed with examples from Table 6.

Big Data Cogn. Comput. 2023, 7, 101

13 of 23

Table 7. Examples of the EGYTOUR ontology's enrichment results.

![](dt=2026-06-05/ht=05/f97038ee16e6ad4b0deb45755f9e210986bfe3b7839cae0294c5a62cb5d692ef.jpg)

<table><tr><td colspan="2">Candidate</td><td>Actions</td><td>Reasons</td></tr><tr><td colspan="2">• Cover</td><td>Approved
Add new object property between “Ticket” and “Place” classes</td><td></td></tr><tr><td colspan="2">• sell</td><td>Rejected</td><td>Already defined</td></tr><tr><td colspan="2">• snap</td><td>Rejected</td><td>Scalper class does not exist</td></tr><tr><td colspan="2">• get</td><td>Approved
Add new object property between “Person” and “Car” classes</td><td></td></tr></table>

As a result of the enrichment process, 71 additional object properties are defined for the 15 classes specified in the previous activity. The metrics of the most recent version of the EGYTOUR ontology are illustrated in Figure 7.

![](dt=2026-06-05/ht=05/8abb4a44fe8a187fd235245f8d7b3d5b21fb3b429f847339b3d2aacb11d076cf.jpg)

# 3.4. Ontology Assessment Module

There are many approaches for measuring the quality of the constructed ontology from different perspectives. Summaries of these approaches were proposed in many papers, such as [58-63]. The ontology engineer decides the best-fitting approach for each situation. In ON-ODM, two different approaches are suggested: (1) CQ-based verification and (2) Metric-based evaluation. Both approaches have many advantages, including:

They will be described in depth in the next sections.

# 3.4.1. CQ-based Verification

In this method, the ontology is verified against a collection of predefined criteria, which are represented in the form of competency questions. This approach aids in evaluating the expressiveness criteria [59], that depends on the ontology's ability to provide answers to competency questions. As the process of CQs specification was already a main step (Section 3.1.3) in ON-ODM, this will facilitate its application in assessing the produced

Big Data Cogn. Comput. 2023, 7, 101

14 of 23

ontology. In the current step, the ontology engineer writes SPARQL queries to answer CQs, executes the queries on the produced ontology, and then compares the outcomes with the expected results, which were also defined in Section 3.1.3. Table 8 provides some examples of SPARQL queries suggested to evaluate the EGYTOUR ontology.

Table 8. Examples of EGYTOUR's SPARQL queries.

![](dt=2026-06-05/ht=05/21feaa2ff3d700c7f97cdae8edcfb0adba752bb102f80c4cbf15686e61003d97.jpg)

<table><tr><td>CQ</td><td>SPARQL Query</td></tr><tr><td>CQ1-1</td><td>SELECT ?TutTextWHERE{tour:Tutankhamun tour:O-hasdescription ?Description}?Description tour:hasText ?TutText.}</td></tr><tr><td>CQ2-1</td><td>SELECT ?Historical ?Governorate ?DescriptionWHERE{?Historical tour:O-inLocation ?Loc.?Loc tour:O-inGovernate ?Governate.?Historical tour:O-hasdescription ?Desc.?Desc tour:hasText ?Description.}</td></tr><tr><td>CQ3-1</td><td>SELECT ?Company ?AddressWHERE{?Company rdf:type tour:TourismCompany.?Company tour:hasAddress ?Address.}</td></tr><tr><td>CQ4-1</td><td>SELECT ?HotelWHERE{?Hotel rdf:type tour:Hotel.?Hotel tour:O-inLocation ?Loc.?Loc tour:O-inGovernate tour:Luxor.}</td></tr><tr><td>CQ5-1</td><td>SELECT ?Day ?Month ?Year ?DescTextWHERE{?Event rdf:type tour:PromotionalEvent.tour:The_Paraofs_Golden_Paradetour:O-hasdescription ?Description {?Description tour:hasText ?DescText}?Event tour:inDay ?Day.?Event tour:inMonth ?Month.?Event tour:inYear ?Year.}</td></tr></table>

# 3.4.2. Metric-Based Evaluation

The second approach is based on the computation of ontology quality metrics. Several metrics correlated to different ontology dimensions have been developed. The author of [60] offers a free online platform called OntoMetrics [64] for metric definition and calculation. In the proposed case study, OntoMetrics was used to calculate 11 different metrics, which are categorized into three groups (Schema, Knowledgebase, and Graph). Further information about calculation of the utilized metrics is provided in Table 9. As indicated in [65], these metrics are correlated to four ontology dimensions, as shown below:

Big Data Cogn. Comput. 2023, 7, 101

15 of 23

Table 9. OntoMetrics equations.

![](dt=2026-06-05/ht=05/16aa15a9ffe22dcc1de05dc667620b6e65c95d11d6cfbad1a57ff509862b8a0e.jpg)

<table><tr><td>Metric</td><td colspan="2">Equation</td><td>Description</td></tr><tr><td>Attribute Richness (AR)</td><td>AR = |att| / |C|</td><td>(1)</td><td>|att| is the total number of attributes |C| is the total number of classes in the ontology</td></tr><tr><td>Inheritance Richness (IR)</td><td>IR = |H| / |C|</td><td>(2)</td><td>|H| is the number of subclass relations |C| is the total number of classes</td></tr><tr><td>Relationship Richness (RR)</td><td>RR = |P| / |H| + |P|</td><td>(3)</td><td>|P| is the number of non-inheritance relations |H| is the number of inheritance relations</td></tr><tr><td>Average Population (AP)</td><td>AP = |I| / |C|</td><td>(4)</td><td>|I| is the total number of instances of the knowledge base |C| is the total number of classes</td></tr><tr><td>Class Richness (CR)</td><td>CR = |C&#x27;| / |C|</td><td>(5)</td><td>|C&#x27;| is the number of classes in the knowledge base |C| is the total number of classes</td></tr><tr><td>Absolute Root Cardinality (ARC)</td><td>ARC = nROO⊆g</td><td>(6)</td><td>nROO⊆g represents the number of elements in the set of root nodes ROO in the directed graph g</td></tr><tr><td>Absolute Leaf Cardinality (AC)</td><td>AC = nLEA⊆g</td><td>(7)</td><td>nLEA⊆g represents the number of elements in the set of leaf nodes LEA in the directed graph g</td></tr><tr><td>Average Depth (AD)</td><td>AD = 1/nP⊆g ∑Nj∈P</td><td>(8)</td><td>P represents the set of paths in the directed graph g
nP⊆g is the number of elements in P
Nj∈P is the number of elements on the path j.</td></tr><tr><td>Maximum Depth (MD)</td><td>MD = Nj∈P ∀i∈j(Nj∈P ≥ Ni∈P)</td><td>(9)</td><td>Nj∈P is the number of elements on the path j
Ni∈P is the number of elements on the path i which belong to the set of paths P in the directed graph g</td></tr><tr><td>Average Breadth (AB)</td><td>AB 1/nL⊆g ∑Nj∈L j</td><td>(10)</td><td>L represents the set of levels in the directed graph g
nL⊆g is the number of elements in L
Nj∈L is the number of elements on the level j.</td></tr><tr><td>Maximum Breadth (MB)</td><td>MB = Nj∈L ∀i∈j(Nj∈L ≥ Ni∈L)</td><td>(11)</td><td>Nj∈L and Ni∈L are the number of elements on the level j and i respectively that belong to the set of levels L in the directed graph g</td></tr></table>

# 3.5. Publication

The goal of this activity is to create a translation file for the final version of the ontology and then publish it online. This activity is strongly suggested, so that the constructed ontology supports localization and becomes available to others. Furthermore, the OMV suggested in Section 3.2.1 facilitates the ontology's access and exchange over the Internet. The current version of the EGYTOUR ontology is available only in English. However, for the final release, an Arabic translation file will be created. Web Protégé [66] can be used to easily accomplish the publication activity.

# 3.6. Maintenance

This module handles making any necessary updates or corrections to the ontology. This occurs in two cases: after evaluation or after publishing the online version. Such updates may be required, as it is possible that the ontology might lack certain domain knowledge or contain some errors.

# 3.7. Documentation

The ON-ODM methodology gives the utmost importance to documentation. Since the first activity, many documents have been presented in different forms. The documen

Big Data Cogn. Comput. 2023, 7, 101

16 of 23

tation activity continues until the completion of the ontology and its publication on the Internet with documents that explain all of its components to facilitate ontology reusability, integration, and interoperability.

# 4. Results and Discussion

The objective of this section is to list and discuss the evaluation results of the ontology that has been developed using the proposed methodology (ON-ODM).

# 4.1. CQ-Based Evaluation Results

The EGYTOUR's SPARQL queries defined in Section 3.4.1 were executed on Protégé [54]. These queries represent one question per each CQ group defined by the domain experts in Section 3.1.3. Figures 8-12 show how EGYTOUR was able to successfully answer all queries.

![](dt=2026-06-05/ht=05/07ef029200252c4886f29938313b8de0bccfe8890752d95c97b2f88ea588145f.jpg)

![](dt=2026-06-05/ht=05/1c8871d1d11097331118a3695cda088e2bc1751a98f7e79fca10db1fd4e2476b.jpg)

![](dt=2026-06-05/ht=05/3d728c31de7cb551cd9e78196ed2b702a447aa53149852fbcf333dfe8c678ffd.jpg)

Big Data Cogn. Comput. 2023, 7, 101

17 of 23

![](dt=2026-06-05/ht=05/9bdba159323afbeafdad5629e813ea1b39b46e56f6c898d0c1baf91acd36d97e.jpg)

![](dt=2026-06-05/ht=05/b4e3d3038df4327b22b18d4747428cb4c56791578fd307a6b836f2da69e8ea53.jpg)

# 4.2. Metric-Based Evaluation Results

The OntoMetrics results of the EGYTOUR ontology are displayed in Table 10. Furthermore, four more tourism ontologies were downloaded; (HONTOLOGY [45], IMHO_EVENTS [46], IMHO [46], and TRAVEL [47]). Table 10 compares the OntoMetrics results of the five ontologies. Whereas Tables 11-14 show the EGYTOUR metrics correlated to the four dimensions mentioned in Section 3.4.2.

Table 10. OntoMetrics results.

![](dt=2026-06-05/ht=05/5ff9177318187eefce6921f5fbfa6750d4c205fc99dca94d273a8f6ac298da41.jpg)

<table><tr><td>Ontology</td><td>Classes</td><td>AR</td><td>IR</td><td>RR</td><td>AP</td><td>CR</td><td>ARC</td><td>AC</td><td>AD</td><td>MD</td><td>AB</td><td>MB</td></tr><tr><td>HONTOLOGY</td><td>284</td><td>0.1092</td><td>0.9613</td><td>0.3209</td><td>0</td><td>0</td><td>17</td><td>247</td><td>2.7254</td><td>5</td><td>7.375</td><td>29</td></tr><tr><td>IMHO_EVENT$</td><td>88</td><td>3.9886</td><td>0.9773</td><td>0.6371</td><td>1.4886</td><td>0.0114</td><td>2</td><td>87</td><td>1.9773</td><td>2</td><td>44</td><td>86</td></tr><tr><td>IMHO</td><td>138</td><td>4.3043</td><td>0.9855</td><td>0.68</td><td>1.4638</td><td>0.0072</td><td>2</td><td>137</td><td>1.9855</td><td>2</td><td>69</td><td>136</td></tr><tr><td>TRAVEL</td><td>35</td><td>0.1143</td><td>0.8571</td><td>0.434</td><td>0.4</td><td>0.2286</td><td>12</td><td>24</td><td>2.0833</td><td>4</td><td>3</td><td>12</td></tr><tr><td>EGYTOUR</td><td>228</td><td>1.0789</td><td>1.693</td><td>0.3216</td><td>7.0263</td><td>0.4605</td><td>4</td><td>189</td><td>3.135</td><td>6</td><td>5.7805</td><td>69</td></tr></table>

Table 11. Accuracy-correlated metrics.

![](dt=2026-06-05/ht=05/9c6e45ceaf085d7563bf7477c2be83416b4ecaaefa7f3b089c9999e584574aba.jpg)

<table><tr><td>Ontology</td><td>AR</td><td>IR</td><td>RR</td><td>AD</td><td>MD</td><td>AB</td><td>MB</td><td>AVG</td><td>Rank</td></tr><tr><td>HONTOLOGY</td><td>0.1092</td><td>0.9613</td><td>0.3209</td><td>2.7254</td><td>5</td><td>7.375</td><td>29</td><td>6.5</td><td>4</td></tr><tr><td>IMHO_EVENT$</td><td>3.9886</td><td>0.9773</td><td>0.6371</td><td>1.9773</td><td>2</td><td>44</td><td>86</td><td>19.94</td><td>2</td></tr><tr><td>IMHO</td><td>4.3043</td><td>0.9855</td><td>0.68</td><td>1.9855</td><td>2</td><td>69</td><td>136</td><td>30.71</td><td>1</td></tr><tr><td>TRAVEL</td><td>0.1143</td><td>0.8571</td><td>0.434</td><td>2.0833</td><td>4</td><td>3</td><td>12</td><td>3.21</td><td>5</td></tr><tr><td>EGYTOUR</td><td>1.0789</td><td>1.693</td><td>0.3216</td><td>3.135</td><td>6</td><td>5.7805</td><td>69</td><td>12.43</td><td>3</td></tr></table>

Big Data Cogn. Comput. 2023, 7, 101

18 of 23

Table 12. Understandability-correlated metrics.

![](dt=2026-06-05/ht=05/fe4974c0b6ee79f00cd0e9a6e071ee95cd894181afaf4e104ecd73b87c8a5892.jpg)

<table><tr><td>Ontology</td><td>AC</td><td>Rank</td></tr><tr><td>HONTOLOGY</td><td>247</td><td>1</td></tr><tr><td>IMHO_EVENTS</td><td>87</td><td>4</td></tr><tr><td>IMHO</td><td>137</td><td>3</td></tr><tr><td>TRAVEL</td><td>24</td><td>5</td></tr><tr><td>EGYTOUR</td><td>189</td><td>2</td></tr></table>

Table 13. Cohesion-correlated metrics.

![](dt=2026-06-05/ht=05/78e26c7f934d84521a1a614f3eae47ab903c6cdc7e9cc0c3339ec721687ed3f5.jpg)

<table><tr><td>Ontology</td><td>ARC</td><td>AC</td><td>AVG</td><td>Rank</td></tr><tr><td>HONTOLOGY</td><td>17</td><td>247</td><td>132</td><td>1</td></tr><tr><td>IMHO_EVENTS</td><td>2</td><td>87</td><td>44.5</td><td>4</td></tr><tr><td>IMHO</td><td>2</td><td>137</td><td>69.5</td><td>3</td></tr><tr><td>TRAVEL</td><td>12</td><td>24</td><td>18</td><td>5</td></tr><tr><td>EGYTOUR</td><td>4</td><td>189</td><td>96.5</td><td>2</td></tr></table>

Table 14. Conciseness-correlated metrics.

![](dt=2026-06-05/ht=05/30b8237661a8272dd9f9b7c13809df72b0a242c84fb197bbdd8a615014357ab7.jpg)

<table><tr><td>Ontology</td><td>AP</td><td>CR</td><td>AVG</td><td>Rank</td></tr><tr><td>HONTOLOGY</td><td>0</td><td>0</td><td>0</td><td>5</td></tr><tr><td>IMHO_EVENTS</td><td>1.4886</td><td>0.0114</td><td>0.75</td><td>2</td></tr><tr><td>IMHO</td><td>1.4638</td><td>0.0072</td><td>0.74</td><td>3</td></tr><tr><td>TRAVEL</td><td>0.4</td><td>0.2286</td><td>0.31</td><td>4</td></tr><tr><td>EGYTOUR</td><td>7.0263</td><td>0.4605</td><td>3.74</td><td>1</td></tr></table>

As displayed in Table 10, EGYTOUR is ranked first in the IR, AP, CR, AD, and MD metrics, second in AC, third in AR, ARC, and MB, and fourth in RR and AB.

Low values of AB and MB indicate that the ontology concentrates on the vertical rather than the horizontal modeling of hierarchies. This can be improved by defining additional classes at the same level (siblings).

In EGYTOUR, only a sample of the data properties and extracted relations were used, as mentioned in Sections 3.2.4 and 3.3.2, respectively. Applying the complete case study data will raise the AR and RR values.

Regarding the ARC metric, it counts the number of roots that do not receive is-a relations. Therefore, EGYTOUR's ARC value is low because it contains numerous is-a relations.

Accuracy-correlated metrics measure the degree to which the ontology represents the real-world domain [65]. As illustrated in Table 11, EGYTOUR placed third in the average of accuracy-related metrics due to low AR, RR, AB, and MB values. As mentioned above, increasing those metrics will improve EGYTOUR's rank.

Understandability-correlated metrics determine the comprehension of the elements of the ontology [65]. According to Table 12, EGYTOUR is the second-ranked ontology. This is due to the high value of AC.

Cohesion-correlated metrics refer to the degree to which the classes in the ontology are related to one another [65]. As seen in Table 13, EGYTOUR has a high average of these metrics, indicating that classes are strongly related.

The degree to which the ontological information is useful is measured using conciseness-correlated metrics [65]. Table 14 shows that among ontologies, EGYTOUR has the greatest average. This means that EGYTOUR does not provide any unnecessary or duplicate information.

Big Data Cogn. Comput. 2023, 7, 101

19 of 23

# 5. Conclusions

Ontologies are widely used in a variety of applications and domains. Nonetheless, developing domain ontologies is a difficult and time-consuming process, which is a significant challenge. Many ontology development methodologies have already been proposed; however, there are still certain activities that have not yet been covered and others that could be enhanced. Furthermore, the scarcity of details and applications provided with the methodologies makes most of them challenging to put into practice. In this article, an enhanced ontology development methodology called (ON-ODM) is proposed. The article offers four main contributions:

In the tourism case study, a portion of data was applied. However, during the application of the complete case study data, the below challenges might be encountered:

In future work, there are several directions that can improve the proposed work. For instance, utilizing different techniques of advanced NLP and observing how this can affect the extracted list of candidates and, subsequently, the developed ontology. As well as applying other approaches for ontology evaluation, such as an application-based approach. Finally, investigating ON-ODM in terms of dimensions such as efficiency, ease of use, and adaptability to different and more complex domains.

Author Contributions: Conceptualization: S.H.; methodology: S.H.; data collection: S.H.; analysis and interpretation of results: S.H.; writing—original draft preparation: S.H.; writing—review and editing: R.M.I., N.B. and M.H.; supervision: R.M.I., N.B. and M.H. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.

Data Availability Statement: The most recent version of EGYTOUR ontology has been made available at [67]. In addition to the use case diagram, OntoUML model, SPARQL queries with their answers, and OANC corpus.

Conflicts of Interest: The authors declare no conflict of interest.

# References

Big Data Cogn. Comput. 2023, 7, 101

20 of 23

Big Data Cogn. Comput. 2023, 7, 101

21 of 23

Big Data Cogn. Comput. 2023, 7, 101

22 of 23

Disclaimer/Publisher's Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.

Big Data Cogn. Comput. 2023, 7, 101

23 of 23