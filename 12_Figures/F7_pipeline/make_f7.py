"""F7 - Where foundation-model output enters the navigation stack (conceptual architecture, no corpus statistics).
Final polish (2026-10-21): the four planner-facing interfaces D1-D4 share one consumer and are drawn as one neutral route; accent
colours are reserved for the exceptional routes D6 (direct action), D7 (training-time supervision) and D8 (human-facing channel);
interface routes are labelled in place, so no separate key is needed (definitions: Section 5). Previous versions:
make_f7_v2_superseded.py, make_f7_v4_superseded.py (2026-10-26: D7 drawn in two pieces; D6 ended between the policy and safety boxes). Print scale: canvas 516 pt (LaTeX \\textwidth 522 pt); all lettering >= 7 pt printed."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figlib import *
H = os.path.dirname(os.path.abspath(__file__))
W, Ht = 516, 224
FMC = (0.99, 0.90, 0.76); NEU = (0.42, 0.42, 0.42); LP = 8.4
C6, C7, C8 = (0.80, 0.30, 0.05), OK['purple'], OK['green']
def path(c, pts, color=NEU, lw=0.7, dash=None, head=True):
    col = OK[color] if isinstance(color, str) else color
    c.save(); c.new_path(); c.set_source_rgb(*col); c.set_line_width(lw)
    if dash: c.set_dash(dash)
    c.move_to(*pts[0])
    for p in pts[1:]: c.line_to(*p)
    c.stroke(); c.restore()
    if head:
        (x1, y1), (x2, y2) = pts[-2], pts[-1]; s = 3 + lw
        c.save(); c.new_path(); c.set_source_rgb(*col); c.move_to(x2, y2)
        if x1 == x2: d = 1 if y2 > y1 else -1; c.line_to(x2 - s * 0.6, y2 - d * s); c.line_to(x2 + s * 0.6, y2 - d * s)
        else: d = 1 if x2 > x1 else -1; c.line_to(x2 - d * s, y2 - s * 0.6); c.line_to(x2 - d * s, y2 + s * 0.6)
        c.close_path(); c.fill(); c.restore()
def box(c, x, y, w, h, title, lines=(), fill=(0.97, 0.97, 0.97), stroke=(0.35, 0.35, 0.35)):
    rect(c, x, y, w, h, fill, stroke, 0.5); text(c, x + w / 2, y + 9.5, title, 7.2, True, 'center')
    for i, s in enumerate(lines): text(c, x + w / 2, y + 18.5 + i * LP, s, 7, False, 'center', 'dark')
def draw(c):
    Y, BH = 118, 40
    # ---- navigation stack (left to right: sensing -> perception -> planner / policy -> safety -> robot -> people)
    box(c, 3, Y, 42, BH, 'Sensors', ['camera', 'LiDAR', 'speech'])
    box(c, 52, Y, 62, BH, 'Perception', ['tracking,', 'localisation, map'])
    rect(c, 214, Y - 3, 144, BH + 6, (1, 1, 1), (0.65, 0.65, 0.65), 0.4)
    box(c, 218, Y, 96, BH, 'Planner / controller', ['classical planning', 'fast loop'])
    box(c, 318, Y, 38, BH, 'Learned', ['policy'])
    box(c, 363, Y, 66, BH, 'Safety layer', ['FM-independent', 'guard, if present'], (0.93, 0.95, 0.98))   # cross-cutting property, coded separately (count in Fig. 6)
    box(c, 434, Y, 30, BH, 'Robot', [])
    box(c, 469, Y, 45, BH, 'Humans &', ['environment'], (0.92, 0.96, 0.92))
    for x1, x2 in [(45, 52), (356, 363), (429, 434), (464, 469)]: path(c, [(x1, Y + 20), (x2, Y + 20)])
    path(c, [(116, Y + 20), (218, Y + 20)])
    # feedback: people react to the robot
    path(c, [(491, Y + BH), (491, Ht - 8), (24, Ht - 8), (24, Y + BH)], NEU, 0.6)
    text(c, 258, Ht - 11, 'people react to the robot', 7, False, 'center', 'dark')
    # ---- foundation-model reasoning (slow loop)
    fx, fy, fw, fh = 70, 6, 118, 52
    rect(c, fx, fy, fw, fh, FMC, OK['orange'], 1.0)
    text(c, fx + fw / 2, fy + 11, 'Foundation-model reasoning', 7.4, True, 'center'); text(c, fx + fw / 2, fy + 20.5, 'VLM / LLM / VLA', 7, False, 'center', 'dark')
    text(c, fx + fw / 2, fy + 32, 'slow loop: per decision,', 7, False, 'center', DRED); text(c, fx + fw / 2, fy + 40.4, 'asynchronous or event-triggered', 7, False, 'center', DRED)
    path(c, [(24, Y), (24, fy + 44), (fx, fy + 44)], NEU, 0.6)                 # observations to the FM (below the offline box)
    path(c, [(96, Y), (96, fy + fh)], NEU, 0.6)                                 # tracks and map to the FM
    # D0: decision not executed (offline)
    rect(c, 3, 4, 46, 28, (0.96, 0.96, 0.96), (0.60, 0.60, 0.60), 0.4)
    text(c, 26, 14.5, 'Offline', 7, True, 'center', 'dark'); text(c, 26, 23.5, 'evaluation', 7, False, 'center', 'dark')
    path(c, [(fx, 14), (49, 14)], (0.55, 0.55, 0.55), 0.7, [1.6, 1.2]); text(c, 59.5, 11.5, 'D0', 7, False, 'center', (0.40, 0.40, 0.40))
    # ---- interface routes, labelled in place (exceptional routes in colour; planner-facing D1-D4 neutral)
    X0 = fx + fw
    path(c, [(X0, 12), (491, 12), (491, Y)], C8, 0.8);  text(c, X0 + 4, 9.5, 'D8 human-facing channel', 7, False, 'left', DGREEN)
    path(c, [(X0, 23), (368, 23), (368, Y)], C6, 0.8);  text(c, X0 + 4, 20.5, 'D6 direct action (bypasses intervening planner)', 7, False, 'left', DRED)   # ends on the Safety-layer box (guard, if present), i.e. downstream of no planner
    path(c, [(X0, 34), (337, 34), (337, Y - 3)], NEU, 0.8); text(c, X0 + 4, 31.5, 'D5 latent conditioning', 7, False, 'left', 'dark')
    path(c, [(X0, 45), (270, 45), (270, Y - 3)], NEU, 1.5); text(c, X0 + 4, 42.5, 'D1–D4 state, candidates, objective, goal', 7, False, 'left', 'dark')
    path(c, [(236, Y - 3), (236, 54), (X0, 54)], NEU, 0.5, [2, 1.5]); text(c, 233, 64, 'candidates (D2)', 7, False, 'right', 'dark')
    # ---- D7: training pathway below the stack
    ty = Y + BH + 12
    rect(c, 128, ty, 98, 24, (0.96, 0.94, 0.98), C7, 0.5); text(c, 177, ty + 9.5, 'Training pipeline', 7.2, True, 'center')
    text(c, 177, ty + 18.5, 'labels, rewards, distillation', 7, False, 'center', 'dark')
    path(c, [(150, fy + fh), (150, ty)], C7, 0.8, [3, 2]); text(c, 154, Y - 17.4, 'D7 training-time', 7, False, 'left', DPURPLE); text(c, 154, Y - 9, 'supervision', 7, False, 'left', DPURPLE)   # one continuous route; it crosses the perception-to-planner arrow
    path(c, [(226, ty + 12), (337, ty + 12), (337, Y + BH + 3)], C7, 0.7, [3, 2]); text(c, 232, ty + 9.5, 'student policy', 7, False, 'left', DPURPLE)
render(draw, W, Ht, os.path.join(H, 'F7_pipeline'))
print('F7 done')
