import Core.utils as utils 

def test_validPath(target_path):
    success, msg = utils.validPath(target_folder=target_path)
    return success 

url_list =["https://github.com/anowii/clone-this-test.git","https://github.com/nonexistent/repo.git"]

def test_cloneURL(url, target_path):
    success, msg = utils.cloneURL(url, target_path=target_path)
    return  success 


if __name__ == "__main__":

    valid_path =["Core", "Reports", "../GLinter", "../scan-me"]
    unvalid_path = ["/some/missing/path", "idontexsist", "fail/this/path"]
    
    count = 0
    for tpath in valid_path:
        if(test_validPath(tpath)):
            count += 1
    
    if(count == 4):
        print("utils.validPath PASSED")
    else:
        print("utils.validPath FAILED")

    count = 0
    for upath in unvalid_path:
        if not test_validPath(upath):
            count += 1
    if(count == 3):
        print("utils.validPath FAILED as expected")
    else:
        print("utils.validPath PASSED")


    if(test_cloneURL(url_list[0], "ClonedPath")):
        print("utils.cloneURL PASSED as expected")

    if not test_cloneURL(url_list[1], "ClonedPath"):
        print("utils.cloneURL FAILED as expected")
  