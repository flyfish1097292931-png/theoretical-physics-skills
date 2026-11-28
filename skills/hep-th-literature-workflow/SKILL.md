---
name: hep-th-literature-workflow
description: Calibrate a theory question against primary papers.
version: 0.1.0
license: MIT
---

# HEP-th literature workflow

Use before investing in a derivation, numerical campaign, or novelty claim. The output is a decision about what to calculate next, not a bibliography ranked by search relevance.

1. **State the proposed result.** Name the model, observable, state or ensemble, regime, and the step that might be new. Write alternate notation and terminology a different subfield might use for the same object.
2. **Find the closest results.** Search arXiv and INSPIRE-HEP or equivalent public indexes; follow citations in both directions. Seek the closest antecedent, a competing route, and a result limiting the proposed extension. These roles can be filled by the same paper; mark a missing role as unlocated, not nonexistent.
3. **Open the primary text.** Record the identifier, version, and exact equation, theorem, or section. Confirm that the cited text actually supports the sentence. Compare operator definitions, boundary conditions, normalization, and limit order before declaring two results equivalent. If only metadata or the abstract is accessible, state what remains unverified.
4. **Decide what changes.** Classify the proposed step as established, an extension under named assumptions, contradicted, or unresolved. Separate a new derivation of a known result from a new physical claim. If a no-go applies only with an assumption, carry that assumption into the comparison.
5. **Stop once the next calculation is clear.** Return the question, closest source and exact support, meaningful difference, smallest next test, and one observation that would kill or redirect the idea. Reopen the search if the physical object or novelty claim changes.

Do not infer priority from lack of search hits or novelty from a new notation. Use the [worked review](../../examples/oscillator/research-review.md) for a historical method citation that does not support a stronger conservation claim.

Method provenance: informed by the public [Google DeepMind science-skills](https://github.com/google-deepmind/science-skills) collection. This public guide is independently written and redistributes no upstream text, templates, or code.
