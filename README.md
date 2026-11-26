# Theoretical Physics Skills

**Four research workflows for the gap between getting an answer and knowing what it supports.**

理论物理研究技能：预先固定验证标准，定位两路计算的分歧，留下可复算的数值证据，写出与证据范围相符的结论。

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

Prepared by Feiyu Deng with Hermes Agent assistance. The four documents are public adaptations of general research workflows. They do not include original research case files or private runtime dependencies. The oscillator example is an elementary, newly written teaching fixture, not a new scientific result. No third-party source code is bundled. [MIT license](LICENSE).
