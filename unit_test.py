import func_utils 

def test_validPath_exists():
    return_value = True
    success, msg = func_utils.validPath("Demo")
    return return_value == success and msg

def test_validPath_does_not_exist():
    return_value = False
    failed, msg= func_utils.validPath("/some/missing/path")
    return return_value == failed and msg

def test_cloneURL_success():
    returncode = 0
    success, msg = func_utils.cloneURL("https://github.com/anowii/clone-this-test.git")
    return returncode == success and msg

def test_cloneURL_failure():
    returncode = 1
    success, msg = func_utils.cloneURL("https://github.com/nonexistent/repo.git")
    return returncode == success and msg

if __name__ == "__main__":
    print("TEST 1", test_validPath_exists())
    print("TEST 2",test_validPath_does_not_exist())
    print("TEST 3",test_cloneURL_failure())
    print("TEST 4",test_cloneURL_success())

