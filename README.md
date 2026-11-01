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
TakeMeter is a text classification project that analyzes public discussions from the r/datascience Reddit community. The goal is to train a machine learning model that classifies posts according to their primary purpose rather than their topic.

During the initial review, I observed discussions about mistakes made while developing machine learning models, preparation for data science interviews, questions about the meaning of artificial intelligence, and tradeoffs in selecting metrics for marketplace experiments. These observations informed three candidate labels: `experience`, `question`, and `opinion`.



---

## Label Taxonomy

<!-- Each label: a one-sentence definition and two real examples from your
     reading. Then your decision rule for the hardest boundary.

     The decision rule is worth a point on its own and it's the thing most
     people leave out. Every taxonomy has a hardest boundary. Name yours. -->

### `label_one`

- **experience:** A post that primarily describes the author's
  personal experiences, projects, challenges, or lessons learned.

- **question:** A post that primarily asks for information,
  explanations, advice, or help.

- **opinion:** A post that primarily expresses an argument,
  evaluation, judgment, or viewpoint about a topic.

- **promotion:** A post that primarily introduces or promotes
  a product, article, project, service, or external resource.
>
### Real Post Examples

#### Experience
**Example 1: Junior analyst without mentorship**

- **Source:** r/datascience
- **Post summary:** A junior analyst describes working without
  experienced colleagues or professional mentorship.
- **Label:** `experience`
- **Reason:** The author describes working in three roles without
  senior analysts or mentors. Although the post ends with career
  questions, its main focus is the author's personal experience.

**Example 2: Adtech modeling take-home assignment**

- **Source:** r/datascience
- **Post:** An applicant describes being rejected after using
  CatBoost for an adtech modeling assignment.
- **Label:** `experience`
- **Reason:** The author recounts a real modeling assignment,
  explains why they selected CatBoost, and describes the
  rejection they received. Although they criticize the
  unclear expectations, the main focus is their firsthand
  experience and modeling decisions.
#### Question
**Example 1: Decision support systems affecting future training data**

- **Source:** r/datascience
- **Post summary:** A user asks how decision-support systems
  can influence the data used to train future models.
- **Label:** `question`
- **Reason:** The author describes a hypothetical customer
  churn model and asks for the technical term describing
  how interventions can affect future training data.
  The main purpose is to seek an explanation.

**Example 2: How widely is R still used in industry today?**

- **Source:** r/datascience
- **Post summary:** A user asks whether R remains widely
  used in professional data science compared with Python.
- **Label:** `question`
- **Reason:** The author explains their background in R and Python
  and asks whether R is still relevant in industry. Although
  the post contains personal context, its primary purpose
  is to seek information about industry practices.
#### Opinion
**Example 1: Choosing metrics in data science interviews**

- **Source:** r/datascience
- **Post summary:** A user discusses the trade-off between
  actionable business metrics and statistical power when
  evaluating marketplace experiments.
- **Label:** `opinion`
- **Reason:** The author argues that actionable business metrics
  can be statistically harder to evaluate than simpler metrics
  such as conversion rates. The post develops a viewpoint
  about how data scientists should approach metric selection.

**Example 2: Silent broadcasting in machine learning**

- **Source:** r/datascience
- **Post summary:** A user argues that unintended tensor
  broadcasting can introduce serious errors into machine
  learning models and deserves greater attention.
- **Label:** `opinion`
- **Reason:** The author argues that silent broadcasting
  can cause serious modeling errors and that data scientists
  should pay more attention to tensor shapes. Although the
  post describes a real incident, its main purpose is to
  emphasize a technical problem and recommend greater caution.
#### Promotion
**Example 1: Interactive ML System Design Tool**

- **Source:** r/datascience
- **Post summary:** A developer introduces a free interactive
  tool designed to help people learn machine learning
  system design.
- **Label:** `promotion`
- **Reason:** The author introduces a free interactive tool,
  shares its website, and describes its features. Although
  the author mentions their professional experience, the
  main purpose is to direct readers to the tool.

**Example 2: AI for Game Design Article**

- **Source:** r/datascience
- **Post summary:** An author shares an article about
  using artificial intelligence in tabletop game design.
- **Label:** `promotion`
- **Reason:** The author shares a link to an article about AI
  in tabletop game design. Although they describe their
  experience building AI playtesting models, the main purpose
  is to introduce readers to their published article.
### The hardest boundary
#### Experience vs Promotion

A post may describe the author's personal work while also
introducing an article, product, or project.

I will use `experience` when the main purpose is to share
what the author did, encountered, or learned.

I will use `promotion` when the main purpose is to introduce
or direct readers to an article, product, project, or resource.

For example, a post introducing an article about AI in
tabletop game design is classified as `promotion` because
the author primarily shares a link to their published article,
even though they also describe their experience using AI.
#### Hard Case 1: Junior analyst without mentorship
**Source:** r/datascience

**Post summary:** A junior analyst describes working in several roles without experienced colleagues or mentorship.
**Possible labels:** `experience` and `question`

**Chosen label:** `experience`

**Reason:** The author describes working in three nonprofit roles without other analysts or a senior colleague to learn from. Although the post ends with questions about career development, I classified it as `experience` because the author's personal history and frustration form the main focus.

**Decision rule:** When a post combines personal experiences and questions, I will classify it as `experience` if the personal account is the main contribution and the questions mainly invite discussion. I will use `question` when the personal account primarily provides context for a specific request for help, advice, or information.

**Remaining ambiguity:** Another person might choose `question` because the author asks for career guidance. I will revisit this example when checking labeling consistency.
#### Hard Case 2: AI for Game Design Article

**Source:** r/datascience

**Post summary:** An author shares a published article about using AI models to support tabletop game design and playtesting.

**Possible labels:** `experience` and `promotion`

**Chosen label:** `promotion`

**Reason:** The author describes using AI to build playtesting
models and writing about machine learning in game design.
However, the main purpose of the post is to share a link
to their published article.

**Decision rule:** When a post describes personal work but
primarily directs readers to an article, product, or project,
I will classify it as `promotion`.

**Remaining ambiguity:** Another annotator might choose
`experience` because the author discusses their own projects.
#### Hard Case 3: Queryable Lossless Compression

**Source:** r/datascience

**Post summary:** A developer presents a lossless compression
tool that supports queries on compressed tables and logs.
**Possible labels:** `opinion` and `promotion`

**Chosen label:** `promotion`

**Reason:** The author introduces the TinyFiles compression
tool and describes its capabilities. Although the post
contains positive claims about the technology, its main
purpose is to present a specific tool to readers.

**Decision rule:** I will use `promotion` when a post
primarily introduces a product, tool, or resource.
I will use `opinion` when the main purpose is to
express or defend a viewpoint, even if the author
mentions a particular product.

**Remaining ambiguity:** Another annotator might choose
`opinion` because the author makes claims about the
benefits of the compression approach.
**Which two labels:**

**The decision rule I used every time:**
<!-- e.g. "If the post names a specific checkable fact, it's `analysis`, even
     if the tone is heated." -->



---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:**

**How I labelled them:** <!-- Cold first? Pre-labelled with AI and corrected?
Say so plainly — the disclosure is required, not penalised. -->

**Counts per label:**

| Label | Count | Share |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
| **Total** |  | 100% |

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

**2.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

**3.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:**

**Settings:** <!-- epochs, learning rate, batch size, seed -->

**Anything I changed from the defaults, and why:**

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->



---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Pre-labelling disclosure:**

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

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
