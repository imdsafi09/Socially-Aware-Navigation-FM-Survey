"""Stage 2: screening record for every unique hit of the three arXiv search passes plus candidates found by web search
and citation chasing. Writes screening_record.csv (one row per candidate). Decisions: INCLUDE (in corpus), EXCLUDE,
BACKGROUND ONLY, RELATED VERSION (of a corpus paper). Title/abstract screening for clear out-of-scope hits (reason codes
R1-R6); full-text screening (fulltext/<id>.txt or downloaded PDF) for every candidate that was plausibly in scope."""
import json, os, csv, glob, yaml
T = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(T, '..', '..', '..'))
R = {'R1': 'Not robot/embodied navigation (non-robotics use of "navigate", NLP/social-science/LLM-evaluation topic)',
     'R2': 'Autonomous driving, UAV or other non-ground-robot domain',
     'R3': 'Robot manipulation / HRI / perception without mobile-navigation behaviour (fails A)',
     'R4': 'Embodied/robot navigation without an explicit social-navigation capability (fails C)',
     'R5': 'Social navigation without an FM role in the navigation method (fails B)',
     'R6': 'Navigation assistance for people (the human navigates, not a robot) (fails A)'}
CODE = {
 'R1': '2305.14310 2310.02457 2407.12425 2409.08027 2410.05243 2410.15044 2501.01544 2501.02092 2502.16671 2503.13975 2503.14484 2503.21986 2503.22040 2504.01588 2505.03434 2505.04354 2505.17461 2505.18553 2505.21479 2505.24315 2506.00900 2506.06606 2506.06737 2506.13276 2506.22493 2506.23046 2506.24019 2507.02592 2507.19672 2508.05129 2508.09036 2508.19004 2509.01035 2509.07819 2509.11648 2509.22537 2510.19687 2510.25224 2511.08639 2511.10810 2512.18582 2512.19992 2601.01546 2602.01959 2602.04456 2602.17734 2602.18710 2602.23400 2603.14341 2603.20231 2603.25422 2604.07502 2604.11721 2604.16022 2605.03287 2605.07550 2605.13706 2605.31574 2606.05896 2606.13397 2607.12195 2607.17394 2607.25620 2607.28094 2608.08320 2608.09946 2608.11973 2608.13239 2608.28968 2608.30428 2609.08637 2609.15972 '
       '2401.13311 2407.09652 2501.05925 2502.04756 2502.16101 2505.01754 2505.23179 2507.02103 2510.00339 2510.24594 2512.21055 2601.05904 2603.04217 2603.16642 2603.26898 2604.01742 2605.17364 2605.24319 2606.08792 2606.09024 2606.23633 2609.02421',
 'R2': '2412.05893 2412.20230 2503.02572 2505.16498 2509.14063 2512.12302 2601.13809 2603.16013 2603.19533 2603.28032 2606.02313 2607.16938 2609.18326 2610.08526 2501.01439 2606.17577',
 'R3': '2309.02561 2406.08824 2408.07910 2501.10105 2501.12128 2504.13898 2506.20566 2508.05646 2508.10287 2510.01642 2510.27033 2511.03676 2512.07177 2601.00978 2602.09472 2604.02032 2604.19522 2605.00943 2605.31196 2606.02775 2606.23339 2608.00652 2608.22035 2609.34220 2610.05964 2608.06898 2508.02505',
 'R4': '2311.08244 2312.16016 2401.17083 2407.09890 2412.01250 2502.19024 2505.01881 2505.01931 2507.11334 2508.12087 2510.01049 2510.21860 2512.01078 2512.16755 2512.20206 2602.02220 2602.15864 2602.18606 2603.12696 2603.28890 2604.07973 2605.07496 2605.23187 2606.08029 2606.17639 2607.06724 2607.23797 2608.01456 2609.21316 2609.22813 2609.26857 2610.19361 2411.01796 2503.08367 2506.02556',
 'R5': '2309.12568 2401.12275 2503.16441 2508.01192 2605.02759',
 'R6': '2410.04005 2503.12731 2503.16475 2509.02425 2511.17581 2603.10703 2603.15624 2604.23970 2605.11782 2503.12844 2609.17882 2610.19330',
}
# Full-text-screened candidates (arXiv id or other identifier): decision, category/target, reason
MANUAL = {
 '2409.13244': ('BACKGROUND ONLY', 'S2/S6 background', 'Falcon (ICRA 2025): RL social navigation + Social-HM3D/MP3D benchmark; no FM (fails B); benchmark used by HUMA'),
 '2412.02655': ('EXCLUDE', '-', 'LLM path planning for industrial pick-and-place; pedestrian distance is one incidental constraint, evaluated only qualitatively (C not met)'),
 '2402.03494': ('EXCLUDE', '-', 'Beyond Text: vocal cues for LLM instruction disambiguation; no social-navigation behaviour (fails C)'),
 '2406.02425': ('EXCLUDE', '-', 'CoNav: human-centered collaborative navigation benchmark; FM used only to animate the simulated humans, not in the navigation method, and the task is collaborative navigation rather than social compliance (fails B and C)'),
 '2503.12333': ('EXCLUDE', '-', 'GameChat: multi-robot LLM dialogue for deadlock resolution among robots; no humans (fails C)'),
 '2508.03138': ('EXCLUDE', '-', 'Language as Cost: VLM hazard mapping for navigation; hazards not social (fails C); adjacent'),
 '2508.11093': ('EXCLUDE', '-', 'GUIDER-VLM: human-robot collaboration intent inference; RO-MAN workshop; not social navigation (fails A/C)'),
 '2509.17941': ('BACKGROUND ONLY', 'S2 background', 'ComposableNav (CoRL 2025): social instruction primitives via diffusion; FM only assumed upstream, not used (fails B); compares with VLM social-navigation baselines'),
 '2509.21189': ('EXCLUDE', '-', 'ReasonNav ("Human-like navigation in a world built for humans"): VLM reads signs/asks for directions; no social-compliance capability evaluated (fails C)'),
 '2510.23509': ('EXCLUDE (WITHDRAWN)', '-', 'NaviWM: withdrawn by authors on arXiv; recorded in EXCLUDED_WITHDRAWN_WORKS.md; not counted'),
 '2511.13524': ('EXCLUDE', '-', 'FreeAskWorld: interactive human-centric simulator; no robot social-navigation capability evaluated (fails C)'),
 '2512.10046': ('EXCLUDE', '-', 'SimWorld-Robotics (NeurIPS 2025): urban simulator with pedestrians; FM-agnostic benchmark without social-navigation metrics (fails B/C)'),
 '2601.14622': ('RELATED VERSION', '2026_Xiao_Prompting-VLMs-JSAI', 'Probing Prompt Design: related, differently titled version of the JSAI 2026 corpus paper (same authors/topic); not a separate work'),
 '2501.09024': ('RELATED VERSION', '2025_Payandeh_Social-LLaVA', 'arXiv version (different title) of the IROS 2025 Social-LLaVA corpus paper'),
 '2602.02459': ('EXCLUDE', '-', 'TIC-VLA: navigation VLA in dynamic environments; no explicit social-navigation evaluation (fails C); adjacent'),
 '2602.12597': ('EXCLUDE', '-', 'PISHYAR: smart cane (human-carried device), not a mobile robot (fails A)'),
 '2602.19983': ('BACKGROUND ONLY', 'S3 background', 'CORE: VLM contextual safety constraints enforced by CBFs; social restriction is one sub-case among hazards; primary contribution is contextual safety (C only marginal)'),
 '2603.03942': ('EXCLUDE', '-', 'Lightweight Visual Reasoning for Socially-Aware Robots: generic VLM reasoning module, no navigation evaluation (fails A/C)'),
 '2603.11290': ('EXCLUDE', '-', 'Causal approach to predicting human perceptions of social-navigation robots: no FM (fails B); background for C4'),
 '2604.05525': ('BACKGROUND ONLY', 'S6 background', 'CrowdVLA: VLA agents for crowd simulation (pedestrians, not a robot) (fails A); relevant to simulated-human realism'),
 '2605.06863': ('BACKGROUND ONLY', 'S6 background', 'Bi3: bicultural social-navigation dataset without FM (fails B); relevant to C25 cultural adaptation'),
 '2605.24562': ('EXCLUDE', '-', 'PedestrianQA: VLM pedestrian-intention benchmark for autonomous driving (fails A)'),
 '2606.20458': ('EXCLUDE', '-', 'Slow Brain, Fast Planner: latency-resilient VLM urban navigation; no explicit social evaluation (fails C); adjacent'),
 '2606.30404': ('EXCLUDE', '-', 'HUMEMBR: routine memory for person search/EQA; finding people is not socially compliant navigation (fails C)'),
 '2607.01044': ('EXCLUDE', '-', 'CommNav ("Robots Ask the Way"): communication-enabled social navigation; the proposed COMM model uses structured sighting data without an FM, and an LLM (Qwen3-8B) only converts these data into instruction text for a language-input variant read by a frozen BERT encoder (fails B); IROS 2026 accepted per authors'),
 '2607.09261': ('EXCLUDE', '-', 'VR validation of multimodal HRI in socially aware navigation: methodological user study, no FM (fails B)'),
 '2608.12515': ('EXCLUDE', '-', 'Proxemic-risk assessment from egocentric robot images with VLMs: ECCV workshop, non-archival; offline perception only'),
 '2609.40245': ('EXCLUDE', '-', 'STARS (CoRL 2026): spatiotemporal social representations (GNN); no FM (fails B)'),
 '2610.02750': ('EXCLUDE', '-', 'CSIR: person-goal navigation (search for a recipient); not social-compliance behaviour (fails C)'),
 '2610.18373': ('EXCLUDE', '-', 'DR-VLA: quadruped navigation from egocentric web videos; no explicit social evaluation (fails C); adjacent'),
 '2610.22092': ('EXCLUDE', '-', 'Onboard LLM reasoning for human-aware UAV navigation: aerial (fails A); workshop paper'),
 '2507.12273': ('EXCLUDE', '-', 'Museum guide robot: LLM used for visitor Q&A; navigation by SLAM; FM is not used in the navigation method (fails B)'),
 '2509.10317': ('EXCLUDE', '-', 'Tour-guide robot with LLM-generated storytelling scenarios; no navigation behaviour evaluated (fails A/C)'),
 '2610.18093': ('BACKGROUND ONLY', 'S6 background', 'LynxScenes: large real-world wheel-legged robot dataset with navigation instructions; no FM method (fails B)'),
 '2608.27456': ('EXCLUDE', '-', 'UrbanGround: MLLM urban navigation sandbox; no social-navigation capability (fails C)'),
}
# Candidates found outside the arXiv result files (web search / citation chasing)
EXTRA = {
 '2409.13393': ('web', 'Hey Robot! Personalizing Robot Navigation Through MPC with an LLM', 'D. Martinez-Baselga et al.', '2025', 'ICRA 2025', 'https://doi.org/10.1109/ICRA55743.2025.11128826'),
 '2303.14880': ('citation', 'Toward Human-Like Social Robot Navigation: ... (MuSoHu)', 'D. M. Nguyen et al.', '2023', 'IROS 2023', 'https://doi.org/10.1109/IROS55552.2023.10342447'),
 '2306.01874': ('citation', 'SACSoN: Scalable Autonomous Control for Social Navigation', 'N. Hirose et al.', '2024', 'IEEE RA-L 9(1)', 'https://doi.org/10.1109/LRA.2023.3329626'),
 '2409.20445': ('citation', 'Robot Navigation Using Physically Grounded VLMs in Outdoor Environments (VLM-GroNav)', 'M. Elnoor et al.', '2024', 'arXiv (ICRA 2025 per citing note)', 'https://arxiv.org/abs/2409.20445'),
 '2308.12537': ('citation', 'HuBo-VLM: Unified VLM designed for HUman roBOt interaction tasks', 'Z. Dong et al.', '2023', 'arXiv', 'https://arxiv.org/abs/2308.12537'),
 '2511.12232': ('citation', 'SocialNav-Map: Dynamic Mapping with Human Trajectory Prediction for Zero-Shot Social Navigation', 'Not recorded', '2025', 'arXiv', 'https://arxiv.org/abs/2511.12232'),
 '2603.15359': ('citation', 'NavThinker: Action-Conditioned World Models for Coupled Prediction and Planning in Social Navigation', 'T. Hu, Z. Gong, L. Kong et al.', '2026', 'arXiv', 'https://arxiv.org/abs/2603.15359'),
 'doi:10.24963/ijcai.2026/696': ('final check', 'AHead-VLN: A Hierarchical Reasoning Framework Guided by Foresight for Human-Aware Navigation', 'J. Zhang et al.', '2026', 'IJCAI 2026, pp. 6254-6262', 'https://doi.org/10.24963/ijcai.2026/696'),
 'doi:10.1609/aaai.v40i22.38941': ('citation', 'Learning from Human Gaze: Human-like Robot Social Navigation in Dense Crowds (GazeNav)', 'Z. Yu et al.', '2026', 'AAAI 2026, 40(22):18728-18736', 'https://doi.org/10.1609/aaai.v40i22.38941'),
 'doi:10.1109/ICRA57147.2024.10611462': ('web', 'LIM2N (ICRA 2024 version of arXiv 2311.08244 "Language and Sketching")', 'Not recorded', '2024', 'ICRA 2024', 'https://doi.org/10.1109/ICRA57147.2024.10611462'),
 'doi:10.1109/ICCVW69036.2025.00262': ('citation', 'Towards Proactive Social Robots: Distilling Visual Knowledge from Large VLMs', 'G. De Simone et al.', '2025', 'ICCV 2025 Workshops (Crossref pp. 2513-2523; CVF pp. 2492-2502)', 'https://doi.org/10.1109/ICCVW69036.2025.00262'),
 'doi:10.1109/IROS58592.2024.10802269': ('web', 'SocialNav-FTI: Field-Theory-Inspired Social-aware Navigation Framework based on Human Behavior', 'Not recorded', '2024', 'IROS 2024, pp. 4808-4815', 'https://doi.org/10.1109/IROS58592.2024.10802269'),
 'doi:10.1145/3737611.3776944': ('web', 'Socially-Aware Robot Navigation Using Large Language Models: System and Evaluation', 'Not recorded', '2026', 'ICDCN 2026 Companion, pp. 50-51', 'https://doi.org/10.1145/3737611.3776944'),
 'doi:10.1145/3748777.3748807': ('web', 'LLM-Powered Embodied Intelligence for Socially-Aware Robot Navigation in Human-Robot Interaction', 'Not recorded', '2025', 'SSTD 2025, pp. 145-148', 'https://doi.org/10.1145/3748777.3748807'),
}
MANUAL.update({
 '2409.20445': ('EXCLUDE', '-', 'VLM-GroNav: VLM terrain/traversability grounding outdoors; no social capability (fails C)'),
 '2308.12537': ('EXCLUDE', '-', 'HuBo-VLM: VLM for HRI perception tasks (detection/grounding); no navigation (fails A)'),
 '2511.12232': ('EXCLUDE', '-', 'SocialNav-Map: dynamic mapping + trajectory prediction for zero-shot social navigation; no FM in the method (fails B)'),
 '2603.15359': ('EXCLUDE', '-', 'NavThinker: world model + RL social navigation; pretrained vision encoder (Depth Anything) only, no language/multimodal reasoning (fails B under the vision-only rule)'),
 'doi:10.24963/ijcai.2026/696': ('INCLUDE', '2026_Zhang_AHead-VLN', 'venue-only paper found in the final check at the cut-off (publisher index); included after full-text screening'),
 'doi:10.1609/aaai.v40i22.38941': ('BACKGROUND ONLY', 'S2/S6 background', 'GazeNav (AAAI 2026): gaze-guided social navigation and dataset; no FM (fails B); in Cai Table 2'),
 'doi:10.1109/ICRA57147.2024.10611462': ('EXCLUDE', '-', 'LIM2N: LLM command/sketch interface for multitask navigation; social behaviour not evaluated (fails C)'),
 'doi:10.1109/ICCVW69036.2025.00262': ('EXCLUDE', '-', 'Proactive social robots (ICCV workshop): VLM distillation for engagement perception, not navigation (fails A)'),
 'doi:10.1109/IROS58592.2024.10802269': ('BACKGROUND ONLY', 'S2 background', 'SocialNav-FTI: field-theory social navigation; no FM use identified in the record (fails B)'),
 'doi:10.1145/3737611.3776944': ('EXCLUDE', '-', '2-page companion abstract (ICDCN 2026); insufficient methods/results for coding'),
 'doi:10.1145/3748777.3748807': ('EXCLUDE', '-', '4-page short paper (SSTD 2025); insufficient methods/results for coding'),
})
def main():
    S = {}
    for pas, fn in [('P1', 'arxiv_union.json'), ('P2', 'pass2_union.json'), ('P3', 'pass3_union.json')]:
        for k, v in json.load(open(os.path.join(T, 'search', fn))).items():
            kk = k.rsplit('v', 1)[0]
            if kk in S: S[kk]['passes'].append(pas); continue
            S[kk] = dict(key=kk, source=pas, passes=[pas], title=v['title'], authors=(v['authors'][0] + (' et al.' if len(v['authors']) > 1 else '')),
                         date=v['published'], comment=v.get('comment') or '', url=f'https://arxiv.org/abs/{kk}')
    for kk, (src, ti, au, yr, ven, url) in EXTRA.items():
        if kk not in S: S[kk] = dict(key=kk, source=src, passes=[src], title=ti, authors=au, date=yr, comment=ven, url=url)
    corp = {}
    for f in glob.glob(os.path.join(ROOT, '08_Paper_Notes', '*.md')):
        y = yaml.safe_load(open(f).read().split('---', 2)[1]); ev = y.get('external_verification') or {}
        ax = str(ev.get('arxiv', ev.get('arxiv_id', ''))).split('v')[0].split(' ')[0]
        corp[ax] = (y['id'], 'stage2' in y)
    code = {i: c for c, ids in CODE.items() for i in ids.split()}
    rows = []
    for kk, r in sorted(S.items()):
        if kk in corp:
            cid, s2 = corp[kk]; r.update(decision='INCLUDE', target=cid, screening='full text', reason=('added in Stage 2' if s2 else 'already in Stage-1 corpus'))
        elif kk in MANUAL:
            d, tg, why = MANUAL[kk]; r.update(decision=d, target=tg, screening='full text' if kk.replace('.', '').isdigit() is False or True else '', reason=why)
        elif kk in code:
            r.update(decision='EXCLUDE', target='-', screening='title/abstract', reason=code[kk] + ': ' + R[code[kk]])
        else:
            raise SystemExit(f'unscreened: {kk} {r["title"]}')
        r['passes'] = '+'.join(r['passes']); rows.append(r)
    cols = ['key', 'source', 'passes', 'title', 'authors', 'date', 'comment', 'url', 'decision', 'target', 'screening', 'reason']
    with open(os.path.join(T, 'screening_record.csv'), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    import collections
    print(len(rows), collections.Counter(r['decision'] for r in rows), collections.Counter((r['source'], r['decision']) for r in rows))
if __name__ == '__main__': main()
