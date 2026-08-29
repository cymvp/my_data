# LLM-Driven Ontology Construction for Enterprise Knowledge Graphs

Abdulsobur Oyewale

Liber AI Research

London, United Kingdom

abdulsobur@liberai.org

Tommaso Soru

Liber AI Research

London, United Kingdom

tom@liberali.org

Abstract—Enterprise Knowledge Graphs have become essential for unifying heterogeneous data and enforcing semantic governance. However, the construction of their underlying ontologies remains a resource-intensive, manual process that relies heavily on domain expertise. This paper introduces OntoEKG, a LLM-driven pipeline designed to accelerate the generation of domain-specific ontologies from unstructured enterprise data.

Our approach decomposes the modelling task into two distinct phases: an extraction module that identifies core classes and properties, and an entailment module that logically structures these elements into a hierarchy before serialising them into standard RDF. Addressing the significant lack of comprehensive benchmarks for end-to-end ontology construction, we adopt a new evaluation dataset derived from documents across the Data, Finance, and Logistics sectors.

Experimental results highlight both the potential and the challenges of this approach, achieving a fuzzy-match F1-score of 0.724 in the Data domain while revealing limitations in scope definition and hierarchical reasoning.

Index Terms—artificial intelligence, large language models, semantic models, ontology construction, RDF, knowledge graphs

# I. INTRODUCTION

In the last decade, enterprises have increasingly embraced semantic technologies and the Resource Description Framework (RDF) to unify heterogeneous data sources, enforce shared meaning, and enable interoperable analytics across business domains. This shift reflects the growing recognition that enterprise data assets require explicit semantics to support governance, lineage, and downstream intelligence at scale. Ontologies play a central role in these ecosystems by capturing conceptual structure, constraining vocabularies, and providing the backbone for enterprise knowledge graphs (EKGs).

At the same time, neural models and more recently large language models (LLMs) have begun to transform data engineering and integration workflows. Their ability to extract semantics from unstructured content, suggest schema patterns, perform question answering, and align business terminology introduces powerful new opportunities for knowledge graph (KG) construction [3], [12]. When embedded in transformation pipelines, LLMs offer the potential to accelerate ontology engineering tasks that previously depended on extensive human interpretation and domain expertise.

Yet ontology construction in enterprises remains largely manual, iterative, and resource-intensive. Domain stakeholders, data architects, and semantic engineers must repeatedly

Purpose. To ensure that all employees handle company data responsibly, maintaining confidentiality, integrity, and availability in accordance with corporate governance and regulatory standards.

Scope. This policy applies to all employees, contractors, and third parties with access to company data assets, including structured databases, unstructured files, and analytics platforms.

![](dt=2026-03-23/ht=13/23dc40b25a99c79f762e8d18f4b2ab78252c58858f8fb88ca5f834c5e8c25418.jpg)

negotiate conceptual boundaries, align schemas, and document modelling decisions. This motivates the development of an AI-based copilot for ontology design — one that collaborates with human experts while maintaining rigour, transparency,

arXiv:2602.01276v1 [cs.AI] 1 Feb 2026

and governance compliance. In this paper, we explore how LLM-driven workflows can support the creation and evolution of ontologies specifically for enterprise knowledge graphs, reducing modelling friction while preserving semantic quality.

This paper is organised as follows. Related work is introduced in section II. We describe the approach in section III. We discuss results in section IV. Finally, we conclude.

# II. RELATED WORK

Ontology extraction for the enterprise has been a research topic for more than two decades. One of the first works in this area, titled A Method for Semi-Automatic Ontology Acquisition from a Corporate Intranet, proposed a comprehensive architecture and methodology that leverages corporate intranet text and semi-structured resources to automatically extract and refine a domain-specific ontology, reducing reliance on purely manual ontology engineering [6].

Much more recently, EOAC-LLM has been introduced as a five-step approach based on LLMs to enable the automatic generation of domain-specific event ontologies. Unlike us, the authors focus on a multi-dimensional aggregation method for semantic temporal relation [9].

The paper Ontology Generation using Large Language Models presents two prompting techniques, Memoryless CQbyCQ and Ontogenia. Differently from our method, these emphasise multi-dimensional evaluation including structural criteria, alongside expert assessment [8].

Also, a recent paper, From human experts to machines: An LLM supported approach to ontology and knowledge graph construction explores semi-automatic construction of KGs facilitated by open source LLMs by formulating competency questions, T-Box Development, KGs population and evaluation with minimal human expert involvement. Their focus was on full KG construction, and they employed an LLM as a Judge for automatic evaluation of Retrieval-Augmented Generation (RAG) generated answers and extracted concepts [7].

The paper Leveraging LLM for Automated Ontology Extraction and Knowledge Graph Generation leverages LLM through an interactive user interface. It employs the use of an iterative Chain of Thought algorithm to allow the users to iteratively refine and confirm the ontology based on their preference [1].

Navigating Ontology Development with Large Language Models investigate LLMs capability to generate OWL ontologies from ontological requirements using various prompting techniques, and explores comparing these prompting techniques across multiple state of the art model [11].

# III. APPROACH

This work is centred around two main contributions:

An example of Ontology Construction task can be seen in Figure 1. Starting from an input text about an enterprise

in the cybersecurity sector, an RDF-based ontology is built. Dashed edges identify hierarchical structure, while solid edges identify relations between classes, specifying domain and ranges.

# A. Formalisation

Our Ontology Construction task can be formalised as follows. Given an input text $T$ , we infer the set of classes $C_T$ and the set of properties $P_T$ from the corpus. Each class $c \in C_T$ is associated with a label and a description. Each property $p \in P_T$ is associated with a label, a domain class, and a range class such that $\text{dom}(p) \in C$ , $\text{rng}(p) \in C$ . Classes may also exist in a hierarchy, where $c_1 \subseteq c_2$ means all elements that belong to class $c_1$ are also in class $c_2$ .

In RDF terms, each class $c$ is an instance of owl:Class and each property $p$ is an instance of owl:ObjectProperty. In OntoEKG, datatypes are reified into their own classes as in Schema.org<sup>1</sup>.

# B. Pipeline

![](dt=2026-03-23/ht=13/79e9beaceb305231605721e8c17198a214f65aa1ed6baf0b3bf8e8793f01840c.jpg)

1 https://schema.org/DataType

The pipeline transforms unstructured enterprise text into a structured Ontology ready for Knowledge Graphs. It utilises a two-step LLM process: first to extract classes and properties, and second to reason about the hierarchical relationships between those classes. Below is a detailed workflow of each steps:

# IV. EVALUATION

# A. Benchmarks

As mentioned in section III, a primary objective of this paper is to issue a call to action for the research community. Specifically, to the best of our knowledge, there is a lack of comprehensive benchmarks for evaluating Ontology Construction from text. According to our findings, previous works either have failed to address the task in its entirety or do not meet the required quality standards.

OntoURL is a comprehensive benchmark for evaluating LLMs' capabilities in handling ontologies across three dimensions: understanding, reasoning, and learning. The second and third task of the learning category target class hierarchy construction and property relation construction, respectively [14]. However, these tasks expect a semi-structured input which includes the list of classes and properties. Therefore, OntoEKG and other approaches that extract knowledge from purely unstructured data cannot be evaluated using this benchmark.

Benchmarks such as Text2KGBench and OSKGC emphasise instance-level extraction within an existing framework,

treating the ontology as a constraint rather than the end product [10], [13].

The LLMs4OL initiative hosts a challenge open to LLM-based approaches for Ontology Learning divided into four tasks. Task A (Text2Onto) targets term and type extraction from text; here, the expected output is a list of potential terms for an ontology, while Task C targets Taxonomy Discovery [4]. Unfortunately, the tasks are not arranged in series, which makes it impossible to evaluate a full Ontology Construction pipeline on them. Moreover, Task C mixes class terms with individuals, making no distinction between T-Box and A-Box.

Given the findings above, we opted for the creation of our own dataset, which consists of three use cases — excerpts from internal enterprise policy text in the sectors of data, finance, and logistics. Source code and data can be found at the OntoEKG repository on Github<sup>2</sup>.

# B. Experiments

We ran our experiments on a cloud machine provided by Google Colab<sup>3</sup>. For the Ontological Extraction step, we chose Google Gemini 3 Flash (preview) [5]; for the Entailment step, we chose Anthropic Claude 4.5 Opus [2].

TABLEI ONTOLOGY CONSTRUCTION PERFORMANCE, EXACT MATCH.

![](dt=2026-03-23/ht=13/6212ade875c74a17fb4e6c2c3411b4845f1bd5832e36797305bf1f0967aaf1a6.jpg)

<table><tr><td>Use case</td><td>Precision</td><td>Recall</td><td>F1</td></tr><tr><td>Data</td><td>0.083</td><td>0.133</td><td>0.102</td></tr><tr><td>Finance</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>Logistics</td><td>0.040</td><td>0.062</td><td>0.048</td></tr></table>

TABLE II ONTOLOGY CONSTRUCTION PERFORMANCE, FUZZY MATCH.

![](dt=2026-03-23/ht=13/9e2506f22cc56d613167f0724a29b1399653cc3c58b4f07b471abc6dab891dfd.jpg)

<table><tr><td>Use case</td><td>Precision</td><td>Recall</td><td>F1</td></tr><tr><td>Data</td><td>0.656</td><td>0.807</td><td>0.724</td></tr><tr><td>Finance</td><td>0.095</td><td>0.166</td><td>0.121</td></tr><tr><td>Logistics</td><td>0.366</td><td>0.523</td><td>0.431</td></tr></table>

Results can be seen in Table I and Table II. Table I shows OntoEKG's performance considering only triples that match exactly. In Table II, we adopted embedding-based fuzzy matching to align predicted triples with their gold standard; we set a similarity threshold of (0.94, 0.94, 0.95) for the three use cases. The best performances were reached in the Data use case, where we had an F1-score of 0.724 in the fuzzy setting. The Finance use case was the most challenging with only 0.121 F1-score; this is likely due to different interpretations of the input text, specifically choosing which terms should be included in the ontology and which ones are out of context.

An example generation can be seen in Figure 3, processed from the text in Figure 1. Here, we can see two issues arising from the graph: "Policy" and "GovernanceStandard" were declared one the subclass of the other, implying an equivalence;

$^{2}$ https://github.com/LiberAI/OntoEKG

<sup>3</sup>https://colab.research.google.com

![](dt=2026-03-23/ht=13/74bed129d3c79205c761c355144bacf6dc5f99888be8fca9a82c4ad207e5ab25.jpg)

also, a "然是" property was introduced, which remains ambiguous in RDF terms between rdf:subClassOf and rdf:type.

We tested the Entailment task with different LLMs, including Gemini 2.5 Flash, 2.5 Pro, 3 Flash (preview), and Claude 4.5 Sonnet. We discarded Gemini 2.5 Pro for being inadequate in terms of efficiency. The other models did not meet the expectations during the development phase. These preliminary results confirm the need for a dedicated benchmark which would enable a more appropriate evaluation.

Despite the promising outcomes, we identified several limitations in our approach:

# V. CONCLUSION

In this paper, we have introduced OntoEKG, an LLM-driven approach to Ontology Construction for enterprise knowledge graphs. The initial results suggest that a tedious and resource-intensive task such as semantic modelling can be supported by automated techniques. We have also underscored the need for a comprehensive benchmark for Ontology Construction from unstructured data.

Future work will include the realisation of an end-to-end method for the translation of text into RDF-based semantic models. We will integrate the possibility to handle named individuals and extract entity metadata directly from text, e.g. keeping information about provenance. Furthermore, we expect to enable progressive construction of enterprise ontologies

by feeding the existing proposed model to OntoEKG itself together with the input text, so that the model stays consistent across different source documents. We plan to engage the research community to collaboratively develop a comprehensive benchmark for end-to-end Ontology Construction.

# REFERENCES