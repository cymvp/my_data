# Construct, Align, and Reason: Large Ontology Models for Enterprise Knowledge Management

Yao Zhang $^{a,b}$ , Hongyin Zhu $^{a,b}$

a Yonyou AI Lab,

b Yonyou Network Technology Co., Ltd.,

# ARTICLE INFO

Keywords: ontology construction large language model knowledge graph graph encoder

# ABSTRACT

Enterprise-scale knowledge management faces significant challenges in integrating multi-source heterogeneous data and enabling effective semantic reasoning. Traditional knowledge graphs often struggle with implicit relationship discovery and lack sufficient semantic understanding for complex question answering. To address these limitations, we introduce a unified construct-align-reason framework, the large ontology model (LOM).

We first build a dual-layer enterprise ontology from structured databases and unstructured text, subsequently fusing these sources into a comprehensive enterprise ontology. To enable instruction-aligned reasoning, we propose a unified three-stage training pipeline: ontology instruction fine-tuning to improve structural understanding; text-ontology grounding to strengthen node semantic encoding; and multi-task instruction tuning on ontology-language pairs with curriculum learning to enhance semantic reasoning and generation.

We also construct comprehensive training and evaluation datasets covering diverse ontology reasoning tasks. On this benchmark, our 4B-parameter LOM achieves $89.47\%$ accuracy and outperforms DeepSeek-V3.2 on complex graph reasoning, indicating effective fusion of ontology structure and language.

# 1. Introduction

In the wave of digital transformation, enterprise knowledge management faces unprecedented challenges. Traditional systems typically rely on relational databases or basic document management systems to store and manage enterprise knowledge. While these approaches can store structured data effectively, they struggle with complex unstructured knowledge and inter-entity relationships. In recent years, knowledge graphs have emerged as a powerful representation that models enterprise knowledge as graphs, using nodes and edges to capture entities and their relationships, thereby enabling more intelligent querying and reasoning.

Existing approaches for enterprise ontology construction and reasoning face distinct limitations. On the construction side, methods often treat structured databases and unstructured text in isolation. Traditional schema mapping tools [6] struggle to identify implicit relationships (e.g., missing foreign keys) in legacy databases, while standard information extraction models [23] lack the domain adaptability to merge these structured backbones with rich textual knowledge.

On the reasoning side, a significant semantic gap persists: graph neural networks (GNNs) [21] capture topology but lack the reasoning depth for complex business questions, whereas large language models (LLMs) [14] possess semantic knowledge but often fail to adhere to rigorous graph structures. This disconnect hampers the ability to perform reliable, multi-hop reasoning over heterogeneous enterprise data. To address these challenges, we present a large ontology model (LOM) that unifies multi-source ontology construction with a structure-aware instruction tuning pipeline,

effectively bridging the divide between data integration and semantic reasoning.

Constructing an enterprise ontology is a non-trivial undertaking. We employ a layered approach to build ontologies from both structured databases and unstructured text. For structured databases, where explicit foreign keys are frequently missing, we propose a multi-factor relationship discovery algorithm that analyzes both schema metadata and data content overlap to uncover implicit connections. This enables the construction of a dual-layer ontology comprising an abstract schema layer and a concrete instance layer.

For unstructured text, we utilize an LLM&LOM-based pipeline that performs entity-relation extraction, link prediction, and robust entity disambiguation via a hybrid of symbolic rules and semantic embeddings. Finally, we fuse these heterogeneous sources into a unified enterprise ontology through cross-modal alignment based on tag-description matching.

The second challenge lies in training an LOM capable of deeply understanding and reasoning over these heterogeneous enterprise ontologies. Existing methods often fail to bridge the semantic gap between graph structures and textual knowledge. To address this, we implement a unified three-stage training pipeline. First, we employ ontology instruction fine-tuning to endow the LLM with foundational ontology structural understanding.

Second, we introduce a text-ontology grounding stage that trains an alignment projector to fuse textual semantics with ontology features via intra- and inter-type alignment. Finally, we conduct multi-task instruction tuning over ontology-language pairs with curriculum learning, guiding the model from simple predictive tasks to complex generative reasoning. To support this pipeline, we construct a comprehensive CoT-enhanced dataset that captures algorithmic reasoning paths, enabling

arXiv:2602.00029v1 [cs.CL] 18 Jan 2026

*Corresponding author

zhuhongyin@yonyou.com (H. Zhu) ORCID(s): 0000-0001-5786-7594 (H.

First Author et al.: Preprint submitted to Elsevier

Page 1 of 8

the model to learn the logic behind ontology-centric operations rather than simple answer mapping.

We conduct systematic evaluation on our datasets, and the 4B-parameter LOM achieves state-of-the-art performance. Our main contributions are:

# 2. Related Work

# 2.1. Ontology Construction from Heterogeneous Data

Recent studies have revisited ontology construction from relational databases by incorporating agent-based reasoning and large language models to reduce manual schema engineering. Trajanoska et al. [17] propose a multi-agent framework in which specialized agents collaboratively perform schema interpretation, mapping rule generation, and semantic alignment between relational tables and knowledge graph schemas. While this approach improves modularity and interpretability, it still relies on explicit coordination protocols and assumes relatively clean schema-level signals, limiting its robustness in large-scale enterprise databases with implicit or noisy relational structures.

More recently, retrieval-augmented and autonomous ontology construction methods have emerged. Nayyeri et al. [13] introduce a RAG-based framework that retrieves schema fragments and instance-level evidence to guide LLM-driven ontology generation, demonstrating improved adaptability across heterogeneous databases. In parallel, AutoSchemaKG [2] explores dynamic schema induction from web-scale corpora, enabling autonomous ontology evolution without predefined schemas. However, these methods primarily focus on either structured databases or unstructured text in isolation, and they do not explicitly address cross-source ontology alignment or the discovery of implicit relational patterns such as hidden foreign keys and enterprise-specific relationship semantics.

A complementary line of research focuses on declarative mapping frameworks for constructing RDF knowledge graphs from structured and heterogeneous data sources. SDM-RDFizer [6] presents an efficient RML interpreter

optimized for large-scale RDF generation through parallel execution and standards-compliant mapping, enabling deterministic and reproducible knowledge graph construction. Building upon such infrastructures, Assche et al. [1] study backward compatibility and rule reuse in RML mapping pipelines, addressing maintainability challenges under evolving schemas. While these systems provide robust engineering solutions for knowledge graph materialization, they rely on manually defined mappings and predefined schemas, and do not address automated ontology induction, implicit relationship discovery, or instruction-aligned reasoning over enterprise knowledge graphs, whichare the focus of our work.

# 2.2. Ontology Reasoning

Recent advances in large language models have motivated the integration of graph-structured knowledge into language-centric reasoning frameworks. Early graph language models focus on encoding graph structures into LLM-compatible representations. HiGPT [16] introduces a heterogeneous graph language model that aligns graph nodes and relations with textual embeddings, enabling joint reasoning over graph topology and semantics. Building upon this paradigm, GraphAgent [19] frames graph reasoning as an agentic process, allowing LLMs to iteratively plan, reason, and interact with graph environments.

These approaches demonstrate the potential of agent-based graph reasoning, yet they primarily target generic graph benchmarks and do not explicitly consider the scale, heterogeneity, and dynamic evolution characteristic of enterprise ontologies.

To enhance LLMs' capability to reason over graph structures, recent work explores instruction tuning and foundation model designs tailored to graph data. GraphInstruct [10] proposes a large-scale instruction dataset covering diverse graph algorithms and demonstrates that instruction-tuned LLMs can acquire non-trivial graph reasoning abilities without explicit graph neural networks. Complementarily, G-Reasoner [9] presents a foundation model for unified reasoning over graph-structured knowledge, emphasizing generalization across tasks and graph modalities.

While these methods significantly advance instruction-aligned graph reasoning, they mainly focus on static or synthetic graph settings and provide limited support for grounding graph reasoning in real-world enterprise semantics and heterogeneous knowledge sources.

Another line of research enhances LLM reasoning through explicit interaction with knowledge graphs [14]. Survey work [24] systematically reviews the emerging capabilities of LLMs in KG construction and reasoning, highlighting both opportunities and limitations. On the modeling side, retrieval- and path-based approaches aim to improve multihop reasoning. GNN-RAG [11] employs graph neural networks to guide retrieval of relevant subgraphs for LLM reasoning, while Zhou et al. [20] introduce reflective mechanisms to iteratively refine KG-based reasoning. Paths-over-Graph [15] further explores path-centric reasoning strategies for complex multi-hop queries. In applied settings, Mendes

Large Ontology Models for Enterprise Knowledge Management

First Author et al.: Preprint submitted to Elsevier

Page 2 of 8

et al. [12] demonstrate the feasibility of deploying LLM-powered KGQA systems in enterprise environments. However, these approaches typically treat the knowledge graph as an external tool or retrieval source, rather than jointly modeling ontology construction, graph representation, and instruction-aligned reasoning within a unified framework.

# 3. Approach

In this section, we present the LOM-based construct-alignment-reason framework, where construct denotes ontology construction, align denotes ontology-text alignment, and reason denotes generative ontology reasoning. We first introduce the model architecture, followed by unified training and inference strategies for complex ontology reasoning. We then detail the construction of our CoT-enhanced graph reasoning dataset. Finally, we describe our ontology construction methodology, which integrates structured databases and unstructured text into a unified enterprise ontology.

# 3.1. Large Ontology Model

![](dt=2026-03-23/ht=13/b90d9e90317a50ab70d8094127c872454ceb002e7e081681299f67ff6c8e38dd.jpg)

As illustrated in Figure 1, the LOM architecture is situated within the enterprise knowledge operations platform, bridging bottom-layer business systems & data (structured and unstructured data) with top-layer ontology applications. Specifically, an ontology construction layer is introduced, constructed from structured and unstructured data. Data flows through an ontology interface into the model, which employs a heterogeneous graph representation $\mathcal{G} = (\mathcal{V},\mathcal{E},\mathcal{N},\mathcal{R})$ to jointly model structured and unstructured data.

The core processing unit consists of three key components: (1) a graph encoder [7, 5] that utilizes a graph transformer to capture structural dependencies; (2) a user input module that processes natural language inquiries (e.g., procurement requests) via a text encoder; and (3) the LOM hybrid cluster, where a linear alignment projector maps graph features into the LOM's embedding space. This deep

fusion enables the model to perform CoT reasoning over enterprise ontologies.

# 3.1.2. Training Method

We begin by fine-tuning the LLM using instruction tuning [4] to enhance ontology-centric understanding and reasoning, and then integrate it into the large ontology model framework. The training objective is:

$$
\mathcal {L} = - \mathbb {E} _ {\mathcal {G}, \mathbf {q}, \mathbf {a} \sim D} \log P (\mathbf {a} \mid (\mathcal {G}, \mathbf {q}); \theta) \tag {1}
$$

where $\mathcal{G}$ is the graph, $\mathbf{q}$ the query, $\mathbf{a}$ the answer, and $\theta$ the model parameters. Given $(\mathcal{G},\mathbf{q})$ , this model is trained under $\theta$ to output correct $\mathbf{a}$ , endowing the model with foundational graph understanding and reasoning.

During the training process, we align not only the knowledge graph data but also the ontology structure. Then we train the alignment projector and graph-token embeddings to align features between the text encoder and GNN. Specifically, we employ graph instruction alignment, where the LLM is trained to understand graph-structured data via graph-token-instruction pairs. We define two alignment datasets for this stage:

Intra-type alignment enhances understanding of tokens within a single meta-type by training the LLM to output the correct text sequence for a given graph-token sequence. The dataset is defined as:

$$
\mathcal {D} ^ {\text {i n t r a}} = \left\{\left[ \left(\mathbf {e} _ {k}, s _ {i}\right), \dots \right], \left[ \left(\mathbf {c} _ {k}, \mathbf {c} _ {s _ {i}}\right), \dots \right] \right\} \tag {2}
$$

We optimize this alignment using a next-token-prediction cross-entropy objective:

$$
\mathcal {L} _ {\text {i n t r a}} = \mathbb {E} _ {d \sim \mathcal {D} ^ {\text {i n t r a}}} [ \mathrm {C E} (d [ 0 ] \mid \mathrm {L L M} (d [ 1 ])) ] \tag {3}
$$

Inter-type alignment introduces multiple meta-types for complex heterogeneous relations, using tokens from different meta-types:

$$
\mathcal {D} ^ {\text {i n t e r}} = \{\left[ \left(\mathbf {e} _ {m}, s _ {m}\right), \left(\mathbf {e} _ {n}, s _ {n}\right), \dots \right], \left[ \left(\mathbf {c} _ {m}, \mathbf {c} _ {s _ {m}}\right), \left(\mathbf {c} _ {n}, \mathbf {c} _ {s _ {n}}\right), \dots \right] \} \tag {4}
$$

Similarly, we train the LLM to predict the text sequence from the heterogeneous graph tokens:

$$
\mathcal {L} _ {\text {i n t e r}} = \mathbb {E} _ {d \sim D ^ {\text {i n t e r}}} [ \mathrm {C E} (d [ 0 ] \mid \mathrm {L L M} (d [ 1 ])) ] \tag {5}
$$

where $\mathrm{CE}(\cdot)$ denotes the cross-entropy loss function. In both intra- and inter-type alignment tasks, $d[0]$ represents the target text sequence (ground truth), while $d[1]$ is the input sequence of graph tokens processed by the LLM. The graph token definitions are: $\mathbf{e}_i$ is the $i$ -th graph token, $s_i$ its metatype, and $\mathbf{c}_i$ the corresponding text description. This builds a foundation for understanding graph-structured data.

Finally, we perform multi-task fine-tuning based on the above alignment to enhance the model's capabilities across predictive and generative tasks. This phase utilizes diverse ontology-language instruction formats defined as:

$$
D ^ {\text {m u l t i}} = \{\left\{\left(\mathbf {x} _ {\text {p r e d}}, \mathbf {x} _ {\text {r e a s o n i ng}}\right) \mid \mathbf {x} _ {\text {g e n}} \right\}, \left\{\mathcal {G} ^ {\exp} \mid \mathcal {G} ^ {\mathrm {s k g}} \right\}, \mathbf {t} _ {i}, \mathbf {a} _ {i} \} \tag {6}
$$

Large Ontology Models for Enterprise Knowledge Management

First Author et al.: Preprint submitted to Elsevier

Page 3 of 8

The model is optimized to generate the target answer $\mathbf{a}_i$ given the instruction $\mathbf{t}_i$ and graph context $\mathcal{G}$ :

$$
\mathcal {L} _ {\text {m u l t i}} = - \mathbb {E} _ {(\mathbf {t}, \mathbf {a}, \mathcal {G}) \sim D ^ {\text {m u l t i}}} \log P (\mathbf {a} \mid \mathbf {t}, \mathcal {G}; \theta) \tag {7}
$$

where $P(\mathbf{a} \mid \mathbf{t}, \mathcal{G}; \theta)$ represents the conditional probability of generating the correct answer $\mathbf{a}$ given the instruction $\mathbf{t}$ and graph context $\mathcal{G}$ , parameterized by the model weights $\theta$ . The input features $\mathbf{x}_{\mathrm{pred}}$ , $\mathbf{x}_{\mathrm{reasoning}}$ , and $\mathbf{x}_{\mathrm{gen}}$ correspond to predictive, reasoning, and generative tasks, respectively. $\mathcal{G}^{\mathrm{exp}}$ denotes explicit graph topology, while $\mathcal{G}^{\mathrm{skg}}$ refers to the schema-enhanced knowledge graph structure. The pair $(\mathbf{t}_i, \mathbf{a}_i)$ corresponds to the task-specific instruction and the ground-truth answer.

To ensure stable convergence and effective knowledge acquisition, we adopt a curriculum learning strategy that organizes training samples by difficulty. The model is first exposed to simpler predictive tasks before progressing to complex generative reasoning scenarios, thereby systematically building its capability to handle diverse graph-instruction pairs.

# 3.1.3. Dataset Construction

Existing graph-task datasets primarily enable LLMs to learn simple reasoning tasks, while complex graph reasoning tasks (e.g., minimum spanning tree, PageRank) remain difficult to learn. To address this, we introduce a CoT-enhanced dataset for learning graph reasoning. The dataset includes problem descriptions, chain-of-thought reasoning, and final answers, enabling LLMs to learn the reasoning processes of complex reasoning tasks and improve performance on graph tasks.

We further design trajectory-generation problems for reasoning tasks via a CoT-enhanced trace generator implementing four core reasoning tasks: Dijkstra shortest path, Kahn topological sorting, Prim minimum spanning tree, and predecessor node search. A stepwise recording system captures intermediate states during execution, including initialization, node visitation, and state updates, and produces natural language chain-of-thought explanations. This converts complex reasoning execution into structured training data, allowing LLMs to learn full reasoning logic rather than memorizing answers.

The final dataset contains 115k training samples spanning 19 graph reasoning tasks, from simple traversals (BFS, DFS) to complex reasoning tasks (shortest path, MST, PageRank). Data are split into two stages: 20k samples for foundational graph language model training and 95k samples for deep fusion training. We additionally build 190 evaluation samples (10 per task) for performance assessment. All data are stored in PyG format, including node feature encodings (sentence-transformer, 768-dim) and graph structure, supporting both heterogeneous and homogeneous graph training.

# 3.2. Ontology Construction

# 3.2.1. Ontology Construction from Structured Data

To address the semantic impedance mismatch and scalability challenges inherent in converting heterogeneous relational databases into ontologies, we propose a layered, decoupled, and incrementally evolving construction framework. We adopt a two-stage scanning strategy to build the ontology $\mathcal{G}_S = (\mathcal{V}_S,\mathcal{E}_S)$ . First, we extract schemas from the source tables $\mathcal{T} = \{T_1,\dots,T_n\}$ to identify explicit keys (e.g., fields containing 'id' or 'code').

To complement this, we utilize LOMs to detect implicit associations, capturing semantic variants like 'number' that elude simple keyword matching. Second, we perform a sliding-window deep scan to infer implicit foreign keys, utilizing a random sample of 1,000 records to assess value overlap. We define a multifactor confidence function $\Phi (\cdot)$ to quantify the relationship between columns $c\in T_i$ and $c^{\prime}\in T_{j}$ :

$$
\Phi (c, c ^ {\prime}) = \lambda_ {1} S _ {\text {n a m e}} (c, c ^ {\prime}) + \lambda_ {2} \mathbb {I} _ {\text {t y p e}} (c, c ^ {\prime}) + \lambda_ {3} S _ {\text {o v e r l a p}} (c, c ^ {\prime}) + \lambda_ {4} S _ {\text {c a r d}} (c, c ^ {\prime}) \tag {8}
$$

where $S_{\text{name}}$ measures semantic similarity, $\mathbb{I}_{\text{type}}$ ensures data type compatibility, $S_{\text{overlap}}$ quantifies value distribution overlap, and $S_{\text{card}}$ infers cardinality patterns (e.g., one-to-many). An edge is established if $\Phi > \delta$ . We construct a dual-layer ontology: the inter-table layer forms a graph via the above method, refined by $k$ -core decomposition to retain the topological backbone, while tables are categorized top-down to abstract higher-level concepts. Finally, instance nodes are connected to their corresponding table nodes to bridge data and concepts.

# 3.2.2. Ontology Construction from Unstructured Data

To harness the rich enterprise knowledge embedded in unstructured text, we construct the ontology $\mathcal{G}_U = (\mathcal{V}_U,\mathcal{E}_U)$ using a systematic pipeline comprising document parsing, triple extraction [22], entity disambiguation, and graph construction. Specifically, during the extraction phase, we deploy a locally hosted vLLM-accelerated Qwen3 [18] model (temperature set to 0.1) to process documents segmented into 2,000-token chunks with a 150-token overlap. This model is tasked with extracting entities along with their descriptive attributes and identifying relationships from the set {MENTS, RELATES_TO, IS_A}.

To resolve non-standard entity mentions and ambiguity, we apply layered merging rules: (1) initial surface matching via edit distance $(\geq 0.85)$ and substring containment $(\geq 60\%)$ ; (2) domain-specific normalization; and (3) deep semantic matching using BGE-M3 [3] embedding cosine similarity $(\geq 0.85)$ . This ensures synonymous mentions are consolidated into canonical nodes in $\mathcal{V}_U$ .

The unified heterogeneous graph $\mathcal{G} = \mathcal{G}_S \cup \mathcal{G}_U$ is synthesized by integrating these two layers. We employ a heuristic tagging algorithm to generate attribute tags for file nodes in $\mathcal{G}_U$ , which are subsequently matched against descriptions in the instance layer of $\mathcal{G}_S$ to establish semantic associations $\Psi: \mathcal{V}_U \to \mathcal{V}_S$ , effectively bridging the semantic gap

Large Ontology Models for Enterprise Knowledge Management

First Author et al.: Preprint submitted to Elsevier

Page 4 of 8

between raw text and relational data. Furthermore, we utilize the link prediction capabilities of the LOM to infer missing relationships, thereby densifying and completing the graph structure.

# 4. Experiments

# 4.1. Dataset

We develop a graph reasoning dataset for training and evaluation, which encompasses 19 diverse tasks across six categories: traversal, graph properties, node similarity, paths and flows, centrality, and tree structures. The data, stored in PyG format, incorporates 768-dimensional node features encoded by sentence-transformers and detailed edge structures. The training corpus consists of 95,000 samples supporting multi-stage instruction tuning, while the evaluation benchmark comprises 190 samples (10 per task type) stratified by difficulty: simple (e.g., BFS, node degree), medium (e.g., connectivity), and difficult (e.g., shortest path, PageRank). The graphs vary in size from 5 to 50 nodes and 5 to 200 edges, covering undirected, directed, and weighted types.

# 4.2. Hyper-parameters

We adopt Qwen3-4B-Instruct as the backbone LLM, featuring 4B parameters, a hidden size of 2,560, 36 layers, 32 attention heads, and a vocabulary of 151,936, with the maximum generation length set to 4,096 tokens. To capture graph structural information, we utilize a pre-trained graph transformer encoder consisting of 3 layers with a hidden dimension of 128 and 8 attention heads. Node semantics are initialized using the all-mynet-base-v2 SentenceTransformer to generate 768-dimensional features. These features are processed by the graph encoder via dimension-matching projection layers and finally mapped to the LLM's 2,560-dimensional embedding space through a linear graph projector.

# 4.3. Evaluation Metrics

We evaluate performance using accuracy as the primary metric on a benchmark comprising 190 test samples, evenly distributed across 19 distinct graph reasoning tasks. These tasks span six categories: traversal (BFS, DFS), graph properties (node degree, neighbor query, edge existence, connectivity, cycle detection, bipartiteness, connected components, diameter), node similarity (common neighbors, Jaccard similarity), paths and flows (predecessor, topological sort, shortest path, maximum flow), centrality (PageRank, clustering coefficient), and tree structure (minimum spanning tree).

For assessment, we apply strict task-specific correctness criteria: exact order for traversals, precise values for numerical tasks, correct classifications for boolean queries, set matching for list outputs, and validity checks for path-related tasks.

# 4.4. Main Results

As shown in Figure 2, LOM-4B demonstrates superior performance across the benchmark, achieving the top rank with an overall accuracy of $89.47\%$ (170/190 correct). This represents a substantial improvement over competing

approaches, validating the effectiveness of our proposed method in handling complex graph reasoning tasks. The model's architecture, which integrates a graph encoder with a powerful large language model, evidently provides a distinct advantage in interpreting and solving graph-structured problems.

The comparison further highlights the performance gap between specialized and general-purpose models. The second-tier models, including DeepSeek-V3.2 [8], GraphInstruct [10], and Doubao-1.8, achieve comparable results in the range of $78.42\%$ to $79.47\%$ , yet they trail LOM-4B by approximately $10\%$ . Notably, the base Qwen3 models (QwenMax and Qwen3-4B-Instruct) exhibit significantly lower accuracies of $57.37\%$ and $18.95\%$ respectively, underscoring the necessity of targeted instruction tuning and structural encoding for effective graph reasoning execution.

![](dt=2026-03-23/ht=13/877bd0b60ee68feea1a72c663f784358865e35811649ee2de6e0268a49c113cf.jpg)

# 4.5. Analysis

As shown in Figure 3, we present a detailed breakdown of model performance across 19 specific graph tasks. On fundamental graph traversal and property retrieval tasks—such as BFS, DFS, neighbor queries, and degree calculation—most advanced models, including LOM-4B, DeepSeek-V3.2, and GraphInstruct, achieve near-perfect accuracy (100%). This indicates that current LLMs, when equipped with appropriate training or structural awareness, have successfully mastered the basic syntax and local connectivity rules of graph data.

However, a significant divergence in performance emerges on computationally intensive and global reasoning tasks. LOM-4B exhibits remarkable robustness on algorithmic challenges that baffle other models. Specifically, for PageRank and minimum spanning tree (MST) tasks, where other leading models like DeepSeek-V3.2 and GraphInstruct score near $0\%$ , LOM-4B maintains high accuracy ( $80\%$ and $60\%$ respectively). Similarly, in topological sorting, LOM-4B achieves $100\%$ accuracy, outperforming the next best competitor by a margin, demonstrating its superior capacity to reason about global graph structures and dependencies.

The results also shed light on the impact of training stages and model specialization. Comparing LOM-Stage2, LOM-Stage3, and the final LOM-4B reveals a clear progression in capability, particularly for complex tasks like bipartite matching and shortest paths. While general-purpose

Large Ontology Models for Enterprise Knowledge Management

First Author et al.: Preprint submitted to Elsevier

Page 5 of 8

![](dt=2026-03-23/ht=13/ed2e4353edbefc9f6d15d65f578695d8b239db926a764938831457f4047d2de4.jpg)

models like Doubao-1.8 and DeepSeek-V3.2 show sporadic strengths (e.g., $100\%$ in maximum flow or shortest path), they lack the consistent versatility of LOM-4B. The contrast with Qwen-Max further emphasizes that scale alone is insufficient for graph reasoning; the specialized architecture and instruction tuning of LOM are critical for bridging the gap between simple retrieval and complex algorithmic execution.

# 4.6. Ablation Study

As shown in Figure 1, we conduct an ablation study to quantify the contribution of each key component in LOM4B. The full model achieves the highest accuracy of $89.47\%$ . Removing the CoT reasoning mechanism leads to a significant drop of over $11\%$ , reducing accuracy to $78.42\%$ . This indicates that explicit reasoning steps are crucial for guiding the model through complex multi-step graph reasoning tasks, preventing it from jumping to incorrect conclusions and ensuring more robust problem-solving strategies.

The impact of instruction tuning and structural encoding is even more profound. Without instruction tuning ("w/o

Table 1 Ablation Study Results

![](dt=2026-03-23/ht=13/63b2126bfa853a5529c460eaf6dda9f385f2a64129bbe2c327048ab81b3e7b4c.jpg)

<table><tr><td>Settings</td><td>Accuracy</td></tr><tr><td>LOM-4B</td><td>89.47%</td></tr><tr><td>w/o CoT</td><td>78.42%</td></tr><tr><td>w/o Instruct</td><td>61.66%</td></tr><tr><td>w/o GNN, Instruct</td><td>18.95%</td></tr></table>

Instruct"), performance further degrades to $61.66\%$ , highlighting the importance of aligning the LLM with specific graph-related tasks. Most strikingly, the baseline model without both the graph encoder and instruction tuning ("w/o GNN, Instruct") collapses to a mere $18.95\%$ . This drastic decline confirms that standard LLMs, lacking specific structural embeddings and task adaptation, are fundamentally ill-equipped for graph reasoning, validating the necessity of our proposed hybrid architecture.

Large Ontology Models for Enterprise Knowledge Management

First Author et al.: Preprint submitted to Elsevier

Page 6 of 8

# 5. Conclusion

We have presented the LOM, a unified framework for enterprise ontology construction and reasoning that effectively bridges the gap between structured databases and unstructured textual knowledge. By integrating a dual-layer ontology construction method with a three-stage instruction alignment pipeline—spanning ontology instruction fine-tuning, text-ontology grounding, and multi-task instruction tuning—we enable the model to perform complex, structure-aware reasoning over heterogeneous enterprise data. Our experiments demonstrate that the LOM-4B achieves state-of-the-art performance on diverse ontology reasoning tasks, proving its efficacy in handling the intricacies of real-world enterprise environments.

In future work, we plan to enhance the performance of LOM on complex ontology reasoning tasks, particularly focusing on challenging tasks like MST and PageRank where current models consistently achieve low scores. We plan to adopt more reinforcement learning strategies to enable deeper structural understanding and more accurate multihop inference to overcome these limitations.

# References

Large Ontology Models for Enterprise Knowledge Management

First Authoret al.: Preprint submitted to Elsevier

Page 7 of 8

Web (WWW) 27, 58. doi:10.1007/S11280-024-01297-W.

Large Ontology Models for Enterprise Knowledge Management

First Author et al.: Preprint submitted to Elsevier

Page 8 of 8