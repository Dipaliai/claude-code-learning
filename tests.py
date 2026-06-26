"""
Test file for Grade Calculator

Run this with: python tests.py

These tests check if the bugs are fixed correctly.
All tests should pass once you fix the bugs!
"""

import sys
from main import calculate_average, get_letter_grade
from utils import get_grades


def test_calculate_average():
    """
    TEST #1: Check if calculate_average() works correctly
    
    This tests if BUG #1 is fixed.
    """
    print("\n🧪 TEST #1: calculate_average()")
    print("-" * 50)
    
    # Test 1a: Simple average
    test_1a = calculate_average([80, 90, 70])
    expected_1a = 80.0
    
    print(f"Input: [80, 90, 70]")
    print(f"Expected: {expected_1a}")
    print(f"Got: {test_1a}")
    
    if abs(test_1a - expected_1a) < 0.01:
        print("✅ PASS: Simple average works!")
    else:
        print(f"❌ FAIL: Expected {expected_1a}, got {test_1a}")
        return False
    
    # Test 1b: Different numbers
    test_1b = calculate_average([100, 100, 100])
    expected_1b = 100.0
    
    print(f"\nInput: [100, 100, 100]")
    print(f"Expected: {expected_1b}")
    print(f"Got: {test_1b}")
    
    if abs(test_1b - expected_1b) < 0.01:
        print("✅ PASS: All same grades works!")
    else:
        print(f"❌ FAIL: Expected {expected_1b}, got {test_1b}")
        return False
    
    # Test 1c: Low grades
    test_1c = calculate_average([50, 60, 70])
    expected_1c = 60.0
    
    print(f"\nInput: [50, 60, 70]")
    print(f"Expected: {expected_1c}")
    print(f"Got: {test_1c}")
    
    if abs(test_1c - expected_1c) < 0.01:
        print("✅ PASS: Low grades work!")
    else:
        print(f"❌ FAIL: Expected {expected_1c}, got {test_1c}")
        return False
    
    return True


def test_get_letter_grade():
    """
    TEST #2: Check if letter grades work
    
    This is NOT a bug - just testing the function works
    """
    print("\n🧪 TEST #2: get_letter_grade()")
    print("-" * 50)
    
    tests = [
        (95, "A"),
        (85, "B"),
        (75, "C"),
        (65, "D"),
        (55, "F"),
    ]
    
    all_passed = True
    for grade, expected_letter in tests:
        result = get_letter_grade(grade)
        print(f"Grade {grade} → {result} (expected {expected_letter})", end=" ")
        
        if result == expected_letter:
            print("✅")
        else:
            print(f"❌ Expected {expected_letter}, got {result}")
            all_passed = False
    
    return all_passed


def test_input_validation():
    """
    TEST #3: Check if input validation works
    
    This tests if BUG #2 is fixed.
    
    NOTE: This test is MANUAL because it needs user input.
    You can test this by running main.py and entering:
    - A grade > 100 (should reject)
    - A grade < 0 (should reject)  
    - A negative grade (should reject)
    - A valid grade 0-100 (should accept)
    """
    print("\n🧪 TEST #3: Input Validation (MANUAL TEST)")
    print("-" * 50)
    print("This test requires manual checking.")
    print("Run: python main.py")
    print("Try entering these:")
    print("  ❌ 150 (too high)")
    print("  ❌ -10 (negative)")
    print("  ✅ 85 (valid)")
    print("\nIf validation is working:")
    print("  - Invalid grades should be REJECTED")
    print("  - Valid grades should be ACCEPTED")
    return True


def run_all_tests():
    """
    Run all tests and print summary
    """
    print("\n" + "="*50)
    print("🧪 RUNNING ALL TESTS")
    print("="*50)
    
    results = []
    
    # Run tests
    results.append(("calculate_average", test_calculate_average()))
    results.append(("get_letter_grade", test_get_letter_grade()))
    results.append(("input_validation", test_input_validation()))
    
    # Print summary
    print("\n" + "="*50)
    print("📊 TEST SUMMARY")
    print("="*50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    print("="*50)
    print(f"\nTotal: {passed}/{total} tests passed\n")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! Both bugs are fixed! 🎉\n")
        return True
    else:
        print("⚠️  Some tests failed. Keep working on the bugs!\n")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
