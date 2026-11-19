[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kkazushi-eng/tiny-chess-v5/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kkazushi-eng/tiny-chess-v5/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

# tiny-chess-01 entry

A chess engine in a single `main.py` that fits the competition's 4,096-byte
entrypoint cap (this entry: 4,092 bytes). The readable engine source is
lzma-compressed into a payload string inside `main.py` and unpacked at
startup by a small loader; the engine itself is Python standard library
only and reads no other file.

## The engine

Written from scratch:

- 0x88 board representation with incremental material / piece-square
  evaluation and Zobrist hashing (repetition and fifty-move handling)
- Negamax alpha-beta search with PVS, a 262,144-entry transposition
  table, null-move pruning, futility pruning and check extensions
- Late-move reductions kept deliberately gentle: reductions start one
  move later than the previous build and never add a second extra ply
  at high move counts (the deeper cut measurably hurt the attacking
  side in head-to-head play)
- Move ordering by transposition-table move, MVV-LVA captures, killers
  and a history heuristic
- Quiescence search over captures and promotions (all evasions when in
  check) with delta pruning
- Tapered evaluation for the king and for pawns (endgame pawn table
  rewards advanced pawns) plus a bishop-pair term, interpolated by
  remaining material
- Deterministic fixed node budget of 84,000 nodes per move (no
  wall-clock dependence)

## Local validation

- Kit practice trials (6 games each against the anchored ladder):
  trial-0 Elo 1654, trial-1 Elo 1809, trial-2 Elo 1545 (average 1669).
  No timeout losses.
- Direct gauntlets over 12 book openings, both colours (24 games each):
  13.5–10.5 against this account's previous submitted build (v3.3) and
  12.0–12.0 against the unsubmitted v3.4 tuning.
- Move generation verified by perft: startpos perft(3)=8,902 and
  perft(4)=197,281; kiwipete perft(3)=97,862, all exact. Make/unmake
  state restoration (hash, both tapered score sums, bishop counts)
  checked over random playouts including promotions, en passant and
  castling.
