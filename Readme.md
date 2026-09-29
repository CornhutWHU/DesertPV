# CESM Desert PV plotting code

This is a curated, redacted release of the plotting scripts that can be linked to the current manuscript. Directories follow the manuscript figure numbers, which differ from some original folder names. The source files remain untouched.

## What was cleaned

- Selected the current source version for each identifiable panel; older `Fig3to6` copies, unrelated demos, duplicate notebook cells, notebook outputs, and large blocks of commented-out code were omitted.
- Renamed scripts by manuscript panel and plot purpose. Local absolute input/output paths were changed to `data/` or `output/` where identifiable.
- Replaced numerical values and digits in strings with `xxx`. Digits embedded in identifiers were spelled out to keep distinct names distinct. No code file contains digits. These files are intentionally not executable until placeholders are restored.

## Coverage and limits

- `fig1` and `fig2` contain the identifiable main-figure scripts.
- `extended_data` contains the identifiable supplementary figure scripts.
- The supplied plotting folder did not contain reliably identifiable code for the manuscript's electricity-generation Fig. 3 or carbon/economic Fig. 4. See the notes in those folders. Scripts for some individual panels of Fig. 1 and Fig. 2 were also not verifiable.
- Some selected scripts use synthetic data, values copied from a figure, or proxy indicators. `SOURCES.md` identifies each one. They must not be represented as independently reproducible analyses.
- No raw data, generated plots, GIS layers, archives, or original notebooks are included.

`SOURCES.md` maps each curated file to its original source and describes its data status.
