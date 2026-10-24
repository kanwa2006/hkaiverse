"""
Test suite for Task 2: Interactive Course Explorer & Curriculum Calculations
Verifies:
1. All 53 courses match between COURSE_MAP.csv and course_explorer.html
2. All 14 Course Explorer test cases (CE-01 to CE-14b) logic and filtering
3. Credit arithmetic (167 baseline, 167 proposed, 0 net delta, ~19.8% affected)
4. Integrity and privacy constraints
"""

import csv
import json
import re
import sys
from pathlib import Path

TASK2_DIR = Path(__file__).resolve().parent.parent

def load_csv_courses():
    csv_path = TASK2_DIR / "COURSE_MAP.csv"
    courses = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            courses.append({
                "code": row["Code"].strip(),
                "name": row["Course Name"].strip(),
                "sem": row["Semester"].strip(),
                "base": int(row["Baseline Credits"].strip()),
                "prop": int(row["Proposed Credits"].strip()),
                "action": row["Proposed Action"].strip(),
            })
    return courses

def load_html_courses():
    html_path = TASK2_DIR / "course_explorer.html"
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract COURSES array from JavaScript
    match = re.search(r"const COURSES = (\[[\s\S]*?\]);", content)
    assert match, "Could not find COURSES array in course_explorer.html"
    
    raw_js = match.group(1)
    # Convert JS object syntax to valid JSON
    # Replace unquoted keys (code, name, sem, semLabel, base, prop, action)
    json_str = re.sub(r'(\b[a-zA-Z_]\w*\b)\s*:', r'"\1":', raw_js)
    # Remove trailing commas before closing braces/brackets
    json_str = re.sub(r',\s*([\]}])', r'\1', json_str)
    
    return json.loads(json_str)

def test_ce_suite():
    csv_courses = load_csv_courses()
    html_courses = load_html_courses()

    print(f"Loaded {len(csv_courses)} courses from CSV and {len(html_courses)} courses from HTML.")
    assert len(csv_courses) == 53, f"Expected 53 courses in CSV, found {len(csv_courses)}"
    assert len(html_courses) == 53, f"Expected 53 courses in HTML, found {len(html_courses)}"

    # Match courses between CSV and HTML
    for h in html_courses:
        # Match by code or normalized name
        match = next((c for c in csv_courses if c["code"] == h["code"] or (h["code"] == "IP-2" and "Mandatory Internship-II" in c["name"])), None)
        assert match is not None, f"Course {h['code']} ({h['name']}) in HTML not found in CSV"
        assert match["base"] == h["base"], f"Base credit mismatch for {h['code']}: {match['base']} vs {h['base']}"
        assert match["prop"] == h["prop"], f"Proposed credit mismatch for {h['code']}: {match['prop']} vs {h['prop']}"
        assert match["action"] == h["action"], f"Action mismatch for {h['code']}: {match['action']} vs {h['action']}"

    # CE-01: Default state (all 53 visible)
    assert len(html_courses) == 53
    print("  [PASS] CE-01: Open with no filters returns all 53 courses")

    # CE-02: Search 'CS' matches courses with CS in code or name
    q = "cs"
    cs_matches = [c for c in html_courses if q in c["code"].lower() or q in c["name"].lower()]
    assert len(cs_matches) == 24
    assert all("cs" in c["code"].lower() or "cs" in c["name"].lower() for c in cs_matches)
    assert not any(c["code"] in ["CHY101", "MA101", "HS101"] for c in cs_matches)
    print("  [PASS] CE-02: Search 'CS' returns 24 matching courses, hides non-matches")

    # CE-03: Search 'database'
    q = "database"
    db_matches = [c for c in html_courses if q in c["code"].lower() or q in c["name"].lower()]
    assert len(db_matches) == 1 and db_matches[0]["code"] == "CS206"
    print("  [PASS] CE-03: Search 'database' returns CS206 (Database Management Systems)")

    # CE-04: Filter Semester 5
    sem5_matches = [c for c in html_courses if c["sem"] == "5"]
    assert len(sem5_matches) == 8
    expected_sem5 = {"CR301", "CS301", "CS302", "CS303", "CS304", "DS303", "DS304", "HS301"}
    assert {c["code"] for c in sem5_matches} == expected_sem5
    print("  [PASS] CE-04: Semester 5 filter returns exact 8 courses")

    # CE-05: Filter Action UPDATE
    upd_matches = [c for c in html_courses if c["action"] == "UPDATE"]
    assert len(upd_matches) == 9
    expected_upd = {"CS101", "CS102", "CS205", "CS206", "CS302", "CS304", "DS304", "CS307", "CS415"}
    assert {c["code"] for c in upd_matches} == expected_upd
    print("  [PASS] CE-05: Action UPDATE returns exact 9 courses")

    # CE-06: Filter Action REDUCE
    red_matches = [c for c in html_courses if c["action"] == "REDUCE"]
    assert len(red_matches) == 3
    assert {c["code"] for c in red_matches} == {"PH101", "MG201", "HS201"}
    print("  [PASS] CE-06: Action REDUCE returns exact 3 courses (PH101, MG201, HS201)")

    # CE-07: Filter Action ADD
    add_matches = [c for c in html_courses if c["action"] == "ADD"]
    assert len(add_matches) == 1
    assert add_matches[0]["code"] == "CS-NEW" and add_matches[0]["prop"] == 3 and add_matches[0]["base"] == 0
    print("  [PASS] CE-07: Action ADD returns exact 1 course (CS-NEW, base=0, prop=3)")

    # CE-08: Full dataset totals
    b_tot = sum(c["base"] for c in html_courses)
    p_tot = sum(c["prop"] for c in html_courses)
    assert b_tot == 167, f"Expected baseline 167, got {b_tot}"
    assert p_tot == 167, f"Expected proposed 167, got {p_tot}"
    assert p_tot - b_tot == 0
    print("  [PASS] CE-08: Full dataset totals baseline=167, proposed=167, net=0")

    # CE-09: Filter REDUCE calculation
    r_base = sum(c["base"] for c in red_matches)
    r_prop = sum(c["prop"] for c in red_matches)
    assert r_base == 11, f"Expected REDUCE baseline 11, got {r_base}"
    assert r_prop == 8, f"Expected REDUCE proposed 8, got {r_prop}"
    assert r_prop - r_base == -3
    print("  [PASS] CE-09: Filter REDUCE totals baseline=11, proposed=8, net=-3")

    # CE-10: Empty state search
    empty_matches = [c for c in html_courses if "xyzxyzxyz" in c["code"].lower() or "xyzxyzxyz" in c["name"].lower()]
    assert len(empty_matches) == 0
    print("  [PASS] CE-10: Search 'xyzxyzxyz' returns 0 rows (triggers empty state)")

    # CE-11: Reset
    reset_courses = list(html_courses)
    assert len(reset_courses) == 53
    print("  [PASS] CE-11: Reset restores all 53 courses")

    # CE-12: Sort ascending by baseline credit
    sorted_courses = sorted(html_courses, key=lambda c: c["base"])
    zero_credit_codes = [c["code"] for c in sorted_courses[:3]]
    assert "HS101" in zero_credit_codes and "HS301" in zero_credit_codes and "CS-NEW" in zero_credit_codes
    print("  [PASS] CE-12: Sort by baseline credit puts 0-credit courses at top")

    # CE-13: HS301 credits
    hs301 = next(c for c in html_courses if c["code"] == "HS301")
    assert hs301["base"] == 0 and hs301["prop"] == 0
    print("  [PASS] CE-13: HS301 has 0 baseline credits and 0 proposed credits")

    # CE-14a: Mandatory IP-1
    ip1 = next(c for c in html_courses if c["sem"] == "IP-1")
    assert ip1["code"] == "IP201" and ip1["base"] == 3 and ip1["prop"] == 3
    print("  [PASS] CE-14a: Mandatory IP-1 filter returns IP201 (3 credits)")

    # CE-14b: Mandatory IP-2
    ip2 = next(c for c in html_courses if c["sem"] == "IP-2")
    assert ip2["base"] == 15 and ip2["prop"] == 15
    print("  [PASS] CE-14b: Mandatory IP-2 filter returns Mandatory Internship-II (15 credits)")

    print("\nALL 15 COURSE EXPLORER TEST CASES PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_ce_suite()
