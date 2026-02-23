# Project Plan — Group B: Project Okavango

**Deadline (first delivery):** March 2, 2026 23:59:59

---

## Phase 1 — Repository & Environment Setup

### Git Repository

- [x] Repository created on GitHub, named `Group_B`
- [x] Initialised with `README.md`, `LICENSE`, and a Python `.gitignore`
- [x] `README.md` includes all group member emails (copy-pasteable into Outlook)
- [x] Maintainer permissions granted to all group members
- [x] Every member has cloned the repository locally

### Python Environment

- [ ] `environment.yml` (conda) and `requirements.txt` are kept up to date
- [ ] All dependencies installable in a clean environment with no manual steps

### Project Structure

**Repo structure to maintain:**
```
|__ downloads/
|__ app/
|    |__ your .py files here
|__ tests/
|    |__ your test files here
|__ notebooks/
|    |__ your notebooks here
|__ .gitignore
|__ README.md
|__ LICENSE
|__ main.py
```

---

## Phase 2 — Data

### Datasets

| # | Dataset | Source |
|---|---------|--------|
| 1 | Annual change in forest area | Our World in Data |
| 2 | Annual deforestation | Our World in Data |
| 3 | Share of land that is protected | Our World in Data |
| 4 | Share of land that is degraded | Our World in Data |
| 5 | *(fifth dataset — TBD, relevant to life on land)* | Our World in Data |
| 6 | Admin 0 – Countries map (110m) | Natural Earth |

### Function 1 — `download_datasets()`

- Downloads all required datasets into the `downloads/` directory
- Must always fetch the **most recent data available** when starting the application (no hardcoded URLs or filenames)
- PEP 8 compliant, type-annotated, Pydantic-validated where applicable

### Function 2 — `merge_datasets()`

- Merges the Natural Earth GeoDataFrame with each downloaded dataset using `geopandas`
- The **left** DataFrame must always be the GeoDataFrame
- Handles column name mismatches and country name normalisation as needed

### Data Preprocessing / EDA

- Handle missing values (N/A)
- Remove duplicate rows
- Identify and handle outliers
- Align country name formats across datasets for successful merges
- Prototype and explore data in notebooks before integrating into the class

### Class — `OkavangoData`

- Defined in a **single `.py` file** inside `app/`
- `__init__` executes both `download_datasets()` and `merge_datasets()` automatically
- `__init__` reads each merged dataset into a corresponding GeoDataFrame attribute
- All method and attribute names are PEP 8 compliant
- All interfaces use type annotations; Pydantic used where applicable
- Fully documented (docstrings on class and all methods)

### Tests

- `test_download_datasets()` — verifies files are downloaded into `downloads/`
- `test_merge_datasets()` — verifies the merge produces a valid GeoDataFrame with expected columns
- Located in `tests/`; all tests must pass when running `pytest` from the project root

---

## Phase 3 — Streamlit App

### App Structure (per page/view)

1. **World Map** (GeoDataFrame choropleth via GeoPandas/Folium or Plotly)
2. **Graph 1** — General overview chart (e.g. top 5 / bottom 5 countries by annual forest change), with tooltip
3. **Graph 2** — Specific chart filtered by the country/region selected on the map, with tooltip
4. **KPI Text Boxes** — Key summary statistics (e.g. total deforested area, global protected land %)

### Sidebar (collapsible)

- **Dataset selector** — choose which dataset/map to display (one at a time)
- **Year / Time slider** — dynamically adjusts to the available year range of the selected dataset

### Behaviour Notes

- Only one map is shown at a time, determined by the sidebar selector
- The time slider updates its range dynamically based on whichever dataset is active
- On app startup, the class is instantiated, which triggers the download of the **most recent** data — this satisfies the "real-time" requirement (no need for per-second polling)
- Import `OkavangoData` from the class file; keep app logic in `app/`

---

## Phase 4 — Testing & Quality

- [ ] `pytest` passes from project root with no errors
- [ ] All code is PEP 8 compliant (use `flake8` or `ruff` to check)
- [ ] Static type checking passes (use `mypy`)
- [ ] Pydantic models used for any external data / configuration inputs
- [ ] All functions and classes have docstrings

---

## Open Questions

- **Real-time update:** Is it enough to fetch data, with the start of the application?
- **Fifth dataset:** Which Dataset are we using as a fith one?
- **Map rendering library:** Decide between Plotly Express (`choropleth_map`), Folium, or native GeoPandas `.plot()` wrapped in Streamlit.
