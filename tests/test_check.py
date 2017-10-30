# -*- coding: utf-8 -*-


def test_check_equal_pass(testdir):
    testdir.makepyfile("""
        def test_pass(check):
            check.equal(1, 1)
            check.equal((1, 2, 3), (1, 2, 3))
    """)
    result = testdir.runpytest('-v', '-s')

    result.assert_outcomes(passed=1)


def test_check_equal_fail(testdir):
    testdir.makepyfile("""
        def test_fail(check):
            check.equal(1, 2)
            check.equal((1, 2, 3), (1, 2, 4))
    """)
    result = testdir.runpytest('-v', '-s')

    result.assert_outcomes(failed=1)
