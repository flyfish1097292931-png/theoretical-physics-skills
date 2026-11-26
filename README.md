# Theoretical Physics Skills

**A growing, open-source collection of skills for theoretical physics research.**

这是一个持续扩充的理论物理研究 skills 仓库，收录可复用的研究方法与实操指南，供研究者和 AI 助手按需使用。

## Skill catalog / 技能目录

| When you need to… | Read |
|---|---|
| Find why two calculations disagree | [Physics anomaly investigation](skills/physics-anomaly-investigation/SKILL.md) |
| Fix the physical question and falsifier before inspecting decisive results | [Physics pre-claim registration](skills/physics-preclaim-registration/SKILL.md) |
| Decide how far a result from a special case or finite scan extends | [Physics claim scope closure](skills/physics-claim-scope-closure/SKILL.md) |
| Leave a numerical result a collaborator can rerun | [Physics numerical evidence system](skills/physics-numerical-evidence-system/SKILL.md) |

Open the relevant `SKILL.md` yourself or give it to your research agent as task context. Load only the checks that could change the scientific decision. No agent runtime is required, and none of the skills certifies a scientific claim.

## A worked example: a conserved quantity is not necessarily the physical energy

The [harmonic-oscillator example](examples/oscillator/README.md) reproduces an exact finite-step invariant for velocity Verlet, tests it using two calculations, and rejects the claim of exact physical-energy conservation. It uses Python 3.9+ and the standard library only:

```sh
python3 examples/oscillator/check.py
python3 -B -m unittest discover -s tests -v
```

## Provenance and license

Prepared by Feiyu Deng with Hermes Agent assistance. The published skills are written for reuse without private research materials or runtime dependencies. The oscillator example is a teaching fixture. No third-party source code is bundled. [MIT license](LICENSE).
