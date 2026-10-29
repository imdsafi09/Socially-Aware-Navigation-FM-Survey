"""Stage-3 taxonomy recoding consistency check: new codes assigned from label-blind method summaries (blind.txt)."""
# R roles: R1 scene/context; R2 human-state & relation; R3 social-norm reasoning & behaviour selection; R4 instruction/preference grounding & task planning; R5 human-facing communication
# X interfaces: X0 unexecuted output; X1 semantic/state representation; X2 candidate selection; X3 objective/constraint/parameter shaping; X4 goal/waypoint/trajectory; X5 runtime latent conditioning of learned policy; X6 direct action; X7 training-time supervision; X8 human-facing channel
# V: off(Y/N) sim(Y/N) robot(none/demo/systematic) humans(none/sim/staged/natural/unspecified) heval(none/text/observer/copresent)
NEW = {
 '2024_Holk_PREDILECT': ('R4', 'X7', 'N Y none sim none', 'training-only'),
 '2024_Sathyamoorthy_CoNVOI': ('R1 R3', 'X4', 'N N systematic unspecified none', 'per-decision'),
 '2024_Wang_SALM': ('R3 R4', 'X6 X2', 'N Y none sim none', 'per-decision'),
 '2024_Yu_PANav': ('R1 R3', 'X2', 'Y N demo none none', 'per-decision'),
 '2025_Kawabata_SocialNav-MoE': ('R1 R2 R3', 'X0', 'Y N none none none', 'offline'),
 '2025_Kong_AutoSpatial': ('R1 R2 R3', 'X0', 'Y N none none text', 'offline'),
 '2025_Liang_MOSU': ('R1 R3', 'X2 X3', 'Y N demo unspecified none', 'per-decision'),
 '2025_Luo_GSON': ('R2', 'X1', 'Y N systematic natural none', 'per-decision'),
 '2025_Martinez-Baselga_Hey-Robot': ('R1 R4', 'X3', 'N Y demo staged none', 'asynchronous'),
 '2025_Narasimhan_OLiVia-Nav': ('R1', 'X5 X7', 'Y N systematic unspecified none', 'per-decision'),
 '2025_Payandeh_Social-LLaVA': ('R1 R2 R3', 'X0', 'Y N demo none text', 'offline'),
 '2025_Saito_VLM-Crowd-Mapping': ('R2', 'X3', 'N N demo staged none', 'per-decision'),
 '2025_Song_VLM-Social-Nav': ('R1 R3', 'X3', 'N N systematic staged copresent', 'per-decision'),
 '2025_Sotomi_Transparent-Social-Nav-VLM': ('R1 R5', 'X1 X8', 'Y N systematic natural observer', 'per-decision'),
 '2025_Wang_SAMALM': ('R3', 'X6 X2', 'N Y none sim none', 'per-decision'),
 '2025_Weerakoon_BehAV': ('R1 R3 R4', 'X3 X4', 'Y N systematic staged none', 'per-decision'),
 '2025_Wen_HSAC-LLM': ('R5', 'X8', 'N Y demo sim none', 'per-decision'),
 '2026_Ahmadi_HUMA': ('R2 R3', 'X5', 'N Y demo sim none', 'event-triggered'),
 '2026_Bejarano_PAD': ('R1 R2 R5', 'X1 X8', 'N N systematic staged copresent', 'per-decision'),
 '2026_Chen_LISN': ('R1 R2 R4', 'X3 X4', 'N Y none sim none', 'asynchronous'),
 '2026_Chen_SocialNav-CVPR': ('R1 R3', 'X6 X7', 'N Y systematic unspecified none', 'per-decision'),
 '2026_Elnoor_ViLAM': ('R2', 'X7', 'N N systematic natural none', 'training-only'),
 '2026_Fang_Group-Joining': ('R2 R4', 'X4', 'Y N systematic staged none', 'asynchronous'),  # 2026-10-27 claim-citation audit correction (CLAIM_CITATION_INTEGRITY_AUDIT.md, Post-audit corrections): inference runs continuously and asynchronously with control (PDF p6)
 '2026_Fang_Obstacles-to-Etiquette': ('R2 R3', 'X2 X7', 'N N systematic staged none', 'asynchronous'),  # 2026-10-27 claim-citation audit correction (CLAIM_CITATION_INTEGRITY_AUDIT.md, Post-audit corrections): asynchronous modules; path selection decoupled from velocity control (p2-3)
 '2026_Hu_SPARK-VLN': ('R1 R4', 'X5', 'N Y none sim none', 'asynchronous'),
 '2026_Huo_NORM-Nav': ('R1 R4', 'X3', 'N Y demo unspecified none', 'per-instruction'),
 '2026_Liao_G2-Nav': ('R1 R2', 'X3', 'Y N systematic natural none', 'asynchronous'),
 '2026_Park_TACET': ('R1 R3', 'X3 X7', 'N N systematic staged observer', 'asynchronous'),  # 2026-10-27 claim-citation audit correction (CLAIM_CITATION_INTEGRITY_AUDIT.md, Post-audit corrections): reasoner at ~0.25 Hz, cached tokens, controller never blocked (p3)
 '2026_Payandeh_Narrate2Nav': ('R1 R2', 'X7', 'Y N systematic unspecified none', 'training-only'),
 '2026_Sethuraman_Context-Aware-Preferences': ('R1 R4', 'X3', 'N N systematic unspecified text', 'asynchronous'),
 '2026_Wang_LE-Nav': ('R1 R2', 'X3', 'N N systematic natural copresent', 'asynchronous'),
 '2026_Wang_MAction-SocialNav': ('R1 R2 R3', 'X0', 'Y N none none none', 'offline'),
 '2026_Wang_SALSA': ('R3', 'X6', 'Y N demo none none', 'per-decision'),
 '2026_Xiao_E-SocialNav': ('R1 R2 R3', 'X0', 'Y N none none none', 'offline'),
 '2026_Xiao_Prompting-VLMs-JSAI': ('R1 R2 R3', 'X0', 'Y N none none none', 'offline'),
 '2026_Xu_HCSG': ('R2', 'X1', 'N Y systematic staged none', 'per-decision'),
 '2026_Zhang_GCL': ('R1 R2 R3', 'X0', 'Y N none none none', 'offline'),
 '2026_Zhang_SAATT-Nav': ('R2 R5', 'X1 X8', 'N Y none sim none', 'per-decision'),
 '2026_Zhang_SOPD-SocialNav': ('R1 R3', 'X0', 'Y N demo none none', 'offline'),
 '2026_Zhang_Walk-With-Me': ('R3 R4', 'X4 X6', 'N N systematic natural none', 'hierarchical'),
 '2026_Zhao_EvoNav': ('R3', 'X7', 'N Y none sim none', 'training-only'),
 '2026_Zhang_AHead-VLN': ('R1 R3 R4', 'X2 X6', 'N Y none sim none', 'per-decision'),  # Stage 9 addition (coded from the IJCAI full text)
 '2025_Ruo_LLM-Social-Cues': ('R2 R3 R4', 'X3 X4', 'Y Y none sim none', 'per-instruction'),  # Stage 11 addition (final coverage search; RO-MAN 2025 full text)
 '2026_Gandotra_RBTLR': ('R1 R4 R5', 'X5 X4 X8', 'N Y none sim none', 'per-decision'),  # Stage 11 addition (HRI 2026 companion full text)
 '2026_Oush_VLA-TurtleBot': ('R1 R3', 'X6', 'N Y none sim none', 'event-triggered'),  # Stage 11 addition (ICCRE 2026 full text); discrete action executed directly, as AHead-VLN/SALM
}
