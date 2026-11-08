# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does
TakeMeter is a text classification project that uses questions collected from Data Science Stack Exchange to identify the primary intent behind a technical question. The goal is to train a machine learning model that distinguishes between four types of questions: conceptual, troubleshooting, learning, and technical_advice.

The categories describe what the author wants to accomplish rather than the technical subject of the question. For example, two questions about machine learning may belong to different categories if one asks for an explanation of an algorithm and the other asks for help resolving an implementation error.

I collected and labeled 225 questions from Data Science Stack Exchange. I then fine-tuned a pretrained DistilBERT model using 157 training examples, 34 validation examples, and 34 held-out test examples.

The initial model achieved 38.2% test accuracy and a macro F1 score of 0.138. Its predictions were heavily concentrated in the technical_advice category, which indicates that the model has not yet learned to distinguish the four question types reliably. These results provide a starting point for the evaluation and improvement work in Unit 6.



---

## Label Taxonomy

TakeMeter uses four labels to classify questions according to the author's primary intent. Each question receives one label, even when it contains elements of more than one category.

1. conceptual

Definition: Questions that seek explanations, interpretations, or deeper understanding of data science concepts, principles, and analytical reasoning.

Example 1: Difference between Global Outlier and Contextual Outlier?

The author questions whether contextual outliers are fundamentally different from global outliers when contextual attributes are included in the feature vector.

Why this label: The main purpose is to understand the conceptual distinction between two types of outliers.

Example 2: Thought process behind data analysis

The author wants to understand how experienced analysts decide which variables to explore, which visualizations to create, and how to approach exploratory data analysis.

Why this label: The question focuses on analytical reasoning rather than fixing a specific technical problem.

2. troubleshooting

Definition: Questions that seek help resolving a technical problem, unexpected result, implementation difficulty, or system limitation.

Example 1: R random forest on Amazon EC2 — cannot allocate vector of size 5.4 GB

The author can train a random forest locally but receives a memory allocation error when running the same model on Amazon EC2.

Why this label: The author describes a specific error and requests a workaround.

Example 2: Image Classification with two very similar and random-ish classes

The author trains neural networks to predict currency movements from chart images but cannot improve accuracy beyond approximately 50%.

Why this label: The author describes an unsuccessful modeling attempt and seeks help identifying the cause.

3. learning

Definition: Questions that seek clarification of a topic or technique as part of the author's learning process, often referencing educational materials or a specific gap in understanding.

Example 1: What exactly is bootstrapping in reinforcement learning?

The author asks what bootstrapping means in reinforcement learning and why temporal-difference methods use it while Monte Carlo methods do not.

Why this label: The author seeks clarification of a concept they are studying.

Example 2: Why do popular search engines not follow the usual AND, OR logic for queries?

The author is studying information retrieval and wants to understand why search engine results do not always follow the Boolean logic described in a textbook exercise.

Why this label: The question arises from a learning exercise and asks for clarification of the observed behavior.

4. technical_advice

Definition: Questions that seek recommendations, comparisons, implementation approaches, or guidance on selecting tools and technologies.

Example 1: How to learn NoSQL databases and how to know when SQL or NoSQL is better

The author asks for learning resources, use cases, and recommendations about choosing between SQL and NoSQL databases.

Why this label: The question requests practical recommendations and technology-selection guidance.

Example 2: What do you use to generate a dashboard in R?

The author wants recommendations for packages that can generate periodic dashboard reports containing tables and charts.

Why this label: The main purpose is to select suitable tools for a specific reporting task.

The Hardest Boundary: conceptual vs. learning

These categories overlap because both can involve requests for explanations.

Decision rule: I use learning when the question explicitly focuses on understanding material the author is studying, such as a textbook exercise or a specific technique they are trying to learn. I use conceptual when the primary purpose is to examine a broader principle, interpretation, or analytical distinction without an explicit educational framing.

For example, the bootstrapping question is labeled learning because it asks for clarification of a technique. The global-versus-contextual-outlier question is labeled conceptual because it challenges the distinction between two theoretical categories.

Remaining ambiguity: This distinction is not always clear. The outlier question also references a textbook, and another annotator could reasonably classify it as learning. The rule is therefore provisional and should be tested for consistency during Unit 6.

Additional Boundary: troubleshooting vs. conceptual

Some questions describe a technical failure while also asking for an explanation.

Decision rule: When the author presents an actual error, failed experiment, or unexpected result and seeks help resolving it, I prefer troubleshooting. When the author primarily seeks an explanation of a principle without requesting a fix, I prefer conceptual.

For example, the Amazon EC2 memory allocation error is troubleshooting because the author requests a workaround.

An existing question about poor CNN validation loss is labeled conceptual in the dataset, although its request for a code-level solution may better fit troubleshooting. I have retained the original label for the initial training run and identified it as a case to review during the labeling consistency assessment.



---

## The Dataset

### Where the questions came from

I collected 225 publicly available questions from Data Science Stack Exchange, a question-and-answer community where users discuss machine learning, statistics, data analysis, and related technical subjects.

I selected this source because the questions represent different types of information needs. Some users want explanations of concepts, others need help resolving technical problems, while others request learning guidance or recommendations about tools and methods.

The dataset is stored in `labels.csv`. Each record contains the question text, assigned label, annotation note, question identifier, source URL, author, and license information.

### How I labeled the questions

I began by manually labeling 20 questions without AI assistance. This initial exercise helped me examine the questions and understand the difficulties involved in distinguishing their primary intent.

For the remaining 205 questions, I used AI-generated label suggestions and reviewed the suggested classifications myself. The AI suggestions were not treated as final labels.

I used four categories: `conceptual`, `troubleshooting`, `learning`, and `technical_advice`.

Each question received one primary label based on its main purpose.

### Counts per label

| Label | Count | Share |
|---|---:|---:|
| `conceptual` | 71 | 31.6% |
| `troubleshooting` | 44 | 19.6% |
| `learning` | 22 | 9.8% |
| `technical_advice` | 88 | 39.1% |
| **Total** | **225** | **100%** |

The largest category is `technical_advice`, representing 39.1% of the dataset. The smallest is `learning`, with 22 questions.

Although no category exceeds the 40% limit established in my acceptance criteria, the distribution is not equal. This imbalance may affect the model's ability to recognize categories with fewer training examples.

### Three Hard Cases

**1. Really bad value of Val loss**

- **The question:** The author trains a CNN for music genre classification and obtains poor validation loss despite otherwise satisfactory results.
- **Could have been:** `conceptual` or `troubleshooting`.
- **I chose:** `conceptual` in the initial dataset.
- **Why it was difficult:** The author discusses overfitting, which involves conceptual understanding, but also asks how to solve the problem in code. Under the current taxonomy, `troubleshooting` may be a better fit. I retained the original label for the initial experiment and identified this example for consistency review.

**2. What exactly is bootstrapping in reinforcement learning?**

- **The question:** The author asks what bootstrapping means and why temporal-difference methods use it while Monte Carlo methods do not.
- **Could have been:** `learning` or `conceptual`.
- **I chose:** `learning`.
- **Why it was difficult:** The question asks for a theoretical explanation, which fits `conceptual`. However, I classified it as `learning` because the author's main purpose is to clarify a specific technique.

**3. How to learn NoSQL databases and how to know when SQL or NoSQL is better**

- **The question:** The author asks for NoSQL learning resources, explanations of SQL and NoSQL use cases, and recommendations.
- **Could have been:** `learning` or `technical_advice`.
- **I chose:** `technical_advice`.
- **Why it was difficult:** The question explicitly mentions learning NoSQL, but it also requests practical guidance about choosing between database technologies. I selected `technical_advice` because recommendations and technology selection form a substantial part of the request.

### Data limitations

The dataset contains only 225 examples, and the categories are unevenly represented. Some questions also contain overlapping intentions, which makes consistent labeling difficult.

The initial training run will serve as a baseline for examining these limitations. I will investigate classification errors and labeling consistency in Unit 6 before deciding whether to revise the taxonomy or training approach.

---

## The Training Run

### Base Model

I used `distilbert-base-uncased`, a pretrained transformer model available through Hugging Face.

I selected DistilBERT because it provides a relatively lightweight starting point for text classification. It also allowed me to fine-tune a pretrained language model on my local computer without requiring a dedicated GPU.

The model was configured to classify questions into four categories: `conceptual`, `troubleshooting`, `learning`, and `technical_advice`.

### Training Configuration

| Parameter | Value |
|---|---|
| Base model | `distilbert-base-uncased` |
| Number of labels | 4 |
| Training epochs | 3 |
| Learning rate | 0.00002 (2e-5) |
| Batch size | 16 |
| Maximum sequence length | 128 tokens |
| Random seed | 42 |
| Training framework | PyTorch and Hugging Face Transformers |
| Training device | CPU |

### Dataset Split

I used a stratified split to preserve the approximate distribution of the four categories across training, validation, and test sets.

| Category | Training | Validation | Test |
|---|---:|---:|---:|
| `conceptual` | 49 | 11 | 11 |
| `troubleshooting` | 30 | 7 | 7 |
| `learning` | 16 | 3 | 3 |
| `technical_advice` | 62 | 13 | 13 |
| **Total** | **157** | **34** | **34** |

The split allocated approximately 70% of the dataset to training, 15% to validation, and 15% to testing.

The `learning` category had only three test examples, while `troubleshooting` had seven. Performance estimates for these smaller categories are therefore sensitive to individual predictions.

### Changes from the Starting Configuration

I replaced the starter notebook's original label names with the four categories used in my dataset.

I also updated the dataset validation check to enforce my chosen maximum category share of 40%, rather than the starter's 70% threshold.

I retained the initial three-epoch training configuration and used a fixed random seed to make the dataset split and training run reproducible.

### Initial Training Results

The model completed three training epochs on the CPU.

| Epoch | Training Loss | Validation Loss | Validation Accuracy | Validation Macro F1 |
|---|---:|---:|---:|---:|
| 1 | 1.3412 | 1.2774 | 47.1% | 0.255 |
| 2 | 1.2456 | 1.2251 | 41.2% | 0.183 |
| 3 | 1.1910 | 1.2040 | 44.1% | 0.221 |

Although training loss decreased, validation performance remained low.

### Held-Out Test Results

After training, I evaluated the model on the 34 held-out test examples.

**Overall test accuracy:** 38.2%

**Macro F1 score:** 0.138

| Category | Test F1 | Number of examples |
|---|---:|---:|
| `conceptual` | 0.000 | 11 |
| `troubleshooting` | 0.000 | 7 |
| `learning` | 0.000 | 3 |
| `technical_advice` | 0.553 | 13 |

The confusion matrix showed that the model predicted `technical_advice` for all 34 test questions.

This explains why the model correctly classified the 13 `technical_advice` questions but failed to identify the other three categories.

The model therefore did not meet my predefined accuracy and per-category F1 targets.

### Output Files

The notebook generated two files:

- `results.json` — records test accuracy, macro F1, per-category performance, confusion counts, confidence statistics, and training environment information.
- `test_split.csv` — preserves the held-out test examples for subsequent evaluation.

These files document the initial training run and provide evidence for the model evaluation and improvement work in Unit 6.

---

## How I Used AI

I used ChatGPT to assist with dataset preparation, Python development, and troubleshooting during this project. I reviewed the suggestions and made the final decisions about the dataset, classification labels, and training configuration.

### Moment 1: Dataset Labeling

**What I asked for:**

I used AI to suggest classifications for questions collected from Data Science Stack Exchange. The objective was to assign each question to one of four categories: `conceptual`, `troubleshooting`, `learning`, or `technical_advice`.

**What came back:**

AI suggested labels based on the apparent purpose of each question. Some questions were straightforward, while others could reasonably fit more than one category.

**What I changed:**

I reviewed the suggested labels rather than accepting them automatically. I also examined ambiguous examples and documented decision rules for distinguishing categories with overlapping meanings.

For example, questions requesting explanations can fit either `conceptual` or `learning`, depending on their primary purpose. Similarly, questions describing implementation problems can overlap with `technical_advice`.

### Moment 2: Model Training and Troubleshooting

**What I asked for:**

I used ChatGPT to help me understand the starter notebook, configure the Python environment, run DistilBERT training, and interpret the evaluation results.

**What came back:**

ChatGPT explained the training configuration, dataset splitting process, and evaluation metrics. It also helped me investigate why the model performed poorly after training.

**What I changed:**

I configured the notebook to use my four classification labels, updated the dataset validation threshold to match my acceptance criteria, and executed the training and evaluation cells.

After obtaining a test accuracy of 38.2% and a macro F1 score of 0.138, I examined the confusion matrix and validation predictions.

The confusion matrix showed that the model predicted `technical_advice` for every test example. I documented this behavior instead of changing the acceptance criteria or reporting the model as successful.

### Pre-Labeling Disclosure

The dataset contains 225 labeled questions.

I manually labeled the first 20 questions without AI assistance. For the remaining 205 questions, I used AI-generated label suggestions and reviewed them before including them in the dataset.

The annotation notes in `labels.csv` distinguish the initial manually labeled questions from the AI-suggested, human-reviewed questions.

AI assisted with the labeling and development process, but the initial model's evaluation results are reported without alteration.

## Baseline vs. Trained

**Prediction:** Based on the initial Unit 5 results, I expect the fine-tuned DistilBERT model to outperform the zero-shot baseline on `technical_advice`, but perform worse on `conceptual`, `learning`, and `troubleshooting`. I also expect the baseline to achieve a higher overall macro F1 because it appears to distinguish more categories.

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy | 0.412 | 0.382 | -0.029 |
| Macro F1 | 0.391 | 0.138 | -0.252 |
| F1 — `conceptual` | 0.462 | 0.000 | -0.462 |
| F1 — `learning` | 0.545 | 0.000 | -0.545 |
| F1 — `technical_advice` | 0.000 | 0.553 | +0.553 |
| F1 — `troubleshooting` | 0.556 | 0.000 | -0.556 |

**Interpretation:** The zero-shot baseline achieved 41.2% accuracy and a macro F1 of 0.391, compared with 38.2% accuracy and a macro F1 of 0.138 for the fine-tuned DistilBERT model. The trained model performed better on `technical_advice` but predicted that category for every test question, resulting in zero F1 for the other three categories. The baseline showed the opposite pattern, with nonzero F1 for `conceptual`, `learning`, and `troubleshooting`, but zero F1 for `technical_advice`. These results suggest that the trained model failed to learn useful distinctions between the four labels. Further testing across three random seeds is needed to determine whether this behavior is consistent.

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

### Run Log — Before

**Training environment:** CPU, PyTorch 2.15.0+cu132, maximum sequence length 128.

**Random seeds:** 42, 7, 2024.

| Metric | Seed 42 | Seed 7 | Seed 2024 |
|---|---|---|---|
| Accuracy | 0.382 | 0.382 | 0.382 |
| Macro F1 | 0.138 | 0.138 | 0.138 |
| F1 — `conceptual` | 0.000 | 0.000 | 0.000 |
| F1 — `troubleshooting` | 0.000 | 0.000 | 0.000 |
| F1 — `learning` | 0.000 | 0.000 | 0.000 |
| F1 — `technical_advice` | 0.553 | 0.553 | 0.553 |

**Confusion matrix**

| true \ predicted | conceptual | troubleshooting | learning | technical_advice |
|---|---|---|---|---|
| **conceptual** | 0 | 0 | 0 | 11 |
| **troubleshooting** | 0 | 0 | 0 | 7 |
| **learning** | 0 | 0 | 0 | 3 |
| **technical_advice** | 0 | 0 | 0 | 13 |

**Initial diagnosis:** The model predicted `technical_advice` for all 34 test questions in every trial. The largest confusion involved 11 `conceptual` questions classified as `technical_advice`, with no errors in the opposite direction. This suggests the classifier did not learn to distinguish the four categories. Although `technical_advice` is the largest category in the training dataset, the results alone cannot establish whether class imbalance, inconsistent labels, or the training configuration caused the collapse. Further investigation is necessary.
**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---
## Dataset Collection Progress

TakeMeter uses public discussions from the r/datascience
Reddit community to classify posts into four categories:
question, experience, opinion, and promotion.

### Current Progress

- Target dataset: 200 posts.
- Posts collected and independently labeled: 20.
- Labeling method: Manual cold labeling for the first 20 posts.
- Remaining posts: 180.
- Reddit Data API access: Requested; approval pending.

### Data Collection and Review

The initial 20 posts were labeled without AI assistance.
Each post has a primary label and a note indicating that
it was cold-labeled.

The remaining posts will be collected through an authorized
method. AI may suggest labels, but every suggested label
will receive human review before inclusion in the dataset.

### Data Handling

The working dataset is stored locally in labels.csv.
Full Reddit post text will not be uploaded to the public
GitHub repository while applicable data-sharing permissions
remain unresolved.
📖 **How to run this project: [RUNNING.md](RUNNING.md)**
