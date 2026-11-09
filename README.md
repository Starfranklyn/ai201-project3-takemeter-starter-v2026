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
**My biggest off-diagonal number, and what it means:**

The largest off-diagonal value was 11: the model classified 11 actual `conceptual` questions as `technical_advice`. There were no errors in the opposite direction because the model never predicted `conceptual`.

This shows that the model failed to learn the boundary between questions seeking conceptual explanations and questions seeking technical advice. The same pattern occurred across all three seeds, suggesting a consistent classification problem rather than an isolated result from one random split.


## Verdicts and Diagnoses

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 | Overall accuracy | ≥65% | MISSED | All three seeds achieved 38.2% accuracy, below the required threshold. |
| 2 | Per-label F1 | ≥0.50 for every label | MISSED | Only `technical_advice` met the threshold (0.553). The other three categories had F1 scores of 0.000 in every run. |
| 3 | Dataset balance | No label above 40% | MET | The largest category, `technical_advice`, contained 88 of 225 posts (39.1%). |
| 4 | Human agreement | ≥80% on 20 posts using the original four-label taxonomy | NOT MEASURED | The available staff exercise used 30 running-related posts and a different three-label taxonomy. Its 77% agreement cannot establish this criterion. |
| 5 | High-confidence accuracy | ≥75% accuracy among predictions with confidence ≥0.80 | NOT MEASURED | The original results saved confidence summaries but not the number or accuracy of predictions reaching the 0.80 threshold. |

**Diagnosis of the missed criteria:**

The original model predicted `technical_advice` for every test example across all three seeds. This explains the low overall accuracy and the zero F1 scores for three categories. The dataset met its balance target, but the model did not learn to distinguish the categories.

The separate human-agreement exercise produced 23 agreements out of 30 posts (77%). All seven disagreements were adjudicated as consistency problems in my application of that exercise's taxonomy. This demonstrates the importance of clear labeling rules, but it does not establish that inconsistent labels caused the TakeMeter model's classification errors.

The original confidence evaluation was insufficient to test Criterion 5 because it compared the most and least confident thirds rather than applying the specified 0.80 threshold. I corrected that measurement for the after-runs without changing the acceptance criterion.

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

### Independent Labeling Results

I independently classified 30 posts using the staff taxonomy before viewing the staff labels. I then compared my classifications against the official labels using `agreement.py`.

| Measure | Result |
|---|---:|
| Total posts | 30 |
| Agreements | 23 |
| Disagreements | 7 |
| Agreement rate | 77% |

The comparison produced `agreement_results.json`. I preserved my original classifications in `my_staff_labels.csv`.

### Disagreement Adjudication

**1. SP_002 — Sleep and running performance**

- **Post:** "I tracked sleep against session quality for eleven weeks. Under seven hours the next day's intervals were 6-8 seconds per mile slower, every time bar one. Small sample, one runner, but it's consistent enough that I've stopped scheduling hard days after late shifts."
- **Staff label:** `analysis`
- **My original label:** `reaction`
- **My final decision:** `analysis`
- **Category:** (a) Consistency problem
- **Reason:** I initially focused on the writer's personal response. However, the eleven weeks of observations and measured differences in running performance support the conclusion.

**2. SP_004 — Hill and marathon slowdown**

- **Post:** "Everyone blames the hill at 18 miles. I split the field into people who ran the first half under 1:45 and over, and the slowdown after 18 was almost identical for both groups. If the hill were the problem the fast starters would fall apart harder."
- **Staff label:** `analysis`
- **My original label:** `reaction`
- **My final decision:** `analysis`
- **Category:** (a) Consistency problem
- **Reason:** I initially interpreted the post as a reaction. On review, the comparison between two groups provides evidence for the writer's argument about the hill.

**3. SP_005 — Carbon-plated shoes**

- **Post:** "Carbon plates aren't the whole story. My times dropped 2% in the shoes and another 2% the following year in the same pair, when the only thing that changed was going from 35 to 50 miles a week."
- **Staff label:** `analysis`
- **My original label:** `reaction`
- **My final decision:** `analysis`
- **Category:** (a) Consistency problem
- **Reason:** I initially thought the numerical evidence was insufficient. However, the comparison between two years supports the argument that improved performance cannot be attributed entirely to carbon-plated shoes.

**4. SP_006 — First-time marathon participants**

- **Post:** "Checked the entry lists. 41% of this year's field have never run the distance before, against 26% five years ago. That's why the finish-line photos look different, not because standards dropped."
- **Staff label:** `analysis`
- **My original label:** `hot_take`
- **My final decision:** `analysis`
- **Category:** (a) Consistency problem
- **Reason:** I initially thought the percentages were insufficient to qualify as analysis. On review, the comparison between 41% and 26% provides evidence for the writer's conclusion.

**5. SP_007 — Temperature and running performance**

- **Post:** "Ran the same loop in 4C and in 24C within a fortnight, same effort by heart rate. 90 seconds slower in the heat over six miles. People keep saying heat costs you 'a bit' and it's more than that."
- **Staff label:** `analysis`
- **My original label:** `reaction`
- **My final decision:** `analysis`
- **Category:** (a) Consistency problem
- **Reason:** I initially considered the measurements insufficient. On review, the comparison between runs at two temperatures supports the writer's argument about the effect of heat on performance.

**6. SP_008 — Marathon non-starter rates**

- **Post:** "Went back through the club results going back to 2012. Every single year the number of people who enter the spring marathon and don't start it sits between 18 and 23 percent. It's not a bad-luck year, it's thebase rate."
- **Staff label:** `analysis`
- **My original label:** `hot_take`
- **My final decision:** `analysis`
- **Category:** (a) Consistency problem
- **Reason:** I initially thought the numbers were insufficient. On review, the historical results support the argument that marathon non-starter rates follow a recurring pattern.

**7. SP_010 — Running shoes and performance**

- **Post:** "Three of us ran the same session on the same day, different shoes, within 10 seconds of each other over 5 miles. I'm not saying shoes do nothing, but whatever they do was smaller than the noise between three people."
- **Staff label:** `analysis`
- **My original label:** `hot_take`
- **My final decision:** `analysis`
- **Category:** (a) Consistency problem
- **Reason:** I initially thought the numerical evidence was insufficient. On review, I accepted that the comparison between three runners supports the argument, although the sample is small.

### Disagreement Categories

| Category | Count |
|---|---:|
| (a) Consistency problem | 7 |
| (b) Gap in the definitions | 0 |
| (c) Defensible alternative interpretation | 0 |

### What I Learned

My disagreements followed a consistent pattern. I sometimes treated posts containing personal experiences as reactions and considered some numerical comparisons insufficient to qualify as analysis.

After reviewing the staff taxonomy, I recognized that the important distinction is whether specific evidence supports the writer's argument. The evidence does not have to establish a scientifically conclusive result to qualify as `analysis`.

All seven disagreements were classified as consistency problems in my application of the taxonomy. I did not identify a definition gap or retain an alternative interpretation in this review.

The original agreement rate remains 77%. My adjudications explain the disagreements; they do not replace my independent labels or retroactively increase the agreement score.



---

## The Improvement

**What I changed:**

I increased the number of training epochs from 3 to 6 while keeping the DistilBERT model, learning rate (2e-5), batch size (16), maximum sequence length (128), and random seeds (42, 7, and 2024) unchanged. I also added an evaluation measurement for predictions with confidence of at least 0.80. This measurement change did not alter the model's training.

**Which diagnosis pointed at it:**

In the original three runs, the model predicted `technical_advice` for every test example. Each run achieved 38.2% accuracy and a macro F1 score of 0.138. The confusion matrices showed that the model failed to recognize the other three categories.

I suspected that three training epochs might not be enough for the model to learn the distinctions between categories. I therefore tested whether additional training would reduce its dependence on `technical_advice`.

The improvement helped, although it did not solve the classification problem. Average accuracy increased from 38.2% to 52.0%, and average macro F1 increased from 0.138 to 0.357. The model began recognizing `conceptual` questions and some `troubleshooting` questions, but it still failed to predict `learning` in every run.
### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Overall accuracy | ≥65% | 50.0% | 55.9% | 50.0% | MISSED — all three |
| 2. Per-label F1 | ≥0.50 for every label | 2/4 labels passed | 2/4 labels passed | 2/4 labels passed | MISSED — all three |
| 3. Dataset balance | No label above 40% | 39.1% maximum | 39.1% maximum | 39.1% maximum | MET — all three |
| 4. Human agreement | ≥80% on 20 posts using the four-label taxonomy | Not measured | Not measured | Not measured | NOT MEASURED |
| 5. High-confidence accuracy | ≥75% accuracy where confidence ≥0.80 | 0 qualifying predictions | 0 qualifying predictions | 0 qualifying predictions | MISSED — all three |

**Did it help, and how do I know:**

Yes. Increasing the training epochs from 3 to 6 improved accuracy and macro F1 across all three seeds. Average accuracy increased from 38.2% to 52.0%, while average macro F1 increased from 0.138 to 0.357.

The confusion matrices also showed a change in model behavior. Before the improvement, all 34 test predictions were `technical_advice` in every run. After the improvement, the model predicted `conceptual` and, in two runs, `troubleshooting`.

However, none of the three runs reached the required 65% accuracy, and none achieved F1 ≥0.50 for all four labels. The model never predicted `learning`, and no prediction reached the 0.80 confidence threshold.

Criterion 3 remained satisfied because the largest category, `technical_advice`, represented 88 of 225 labeled posts (39.1%).

Criterion 4 could not be evaluated using the available human-agreement exercise. That exercise measured 77% agreement on 30 running-related posts using a separate three-label taxonomy (`analysis`, `hot_take`, and `reaction`). It does not establish agreement on 20 posts using TakeMeter's original four-label taxonomy.
---

## What's Still Broken

The six-epoch model performed better than the original three-epoch model, but several problems remain.

**Criterion 1 — Overall accuracy:** All three runs remained below the required 65% accuracy. The best result was 55.9% (seed 7). I would next examine misclassified posts to determine whether the model struggles with overlapping category definitions or lacks sufficient training examples.

**Criterion 2 — Per-label F1:** The model met the F1 threshold for `conceptual` and `technical_advice`, but not for `troubleshooting` or `learning`. The most serious problem was `learning`, which received zero predictions across all three runs. I would prioritize collecting and reviewing additional `learning` examples, since this is the smallest category, with only 22 posts.

**Criterion 3 — Dataset balance:** This criterion was met. The largest category represented 39.1% of the dataset. However, the model still favored `technical_advice`, showing that satisfying the dataset-balance threshold did not guarantee balanced predictions.

**Criterion 4 — Human agreement:** This criterion remains unmeasured under the original four-label taxonomy. The separate staff exercise produced 77% agreement on 30 running-related posts, but it cannot establish whether a second annotator would agree on at least 80% of 20 TakeMeter posts. I would conduct that specific annotation exercise before claiming this criterion was met.

**Criterion 5 — High-confidence accuracy:** None of the improved runs produced predictions with confidence ≥0.80. I would investigate model calibration after improving classification performance, then evaluate accuracy on predictions that meet the original confidence threshold.

**Why I stopped:**

The assignment required one justified improvement and a comparison across the same three random seeds. I tested one change—increasing training from 3 to 6 epochs—and documented its effects. Further changes would require a separate experiment to determine which modification caused any improvement.

**The gap between what I meant my labels to capture and what the model learned:**

My taxonomy distinguishes conceptual explanations, troubleshooting requests, learning guidance, and technical advice, but the model still relies heavily on `technical_advice` predictions. Although additional training helped it recognize other categories, the confusion matrices show that it has not learned to identify `learning` questions reliably.
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


📖 **How to run this project: [RUNNING.md](RUNNING.md)**
