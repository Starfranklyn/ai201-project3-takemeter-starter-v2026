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

The dataset contains four labels: experience, question,
opinion, and promotion. Some posts combine personal experiences
with questions or promote resources while expressing opinions.
I chose 65% because it represents useful performance despite
these overlapping categories and is substantially higher than
the 25% accuracy of uniform random guessing.
## 2. Minimum F1-Score for Every Label

The classifier must achieve an F1-score of at least 0.50
for each of the four labels on the held-out test dataset.

**Why this target:**

The dataset contains four categories, and some posts
have overlapping characteristics. For example, an
experience post may end with a question, while a
promotion post may contain personal experiences.
I chose 0.50 because each category should have
reasonable predictive performance, even when the
small number of test examples causes scores to vary.

## 3. Dataset Label Balance

No single label should represent more than 40% of the
total labeled dataset.

**Why this target:**

The dataset contains four categories: experience,
question, opinion, and promotion. Since posts from
r/datascience frequently ask technical questions,
the question category could dominate the dataset.
I chose 40% to limit this imbalance while allowing
for natural differences in how frequently each type
of post appears.


## 4. Labeling Consistency

A second human annotator must independently assign the
same label as me to at least 80% of a sample of 20 posts.

**Why this target:**

The four labels can overlap. For example, a post may
describe a personal experience while asking for advice,
or introduce a tool while expressing an opinion.
I chose 80% agreement because the taxonomy should
be clear enough for another person to apply consistently.
On a sample of 20 posts, this means agreeing on at
least 16 classifications.

## 5. High-Confidence Prediction Accuracy

Among test predictions with a confidence score of at
least 0.80, the classifier must achieve at least 75%
accuracy.

**Why this target:**

Some r/datascience posts overlap multiple labels,
especially experience versus question and opinion
versus promotion. When the classifier assigns a
confidence score of 0.80 or higher, I expect its
predictions to be more reliable. I chose 75% because
high-confidence predictions should outperform the
65% overall accuracy target.

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
