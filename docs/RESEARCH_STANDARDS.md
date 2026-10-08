# Research standards

[← Legendary](../README.md)

Each finding should make its conclusion, dependencies, and evidence easy to inspect. Significance is a reason to investigate a result, not a substitute for verification.

## Two separate status fields

**Mathematical status** records what the argument establishes:

| Status | Meaning |
| :--- | :--- |
| Conditional | A stated conclusion depends on a named assumption or upstream claim. |
| Proposed theorem | A complete proof draft is supplied for a precise theorem and is offered for review. The label does not certify its correctness or novelty. |
| Established from cited results | The argument relies on stated published inputs without an additional conjectural premise. This label alone is not a review certificate. |
| Conjectural | The note proposes a claim and does not supply a complete deduction. |
| Withdrawn | A recorded defect invalidates the stated conclusion; the history and reason remain available. |

**Review status** records actual checks: source inspection, AI-assisted review, human review, or formal verification. Name the scope of a check and link its evidence. Never infer external review from publication, model agreement, or the presence of Lean files.

## Required contents

1. A stable finding ID and descriptive title.
2. An overview understandable without reading the investigation history.
3. A precise statement with quantifiers, mathematical setting, and assumptions.
4. An argument that separates cited theorems from the note's own deductions.
5. Primary references, with theorem numbers and pinned versions when available.
6. A verification record and explicit limitations.
7. A short revision log.

Use one directory per finding. Keep the overview, proof, references, and verification record together. Add the finding to the root catalogue and `findings/index.json`; keep the ID stable if the title changes.

## Attribution and prior art

Credit established machinery at the point where it is used. Applying a known conditional theorem to a new premise does not make that conditional theorem a new result of this collection.

Record what a novelty search actually covered. An unsuccessful search supports a limited statement about the sources examined; it does not prove that nobody has noticed a consequence. Add earlier sources when they are identified.

## AI assistance and formal proofs

Disclose AI assistance in each affected finding. Multiple agent checks can catch mistakes, but agents may share models, sources, and failure modes. Describe them as AI-assisted checks rather than independent peer review.

For formal verification, record the exact statement, source revision, environment, command, and outcome. Distinguish inspecting a declaration from successfully rebuilding its proof. Distinguish a formalized premise from a formalized downstream conclusion.

## Corrections and revisions

Make corrections explicit. Update the finding's revision log, status, and catalogue as needed. Preserve a record of substantive mistakes or withdrawals instead of silently replacing an invalid claim with a different one.

Use commit-specific links for citations. A version number identifies an editorial revision; it does not certify mathematical correctness.
