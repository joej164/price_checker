import pytest
import os.path


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures.txt") else "w"
        with open("failures.txt", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                print('in tmpdir')
                extra = " ({})".format(item.funcargs["tmpdir"])
            else:
                extra = ""
            print(rep.nodeid, extra)
            f.write(rep.nodeid + extra + "\n")
