# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1. Overall Classification Accuracy

The TakeMeter classifier must achieve at least 65% accuracy
on the held-out test dataset.

**Why this target:**

The dataset contains 225 Data Science Stack Exchange questions
across four categories: conceptual, troubleshooting, learning,
and technical_advice. Some questions ask for both explanations
and implementation guidance, making their primary intent
difficult to distinguish. I chose 65% because it represents
useful classification performance and substantially exceeds
the 25% accuracy of uniform random guessing.

## 2. Minimum F1-Score for Every Label

The classifier must achieve an F1-score of at least 0.50
for each of the four labels on the held-out test dataset.

**Why this target:**

The learning category contains only 22 questions, compared
with 88 technical_advice questions. This imbalance means
that learning will have relatively few examples in the
held-out test set, making its F1-score more sensitive to
individual prediction errors. I chose 0.50 to require
reasonable performance across all four categories without
expecting identical results from differently sized groups.

## 3. Dataset Label Balance

No single label should represent more than 40% of the
total labeled dataset.

**Why this target:**

Technical_advice is the largest category, with 88 of the
225 questions (39.1%). Many Data Science Stack Exchange
users ask for help choosing algorithms, libraries, or
implementation methods. I chose 40% to prevent this
category from dominating the dataset while preserving
the natural distribution of question types.

## 4. Labeling Consistency

A second human annotator must independently assign the
same label as me to at least 80% of a sample of 20 posts.

**Why this target:**

Some questions fall near the boundary between conceptual
and technical_advice, while others could be interpreted
as troubleshooting or learning. I chose 80% because
another annotator should be able to apply the category
definitions consistently. For 20 questions, this
requires agreement on at least 16.

## 5. High-Confidence Prediction Accuracy

Among test predictions with a confidence score of at
least 0.80, the classifier must achieve at least 75%
accuracy.

**Why this target:**

Questions that clearly describe software errors may be
easier to classify than questions that combine explanations
with requests for technical recommendations. I chose 75%
because predictions with confidence of at least 0.80
should be more reliable than the overall 65% accuracy
target. This criterion will be evaluated only if the
model produces such predictions; an empty group does
not count as a pass.

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
