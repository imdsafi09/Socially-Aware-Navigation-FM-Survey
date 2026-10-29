"""Stage-11 screening decisions for every unique candidate of the final coverage search (2026-10-26). Indices refer to the
alphabetical list of candidates new to the project (union.json, status 'new'). Codes R1-R6 as in Stage 2; R7 = survey, review,
position paper or thesis (outside the expansion scope: surveys enter the corpus only through the seed set; theses repackage
published work); U = appears to meet criteria A-C on title/abstract (or cannot be decided from the abstract) but the full text was not
legitimately accessible in this session -> not coded, listed as unresolved. Writes stage11/S1_final_search_record.csv."""
import csv, json, os
H = os.path.dirname(os.path.abspath(__file__))
R = {'R1': 'R1: Not robot/embodied navigation (incl. non-scholarly repository items)', 'R2': 'R2: Autonomous driving, UAV or other non-ground-robot domain',
     'R3': 'R3: Manipulation / HRI / perception without mobile-navigation behaviour (fails A)', 'R4': 'R4: Embodied navigation without explicit social capability (fails C)',
     'R5': 'R5: Social navigation without an FM role in the navigation method (fails B)', 'R6': 'R6: Navigation assistance for people (fails A)',
     'R7': 'R7: Survey, review, position paper or thesis (outside the screening scope)',
     'R8': 'R8: Central claims or data not verifiable after full-text assessment'}  # exclusion rule stated in manuscript Section 2.2 (adopted 2026-10-28); applied to one record (86)
D = {}
codes = """0 R1;1 R7;2 R7;3 R4;4 R7;5 R7;6 R7;7 R4;8 R4;9 R3;10 R4;11 U;12 R3;13 R3;14 R7;15 R1;16 I;17 R5;18 R2;19 R6;20 R2;21 R4;22 R4;23 R4;24 R1;25 R7;26 R3;27 R5;28 R3;29 R4;
30 R4;31 R4;32 R3;33 R3;34 R3;35 R3;36 R2;37 R2;38 R4;39 R1;40 R7;41 R1;42 R6;43 R4;44 R1;45 R2;46 R7;47 R7;48 R5;49 R3;50 U;51 R1;52 R4;53 R3;54 R2;55 R4;56 R3;57 R3;58 R7;59 R3;
60 R2;61 R1;62 R3;63 R3;64 R2;65 R3;66 R7;67 R7;68 R3;69 R1;70 R2;71 R2;72 R6;73 R1;74 R4;75 R4;76 R3;77 R4;78 R1;79 R3;80 R2;81 R4;82 R4;83 R1;84 R7;85 R4;86 R8;87 R7;88 R7;89 R4;
90 R4;91 R1;92 R2;93 R4;94 R1;95 R3;96 R4;97 R3;98 R3;99 R4;100 R3;101 R4;102 R6;103 R4;104 R3;105 R6;106 R4;107 R4;108 R4;109 R4;110 R1;111 R7;112 R4;113 R7;114 R7;115 R3;116 R4;117 R1;118 R7;119 R4;
120 R4;121 R7;122 R3;123 R3;124 R4;125 R1;126 R1;127 R4;128 R1;129 U;130 R3;131 R7;132 I;133 R5;134 R4;135 R4;136 R4;137 R1;138 R7;139 R4;140 R1;141 R7;142 R5;143 R3;144 R4;145 R4;146 R5;147 R4;148 R1;149 R5;
150 R1;151 R4;152 R5;153 R6;154 R1;155 R4;156 R3;157 R5;158 R3;159 R4;160 R3;161 R4;162 R6;163 R1;164 R1;165 R1;166 R3;167 R4;168 R1;169 R4;170 R4;171 R4;172 R4;173 R4;174 R3;175 R1;176 R7;177 R4;178 R1;179 R4;
180 R5;181 R1;182 R3;183 R3;184 R4;185 I;186 R4;187 R3;188 R7;189 R6;190 R7;191 R4;192 R4;193 R3;194 S2;195 R3;196 R1;197 R7;198 R3;199 R1;200 R7"""
for it in codes.replace('\n', '').split(';'):
    i, c = it.split(); D[int(i)] = c
NOTE = {11: 'U: VLM decodes social cues and commands; Instruct-MuSoHu; real datasets + simulation (abstract). Springer Proc. Math. Stat. 2025; full text paywalled',
        16: 'U: LLM turns social cues into navigation constraints enforced by control barrier functions; simulation (abstract). RO-MAN 2025 (peer-reviewed); IEEE full text not accessible',
        50: 'U: VLM+LLM human detection, 1 m distance, attention signalling, gesture instructions; Isaac Sim (abstract). Mech. Mach. Sci. 2025; full text paywalled',
        86: 'U: frozen VLA + yield head, real TurtleBot 4 trials, 28 participants (abstract). Figshare preprint only (2026-02-13); no ORCID/affiliation metadata; provenance unverified; PDF not downloaded',
        129: 'U: VLM used for pedestrian detection + TRPO reward for polite detouring; Pepper trials (abstract). LNEE 2026; full text paywalled',
        132: 'U: VLM social context + LLM goal assignment; early results in simulated restaurant (abstract). HRI 2026 companion (early-stage); ACM DL behind bot check',
        133: 'U: pedestrian-safety TTC reasoning for autonomous ground vehicles; FM use not determinable (abstract not retrievable: ScienceDirect blocked)',
        171: 'U: LLM advisory layer for navigation incl. privacy-boundary enforcement; criterion C uncertain (abstract). IEEE BigDataService 2026; full text not accessible',
        185: 'U: LLM high-level decisions; avoidance of a human agent; criterion C uncertain (abstract). ICCRE 2026; full text not accessible',
        120: 'Borderline: LLM explains guide-dog obstacle avoidance to a blind user; no social-navigation capability among people (arXiv 2610.28920 read)',
        145: 'Full text read (arXiv 2604.16993): traffic-signage compliance in street-view VLN; no people (fails C)',
        186: 'Borderline, full text read (arXiv 2508.02338): VLM-generated human behaviours to test generic AMR safety requirements (collision, stability, efficiency); not a social-navigation capability',
        198: 'Borderline: VLM ranks museum visitors for approach receptiveness from video clips; no navigation behaviour executed',
        146: 'Abstract (IEEE): attention-aware costmap uses a Random Forest on skeletal features; no FM', 157: 'Abstract (IEEE): sampling-based multi-policy planner; no FM',
        180: 'Abstract (IEEE): HJ reachability + U-Net; no FM',
        159: 'Record without abstract; the title names deep RL, an LLM and iris tracking for the autonomous wheelchair of a patient with ALS but indicates no social-navigation capability among people (fails C)',
        152: 'Record without abstract; the title describes motion control for a robotic guide dog and names no FM (fails B)', 17: 'Abstract (IEEE): benchmark of learning- and model-based planners; no FM component',
        194: 'Already screened in Stage 2 under the title variant "Robot Navigation Using Physically Grounded VLMs in Outdoor Environments (VLM-GroNav)": EXCLUDE (fails C)'}
NOTE.update({
 16: 'INCLUDE (full text, 2026-10-26): local LLM sets navigation mode, speed bound and social-zone distance enforced by CBFs; Gazebo + offline accuracy test. Corpus entry 2025_Ruo_LLM-Social-Cues',
 132: 'INCLUDE (full text, 2026-10-26): CLIP/Qwen social context conditions a learned selector of collision-free candidates; LLM goal assignment and clarification. Early-stage. Corpus entry 2026_Gandotra_RBTLR',
 185: 'INCLUDE (full text, 2026-10-26): LLM chooses proceed/yield/avoid/stop around a detected human; independent LiDAR safety layer; Gazebo. Corpus entry 2026_Oush_VLA-TurtleBot',
 86: 'Full text read (Figshare PDF supplied by the authors): claimed dataset not locatable, several reference errors, and a frozen manipulation VLA said to output holonomic velocities for a differential-drive robot',
 133: 'Full text read (EAAI 2026): YOLOv8-Pose and Kalman-filter time-to-collision reasoning; no FM',
 171: 'Full text read (BigDataService 2026): no people in any scenario; privacy means stopping at a signed restricted zone; the follower is a robot',
})
U = json.load(open(os.path.join(H, 'union.json')))['unique']
new = sorted([u for u in U if u['status'] == 'new'], key=lambda u: u['title'].lower())
assert len(new) == 201 and set(D) == set(range(201))
rows = []
for i, u in enumerate(new):
    c = D[i]
    dec = {'U': 'UNRESOLVED (not coded)', 'S2': 'ALREADY SCREENED (Stage 2)', 'I': 'INCLUDE'}.get(c, 'EXCLUDE')
    rows.append({'title': u['title'], 'first_author': u.get('first_author') or '', 'date': u.get('date') or '', 'venue': u.get('venue') or '', 'doi': (u.get('doi') or '').replace('https://doi.org/', ''),
                 'sources': '+'.join(u['sources']), 'project_status': 'new to project' if c != 'S2' else 'screened in Stage 2', 'decision': dec,
                 'level': 'full text' if i in (145, 186, 120, 16, 132, 185, 86, 133, 171) else 'title/abstract', 'reason': (NOTE[i] if c in ('U', 'I') else (f'{c}: ' + NOTE[i] if i in NOTE and c.startswith('R') else NOTE.get(i, R.get(c, ''))))})
for u in sorted([u for u in U if u['status'] != 'new'], key=lambda u: u['title'].lower()):
    rows.append({'title': u['title'], 'first_author': u.get('first_author') or '', 'date': u.get('date') or '', 'venue': u.get('venue') or '', 'doi': (u.get('doi') or '').replace('https://doi.org/', ''),
                 'sources': '+'.join(u['sources']), 'project_status': {'corpus': 'in corpus', 'screened_stage2': 'screened in Stage 2', 'screened_stage7': 'screened in Stage 7'}[u['status']],
                 'decision': 'ALREADY KNOWN', 'level': '-', 'reason': f"{u['status']}: {u['match']}"})
with open(os.path.join(H, 'S1_final_search_record.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
from collections import Counter
print(len(rows), Counter(r['decision'] for r in rows)); print(Counter(D.values()))
