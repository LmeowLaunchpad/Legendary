# Legendary

**Mathematical findings, with the arguments and evidence attached.**

Research by **Roger Malcolm III**, using **GPT-6**.

A growing collection of research notes on substantial mathematical consequences. Each finding has a stable identifier, a readable overview, a detailed argument, primary references, and an explicit verification record.

> [!IMPORTANT]
> The first finding is **conditional on an upstream claimed theorem**. Its deduction has undergone AI-assisted source checks, but neither external peer review nor an independent rebuild of the upstream formal proof is recorded here. Publication is not a claim of established novelty.

## Findings

| ID | Finding | Mathematical status | Review status |
| :--- | :--- | :--- | :--- |
| **001** | [From a group-algebra counterexample to universal zero Rokhlin entropy](findings/001-rokhlin-entropy-collapse/) | Conditional corollary | AI-assisted checks; no external review recorded |

### Featured finding · 001

If the cited finitely presented group-algebra counterexample is correct, there is a finitely presented group $H$ for which **every free ergodic probability-preserving action has zero Rokhlin entropy**. This includes a Bernoulli shift with independent continuous labels.

The argument combines the claimed counterexample with Brandon Seward's published theorems. It also yields binary generating observations with arbitrarily small probability of a 1, and an obstruction to extending a familiar pair of entropy requirements to every countable group.

**[Read the overview →](findings/001-rokhlin-entropy-collapse/)** · [Proof](findings/001-rokhlin-entropy-collapse/proof.md) · [Verification record](findings/001-rokhlin-entropy-collapse/verification.md) · [References](findings/001-rokhlin-entropy-collapse/references.md)

## How to read this collection

- **Overview:** what a finding says and why it matters.
- **Proof:** precise assumptions, deductions, and limitations.
- **Verification record:** what was checked, what remains unresolved, and the scope of any prior-art search.
- **References:** the sources and exact versions on which the argument depends.

Mathematical status and review status are recorded separately. A conditional deduction can have a complete argument while its premise remains unverified. Agreement among AI agents is not independent human peer review.

## Keeping the record useful

[Research standards](docs/RESEARCH_STANDARDS.md) · [Finding template](docs/FINDING_TEMPLATE.md) · [Corrections and contributions](CONTRIBUTING.md) · [Machine-readable index](findings/index.json)

For a correction or an earlier source for a claimed consequence, [open a correction or prior-art report](https://github.com/LmeowLaunchpad/Legendary/issues/new?template=correction.yml). Please identify the finding and the exact claim involved.

When citing a note, include its title, finding ID, version, and a commit-specific GitHub URL. Git history records revisions; each note also carries a short revision log.

---

Maintained by **Roger Malcolm III** ([LmeowLaunchpad](https://github.com/LmeowLaunchpad)). The initial note was researched and drafted using **GPT-6**, including multiple agent checks. The mathematical sources and the scope of that assistance are documented in the note.
