# Unit Testing Track

A practical, staged testing curriculum designed for both personal mastery and future teaching.

## Stage roadmap

| Stage | Time Estimate | Key Tool | Learning Goal |
|---|---:|---|---|
| 1 — unittest basics | 1–2 days | `unittest` | Core assertions, test classes, setup hooks, exception testing |
| 2 — pytest | 2–3 days | `pytest` | Parametrization, concise tests, built-in fixtures |
| 3 — Mocking | 2–3 days | `unittest.mock` | Isolate dependencies and verify interactions |
| 4 — Test design | Ongoing | `pytest-cov` | Better test cases, boundary thinking, useful coverage |
| 5 — Real projects | 1–2 weeks | Everything above | End-to-end confidence with maintainable suites |

---

## Directory contents

- `stage1_unittest_basics.py`
  - Functions/classes intentionally built for testing with standard library tools.
- `test_stage1_unittest.py`
  - Classic `unittest` style: `TestCase`, `setUp`, `assertRaises`.

- `stage2_pytest_basics.py`
  - Small, pure functions to demonstrate clean pytest workflows.
- `test_stage2_pytest.py`
  - `pytest.mark.parametrize`, `pytest.raises`, function-based tests.

- `stage3_mocking.py`
  - Modules with external boundaries (clock, HTTP client, email gateway).
- `test_stage3_mocking.py`
  - Mocks + interaction assertions (`assert_called_once`, call argument checks).

- `stage4_test_design.py`
  - Boundary-driven business logic examples.
- `test_stage4_design.py`
  - Boundary/value-partition tests and behavior-focused checks.

- `stage5_real_project.py`
  - Mini ETL-style pipeline: load → clean → summarize.
- `test_stage5_real_project.py`
  - Unit and integration-leaning tests with `tmp_path` file fixtures.

---

## How to use this track

### Stage 1 first (standard library only)

Run only the `unittest` examples:

```bash
python -m unittest discover -s 06_unit_tests -p "test_stage1_unittest.py" -v
```

### Then move to pytest stages

Install tooling:

```bash
pip install pytest pytest-cov
```

Run pytest examples:

```bash
pytest 06_unit_tests/test_stage2_pytest.py -q
pytest 06_unit_tests/test_stage3_mocking.py -q
pytest 06_unit_tests/test_stage4_design.py -q
pytest 06_unit_tests/test_stage5_real_project.py -q
```

Run full test suite:

```bash
pytest 06_unit_tests -q
```

Coverage report:

```bash
pytest 06_unit_tests --cov=06_unit_tests --cov-report=term-missing
```

---

## Teaching notes (why these examples are structured this way)

- **Stage 1** keeps everything explicit so learners understand test lifecycle and assertion APIs.
- **Stage 2** shifts to readability and speed; tests look closer to behavior specs.
- **Stage 3** introduces dependency boundaries so tests remain deterministic and fast.
- **Stage 4** focuses on *test quality*, not just test quantity:
  - boundary values,
  - failure modes,
  - invariants,
  - and meaningful names.
- **Stage 5** mirrors real work: file I/O plus transformation logic with testable seams.

---

## Suggested progression exercises

1. Add one failing test before changing each stage module.
2. Refactor implementation and keep tests green.
3. Increase branch coverage in Stage 4 and Stage 5.
4. Add one regression test whenever you fix a bug.
5. Convert at least one Stage 1 test file into pytest style to compare ergonomics.

---

## Teaching extension ideas

- Add a `conftest.py` and shared fixtures once patterns repeat.
- Introduce flaky test examples and stabilization strategies.
- Add CI with GitHub Actions to run `pytest` and coverage on each push.
- Add mutation testing later to evaluate assertion strength.
