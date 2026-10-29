# From Proxemics to Foundation Models: A Survey of Socially Aware Robot Navigation

Coding records, screening records and scripts accompanying the survey *From Proxemics to Foundation Models: A Survey of Socially Aware Robot Navigation* (M. Imad and S. Y. Shin). The citation will be added on publication.

The corpus contains 98 works, including 45 direct foundation-model (FM) social-navigation papers, with a literature cut-off of 19 October 2026 and a final coverage search on 26 October 2026 restricted to works dated up to the cut-off. A representative pre-FM comparison set of 40 works is coded with the same scheme. Every count, table and data-driven figure of the survey and its supplementary material is generated from the records in this repository by the scripts below.

## Copyright of the reviewed articles

The reviewed articles are **not** included in this repository, because most of them are under publisher copyright. Each work is listed below with a link to its DOI, publisher page or arXiv abstract page; readers obtain the articles from these sources. The version used for coding is recorded in [`16_Supplementary/S2_publication_status.csv`](16_Supplementary/S2_publication_status.csv). The paper notes in `08_Paper_Notes/` are the authors' structured summaries with page references, not copies of the articles.

## Repository contents

| Path | Content |
|---|---|
| [`08_Paper_Notes/`](08_Paper_Notes) | One structured note per corpus work (YAML front matter with the final coding, followed by a summary) |
| [`07_Literature_Analysis/`](07_Literature_Analysis) | Coding matrices generated from the notes (direct papers, capabilities, evidence, deployment, metrics, reproducibility, datasets), the pre-FM comparison set, and the search and screening scripts and records (`_tools/stage2`: expansion search and screening; `_tools/stage11`: final coverage search; `_tools/stage9`: pre-FM comparison set) |
| [`10_PreWriting/`](10_PreWriting) | `quantitative_findings.json`: every count reported in the survey, with numerator, denominator, population and source (`build_findings.py`) |
| [`11_Tables/`](11_Tables) | Generated tables (CSV and Markdown) |
| [`12_Figures/`](12_Figures) | Figure scripts (pycairo, deterministic vector output) and the generated figures; no generative image model is used |
| [`13_References/`](13_References) | Verified bibliographic metadata and the generated reference database |
| [`16_Supplementary/`](16_Supplementary) | Supplementary material: Tables S1–S13 (CSV and Markdown), Figs. S1–S4, the supplement PDF and its LaTeX source |
| [`15_Manuscript/references.bib`](15_Manuscript/references.bib) | Bibliography used by the supplement build |

## Rebuilding

Requirements: Python 3 (tested with 3.12) with `pycairo` and `PyYAML` (`pip install -r requirements.txt`); XeLaTeX with the TeX Gyre, DejaVu and Latin Modern fonts for the supplement PDF (optional).

```bash
./build.sh
```

The build regenerates the pre-FM comparison set, the reference database, the quantitative findings, the tables, the figures, the supplementary tables and (if XeLaTeX is available) the supplement PDF, and finally this README. The earlier stages that produced the notes from the source articles (`07_Literature_Analysis/_tools/build_matrices.py` and `stage3/`) and the retrieval scripts (arXiv, OpenAlex, forward citation chasing) are included to document the procedure; they need the source articles or network access and are not part of `build.sh`.

## Licence

Code (`*.py`, `*.sh`): MIT licence ([`LICENSE`](LICENSE)). Data, notes, tables and figures: Creative Commons Attribution 4.0 International ([`LICENSE-DATA.md`](LICENSE-DATA.md)). Bibliographic metadata of the reviewed works and short quotations remain subject to the rights of their owners.

## Reviewed works

Links only; no article PDF is redistributed. Sorted by year (newest first).

### Direct foundation-model social navigation (45)

| Year | Title | Venue | Status | Links |
|---|---|---|---|---|
| 2026 | Act on What You See: Unlocking Safe Social Navigation in Vision-Language-Action Models | arXiv preprint | preprint | [arXiv](https://arxiv.org/abs/2606.10495) |
| 2026 | AHead-VLN: A Hierarchical Reasoning Framework Guided by Foresight for Human-Aware Navigation | Proceedings of the Thirty-Fifth International Joint Conference on Artificial Intelligence (IJCAI) | peer-reviewed | [DOI](https://doi.org/10.24963/ijcai.2026/696) |
| 2026 | E-SocialNav: Efficient Socially Compliant Navigation with Language Models | ICASSP 2026 - IEEE International Conference on Acoustics, Speech and Signal Processing | peer-reviewed | [DOI](https://doi.org/10.1109/ICASSP55912.2026.11462076) · [arXiv](https://arxiv.org/abs/2603.20664) |
| 2026 | Enhancing Lightweight Vision Language Models through Group Competitive Learning for Socially Compliant Navigation | arXiv preprint | preprint | [arXiv](https://arxiv.org/abs/2603.11447) |
| 2026 | EvoNav: Evolutionary Reward Function Design for Robot Navigation with Large Language Models | arXiv preprint | preprint | [arXiv](https://arxiv.org/abs/2605.11859) |
| 2026 | From Obstacles to Etiquette: Robot Social Navigation With VLM-Informed Path Selection | IEEE Robotics and Automation Letters | peer-reviewed | [DOI](https://doi.org/10.1109/LRA.2026.3662586) · [arXiv](https://arxiv.org/abs/2602.09002) |
| 2026 | G2-Nav: Grounded and Guarded Vision-Language Costmaps for Robot Social Navigation | arXiv preprint | accepted, not yet indexed | [arXiv](https://arxiv.org/abs/2607.16956) |
| 2026 | HCSG: Human-Centric Semantic-Geometric Reasoning for Vision-Language Navigation | arXiv preprint | preprint | [arXiv](https://arxiv.org/abs/2605.13321) |
| 2026 | Interpreting Context-Aware Human Preferences for Multi-Objective Robot Navigation | arXiv preprint | preprint | [arXiv](https://arxiv.org/abs/2603.17510) |
| 2026 | Learning to Tune Like an Expert: Interpretable and Scene-Aware Navigation via MLLM Reasoning and CVAE-Based Adaptation | IEEE Transactions on Automation Science and Engineering | peer-reviewed | [DOI](https://doi.org/10.1109/TASE.2026.3673004) · [arXiv](https://arxiv.org/abs/2507.11001) |
| 2026 | LISN: Language-Instructed Social Navigation with VLM-based Controller Modulating | 2026 IEEE International Conference on Robotics and Automation (ICRA) | peer-reviewed | [DOI](https://doi.org/10.1109/ICRA57385.2026.11695757) · [arXiv](https://arxiv.org/abs/2512.09920) |
| 2026 | MAction-SocialNav: Multi-Action Socially Compliant Navigation via Reasoning-enhanced Prompt Tuning | IEEE Robotics and Automation Letters | peer-reviewed | [DOI](https://doi.org/10.1109/LRA.2026.3706951) · [arXiv](https://arxiv.org/abs/2512.21722) |
| 2026 | Narrate2Nav: Real-Time Visual Navigation with Implicit Language Reasoning in Human-Centric Environments | 2026 IEEE International Conference on Robotics and Automation (ICRA) | peer-reviewed | [DOI](https://doi.org/10.1109/ICRA57385.2026.11696112) · [arXiv](https://arxiv.org/abs/2506.14233) |
| 2026 | NORM-Nav: Zero-Shot Mobile Robot Navigation with Natural Language Behavioral Constraints | 2026 IEEE International Conference on Robotics and Automation (ICRA) | peer-reviewed | [DOI](https://doi.org/10.1109/ICRA57385.2026.11696526) · [arXiv](https://arxiv.org/abs/2605.16979) |
| 2026 | Perception-Awareness-Decision: Socially-Aware Robot Navigation and Interaction | Companion Proceedings of the 21st ACM/IEEE International Conference on Human-Robot Interaction (HRI 2026 Companion) | peer-reviewed | [DOI](https://doi.org/10.1145/3776734.3794394) |
| 2026 | Prompting Vision-Language Models for Socially Compliant Robot Navigation | Proceedings of the Annual Conference of JSAI, JSAI2026 (40th Annual Conference of the Japanese Society for Artificial Intelligence) | acceptance verified | [DOI](https://doi.org/10.11517/pjsai.JSAI2026.0_2E5GS10o01) |
| 2026 | RBTLR: A Framework for Safe Social Robot Navigation in Novel Human-Centric Environments | Companion Proceedings of the 21st ACM/IEEE International Conference on Human-Robot Interaction (HRI Companion '26) | acceptance verified | [DOI](https://doi.org/10.1145/3776734.3794437) |
| 2026 | SAATT Nav: a Socially Aware Autonomous Transparent Transportation Navigation Framework for Wheelchairs | arXiv preprint | preprint | [arXiv](https://arxiv.org/abs/2603.13698) |
| 2026 | SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2026) | peer-reviewed | [Publisher page](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2511.21135) |
| 2026 | SOPD-SocialNav: Selective On-Policy Distillation for Vision-Language Social Navigation | arXiv preprint | accepted, not yet indexed | [arXiv](https://arxiv.org/abs/2607.19850) |
| 2026 | TACET: Context-Appropriate Acoustic-Social Navigation for Quadrupeds | arXiv preprint | preprint | [arXiv](https://arxiv.org/abs/2610.03828) |
| 2026 | Think When It Matters: Conditional VLM Reasoning for Social Navigation with RL Policies | arXiv preprint | preprint | [arXiv](https://arxiv.org/abs/2607.10991) |
| 2026 | Token-Wise Latent Streaming from Slow Reasoners to Fast Planners for Dynamic Vision Language Navigation | arXiv preprint | preprint | [arXiv](https://arxiv.org/abs/2607.16806) |
| 2026 | ViLAM: Distilling Vision-Language Reasoning into Attention Maps for Social Robot Navigation | arXiv preprint | preprint | [arXiv](https://arxiv.org/abs/2503.09820) |
| 2026 | Vision Language Action for TurtleBot Mobile Robot Path Planning | 2026 11th International Conference on Control and Robotics Engineering (ICCRE) | peer-reviewed | [DOI](https://doi.org/10.1109/ICCRE69951.2026.11593560) |
| 2026 | Walk With Me: Long-Horizon Social Navigation for Human-Centric Outdoor Assistance | arXiv preprint | preprint | [arXiv](https://arxiv.org/abs/2604.26839) |
| 2026 | Where Should I Join? Robot Group Joining via Language-Guided Goal Prediction | arXiv preprint | preprint | [arXiv](https://arxiv.org/abs/2609.28467) |
| 2025 | An LLM-based Architecture for Socially Intelligent Robot Navigation based on Social Cues | 2025 34th IEEE International Conference on Robot and Human Interactive Communication (RO-MAN) | peer-reviewed | [DOI](https://doi.org/10.1109/RO-MAN63969.2025.11217843) |
| 2025 | AutoSpatial: Visual-Language Reasoning for Social Robot Navigation through Efficient Spatial Reasoning Learning | 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) | peer-reviewed | [DOI](https://doi.org/10.1109/IROS60139.2025.11245987) · [arXiv](https://arxiv.org/abs/2503.07557) |
| 2025 | BehAV: Behavioral Rule Guided Autonomy Using VLMs for Robot Navigation in Outdoor Scenes | 2025 IEEE International Conference on Robotics and Automation (ICRA) | peer-reviewed | [DOI](https://doi.org/10.1109/ICRA55743.2025.11127890) · [arXiv](https://arxiv.org/abs/2409.16484) |
| 2025 | GSON: A Group-Based Social Navigation Framework With Large Multimodal Model | IEEE Robotics and Automation Letters | peer-reviewed | [DOI](https://doi.org/10.1109/LRA.2025.3595038) · [arXiv](https://arxiv.org/abs/2409.18084) |
| 2025 | Hey Robot! Personalizing Robot Navigation Through Model Predictive Control with a Large Language Model | 2025 IEEE International Conference on Robotics and Automation (ICRA) | peer-reviewed | [DOI](https://doi.org/10.1109/ICRA55743.2025.11128826) · [arXiv](https://arxiv.org/abs/2409.13393) |
| 2025 | MOSU: Autonomous Long-range Robot Navigation with Multi-modal Scene Understanding | International Symposium on Experimental Robotics (ISER) 2025 - per citation in Fang et al. (RA-L 2026, ref. [11]); proceedings not located | accepted, not yet indexed | [arXiv](https://arxiv.org/abs/2507.04686) |
| 2025 | Multi-Agent LLM Actor-Critic Framework for Social Robot Navigation | arXiv preprint | preprint | [arXiv](https://arxiv.org/abs/2503.09758) |
| 2025 | OLiVia-Nav: An Online Lifelong Vision Language Approach for Mobile Robot Social Navigation | 2025 IEEE International Conference on Robotics and Automation (ICRA) | peer-reviewed | [DOI](https://doi.org/10.1109/ICRA55743.2025.11128004) · [arXiv](https://arxiv.org/abs/2409.13675) |
| 2025 | Safe mobility support system using crowd mapping and avoidance route planning using VLM | 2025 IEEE International Conference on Real-time Computing and Robotics (RCAR) | peer-reviewed | [DOI](https://doi.org/10.1109/RCAR65431.2025.11139707) · [arXiv](https://arxiv.org/abs/2602.10910) |
| 2025 | Social-LLaVA: Enhancing Social Robot Navigation through Human-Language Reasoning | 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) | peer-reviewed | [DOI](https://doi.org/10.1109/IROS60139.2025.11247618) |
| 2025 | Socially-Aware Robot Navigation Enhanced by Bidirectional Natural Language Conversations Using Large Language Models | 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) | peer-reviewed | [DOI](https://doi.org/10.1109/IROS60139.2025.11246738) · [arXiv](https://arxiv.org/abs/2409.04965) |
| 2025 | SocialNav-MoE: A Mixture-of-Experts Vision Language Model for Socially Compliant Navigation with Reinforcement Fine-Tuning | arXiv preprint | preprint | [arXiv](https://arxiv.org/abs/2512.14757) |
| 2025 | Transparent Social Navigation for Autonomous Mobile Robots Via Vision-Language Models | 2025 34th IEEE International Conference on Robot and Human Interactive Communication (RO-MAN) | peer-reviewed | [DOI](https://doi.org/10.1109/RO-MAN63969.2025.11217693) · [arXiv](https://arxiv.org/abs/2504.05477) |
| 2025 | VLM-Social-Nav: Socially Aware Robot Navigation Through Scoring Using Vision-Language Models | IEEE Robotics and Automation Letters | peer-reviewed | [DOI](https://doi.org/10.1109/LRA.2024.3511409) · [arXiv](https://arxiv.org/abs/2404.00210) |
| 2024 | CoNVOI: Context-aware Navigation using Vision Language Models in Outdoor and Indoor Environments | 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) | peer-reviewed | [DOI](https://doi.org/10.1109/IROS58592.2024.10802716) · [arXiv](https://arxiv.org/abs/2403.15637) |
| 2024 | PANav: Toward Privacy-Aware Robot Navigation via Vision-Language Models | arXiv preprint | preprint | [arXiv](https://arxiv.org/abs/2410.04302) |
| 2024 | PREDILECT: Preferences Delineated with Zero-Shot Language-based Reasoning in Reinforcement Learning | Proceedings of the 2024 ACM/IEEE International Conference on Human-Robot Interaction (HRI 2024) | peer-reviewed | [DOI](https://doi.org/10.1145/3610977.3634970) · [arXiv](https://arxiv.org/abs/2402.15420) |
| 2024 | Unifying Large Language Model and Deep Reinforcement Learning for Human-in-Loop Interactive Socially-aware Navigation | arXiv preprint | preprint | [arXiv](https://arxiv.org/abs/2403.15648) |

### Adjacent foundation-model navigation (13)

| Year | Title | Venue | Links |
|---|---|---|---|
| 2025 | VL-TGS: Trajectory Generation and Selection Using Vision Language Models in Mapless Outdoor Environments | IEEE Robotics and Automation Letters | [DOI](https://doi.org/10.1109/LRA.2025.3559822) · [arXiv](https://arxiv.org/abs/2408.02454) |
| 2024 | NavGPT: Explicit Reasoning in Vision-and-Language Navigation with Large Language Models | Proceedings of the AAAI Conference on Artificial Intelligence (AAAI-24) | [DOI](https://doi.org/10.1609/aaai.v38i7.28597) · [arXiv](https://arxiv.org/abs/2305.16986) |
| 2024 | NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration | 2024 IEEE International Conference on Robotics and Automation (ICRA) | [DOI](https://doi.org/10.1109/ICRA57147.2024.10610665) · [arXiv](https://arxiv.org/abs/2310.07896) |
| 2024 | VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation | 2024 IEEE International Conference on Robotics and Automation (ICRA) | [DOI](https://doi.org/10.1109/ICRA57147.2024.10610712) · [arXiv](https://arxiv.org/abs/2312.03275) |
| 2023 | Code as Policies: Language Model Programs for Embodied Control | 2023 IEEE International Conference on Robotics and Automation (ICRA) | [DOI](https://doi.org/10.1109/ICRA48891.2023.10160591) · [arXiv](https://arxiv.org/abs/2209.07753) |
| 2023 | GNM: A General Navigation Model to Drive Any Robot | 2023 IEEE International Conference on Robotics and Automation (ICRA) | [DOI](https://doi.org/10.1109/ICRA48891.2023.10161227) · [arXiv](https://arxiv.org/abs/2210.03370) |
| 2023 | PaLM-E: An Embodied Multimodal Language Model | Proceedings of the 40th International Conference on Machine Learning (ICML 2023), PMLR 202 | [Publisher page](https://proceedings.mlr.press/v202/driess23a.html) · [arXiv](https://arxiv.org/abs/2303.03378) |
| 2023 | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Proceedings of The 7th Conference on Robot Learning (CoRL 2023), PMLR 229 | [Publisher page](https://proceedings.mlr.press/v229/zitkovich23a.html) · [arXiv](https://arxiv.org/abs/2307.15818) |
| 2023 | ViNT: A Foundation Model for Visual Navigation | Proceedings of The 7th Conference on Robot Learning (CoRL 2023), PMLR 229 | [Publisher page](https://proceedings.mlr.press/v229/shah23a.html) · [arXiv](https://arxiv.org/abs/2306.14846) |
| 2023 | Visual Language Maps for Robot Navigation | 2023 IEEE International Conference on Robotics and Automation (ICRA) | [DOI](https://doi.org/10.1109/ICRA48891.2023.10160969) · [arXiv](https://arxiv.org/abs/2210.05714) |
| 2023 | VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models | Proceedings of The 7th Conference on Robot Learning (CoRL 2023), PMLR 229 | [Publisher page](https://proceedings.mlr.press/v229/huang23b.html) · [arXiv](https://arxiv.org/abs/2307.05973) |
| 2022 | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | Proceedings of The 6th Conference on Robot Learning (CoRL 2022), PMLR 205 | [Publisher page](https://proceedings.mlr.press/v205/ichter23a.html) · [arXiv](https://arxiv.org/abs/2204.01691) |
| 2022 | LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action | Proceedings of The 6th Conference on Robot Learning (CoRL 2022), PMLR 205 | [Publisher page](https://proceedings.mlr.press/v205/shah23b.html) · [arXiv](https://arxiv.org/abs/2207.04429) |

### Datasets, simulators and benchmarks (15)

| Year | Title | Venue | Links |
|---|---|---|---|
| 2026 | DPed-VLN: A Benchmark for Socially Compliant Vision-and-Language Navigation in Dynamic Pedestrian Environments | arXiv preprint | [arXiv](https://arxiv.org/abs/2609.21504) |
| 2026 | HA-VLN 2.0: An Open Benchmark and Leaderboard for Human-Aware Navigation in Discrete and Continuous Environments with Dynamic Multi-Human Interactions | arXiv preprint | [arXiv](https://arxiv.org/abs/2503.14229) |
| 2026 | MUSON: A Reasoning-oriented Multimodal Dataset for Socially Compliant Navigation in Urban Environments | arXiv preprint | [arXiv](https://arxiv.org/abs/2512.22867) |
| 2026 | SocRATES: Language-Driven Scenario Generation for Evaluating Social Navigation Algorithms | IEEE Robotics and Automation Letters | [DOI](https://doi.org/10.1109/LRA.2026.3737041) · [arXiv](https://arxiv.org/abs/2412.19595) |
| 2026 | SONG: A Photorealistic 3D Gaussian Simulation Platform for Benchmarking Social Navigation | arXiv preprint | [arXiv](https://arxiv.org/abs/2607.25219) |
| 2025 | Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation | 2025 IEEE International Conference on Robotics and Automation (ICRA) | [DOI](https://doi.org/10.1109/ICRA55743.2025.11127635) · [arXiv](https://arxiv.org/abs/2409.12471) |
| 2025 | Few-Shot Inference of Human Perceptions of Robot Performance in Social Navigation Scenarios | arXiv preprint | [arXiv](https://arxiv.org/abs/2512.16019) |
| 2025 | SocialNav-SUB: Benchmarking VLMs for Scene Understanding in Social Robot Navigation | Proceedings of The 9th Conference on Robot Learning (CoRL 2025), PMLR 305 | [Publisher page](https://proceedings.mlr.press/v305/munje25a.html) · [arXiv](https://arxiv.org/abs/2509.08757) |
| 2024 | Human-Aware Vision-and-Language Navigation: Bridging Simulation to Reality with Dynamic Human Interactions | Advances in Neural Information Processing Systems 37 (NeurIPS 2024, Datasets and Benchmarks Track) | [DOI](https://doi.org/10.52202/079017-3795) · [arXiv](https://arxiv.org/abs/2406.19236) |
| 2024 | SACSoN: Scalable Autonomous Control for Social Navigation | IEEE Robotics and Automation Letters | [DOI](https://doi.org/10.1109/LRA.2023.3329626) · [arXiv](https://arxiv.org/abs/2306.01874) |
| 2023 | Toward Human-Like Social Robot Navigation: A Large-Scale, Multi-Modal, Social Human Navigation Dataset | 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) | [DOI](https://doi.org/10.1109/IROS55552.2023.10342447) · [arXiv](https://arxiv.org/abs/2303.14880) |
| 2022 | Socially CompliAnt Navigation Dataset (SCAND): A Large-Scale Dataset Of Demonstrations For Social Navigation | IEEE Robotics and Automation Letters | [DOI](https://doi.org/10.1109/LRA.2022.3184025) · [arXiv](https://arxiv.org/abs/2203.15041) |
| 2022 | SocNavBench: A Grounded Simulation Testing Framework for Evaluating Social Navigation | ACM Transactions on Human-Robot Interaction | [DOI](https://doi.org/10.1145/3476413) · [arXiv](https://arxiv.org/abs/2103.00047) |
| 2021 | Arena-Rosnav: Towards Deployment of Deep-Reinforcement-Learning-Based Obstacle Avoidance into Conventional Autonomous Navigation Systems | 2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) | [DOI](https://doi.org/10.1109/IROS51168.2021.9636226) · [arXiv](https://arxiv.org/abs/2104.03616) |
| 2020 | SEAN: Social Environment for Autonomous Navigation | Proceedings of the 8th International Conference on Human-Agent Interaction (HAI 2020) | [DOI](https://doi.org/10.1145/3406499.3418760) · [arXiv](https://arxiv.org/abs/2009.04300) |

### Classical and learning-based social navigation (12)

| Year | Title | Venue | Links |
|---|---|---|---|
| 2024 | Rethinking Social Robot Navigation: Leveraging the Best of Two Worlds | 2024 IEEE International Conference on Robotics and Automation (ICRA) | [DOI](https://doi.org/10.1109/ICRA57147.2024.10611710) · [arXiv](https://arxiv.org/abs/2309.13466) |
| 2023 | NaviSTAR: Socially Aware Robot Navigation with Hybrid Spatio-Temporal Graph Transformer and Preference Learning | 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) | [DOI](https://doi.org/10.1109/IROS55552.2023.10341395) · [arXiv](https://arxiv.org/abs/2304.05979) |
| 2022 | Group Estimation for Social Robot Navigation in Crowded Environments | 2022 22nd International Conference on Control, Automation and Systems (ICCAS) | [DOI](https://doi.org/10.23919/ICCAS55662.2022.10003761) |
| 2019 | Crowd-Robot Interaction: Crowd-aware Robot Navigation with Attention-based Deep Reinforcement Learning | 2019 International Conference on Robotics and Automation (ICRA) | [DOI](https://doi.org/10.1109/ICRA.2019.8794134) · [arXiv](https://arxiv.org/abs/1809.08835) |
| 2018 | Socially Compliant Navigation through Raw Depth Inputs with Generative Adversarial Imitation Learning | 2018 IEEE International Conference on Robotics and Automation (ICRA) | [DOI](https://doi.org/10.1109/ICRA.2018.8460968) · [arXiv](https://arxiv.org/abs/1710.02543) |
| 2017 | Decentralized Non-communicating Multiagent Collision Avoidance with Deep Reinforcement Learning | 2017 IEEE International Conference on Robotics and Automation (ICRA) | [DOI](https://doi.org/10.1109/ICRA.2017.7989037) · [arXiv](https://arxiv.org/abs/1609.07845) |
| 2017 | Socially Aware Motion Planning with Deep Reinforcement Learning | 2017 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) | [DOI](https://doi.org/10.1109/IROS.2017.8202312) · [arXiv](https://arxiv.org/abs/1703.08862) |
| 2016 | Learning Socially Normative Robot Navigation Behaviors with Bayesian Inverse Reinforcement Learning | 2016 IEEE International Conference on Robotics and Automation (ICRA) | [DOI](https://doi.org/10.1109/ICRA.2016.7487452) |
| 2016 | Socially Compliant Mobile Robot Navigation via Inverse Reinforcement Learning | The International Journal of Robotics Research | [DOI](https://doi.org/10.1177/0278364915619772) |
| 2012 | Feature-Based Prediction of Trajectories for Socially Compliant Navigation | Robotics: Science and Systems VIII (RSS 2012) | [DOI](https://doi.org/10.15607/RSS.2012.VIII.025) |
| 2010 | Unfreezing the Robot: Navigation in Dense, Interacting Crowds | 2010 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) | [DOI](https://doi.org/10.1109/IROS.2010.5654369) |
| 1995 | Social force model for pedestrian dynamics | Physical Review E | [DOI](https://doi.org/10.1103/PhysRevE.51.4282) · [arXiv](https://arxiv.org/abs/cond-mat/9805244) |

### Existing surveys, reviews and guidelines (13)

| Year | Title | Venue | Links |
|---|---|---|---|
| 2026 | Robot Navigation via Foundation Language Models: A Review | ACM Computing Surveys | [DOI](https://doi.org/10.1145/3802539) |
| 2026 | Socially aware navigation for mobile robots: a survey on deep reinforcement learning approaches | Applied Intelligence | [DOI](https://doi.org/10.1007/s10489-025-06982-5) · [arXiv](https://arxiv.org/abs/2512.00049) |
| 2026 | Vision-Language Models for Deployable Social Robot Navigation: Bridging Semantic Reasoning and Low-Level Control | arXiv preprint | [arXiv](https://arxiv.org/abs/2606.28760) |
| 2025 | Principles and Guidelines for Evaluating Social Robot Navigation Algorithms | ACM Transactions on Human-Robot Interaction | [DOI](https://doi.org/10.1145/3700599) · [arXiv](https://arxiv.org/abs/2306.16740) |
| 2025 | Social robot navigation: a review and benchmarking of learning-based methods | Frontiers in Robotics and AI | [DOI](https://doi.org/10.3389/frobt.2025.1658643) |
| 2024 | A Survey on Socially Aware Robot Navigation: Taxonomy and Future Challenges | The International Journal of Robotics Research | [DOI](https://doi.org/10.1177/02783649241230562) · [arXiv](https://arxiv.org/abs/2311.06922) |
| 2024 | Bridging Requirements, Planning, and Evaluation: A Review of Social Robot Navigation | Sensors | [DOI](https://doi.org/10.3390/s24092794) |
| 2024 | Conflict Avoidance in Social Navigation—a Survey | ACM Transactions on Human-Robot Interaction | [DOI](https://doi.org/10.1145/3647983) · [arXiv](https://arxiv.org/abs/2106.12113) |
| 2023 | Core Challenges of Social Robot Navigation: A Survey | ACM Transactions on Human-Robot Interaction | [DOI](https://doi.org/10.1145/3583741) · [arXiv](https://arxiv.org/abs/2103.05668) |
| 2022 | Evaluation of Socially-Aware Robot Navigation | Frontiers in Robotics and AI | [DOI](https://doi.org/10.3389/frobt.2021.721317) |
| 2021 | A survey on human-aware robot navigation | Robotics and Autonomous Systems | [DOI](https://doi.org/10.1016/j.robot.2021.103837) · [arXiv](https://arxiv.org/abs/2106.11650) |
| 2017 | Recent trends in social aware robot navigation: A survey | Robotics and Autonomous Systems | [DOI](https://doi.org/10.1016/j.robot.2017.03.002) |
| 2013 | Human-aware robot navigation: A survey | Robotics and Autonomous Systems | [DOI](https://doi.org/10.1016/j.robot.2013.05.007) |

### Representative pre-FM comparison set (40)

Representative rather than exhaustive: exemplars cited by at least three of seven reference surveys per paradigm, plus the corpus works (survey Section 2.3). 12 of these works are also listed above.

| Paradigm | Year | Title | Venue | Link |
|---|---|---|---|---|
| Geometric and socially aware planning | 2000 | Probabilistic algorithms and the interactive museum tour-guide robot Minerva | The International Journal of Robotics Research | [DOI](https://doi.org/10.1177/02783640022067922) |
| Geometric and socially aware planning | 2007 | A human aware mobile robot motion planner | IEEE T-RO 23(5) 2007 | [DOI](https://doi.org/10.1109/tro.2007.904911) |
| Geometric and socially aware planning | 2008 | Reciprocal velocity obstacles for real-time multi-agent navigation | 2008 IEEE International Conference on Robotics and Automation | [DOI](https://doi.org/10.1109/robot.2008.4543489) |
| Geometric and socially aware planning | 2010 | A framework towards a socially aware mobile robot motion in human-centered dynamic environment | 2010 IEEE/RSJ International Conference on Intelligent Robots and Systems | [DOI](https://doi.org/10.1109/iros.2010.5649688) |
| Geometric and socially aware planning | 2010 | Trajectory planning for robots in dynamic human environments | 2010 IEEE/RSJ International Conference on Intelligent Robots and Systems | [DOI](https://doi.org/10.1109/iros.2010.5651531) |
| Geometric and socially aware planning | 2018 | Social momentum: A framework for legible navigation in dynamic multi-agent environments | HRI 2018 | [DOI](https://doi.org/10.1145/3171221.3171255) |
| Geometric and socially aware planning | 2019 | Effects of distinct robot navigation strategies on human behavior in a crowded environment | HRI 2019 | [DOI](https://doi.org/10.1109/hri.2019.8673115) |
| Hybrid model-based and learned | 2020 | Frozone: Freezing-free pedestrian-friendly navigation in human crowds | IEEE Robotics and Automation Letters | [DOI](https://doi.org/10.1109/lra.2020.2996593) |
| Hybrid model-based and learned | 2021 | Where to go next: Learning a subgoal recommendation policy for navigation in dynamic environments | IEEE Robotics and Automation Letters | [DOI](https://doi.org/10.1109/lra.2021.3068662) |
| Hybrid model-based and learned | 2024 | Rethinking Social Robot Navigation: Leveraging the Best of Two Worlds | 2024 IEEE International Conference on Robotics and Automation (ICRA) | [DOI](https://doi.org/10.1109/ICRA57147.2024.10611710) |
| Proxemics and social costmaps | 2006 | Evaluation of passing distance for social robots | ROMAN 2006 - The 15th IEEE International Symposium on Robot and Human Interactive Communication | [DOI](https://doi.org/10.1109/roman.2006.314436) |
| Proxemics and social costmaps | 2010 | A mobile robot that understands pedestrian spatial behaviors | 2010 IEEE/RSJ International Conference on Intelligent Robots and Systems | [DOI](https://doi.org/10.1109/iros.2010.5649718) |
| Proxemics and social costmaps | 2016 | Robot navigation in large-scale social maps: An action recognition approach | Expert Systems with Applications | [DOI](https://doi.org/10.1016/j.eswa.2016.09.026) |
| Social-force models | 1995 | Social force model for pedestrian dynamics | Physical Review E | [DOI](https://doi.org/10.1103/PhysRevE.51.4282) |
| Social-force models | 2013 | Robot companion: A social-force based approach with human awareness-navigation in crowded environments | 2013 IEEE/RSJ International Conference on Intelligent Robots and Systems | [DOI](https://doi.org/10.1109/iros.2013.6696576) |
| Social-force models | 2014 | Towards a socially acceptable collision avoidance for a mobile robot navigating among pedestrians using a pedestrian model | International Journal of Social Robotics | [DOI](https://doi.org/10.1007/s12369-014-0238-y) |
| Group and F-formation navigation | 2018 | To approach humans?: A unified framework for approaching pose prediction and socially aware robot navigation | IEEE Transactions on Cognitive and Developmental Systems | [DOI](https://doi.org/10.1109/tcds.2017.2751963) |
| Group and F-formation navigation | 2021 | Group-based motion prediction for navigation in crowded environments | CoRL 2021 | [arXiv](https://arxiv.org/abs/2107.11637) |
| Group and F-formation navigation | 2022 | Group Estimation for Social Robot Navigation in Crowded Environments | 2022 22nd International Conference on Control, Automation and Systems (ICCAS) | [DOI](https://doi.org/10.23919/ICCAS55662.2022.10003761) |
| Group and F-formation navigation | 2022 | Learning a group-aware policy for robot navigation | 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) | [DOI](https://doi.org/10.1109/iros47612.2022.9981183) |
| Trajectory prediction and prediction-coupled planning | 2009 | You'll never walk alone: Modeling social behavior for multi-target tracking | ICCV 2009 | [DOI](https://doi.org/10.1109/iccv.2009.5459260) |
| Trajectory prediction and prediction-coupled planning | 2010 | Unfreezing the Robot: Navigation in Dense, Interacting Crowds | 2010 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) | [DOI](https://doi.org/10.1109/IROS.2010.5654369) |
| Trajectory prediction and prediction-coupled planning | 2016 | Social LSTM: Human trajectory prediction in crowded spaces | CVPR 2016 | [DOI](https://doi.org/10.1109/cvpr.2016.110) |
| Trajectory prediction and prediction-coupled planning | 2018 | Social attention: Modeling attention in human crowds | 2018 IEEE International Conference on Robotics and Automation (ICRA) | [DOI](https://doi.org/10.1109/icra.2018.8460504) |
| Inverse reinforcement learning | 2010 | Learning to navigate through crowded environments | 2010 IEEE International Conference on Robotics and Automation | [DOI](https://doi.org/10.1109/robot.2010.5509772) |
| Inverse reinforcement learning | 2012 | Feature-Based Prediction of Trajectories for Socially Compliant Navigation | Robotics: Science and Systems VIII (RSS 2012) | [DOI](https://doi.org/10.15607/RSS.2012.VIII.025) |
| Inverse reinforcement learning | 2012 | Socially-aware robot navigation: A learning approach | 2012 IEEE/RSJ International Conference on Intelligent Robots and Systems | [DOI](https://doi.org/10.1109/iros.2012.6385716) |
| Inverse reinforcement learning | 2014 | Inverse reinforcement learning algorithms and features for robot navigation in crowds | 2014 IEEE/RSJ International Conference on Intelligent Robots and Systems | [DOI](https://doi.org/10.1109/iros.2014.6942731) |
| Inverse reinforcement learning | 2016 | Socially Compliant Mobile Robot Navigation via Inverse Reinforcement Learning | The International Journal of Robotics Research | [DOI](https://doi.org/10.1177/0278364915619772) |
| Inverse reinforcement learning | 2016 | Learning Socially Normative Robot Navigation Behaviors with Bayesian Inverse Reinforcement Learning | 2016 IEEE International Conference on Robotics and Automation (ICRA) | [DOI](https://doi.org/10.1109/ICRA.2016.7487452) |
| Inverse reinforcement learning | 2016 | Socially adaptive path planning in human environments using inverse reinforcement learning | International Journal of Social Robotics | [DOI](https://doi.org/10.1007/s12369-015-0310-2) |
| Imitation learning | 2018 | Socially Compliant Navigation through Raw Depth Inputs with Generative Adversarial Imitation Learning | 2018 IEEE International Conference on Robotics and Automation (ICRA) | [DOI](https://doi.org/10.1109/ICRA.2018.8460968) |
| Imitation learning | 2019 | DeepMoTIon: Learning to navigate like humans | 2019 28th IEEE International Conference on Robot and Human Interactive Communication (RO-MAN) | [DOI](https://doi.org/10.1109/ro-man46459.2019.8956408) |
| Deep reinforcement learning | 2017 | Decentralized Non-communicating Multiagent Collision Avoidance with Deep Reinforcement Learning | 2017 IEEE International Conference on Robotics and Automation (ICRA) | [DOI](https://doi.org/10.1109/ICRA.2017.7989037) |
| Deep reinforcement learning | 2017 | Socially Aware Motion Planning with Deep Reinforcement Learning | 2017 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) | [DOI](https://doi.org/10.1109/IROS.2017.8202312) |
| Deep reinforcement learning | 2018 | Motion planning among dynamic decision-making agents with deep reinforcement learning | IROS 2018 | [DOI](https://doi.org/10.1109/iros.2018.8593871) |
| Deep reinforcement learning | 2020 | Robot navigation in crowded environments using deep reinforcement learning | 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) | [DOI](https://doi.org/10.1109/iros45743.2020.9341540) |
| Attention, graph and transformer models | 2019 | Crowd-Robot Interaction: Crowd-aware Robot Navigation with Attention-based Deep Reinforcement Learning | 2019 International Conference on Robotics and Automation (ICRA) | [DOI](https://doi.org/10.1109/ICRA.2019.8794134) |
| Attention, graph and transformer models | 2020 | Relational graph learning for crowd navigation | IROS 2020 | [DOI](https://doi.org/10.1109/iros45743.2020.9340705) |
| Attention, graph and transformer models | 2023 | NaviSTAR: Socially Aware Robot Navigation with Hybrid Spatio-Temporal Graph Transformer and Preference Learning | 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) | [DOI](https://doi.org/10.1109/IROS55552.2023.10341395) |
